#!/usr/bin/env python3
"""오늘의 타로 유튜브 쇼츠 자동 업로드 (2026-11-21 미오 님 결정)

  python3 tools/youtube/tarot_short.py YYYY-MM-DD [check|all] [폴더]

 - 입력: posts/<날짜>-1000/ (make_reel_post.py 가 만든 short_yt.mp4, tarot.json)
 - 썸네일: short_yt.mp4 에서 카드 세 장이 모두 뒤집혀 이름까지 다 보이는 장면(THUMB_AT 초)을 잘라 short_thumb.jpg 로 만든다.
   (2026-11-25 미오 님 결정: 카드 뒷면(reel_first.jpg)이 아니라 카드가 다 보이는 장면으로)
 - 순서(반드시): ① 썸네일 없이 업로드(비공개+예약) → ② 영어 번역 넣기 → ③ 영상 처리가 끝날 때까지 기다린 뒤 다시 들어가 썸네일 넣기
   (썸네일을 먼저 넣으면 번역 뒤에 썸네일이 빠지는 일이 있었음, 11/21.
    API가 너무 빨라 처리 전에 넣으면 썸네일이 무시됨 → 처리 완료 확인 + THUMB_WAIT 초 더 쉰 뒤에 넣는다, 11/25 미오 님)
 - 공개: 그날 10:00 KST (인스타 릴스와 같은 시각). 이미 지났으면 지금부터 15분 뒤.
 - 언어: 기본 한국어 + 영어 번역 1개만 (미오 님 11/21: 타로는 한영만).
 - 재생목록 「쇼츠」, AI 사용 「예」, 아동용 아님, 카테고리 음악.
 - 결과: posts/<날짜>-1000/yt_result.json. 같은 제목이 이미 있으면 올리지 않는다(중복 방지).
 - 끝나면 호출한 작업이 log/youtube/ 와 yt_result.json 을 커밋·푸시한다.
"""
import datetime, json, os, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cloud  # noqa: E402

CHANNEL_URL = 'https://www.youtube.com/@goyo_mio'
MUSIC = {'갑목': 'g3Eeu8QVaJY', '을목': 'jtYiLzQkUJs', '병화': 'oIt-DzA96Bw', '정화': 'xDGOypKeG_s', '무토': 'q8w4WV76ah4',
         '기토': '8hLmKk8ag08', '경금': 'VzDuEs2i5es', '신금': '6p_X4z3terE', '임수': 'm_t33eB1bkc', '계수': 'wzt4ETUmOto'}
STEM_EN = {'갑목': '甲木', '을목': '乙木', '병화': '丙火', '정화': '丁火', '무토': '戊土',
           '기토': '己土', '경금': '庚金', '신금': '辛金', '임수': '壬水', '계수': '癸水'}
STEM_FULL_EN = {'갑목': '甲木 Yang Wood (Gapmok)', '을목': '乙木 Yin Wood (Eulmok)', '병화': '丙火 Yang Fire (Byeonghwa)', '정화': '丁火 Yin Fire (Jeonghwa)',
                '무토': '戊土 Yang Earth (Muto)', '기토': '己土 Yin Earth (Gito)', '경금': '庚金 Yang Metal (Gyeonggeum)', '신금': '辛金 Yin Metal (Singeum)',
                '임수': '壬水 Yang Water (Imsu)', '계수': '癸水 Yin Water (Gyesu)'}
MAJ_EN = ['The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor', 'The Hierophant', 'The Lovers',
          'The Chariot', 'Strength', 'The Hermit', 'Wheel of Fortune', 'Justice', 'The Hanged Man', 'Death', 'Temperance',
          'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun', 'Judgement', 'The World']
SU_EN = {'wands': 'Wands', 'cups': 'Cups', 'swords': 'Swords', 'pents': 'Pentacles'}
RK_EN = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Page', 'Knight', 'Queen', 'King']
POS_EN = ["Today's flow", 'What to keep', 'What to let go']
MON = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
PLAYLIST_URL = 'https://www.youtube.com/playlist?list=PLRm375HI5ZcA'
# tools/tarot/reel.py 기준: 세 번째 카드 이름까지 다 보이는 때 6.1초, 끝 장면으로 넘어가기 시작 7.5초(END)
THUMB_AT = 7.0
THUMB_WAIT = 90          # 처리 완료 확인 뒤 썸네일 넣기 전 추가로 쉬는 초


def make_thumb(folder):
    out = f'{folder}/short_thumb.jpg'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(THUMB_AT), '-i', f'{folder}/short_yt.mp4',
                    '-frames:v', '1', '-q:v', '3', out], check=True)
    if not os.path.exists(out) or os.path.getsize(out) > 2_000_000:
        sys.exit('멈춤: 썸네일(short_thumb.jpg)을 만들지 못했거나 2MB를 넘어요.')
    return out


def wait_processed(vid, limit=900):
    """영상 처리(processingStatus)가 succeeded 가 될 때까지 기다린다. 한도 1/회."""
    cloud.prepare(); g = cloud.load()
    yt, _ = g.login('goyo')
    t0 = time.time(); st = '?'
    while time.time() - t0 < limit:
        g.guard(1)
        r = yt.videos().list(part='processingDetails,status', id=vid).execute(); g.spend(1)
        it = (r.get('items') or [{}])[0]
        st = it.get('processingDetails', {}).get('processingStatus', '?')
        print('처리 상태:', st, int(time.time() - t0), '초')
        if st in ('succeeded', 'failed', 'terminated'):
            break
        time.sleep(30)
    cloud.finish()
    return st


def en_name(c):
    i = c['id']
    n = MAJ_EN[int(i[1:])] if i.startswith('m') else f"{RK_EN[int(i[-2:]) - 1]} of {SU_EN[i[:-2]]}"
    return n + (' (reversed)' if c.get('rev') else '')



def ig_post_url(date):
    """그날 06:00 타로 캐러셀 주소(posts/<날짜>-tarot/result.json). 못 찾으면 프로필 주소."""
    for name in (f'posts/{date}-tarot2/result.json', f'posts/{date}-tarot/result.json'):   # 다시 올린 판(tarot2)이 있으면 그쪽 우선
        try:
            txt = open(name, encoding='utf-8').read()
        except OSError:
            continue
        m = re.search(r'https://www\.instagram\.com/p/[A-Za-z0-9_-]+/?', txt)
        if m:
            return m.group(0).rstrip('/') + '/'
    return 'https://www.instagram.com/goyo_mio'


def build(date, folder):
    t = json.load(open(f'{folder}/tarot.json', encoding='utf-8'))
    y, m, d = map(int, date.split('-'))
    stem = re.search('|'.join(MUSIC), t['music']['title_html']).group(0)
    hz = re.search(r'\((.{2})\)', t['music']['title_html'])
    hz = f'({hz.group(1)})' if hz else ''
    cards = t['cards']
    ig = ig_post_url(date)
    ko_names = '·'.join(c['ko'] for c in cards)
    title = f"{m}월 {d}일 오늘의 타로｜{ko_names}｜Daily Tarot"
    desc = (f"{m}월 {d}일, 고요가 뽑은 오늘의 타로 세 장이에요.\n\n"
            f"🎧 지금 듣는 음악: 다섯 가지 고요 {stem}{hz} 편\n▶ https://youtu.be/{MUSIC[stem]}\n\n"
            "🔎 무료 사주 앱에서 내 오행을 찾고 그 오행의 음악을 들어 보세요.\n▶ https://goyomio.com\n\n"
            f"📺 고요 채널 · 오행음악 전체 듣기\n▶ {CHANNEL_URL}\n▶ {PLAYLIST_URL}\n\n"
            f"🃏 세 장의 풀이는 인스타 @goyo_mio 오늘의 타로 게시물에 있어요.\n▶ {ig}\n\n"
            + '\n'.join(f"{p} · {c['title']}" for p, c in zip(t['positions'], cards))
            + "\n\n#오늘의타로 #타로 #고요")
    en_title = f"Today's Tarot, {MON[m - 1]} {d}｜" + ' · '.join(en_name(c).replace(' (reversed)', '') for c in cards)
    if len(en_title) > 95:
        en_title = f"Today's Tarot, {MON[m - 1]} {d}｜Three Cards from GOYO"
    en_desc = (f"Today's three tarot cards, drawn by GOYO for {MON[m - 1]} {d}.\n\n"
               f"🎧 The music in this video: Five Kinds of Quiet · {STEM_FULL_EN[stem]}\n▶ https://youtu.be/{MUSIC[stem]}\n\n"
               "🔎 Find your element in our free saju (BaZi) app and listen to its music.\n▶ https://goyomio.com\n\n"
               f"📺 GOYO channel · all five-element music\n▶ {CHANNEL_URL}\n▶ {PLAYLIST_URL}\n\n"
               f"🃏 The full reading is in today's tarot post on Instagram @goyo_mio.\n▶ {ig}\n\n"
               + '\n'.join(f"{p} · {en_name(c)}" for p, c in zip(POS_EN, cards))
               + "\n\n#dailytarot #tarot #GOYO")
    pub = datetime.datetime(y, m, d, 1, 0, tzinfo=datetime.timezone.utc)   # 10:00 KST
    now = datetime.datetime.now(datetime.timezone.utc)
    if pub < now + datetime.timedelta(minutes=5):
        pub = (now + datetime.timedelta(minutes=15)).replace(second=0, microsecond=0)
    plan = [{"file": f'{folder}/short_yt.mp4', "thumb": "", "title": title, "description": desc,
             "tags": ['오늘의타로', '타로', '타로카드', 'daily tarot', '고요'],
             "publishAt": pub.strftime('%Y-%m-%dT%H:%M:%SZ'), "playlist": "쇼츠"}]
    loc = {"en": {"title": en_title, "description": en_desc}}
    bad = [k for k, v in (('제목', title), ('영어 제목', en_title)) if len(v) > 95]
    if bad:
        sys.exit(f'멈춤: 제목이 95자를 넘어요 {bad}')
    return plan, loc


def main():
    date = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else 'check'
    folder = sys.argv[3] if len(sys.argv) > 3 else f'posts/{date}-1000'
    plan, loc = build(date, folder)
    thumb = make_thumb(folder)
    print('썸네일:', thumb, f'({THUMB_AT}초 장면)')
    pp, lp = f'/tmp/yt_tarot_plan_{date}.json', f'/tmp/yt_tarot_loc_{date}.json'
    json.dump(plan, open(pp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('제목:', plan[0]['title'], f"({len(plan[0]['title'])}자)")
    print('영어 제목:', loc['en']['title'], f"({len(loc['en']['title'])}자)")
    print('공개:', plan[0]['publishAt'])
    if mode == 'check':
        print('\n--- 설명 ---\n' + plan[0]['description'] + '\n\n--- 영어 설명 ---\n' + loc['en']['description'])
        cloud.run(['goyo', 'shorts-upload', 'check', pp])
        return
    # ① 썸네일 없이 업로드
    g = cloud.run(['goyo', 'shorts-upload', 'all', pp])
    yt, channel = g.login('goyo')
    vids = [v for v in g.all_videos(yt, channel) if v['snippet']['title'] == plan[0]['title']]
    if len(vids) != 1:
        sys.exit(f'멈춤: 올린 영상을 제목으로 하나만 찾지 못했어요 ({len(vids)}개).')
    vid = vids[0]['id']
    cloud.finish()
    # ② 영어 번역
    json.dump({vid: loc}, open(lp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cloud.run(['goyo', 'loc-apply', 'all', lp])
    # ③ 처리 끝날 때까지 기다렸다가 다시 들어가 썸네일
    st = wait_processed(vid)
    if st != 'succeeded':
        print('주의: 처리 상태가', st, '— 그래도 썸네일을 넣어 봄')
    time.sleep(THUMB_WAIT)
    tp = f'/tmp/yt_tarot_thumb_{date}.json'
    json.dump([{"id": vid, "thumb": thumb}], open(tp, 'w', encoding='utf-8'))
    cloud.run(['goyo', 'thumb-set', 'all', tp])
    json.dump({"video_id": vid, "url": f"https://youtube.com/shorts/{vid}", "publishAt": plan[0]['publishAt'],
               "title": plan[0]['title'], "languages": ["ko", "en"], "thumb": "short_thumb.jpg", "thumb_at": THUMB_AT,
               "done": datetime.datetime.now().isoformat(timespec='seconds')},
              open(f'{folder}/yt_result.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('끝:', vid)


if __name__ == '__main__':
    if os.environ.get('YT_IN_VENV') != '1':
        import subprocess
        os.environ['YT_IN_VENV'] = '1'
        os.environ.setdefault('TZ', 'Asia/Seoul')
        sys.exit(subprocess.call([cloud._venv(), os.path.abspath(__file__)] + sys.argv[1:]))
    main()
