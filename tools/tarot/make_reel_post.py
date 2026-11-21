#!/usr/bin/env python3
"""오늘의 타로 릴스·쇼츠 만들기 (2026-11-21 미오 님 결정: 06:00 캐러셀 게시 뒤 만들어 두고 10:00에 릴스 게시)
사용: python3 tools/tarot/make_reel_post.py YYYY-MM-DD
 - 입력: posts/<날짜>-tarot/tarot.json (06:00 작업이 쓴 원고)
 - 출력: posts/<날짜>-1000/ 에 tarot.json 복사, reel.mp4(인스타), short_yt.mp4(유튜브 쇼츠), reel_first.jpg, post.json(approved)
"""
import json, os, re, shutil, subprocess, sys

date = sys.argv[1]
src = f'posts/{date}-tarot/tarot.json'
dst = f'posts/{date}-1000'
os.makedirs(dst, exist_ok=True)
shutil.copy(src, f'{dst}/tarot.json')
cfg = json.load(open(src, encoding='utf-8'))

for v in ('ig', 'yt'):
    subprocess.run(['python3', 'tools/tarot/reel.py', f'{dst}/tarot.json', v], check=True)

stem = re.search(r'(갑목|을목|병화|정화|무토|기토|경금|신금|임수|계수)', cfg['music']['title_html']).group(1)
hz = re.search(r'\((.{2})\)', cfg['music']['title_html'])
hz = f'({hz.group(1)})' if hz else ''
STEM_EN = {'갑목': 'Yang Wood (Gapmok)', '을목': 'Yin Wood (Eulmok)', '병화': 'Yang Fire (Byeonghwa)', '정화': 'Yin Fire (Jeonghwa)',
           '무토': 'Yang Earth (Muto)', '기토': 'Yin Earth (Gito)', '경금': 'Yang Metal (Gyeonggeum)', '신금': 'Yin Metal (Singeum)',
           '임수': 'Yang Water (Imsu)', '계수': 'Yin Water (Gyesu)'}
MON = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
y, m, d = map(int, date.split('-'))

cap = (f"{m}월 {d}일, 오늘의 타로.\n\n"
       "오늘 고요를 찾으시는 분들을 위해 뽑은 세 장이에요. 세 장의 풀이는 오늘 피드 게시물 「오늘의 타로」에 적어 두었어요.\n\n"
       "고요는 매일 아침 타로 세 장을 뽑아 풀어드려요. 무료 사주 앱에서 내 오행을 찾고, 그 오행의 음악을 들을 수 있어요. 앱과 음악은 프로필 링크에서 열 수 있어요.\n\n"
       f"이 영상에 깔린 소리는 다섯 가지 고요 {stem}{hz} 편이에요.\n\n"
       f"· English ·\nToday's Tarot, {MON[m - 1]} {d}.\n\n"
       "Three cards drawn for everyone who finds GOYO today. The full reading is in today's feed post, \"Today's Tarot.\"\n\n"
       "Every morning, GOYO draws three cards and reads them for you. Find your element in our free saju app and listen to its music. App and music: link in bio.\n\n"
       f"The music in this video is Five Kinds of Quiet · {STEM_EN[stem]}.\n\n"
       "#고요 #오늘의타로 #타로 #고요타로 #오행음악 #플레이리스트 #dailytarot #tarot")
json.dump({"type": "reel", "via": "api", "approved": True, "video_file": f"{dst}/reel.mp4", "caption": cap,
           "note": f"{m}/{d} 오늘의 타로 릴스(10:00). 06:00 작업이 make_reel_post.py 로 자동 생성. 같은 폴더 short_yt.mp4 는 유튜브 쇼츠용(미오 님이 올림)",
           "thumb_offset": 0},
          open(f'{dst}/post.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', dst)
