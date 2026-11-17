#!/usr/bin/env python3
"""python3 tools/tarot/render.py posts/<date>-tarot/tarot.json
tarot.json: {"label":"11월 18일 · 오늘의 타로","positions":["오늘의 결","머물 것","내려놓을 것"],
 "cards":[{"id","ko","rev","file","title","text"}x3],"story":[문단...],"story_q":"질문 한 줄",
 "music":{"intro":"...","element":"화","title_html":"...","line":"..."}}
→ 같은 폴더에 01~06.jpg + story.jpg(1080x1920) 생성 (1909 원판 스캔, 역방향은 180도 회전)"""
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
# 1장: 표지(PIL, 새 디자인 2026-11-18 미오 님 승인) — 아래 main()에서 따로 그림
date_txt=cfg['label'].split('·')[0].strip()
slides=[None]
# 2장: 세 장을 한 화면에
cells=''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:18px"><img src="{s}" style="height:560px;width:auto;border-radius:12px"><div style="font-size:38px;color:#c9a96a">{p}</div></div>' for s,p in zip(imgs,cfg['positions']))
slides.append((f'<div class="step">오늘의 세 장</div><div style="display:flex;gap:28px;justify-content:center;margin-top:40px">{cells}</div>', ""))
for i,c in enumerate(cfg['cards']):
    slides.append((card(imgs[i])+f'<div class="step">{cfg["positions"][i]}</div><h2>{c["title"]}</h2><div class="rule" style="margin:22px 0"></div><p {P}>{c["text"]}</p>',""))
slides.append(('<div class="step">세 장의 이야기</div><div class="rule"></div>'+''.join(f'<p>{x}</p><br>' for x in cfg['story'])+f'<h2>{cfg["story_q"]}</h2>',""))
m=cfg['music']
slides.append(('<div class="step">오늘 어울리는 고요의 소리</div><div class="rule"></div>'
  f'<p>{m["intro"]}</p><br><h2 style="font-size:64px">{m["title_html"]}</h2><br><p>{m["line"]}</p>',""))

from PIL import ImageDraw, ImageFont
def cover(path, H=1350, foot=None):
    W=1080; sys.path.insert(0,os.path.join(root,'tools')); from tarot_reel import F
    im=Image.new('RGB',(W,H),(10,10,12)); dr=ImageDraw.Draw(im); oy=(H-1350)//2
    def ct(y,t,f,fill):
        w=dr.textlength(t,font=f); dr.text(((W-w)/2,y+oy),t,font=f,fill=fill)
    ct(330,'오늘의',F(170,True),(250,248,242)); ct(530,'타로',F(170,True),(250,248,242))
    ct(790,date_txt,F(62),(201,169,106))
    ct(900,'오늘 고요를 찾으시는 분께',F(58),(225,220,210)); ct(975,'건네는 말',F(58),(225,220,210))
    cg=ImageFont.truetype(os.path.join(root,'tools','fonts','CormorantGaramond-500.ttf'),60); sp=26
    ws=[dr.textlength(c,font=cg) for c in 'GOYO']; x=(W-sum(ws)-sp*3)/2
    for c,w in zip('GOYO',ws): dr.text((x,1150+oy),c,font=cg,fill=(200,190,170)); x+=w+sp
    if foot: ct(1290,foot,F(44),(170,165,155))
    im.save(path,quality=92)
async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        cover(f"{d}/01.jpg", H=1350)
        for i,sl in enumerate(slides,1):
            if sl is None: continue
            body,extra=sl
            html=BASE.replace("{body}",body).replace("{extra}",extra).replace("{page}",f"{i:02d} / {len(slides):02d}")
            await pg.set_content(html); await pg.wait_for_timeout(300)
            p=f"{d}/{i:02d}.png"; await pg.screenshot(path=p)
            Image.open(p).convert('RGB').save(f"{d}/{i:02d}.jpg",quality=92); os.remove(p)
        # 스토리용(1080x1920): 표지와 같은 디자인
        cover(f"{d}/story.jpg", H=1920, foot='오늘의 타로 이야기는 피드에 있어요')
        await b.close()
asyncio.run(main()); print('ok',len(slides))
