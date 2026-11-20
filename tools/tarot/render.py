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
# 영어 (2026-11-18 미오 님: 모든 게시물에 영어). 카드 영어 이름은 코드에서 정함(1909 원판 표준 이름)
MAJ_EN=['The Fool','The Magician','The High Priestess','The Empress','The Emperor','The Hierophant','The Lovers','The Chariot','Strength','The Hermit','Wheel of Fortune','Justice','The Hanged Man','Death','Temperance','The Devil','The Tower','The Star','The Moon','The Sun','Judgement','The World']
SU_EN={'wands':'Wands','cups':'Cups','swords':'Swords','pents':'Pentacles'}
RK_EN=['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Page','Knight','Queen','King']
def card_en(c):
    i=c['id']; n=MAJ_EN[int(i[1:])] if i.startswith('m') else f"{RK_EN[int(i[-2:])-1]} of {SU_EN[i[:-2]]}"
    return n+(', reversed' if c.get('rev') else '')
POS_EN=["Today's flow","What to keep","What to let go"]
MON_EN=['January','February','March','April','May','June','July','August','September','October','November','December']
import re as _re
_m=_re.search(r'(\d{4})-(\d{2})-(\d{2})',os.path.abspath(d))
date_en=f"{MON_EN[int(_m.group(2))-1]} {int(_m.group(3))}" if _m else ''
EN_S='style="font-family:Logo,serif;font-size:34px;color:#9a958b;letter-spacing:.04em"'
card=lambda s,h=500: f'<img src="{s}" style="height:{h}px;width:auto;align-self:flex-start;border-radius:10px;display:block;margin-bottom:34px">'
P='style="font-size:42px;line-height:1.6"'
# 1장: 표지(PIL, 2026-11-21 미오 님: 「오늘의 타로」+세 장 카드) — 아래 main()에서 따로 그림
date_txt=cfg['label'].split('·')[0].strip()
slides=[None]
# 2장: 세 장을 한 화면에
cells=''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:18px"><img src="{s}" style="height:560px;width:auto;border-radius:12px"><div style="font-size:38px;color:#c9a96a">{p}</div><div {EN_S}>{pe}</div></div>' for s,p,pe in zip(imgs,cfg['positions'],POS_EN))
slides.append((f'<div class="step">오늘의 세 장 <span style="font-family:Logo,serif;letter-spacing:.06em">· Today\'s three cards</span></div><div style="display:flex;gap:28px;justify-content:center;margin-top:40px">{cells}</div>', ""))
for i,c in enumerate(cfg['cards']):
    slides.append((card(imgs[i])+f'<div class="step">{cfg["positions"][i]} <span style="font-family:Logo,serif;letter-spacing:.06em">· {POS_EN[i]}</span></div><h2>{c["title"]}</h2><div {EN_S}>{card_en(c)}</div><div class="rule" style="margin:22px 0"></div><p {P}>{c["text"]}</p>',""))
slides.append(('<div class="step">세 장의 이야기</div><div class="rule"></div>'+''.join(f'<p>{x}</p><br>' for x in cfg['story'])+f'<h2>{cfg["story_q"]}</h2>',""))
m=cfg['music']
slides.append(('<div class="step">오늘 어울리는 고요의 소리</div><div class="rule"></div>'
  f'<p>{m["intro"]}</p><br><h2 style="font-size:64px">{m["title_html"]}</h2><br><p>{m["line"]}</p>',""))

from PIL import ImageDraw, ImageFont
def cover(path, H=1350, foot=None):
    """표지 (2026-11-21 미오 님: 「오늘의 타로」 + 그날 뽑은 세 장을 첫 화면에)"""
    W=1080; sys.path.insert(0,os.path.join(root,'tools')); from tarot_reel import F
    im=Image.new('RGB',(W,H),(10,10,12)); dr=ImageDraw.Draw(im); oy=(H-1350)//2
    def ct(y,t,f,fill):
        w=dr.textlength(t,font=f); dr.text(((W-w)/2,y+oy),t,font=f,fill=fill)
    ct(70,'오늘의 타로',F(132,True),(250,248,242))
    ct(250,date_txt,F(54),(201,169,106))
    # 세 장
    ch=520; gap=30; cims=[]
    for c in cfg['cards']:
        ci=Image.open(os.path.join(root,'deck_1909',c['file'])).convert('RGB')
        if c.get('rev'): ci=ci.rotate(180)
        cims.append(ci.resize((int(ci.width*ch/ci.height),ch),Image.LANCZOS))
    tw=sum(c.width for c in cims)+gap*2; x=(W-tw)//2; y=350+oy
    for ci in cims:
        im.paste(ci,(x,y)); x+=ci.width+gap
    ct(940,'오늘 고요를 찾으시는 분께 건네는 말',F(46),(225,220,210))
    ce=ImageFont.truetype(os.path.join(root,'tools','fonts','CormorantGaramond-500.ttf'),46)
    ct(1015,f"Today's Tarot · {date_en}" if date_en else "Today's Tarot",ce,(170,165,155))
    # GOYO: 채널 배너 워드마크에서 잘라 둔 글자 그림(글꼴로 치지 않음)
    gl=[Image.open(os.path.join(root,'tools','assets','goyo_letters',f'{i}_{ch_}.png')).convert('RGBA') for i,ch_ in enumerate('GOYO')]
    gh=50; gl=[g.resize((max(1,int(g.width*gh/g.height)),gh),Image.LANCZOS) for g in gl]; sp=22
    x=(W-sum(g.width for g in gl)-sp*3)//2; base=im.convert('RGBA')
    for g in gl: base.alpha_composite(g,(x,1110+oy)); x+=g.width+sp
    im=base.convert('RGB'); dr=ImageDraw.Draw(im)
    if foot: ct(1250,foot,F(44),(170,165,155))
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
