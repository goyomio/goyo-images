#!/usr/bin/env python3
"""python3 tools/tarot/render.py posts/<date>-tarot/tarot.json
tarot.json: {"label":"11월 18일 · 고요의 세 장","positions":["오늘의 결","머물 것","내려놓을 것"],
 "cards":[{"id","ko","rev","file","title","text"}x3],"story":[문단...],"story_q":"질문 한 줄",
 "music":{"intro":"...","element":"화","title_html":"...","line":"..."}}
→ 같은 폴더에 01~06.jpg 생성 (1909 원판 스캔, 역방향은 180도 회전)"""
import asyncio, base64, json, os, sys, io
from PIL import Image
here=os.path.dirname(os.path.abspath(__file__)); root=os.path.abspath(os.path.join(here,'..','..'))
exec(open(os.path.join(root,'tools','slide_base.py')).read())
cfg_path=sys.argv[1]; d=os.path.dirname(cfg_path); cfg=json.load(open(cfg_path))
def b64(c):
    im=Image.open(os.path.join(root,'deck_1909',c['file'])).convert('RGB')
    if c.get('rev'): im=im.rotate(180)
    buf=io.BytesIO(); im.save(buf,'JPEG',quality=90); return 'data:image/jpeg;base64,'+base64.b64encode(buf.getvalue()).decode()
imgs=[b64(c) for c in cfg['cards']]
card=lambda s,h=500: f'<img src="{s}" style="height:{h}px;width:auto;align-self:flex-start;border-radius:10px;display:block;margin-bottom:34px">'
P='style="font-size:42px;line-height:1.6"'
slides=[(f'<div class="step">{cfg["label"]}</div>'
  f'<div style="display:flex;gap:26px;margin:20px 0 50px">{"".join(card(s,400) for s in imgs)}</div>'
  '<h2>오늘, 고요를 찾아온<br>사람들에게 건네는 이야기</h2>', SWIPE)]
for i,c in enumerate(cfg['cards']):
    slides.append((card(imgs[i])+f'<div class="step">{cfg["positions"][i]}</div><h2>{c["title"]}</h2><div class="rule" style="margin:22px 0"></div><p {P}>{c["text"]}</p>',""))
slides.append(('<div class="step">세 장의 이야기</div><div class="rule"></div>'+''.join(f'<p>{x}</p><br>' for x in cfg['story'])+f'<h2>{cfg["story_q"]}</h2>',""))
m=cfg['music']
slides.append(('<div class="step">오늘 어울리는 고요의 결</div><div class="rule"></div>'
  f'<p>{m["intro"]}</p><br><h2 style="font-size:64px">{m["title_html"]}</h2><br><p>{m["line"]}</p>',""))
async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for i,(body,extra) in enumerate(slides,1):
            html=BASE.replace("{body}",body).replace("{extra}",extra).replace("{page}",f"{i:02d} / {len(slides):02d}")
            await pg.set_content(html); await pg.wait_for_timeout(300)
            p=f"{d}/{i:02d}.png"; await pg.screenshot(path=p)
            Image.open(p).convert('RGB').save(f"{d}/{i:02d}.jpg",quality=92); os.remove(p)
        await b.close()
asyncio.run(main()); print('ok',len(slides))
