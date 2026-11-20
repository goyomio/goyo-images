"""예시 사주 풀이 캐러셀 렌더: python3 tools/week_src/example_saju.py example_saju/01/slides.json"""
import json, sys, os
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1350; M = 70; LW = 4; R = 70
BG = (8, 8, 10); FG = (236, 233, 226); GOLD = (200, 180, 140); SOFT = (190, 186, 178); EN = (214, 210, 202)
EL = {'목': (88, 168, 96), '화': (214, 72, 60), '토': (222, 186, 70), '금': (236, 233, 226), '수': (10, 10, 12)}
HZ = dict(zip('甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥', '목목화화토토금금수수수토목목토화화토금금토수'))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LET = os.path.join(ROOT, 'tools/assets/goyo_letters')
def F(sz, bold=False): return ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSerifCJK-%s.ttc' % ('Bold' if bold else 'Regular'), sz, index=1)

def frame(im, d):
    d.line([(M+R, M), (W-M-R, M)], fill=FG, width=LW); d.line([(M+R, H-M), (W-M-R, H-M)], fill=FG, width=LW)
    d.line([(M, M+R), (M, H-M-R)], fill=FG, width=LW); d.line([(W-M, M+R), (W-M, H-M-R)], fill=FG, width=LW)
    for i, (cx, cy, a0) in enumerate([(M, M, 0), (W-M, M, 90), (M, H-M, 270), (W-M, H-M, 180)]):
        d.arc([cx-R, cy-R, cx+R, cy+R], a0, a0+90, fill=FG, width=LW)
        g = Image.open(os.path.join(LET, '%d_%s.png' % (i, 'GOYO'[i]))); s = 46 / g.height
        g = g.resize((max(1, int(g.width*s)), 46), Image.LANCZOS)
        tx = cx + (R*.28 if cx == M else -R*.28); ty = cy + (R*.28 if cy == M else -R*.28)
        im.alpha_composite(g, (int(tx-g.width/2), int(ty-g.height/2)))

def wrap(d, t, f, maxw):
    out = []
    for para in t.split('\n'):
        words = para.split(' '); line = ''
        for w in words:
            tt = (line + ' ' + w).strip()
            if d.textlength(tt, font=f) <= maxw: line = tt
            else: out.append(line); line = w
        out.append(line)
    return out

def block(d, items, top=None):
    """items: (kind, text, size, color, bold, gap_after)"""
    maxw = W - 2*M - 120; lines = []
    for kind, t, sz, col, bold, gap in items:
        f = F(sz, bold)
        for ln in wrap(d, t, f, maxw): lines.append((ln, f, col, int(sz*1.42)))
        lines.append(None if gap is None else ('', None, None, gap))
    total = sum(l[3] for l in lines if l); y = top if top is not None else (H - total)//2
    for l in lines:
        if not l: continue
        ln, f, col, lh = l; col = tuple(col) if col else col
        if f:
            w = d.textlength(ln, font=f)
            sw = 2 if col == FG else 0
            d.text(((W-w)/2, y), ln, font=f, fill=col, stroke_width=sw, stroke_fill=(10, 10, 14))
        y += lh

def pillars(d, y, pil):
    labels = ['태어난 해', '달', '날', '시']; cw = 190; x0 = (W - cw*4)/2
    for i, p in enumerate(pil.split()):
        cx = x0 + cw*i + cw/2
        lf = F(32); w = d.textlength(labels[i], font=lf); d.text((cx-w/2, y), labels[i], font=lf, fill=SOFT)
        for j, ch in enumerate(p):
            col = EL[HZ[ch]]; f = F(110, True); w = d.textlength(ch, font=f)
            stroke = FG if HZ[ch] == '수' else (10, 10, 14)
            d.text((cx-w/2, y+56+j*132), ch, font=f, fill=col, stroke_width=3, stroke_fill=stroke)
    return y + 56 + 2*132 + 20

def card(im, d, s, top):
    """타로 장: s['card'] = {'file': 'deck_1909/m06_lovers.jpg', 'reversed': false, 'h': 600}. 그림 아래 y를 돌려줌."""
    c = s['card']; g = Image.open(os.path.join(ROOT, c['file'])).convert('RGB'); h = c.get('h', 600)
    g = g.resize((int(g.width * h / g.height), h), Image.LANCZOS)
    if c.get('reversed'): g = g.rotate(180)
    x = (W - g.width) // 2; im.paste(g, (x, top)); d.rectangle([x-1, top-1, x+g.width, top+h], outline=SOFT, width=2)
    return top + h

def draw_slide(s, k, n):
    im = Image.new('RGBA', (W, H), BG + (255,)); d = ImageDraw.Draw(im); frame(im, d)
    tag = s.get('tag')
    if tag:
        f = F(34); w = d.textlength(tag, font=f); d.text(((W-w)/2, M+90), tag, font=f, fill=GOLD)
    items = [('k', x, sz, c, b, g) for x, sz, c, b, g in s['items']]
    if s.get('pillars'):
        y = pillars(d, 330, s['pillars']); block(d, items, top=y+30)
    elif s.get('card'):
        y = card(im, d, s, M + 160); block(d, items, top=y+36)
    else:
        block(d, items)
    pg = '%02d / %02d' % (k, n); f = F(24); w = d.textlength(pg, font=f)
    d.text((W-M-90-w, H-M-58), pg, font=f, fill=(110, 106, 100))
    return im.convert('RGB')

def render(js):
    cfg = json.load(open(js, encoding='utf-8')); out = os.path.dirname(js)
    for k, s in enumerate(cfg['slides'], 1):
        draw_slide(s, k, len(cfg['slides'])).save(os.path.join(out, '%02d.jpg' % k), quality=92)
    print('ok', len(cfg['slides']))

if __name__ == '__main__': render(sys.argv[1])
