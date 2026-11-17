#!/usr/bin/env python3
"""고요 글 점검: 댓글 유도·효능·금지어·AI 말투 흔적. 사용: python3 tools/ko_check.py <파일 또는 post.json>... (없으면 posts/ 전체)
문제 있으면 줄마다 [종류] 위치: 문맥 을 출력하고 종료코드 1."""
import json, re, sys, glob, unicodedata
RULES=[
 ('댓글유도', r'댓글(로|에|을|를)?\s*(남겨|달아|적어|알려)|남겨\s?주세요|알려\s?주세요|적어\s?주세요|DM(으로)?\s*(보내|주세요)'),
 ('금지어', r'부적'),
 ('효능', r'운이\s?(바뀌|좋아지)|조후를\s?맞춰\s?(줘|드려|줍)|기운을\s?(채워|채운|보충)|효과가\s?있'),
 ('AI말투', r'—|여정|진정한|특별한 경험|마법 같은|선물 같은|깊이 있는|다채로운|한 걸음 더|놓치지 마세요|지금 바로'),
 ('대조반복', None),
]
INVIS=re.compile('[​-‏⁠-⁤﻿­]')
def check(name, text):
    bad=[]
    for k,pat in RULES:
        if pat:
            for m in re.finditer(pat,text): bad.append((k,text[max(0,m.start()-15):m.end()+10]))
    if len(re.findall('아니라',text))>=3: bad.append(('대조반복',f"'아니라' {len(re.findall('아니라',text))}번"))
    if INVIS.search(text): bad.append(('보이지않는문자','제거 필요'))
    return [(name,)+b for b in bad]
def texts(p):
    if p.endswith('post.json'):
        j=json.load(open(p)); yield p+':caption', j.get('caption','')
    elif p.endswith('.json'):
        yield p, json.dumps(json.load(open(p)),ensure_ascii=False)
    else: yield p, open(p).read()
paths=sys.argv[1:] or sorted(glob.glob('posts/*/post.json'))
out=[]; hooks={}
for p in paths:
    for n,t in texts(p):
        out+=check(n,t)
        if n.endswith(':caption') and t: hooks.setdefault(t.split('\n')[0].strip(),[]).append(n.split('/')[-2])
for h,ds in hooks.items():
    if len(ds)>1: out.append(('여러 게시물','첫줄중복',f'{h} ← {", ".join(ds)}'))
for o in out: print(f'[{o[1]}] {o[0]}: {o[2]}')
sys.exit(1 if out else 0)
