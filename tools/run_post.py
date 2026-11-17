#!/usr/bin/env python3
"""예약 실행용: python3 tools/run_post.py 2026-11-17 [--dry]
posts/<date>/post.json 의 files/video_file 을 현재 커밋의 raw URL로 바꿔 ig_post 로 올리고 결과를 posts/<date>/result.json 에 남김."""
import json,sys,subprocess,urllib.parse,os,datetime
date=sys.argv[1]; d=f'posts/{date}'
cfg=json.load(open(f'{d}/post.json'))
if cfg['type']=='reel':
    _c=subprocess.run(['python3','tools/reel_check.py',f'{d}/post.json'])
    if _c.returncode: sys.exit('곡 이름 점검 실패: 게시하지 않았어요')
H=subprocess.check_output(['git','rev-parse','HEAD']).decode().strip()
raw=lambda p:f'https://raw.githubusercontent.com/goyomio/goyo-images/{H}/'+urllib.parse.quote(p)
out={'type':cfg['type'],'caption':cfg['caption']}
if cfg['type']=='carousel': out['urls']=[raw(p) for p in cfg['files']]
else: out['video']=raw(cfg['video_file'])
json.dump(out,open('/tmp/_post.json','w'),ensure_ascii=False)
print(json.dumps(out,ensure_ascii=False)[:300])
args=['python3','tools/ig_post.py','/tmp/_post.json']+(['--dry'] if '--dry' in sys.argv else [])
r=subprocess.run(args,capture_output=True,text=True); print(r.stdout,r.stderr)
if '--dry' not in sys.argv:
    json.dump({'when':datetime.datetime.now(datetime.timezone.utc).isoformat(),'via':'api','ok':r.returncode==0,'out':r.stdout.strip()[-500:]},open(f'{d}/result.json','w'),ensure_ascii=False,indent=1)
sys.exit(r.returncode)
