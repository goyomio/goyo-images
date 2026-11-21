#!/usr/bin/env python3
"""오늘의 타로 유튜브 쇼츠 자동 업로드 (2026-11-21 미오 님 결정)

  python3 tools/youtube/tarot_short.py YYYY-MM-DD [check|all] [폴더]

 - 입력: posts/<날짜>-1000/ (make_reel_post.py 가 만든 short_yt.mp4, reel_first.jpg, tarot.json)
 - 순서(반드시): ① 썸네일 없이 업로드(비공개+예약) → ② 영어 번역 넣기 → ③ 썸네일 넣기
   (썸네일을 먼저 넣으면 번역 뒤에 썸네일이 빠지는 일이 있었음, 11/21)
 - 공개: 그날 10:00 KST (인스타 릴스와 같은 시각). 이미 지났으면 지금부터 15분 뒤.
 - 언어: 기본 한국어 + 영어 번역 1개만 (미오 님 11/21: 타로는 한영만).
 - 재생목록 「쇼츠」, AI 사용 「예」, 아동용 아님, 카테고리 음악.
 - 결과: posts/<날짜>-1000/yt_result.json. 같은 제목이 이미 있으면 올리지 않는다(중복 방지).
 - 끝나면 호출한 작업이 log/youtube/ 와 yt_result.json 을 커밋·푸시한다.
"""
import datetime, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cloud  # noqa: E402

MUSIC = {'갑목': 'g3Eeu8QVaJY', '을목': 'jtYiLzQkUJs', '병화': 'oIt-DzA96Bw', '정화': 'xDGOypKeG_s', '무토': 'q8w4WV76ah4',
         '기토': '8hLmKk8ag08', '경금': 'VzDuEs2i5es', '신금': '6p_X4z3terE', '임수': 'm_t33eB1bkc', '계수': 'wzt4ETUmOto'}
STEM_EN = {'갑목': 'Gapmok', '을목': 'Eulmok', '병화': 'Byeonghwa', '정화': 'Jeonghwa', '무토': 'Muto',
           '기토': 'Gito', '경금': 'Gyeonggeum', '신금': 'Singeum', '임수': 'Imsu', '계수': 'Gyesu'}
STEM_FULL_EN = {'갑목': 'Yang Wood (Gapmok)', '을목': 'Yin Wood (Eulmok)', '병화': 'Yang Fire (Byeonghwa)', '정화': 'Yin Fire (Jeonghwa)',
                '무토': 'Yang Earth (Muto)', '기토': 'Yin Earth (Gito)', '경금': 'Yang Metal (Gyeonggeum)', '신금': 'Yin Metal (Singeum)',
                '임수': 'Yang Water (Imsu)', '계수': 'Yin Water (Gyesu)'}
MAJ_EN = ['The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor', 'The Hierophant', 'The Lovers',
          'The Chariot', 'Strength', 'The Hermit', 'Wheel of Fortune', 'Justice', 'The Hanged Man', 'Death', 'Temperance',
          'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun', 'Judgement', 'The World']
SU_EN = {'wands': 'Wands', 'cups': 'Cups', 'swords': 'Swords', 'pents': 'Pentacles'}
RK_EN = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Page', 'Knight', 'Queen', 'King']
POS_EN = ["Today's flow", 'What to keep', 'What to let go']
MON = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
PLAYLIST_URL = 'https://www.youtube.com/playlist?list=PLRm375HI5ZcA'


def en_name(c):
    i = c['id']
    n = MAJ_EN[int(i[1:])] if i.startswith('m') else f"{RK_EN[int(i[-2:]) - 1]} of {SU_EN[i[:-2]]}"
    return n + (' (reversed)' if c.get('rev') else '')


def build(date, folder):
    t = json.load(open(f'{folder}/tarot.json', encoding='utf-8'))
    y, m, d = map(int, date.split('-'))
    stem = re.search('|'.join(MUSIC), t['music']['title_html']).group(0)
    hz = re.search(r'\((.{2})\)', t['music']['title_html'])
    hz = f'({hz.group(1)})' if hz else ''
    cards = t['cards']
    ko_names = '·'.join(c['ko'] for c in cards)
    title = f"{m}월 {d}일 오늘의 타로｜{ko_names}｜Daily Tarot"
    desc = (f"{m}월 {d}일, 고요가 뽑은 오늘의 타로 세 장이에요.\n\n"
            + '\n'.join(f"{p} · {c['title']}" for p, c in zip(t['positions'], cards))
            + "\n\n세 장의 풀이는 인스타 @goyo_mio 오늘의 타로 게시물에 있어요.\n▶ https://www.instagram.com/goyo_mio\n\n"
            f"지금 듣는 음악은 다섯 가지 고요 {stem}{hz} 편이에요.\n▶ https://youtu.be/{MUSIC[stem]}\n\n"
            "무료 사주 앱에서 내 오행을 찾고 그 오행의 음악을 들어 보세요.\n▶ https://goyomio.com\n\n"
            f"고요 오행음악 전체 듣기\n▶ {PLAYLIST_URL}\n\n"
            "#오늘의타로 #타로 #고요")
    en_title = f"Today's Tarot, {MON[m - 1]} {d}｜" + ' · '.join(en_name(c).replace(' (reversed)', '') for c in cards)
    if len(en_title) > 95:
        en_title = f"Today's Tarot, {MON[m - 1]} {d}｜Three Cards from GOYO"
    en_desc = (f"Today's three tarot cards, drawn by GOYO for {MON[m - 1]} {d}.\n\n"
               + '\n'.join(f"{p} · {en_name(c)}" for p, c in zip(POS_EN, cards))
               + "\n\nThe full reading is in today's tarot post on Instagram @goyo_mio.\n▶ https://www.instagram.com/goyo_mio\n\n"
               f"The music in this video is Five Kinds of Quiet · {STEM_FULL_EN[stem]}.\n▶ https://youtu.be/{MUSIC[stem]}\n\n"
               "Find your element in our free saju (BaZi) app and listen to its music.\n▶ https://goyomio.com\n\n"
               f"All GOYO five-element music\n▶ {PLAYLIST_URL}\n\n"
               "#dailytarot #tarot #GOYO")
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
    # ③ 썸네일
    tp = f'/tmp/yt_tarot_thumb_{date}.json'
    json.dump([{"id": vid, "thumb": f'{folder}/reel_first.jpg'}], open(tp, 'w', encoding='utf-8'))
    cloud.run(['goyo', 'thumb-set', 'all', tp])
    json.dump({"video_id": vid, "url": f"https://youtube.com/shorts/{vid}", "publishAt": plan[0]['publishAt'],
               "title": plan[0]['title'], "languages": ["ko", "en"], "thumb": "reel_first.jpg",
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
