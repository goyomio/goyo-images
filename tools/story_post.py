#!/usr/bin/env python3
"""스토리 게시: 이미지 한 장을 1080x1920 검정 바탕에 가운데 놓아 스토리로 올린다.
사용: python3 tools/story_post.py posts/<폴더>/story.jpg (render.py가 만든 세로판, 없으면 01.jpg를 넣으면 검정 여백으로 세로판을 만듦)
결과: posts/<폴더>/story.jpg, posts/<폴더>/story_result.json (ok:true면 다시 올리지 않음)"""
import json, os, subprocess, sys, urllib.parse
from PIL import Image
src=sys.argv[1]; d=os.path.dirname(src); out=os.path.join(d,'story.jpg'); res=os.path.join(d,'story_result.json')
if os.path.exists(res) and json.load(open(res)).get('ok'): print('이미 올림', res); sys.exit(0)
im=Image.open(src).convert('RGB')
if im.size!=(1080,1920):
    im=im.resize((1080, round(im.height*1080/im.width)))
    bg=Image.new('RGB',(1080,1920),(0,0,0)); bg.paste(im,(0,(1920-im.height)//2)); im=bg
im.save(out,quality=92)
R=lambda *a: subprocess.run(a,check=True,capture_output=True,text=True).stdout.strip()
R('git','add',out); subprocess.run(['git','commit','-qm',f'스토리 이미지 {d}\n\nCo-Authored-By: Claude <noreply@anthropic.com>']); R('git','push','-q')
h=R('git','rev-parse','HEAD')
url=f'https://raw.githubusercontent.com/goyomio/goyo-images/{h}/'+urllib.parse.quote(out)
cfg=os.path.join(d,'_story.json'); json.dump({'type':'story','urls':[url]},open(cfg,'w'))
r=subprocess.run([sys.executable,'tools/ig_post.py',cfg],capture_output=True,text=True); os.remove(cfg)
ok=r.returncode==0 and 'ERR' not in r.stdout
json.dump({'ok':ok,'out':r.stdout.strip()[-400:]},open(res,'w'),ensure_ascii=False)
R('git','add',res); R('git','commit','-qm',f'스토리 결과 {d}\n\nCo-Authored-By: Claude <noreply@anthropic.com>'); R('git','push','-q')
print('성공' if ok else '실패', r.stdout.strip()[-300:])
