#!/usr/bin/env python3
"""goyo_mio 인스타 업로드 (Instagram Graph API). 사용: python3 ig_post.py <post.json> [--dry]
post.json: {"type":"carousel"|"reel"|"image"|"story","urls":[...]|"video":url,"caption":str}
토큰: goyo-keys/ig_token.txt (비공개 저장소). --dry 는 컨테이너만 만들고 게시하지 않음."""
import json, sys, time, urllib.request, urllib.parse, os
IG='17841458898232975'; V='v23.0'
KEY=os.environ.get('GOYO_TOKEN_FILE') or next(p for p in ['/home/claude/goyo-keys/ig_token.txt','../goyo-keys/ig_token.txt',os.path.expanduser('~/goyo-keys/ig_token.txt')] if os.path.exists(p))
T=open(KEY).read().strip()
def call(path, data=None):
    url=f'https://graph.facebook.com/{V}/{path}'
    if data is None:
        url+=('&' if '?' in url else '?')+'access_token='+T; req=urllib.request.Request(url)
    else:
        req=urllib.request.Request(url, urllib.parse.urlencode(dict(data,access_token=T)).encode())
    try: return json.load(urllib.request.urlopen(req, timeout=180))
    except urllib.error.HTTPError as e: print('ERR', e.read().decode()); sys.exit(1)
PACE=int(os.environ.get('GOYO_PACE','8'))  # 요청 사이 쉬는 초 (너무 빠르면 2207051·다운로드 시간 초과)
def wait(cid, tries=60):
    for _ in range(tries):
        s=call(f'{cid}?fields=status_code,status')
        if s.get('status_code')=='FINISHED': return
        if s.get('status_code')=='ERROR': print('ERR status',s); sys.exit(1)
        time.sleep(10)
    print('ERR timeout',cid); sys.exit(1)
def build(cfg):
    t=cfg['type']
    if t=='carousel':
        # 천천히: 한 장씩 만들고 다 될 때까지 기다린 뒤 다음 장 (2026-11-23 미오 님 요청)
        kids=[]
        for u in cfg['urls']:
            k=call(f'{IG}/media',{'image_url':u,'is_carousel_item':'true'})['id']
            time.sleep(PACE); wait(k); kids.append(k); time.sleep(PACE)
        c=call(f'{IG}/media',{'media_type':'CAROUSEL','children':','.join(kids),'caption':cfg['caption']})
        time.sleep(PACE)
    elif t=='story':
        c=call(f'{IG}/media',{'media_type':'STORIES','image_url':cfg['urls'][0]})
    elif t=='reel':
        prm={'media_type':'REELS','video_url':cfg['video'],'caption':cfg['caption'],'share_to_feed':'true'}
        if cfg.get('thumb_offset') is not None: prm['thumb_offset']=str(int(cfg['thumb_offset']))
        if cfg.get('cover'): prm['cover_url']=cfg['cover']
        c=call(f'{IG}/media',prm)
    else:
        c=call(f'{IG}/media',{'image_url':cfg['urls'][0],'caption':cfg['caption']})
    wait(c['id']); return c['id']
if __name__=='__main__':
    cfg=json.load(open(sys.argv[1])); cid=build(cfg)
    if '--dry' in sys.argv: print(json.dumps({'dry_container':cid})); sys.exit(0)
    time.sleep(PACE*2)  # 컨테이너 준비 뒤 게시 전 한숨 쉬기
    r=call(f'{IG}/media_publish',{'creation_id':cid})
    time.sleep(PACE*2)  # 게시 직후 바로 조회하지 않기
    print(json.dumps(call(f"{r['id']}?fields=permalink,timestamp"),ensure_ascii=False))
