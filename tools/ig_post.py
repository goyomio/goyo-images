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
def wait(cid, tries=60):
    for _ in range(tries):
        s=call(f'{cid}?fields=status_code,status')
        if s.get('status_code')=='FINISHED': return
        if s.get('status_code')=='ERROR': print('ERR status',s); sys.exit(1)
        time.sleep(5)
    print('ERR timeout',cid); sys.exit(1)
def build(cfg):
    t=cfg['type']
    if t=='carousel':
        kids=[call(f'{IG}/media',{'image_url':u,'is_carousel_item':'true'})['id'] for u in cfg['urls']]
        for k in kids: wait(k)
        c=call(f'{IG}/media',{'media_type':'CAROUSEL','children':','.join(kids),'caption':cfg['caption']})
    elif t=='story':
        c=call(f'{IG}/media',{'media_type':'STORIES','image_url':cfg['urls'][0]})
    elif t=='reel':
        c=call(f'{IG}/media',{'media_type':'REELS','video_url':cfg['video'],'caption':cfg['caption'],'share_to_feed':'true'})
    else:
        c=call(f'{IG}/media',{'image_url':cfg['urls'][0],'caption':cfg['caption']})
    wait(c['id']); return c['id']
if __name__=='__main__':
    cfg=json.load(open(sys.argv[1])); cid=build(cfg)
    if '--dry' in sys.argv: print(json.dumps({'dry_container':cid})); sys.exit(0)
    r=call(f'{IG}/media_publish',{'creation_id':cid})
    print(json.dumps(call(f"{r['id']}?fields=permalink,timestamp"),ensure_ascii=False))
