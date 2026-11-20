"""예시 사주 풀이 #2~#10 인스타 예약 폴더 만들기 (캐러셀 posts/D, 릴스 posts/D-1820).
python3 tools/week_src/example_posts.py"""
import json, os, re, shutil

PLAN = {  # 편 번호: (날짜, 주제 해시태그)
    '02': ('2026-11-25', '돈'), '03': ('2026-11-27', '인간관계'), '04': ('2026-11-29', '쉼'),
    '05': ('2026-12-02', '부업'), '06': ('2026-12-04', '진로'), '07': ('2026-12-06', '결혼'),
    '08': ('2026-12-09', '이사'), '09': ('2026-12-11', '시험'), '10': ('2026-12-13', '연애'),
}
HZ = {'갑목': '甲木', '을목': '乙木', '병화': '丙火', '정화': '丁火', '무토': '戊土', '기토': '己土',
      '경금': '庚金', '신금': '辛金', '임수': '壬水', '계수': '癸水'}
EN = lambda s: bool(re.match(r'^[A-Za-z]', s))


def texts(sl):
    ko = [it[0].replace('\n', ' ').replace(' ', ' ') for it in sl.get('items', []) if not EN(it[0])]
    en = [it[0].replace(' ', ' ') for it in sl.get('items', []) if EN(it[0])]
    return ko, en


def build(n):
    date, tag = PLAN[n]
    src = f'example_saju/{n}'
    S = json.load(open(f'{src}/slides.json', encoding='utf-8'))
    sl = S['slides']; num = int(n); music = S['music']
    q_ko = texts(sl[0])[0][1]; q_en = texts(sl[0])[1][1]
    birth_ko, birth_en = texts(sl[1])[0][0], texts(sl[1])[1][0]
    core_ko, core_en = texts(sl[2])
    ans_ko, ans_en = texts(sl[3])
    tags = [s.get('tag', '') for s in sl]
    when = [i + 1 for i, t in enumerate(tags) if t in ('언제', '쉬어 갈 때')]
    tarot = [i for i, t in enumerate(tags) if t.startswith('타로')]
    music_en = [e for e in texts([s for s in sl if s.get('tag') == '이 사주에 깔린 소리'][0])[1]][0]
    music_en = re.search(r'Five Kinds of Quiet · ([^.]+?)\.', music_en).group(1)
    b, sex = birth_ko.rsplit(' · ', 1)
    slides_ko = '장과 '.join(str(x) for x in when) + '장'
    slides_en = (f'slides {when[0]} and {when[1]}' if len(when) == 2 else f'slide {when[0]}')

    ko = (f"예시 사주 풀이 #{num} · {q_ko}\n\n"
          f"{b}에 태어난 {sex}, 예시로 만든 사주로 풀어 봤어요. {core_ko[0]} {core_ko[1]}\n\n"
          f"{ans_ko[0]} {ans_ko[1]} 달까지 짚은 시기는 {slides_ko}에 있어요.")
    en = (f"Example Saju Reading #{num} · {q_en}\n\n"
          f"This is an example chart: {(birth_en[0].lower() + birth_en[1:]).replace(' · ', ', ').replace(', Female', ', female').replace(', Male', ', male')}. {core_en[0]}\n\n"
          f"{ans_en[0]} The month-by-month timing is on {slides_en}.")
    if tarot:
        tk, te = texts(sl[tarot[0]])
        ko += f"\n이 사주를 위해 뽑은 타로 한 장은 {tk[0]}예요."
        en += f"\nThe tarot card drawn for this reading: {te[0].split(':')[0]}."
    ko += (f"\n\n이 사주에 깔린 소리는 다섯 가지 고요 {music}({HZ[music]}) 편이에요. 프로필 링크에서 들을 수 있어요.\n"
           f"내 사주 오행과 신살은 프로필 링크의 무료 앱에서 먼저 확인해 보세요.")
    en += (f"\n\nThe sound beneath this chart is Five Kinds of Quiet · {music_en}. Listen via the link in bio.\n"
           f"To see your own elements and stars, try the free app: link in bio.")
    hashtags = f"#고요 #예시사주 #사주풀이 #{tag} #사주 #명리학 #오행 #오행음악 #saju #fourpillars"
    cap = ko + "\n\n· English ·\n" + en + "\n\n" + hashtags

    files = sorted(f for f in os.listdir(src) if re.match(r'^\d\d\.jpg$', f))
    D = f'posts/{date}'
    if os.path.exists(f'{D}/post.json'):
        raise SystemExit(f'이미 게시물이 있어요: {D}')
    os.makedirs(D, exist_ok=True)
    for f in files: shutil.copy(f'{src}/{f}', f'{D}/{f}')
    json.dump({"type": "carousel", "via": "api", "approved": True, "files": [f'{D}/{f}' for f in files], "caption": cap,
               "note": f"예시 사주 풀이 #{num}. 원본 example_saju/{n}. 11/21 07:36 미오 님 「인스타에 맞게 수정해서 예약」 승인"},
              open(f'{D}/post.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    rk = (f"{q_ko}\n\n예시 사주로 풀어 봤어요. 해도 되는지, 언제가 나은지는 오늘 피드 게시물 「예시 사주 풀이 #{num}」에 달까지 짚어 두었어요.\n\n"
          f"이 영상에 깔린 소리는 다섯 가지 고요 {music}({HZ[music]}) 편이에요. 프로필 링크에서 들을 수 있어요.")
    re_ = (f"{q_en}\n\nWe read one example chart: whether to go ahead, and when, down to the month. "
           f"The full reading is in today's feed post, \"Example Saju Reading #{num}.\"\n\n"
           f"The music in this video is Five Kinds of Quiet · {music_en}. Listen via the link in bio.")
    R = f'posts/{date}-1820'
    if os.path.exists(f'{R}/post.json'):
        raise SystemExit(f'이미 게시물이 있어요: {R}')
    os.makedirs(R, exist_ok=True)
    json.dump({"type": "reel", "via": "api", "approved": True, "video_file": f'{src}/reel_ig_v2.mp4',
               "caption": rk + "\n\n· English ·\n" + re_ + f"\n\n#고요 #예시사주 #사주풀이 #{tag} #오행음악 #saju",
               "thumb_offset": 500,
               "note": f"예시 사주 풀이 #{num} 릴스. 인스타판 v2: 첫 장면 0초부터 보이게. 같은 날 18:00 캐러셀 뒤 18:20. 11/21 미오 님 승인"},
              open(f'{R}/post.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return cap


if __name__ == '__main__':
    import sys
    only = sys.argv[1:] or list(PLAN)
    for n in only:
        print('=====', n); print(build(n)[:700])
