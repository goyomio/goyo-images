#!/usr/bin/env python3
"""그림이 있는 사주 릴스(1080x1920). 배경 그림은 코드로 직접 그린 원본(복숭아꽃 가지 등),
꽃잎이 천천히 떨어지고 글줄은 한 줄씩 떠오른다. 음악은 기존 쇼츠 음원을 그대로 깐다.
python3 tools/saju_reel.py <config.json> <out.mp4>
config: {"audio","theme":"blossom|stars|road|lamp|moon","scenes":[{"sec","small","big":[...],"big_size","after":[...],"en"}]}"""
import json, math, os, random, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarot_reel import F, W, H, FPS, GOLD, SOFT, DIM, ROOT
from PIL import Image, ImageDraw, ImageFilter, ImageChops

R = random.Random(7)
PINK, PINK2, CORE = (240, 168, 186), (252, 214, 222), (255, 236, 196)

def gradient():
    bg = Image.new('RGB', (W, H), (12, 14, 22))
    glow = Image.new('L', (W, H), 0)
    ImageDraw.Draw(glow).ellipse([-300, 300, W + 300, 1700], fill=80)
    glow = glow.filter(ImageFilter.GaussianBlur(260))
    bg.paste(Image.new('RGB', (W, H), (58, 44, 60)), mask=glow)
    return bg

def blossom(d, x, y, r, rot, col):
    for k in range(5):
        a = rot + k * 2 * math.pi / 5
        cx, cy = x + math.cos(a) * r * 0.62, y + math.sin(a) * r * 0.62
        d.ellipse([cx - r * 0.55, cy - r * 0.55, cx + r * 0.55, cy + r * 0.55], fill=col)
    d.ellipse([x - r * 0.22, y - r * 0.22, x + r * 0.22, y + r * 0.22], fill=CORE)

def branch_layer():
    """오른쪽 위에서 들어오는 복숭아 가지 (RGBA, 화면보다 약간 크게: 줌용)."""
    LW, LH = int(W * 1.12), int(H * 1.12)
    ink = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); d = ImageDraw.Draw(ink)
    flowers = []
    def grow(x, y, ang, length, width, depth):
        if depth == 0 or length < 18:
            flowers.append((x, y)); return
        pts = [(x, y)]
        for s in range(6):
            ang += R.uniform(-0.18, 0.18)
            x += math.cos(ang) * length / 6; y += math.sin(ang) * length / 6
            pts.append((x, y))
        for a, b in zip(pts, pts[1:]):
            d.line([a, b], fill=(46, 32, 30, 255), width=max(2, int(width)))
        if depth <= 3 and R.random() < 0.7: flowers.append((x, y))
        n = 2 if depth > 2 else R.choice([1, 2, 2, 3])
        for _ in range(n):
            grow(x, y, ang + R.uniform(-0.75, 0.75), length * R.uniform(0.6, 0.78), width * 0.66, depth - 1)
    grow(LW + 20, 160, math.pi * 0.86, 420, 26, 6)
    grow(LW + 20, 520, math.pi * 1.02, 300, 16, 5)
    grow(-20, LH - 260, -math.pi * 0.18, 300, 18, 5)
    glow = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
    fl = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); f = ImageDraw.Draw(fl)
    for (x, y) in flowers:
        for _ in range(R.choice([1, 1, 2])):
            ox, oy = R.uniform(-22, 22), R.uniform(-22, 22); r = R.uniform(13, 24)
            g.ellipse([x + ox - r * 2, y + oy - r * 2, x + ox + r * 2, y + oy + r * 2], fill=(240, 160, 180, 60))
            blossom(f, x + ox, y + oy, r, R.uniform(0, 6.3), PINK if R.random() < 0.6 else PINK2)
    glow = glow.filter(ImageFilter.GaussianBlur(28))
    out = Image.alpha_composite(glow, ink); out = Image.alpha_composite(out, fl)
    # 글자 자리(가운데 띠, 머리글)는 그림을 옅게 비워 둔다
    hole = Image.new('L', (LW, LH), 0); hd = ImageDraw.Draw(hole)
    ox, oy = (LW - W) // 2, (LH - H) // 2
    hd.rectangle([ox - 100, oy + 640, ox + W + 100, oy + 1360], fill=235)
    hd.rectangle([ox + 220, oy + 150, ox + W - 220, oy + 330], fill=200)
    hole = hole.filter(ImageFilter.GaussianBlur(90))
    a = ImageChops.multiply(out.getchannel('A'), ImageChops.invert(hole)); out.putalpha(a)
    return out

class Petals:
    def __init__(s, n=26):
        s.p = [dict(x=R.uniform(0, W), y=R.uniform(-H, H), v=R.uniform(40, 90), sw=R.uniform(20, 60),
                    ph=R.uniform(0, 6.3), r=R.uniform(7, 13), rot=R.uniform(0, 6.3), c=PINK if R.random() < .6 else PINK2)
               for _ in range(n)]
    def draw(s, im, t):
        lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for q in s.p:
            y = (q['y'] + q['v'] * t) % (H + 100) - 50
            x = q['x'] + math.sin(t * 0.9 + q['ph']) * q['sw']
            a = q['rot'] + t * 0.8; r = q['r']
            dx, dy = math.cos(a) * r, math.sin(a) * r * 0.5
            d.ellipse([x - abs(dx) - 3, y - abs(dy) - 3, x + abs(dx) + 3, y + abs(dy) + 3], fill=q['c'] + (190,))
        im.alpha_composite(lay)

def text_layer(cfg, sc, t):
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    def ct(y, s, f, col, a, stroke=0):
        if a <= 0: return
        w = d.textlength(s, font=f)
        d.text(((W - w) / 2 + 3, y + 3), s, font=f, fill=(0, 0, 0, int(160 * a)))
        d.text(((W - w) / 2, y), s, font=f, fill=col + (int(255 * a),), stroke_width=stroke, stroke_fill=(255, 255, 255, int(255 * a)))
    ct(200, cfg.get('header', '사주 · 오행음악 · 고요'), F(cfg.get('header_size', 46), True), SOFT, 1)
    ct(200 + cfg.get('header_size', 46) + 18, "FIVE ELEMENTS MUSIC", F(28), DIM, 1)
    lines = []
    def fit(s, size, bold=False):
        f = F(size, bold)
        while d.textlength(s, font=f) > W - 90 and size > 24:
            size -= 2; f = F(size, bold)
        return f, size
    if sc.get('small'):
        f, z = fit(sc['small'], sc.get('small_size', 58), True); lines.append((sc['small'], f, SOFT, int(z * 2.3)))
    bs = sc.get('big_size', 96)
    for s in sc.get('big', []):
        bc = tuple(sc['big_color']) if sc.get('big_color') else ((246, 243, 236) if sc.get('instant') else GOLD)
        f, z = fit(s, bs, True); lines.append((s, f, bc, int(z * 1.12) if sc.get('instant') else z + 42))
    if sc.get('after') and lines:
        a0 = lines[-1]; lines[-1] = (a0[0], a0[1], a0[2], a0[3] + 30)
    for s in sc.get('after', []):
        f, z = fit(s, sc.get('after_size', 56)); lines.append((s, f, SOFT, int(z * 1.65)))
    if sc.get('en'):
        f, z = fit(sc['en'], sc.get('en_size', 40)); lines.append((sc['en'], f, DIM, int(z * 1.76)))
    total = sum(l[3] for l in lines); y = (H - total) // 2 + 60
    step = sc.get('step', 0.45)
    for i, (s, f, col, h) in enumerate(lines):
        if col is DIM or (h == 76 + 30 and False): pass
        a = 1 if sc.get('instant') else max(0, min(1, (t - 0.25 - i * step) / 0.5))
        ct(y + (1 - a) * 18, s, f, col, a, 5 if (sc.get('big_stroke') and s in sc.get('big', [])) else 0); y += h
    return lay

def star_layer():
    """밤하늘: 잔별 + 빛나는 큰 별 몇 개 + 옅은 별자리 선 (원본 그림)."""
    LW, LH = int(W * 1.12), int(H * 1.12)
    lay = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for _ in range(420):
        x, y = R.uniform(0, LW), R.uniform(0, LH); r = R.choice([1, 1, 1, 1.5, 2])
        a = int(R.uniform(60, 200)); d.ellipse([x - r, y - r, x + r, y + r], fill=(235, 230, 255, a))
    glow = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
    cons = [(860, 260), (980, 330), (1060, 470), (950, 560), (1120, 640)]
    for a, b in zip(cons, cons[1:]): d.line([a, b], fill=(231, 205, 150, 70), width=2)
    bright = cons + [(170, 1720), (330, 1880), (120, 1960), (900, 1820)]
    for i, (x, y) in enumerate(bright):
        r = 26 if i == 0 else R.uniform(10, 16)
        g.ellipse([x - r * 3, y - r * 3, x + r * 3, y + r * 3], fill=(255, 220, 150, 90))
        d.ellipse([x - r * .35, y - r * .35, x + r * .35, y + r * .35], fill=(255, 245, 220, 255))
        d.line([x - r * 1.6, y, x + r * 1.6, y], fill=(255, 240, 210, 200), width=2)
        d.line([x, y - r * 1.6, x, y + r * 1.6], fill=(255, 240, 210, 200), width=2)
    glow = glow.filter(ImageFilter.GaussianBlur(26))
    out = Image.alpha_composite(glow, lay)
    hole = Image.new('L', (LW, LH), 0); hd = ImageDraw.Draw(hole); ox, oy = (LW - W) // 2, (LH - H) // 2
    hd.rectangle([ox - 100, oy + 640, ox + W + 100, oy + 1360], fill=200)
    hole = hole.filter(ImageFilter.GaussianBlur(90))
    out.putalpha(ImageChops.multiply(out.getchannel('A'), ImageChops.invert(hole)))
    return out

class Twinkle:
    def __init__(s, n=60):
        s.p = [dict(x=R.uniform(0, W), y=R.uniform(0, H), ph=R.uniform(0, 6.3), sp=R.uniform(1.2, 3), r=R.uniform(1.5, 3)) for _ in range(n)]
    def draw(s, im, t):
        lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for q in s.p:
            a = (math.sin(t * q['sp'] + q['ph']) + 1) / 2
            r = q['r'] * (0.6 + 0.6 * a)
            d.ellipse([q['x'] - r, q['y'] - r, q['x'] + r, q['y'] + r], fill=(255, 240, 210, int(220 * a)))
        # 가끔 지나가는 별똥별
        c = (t % 9.0)
        if c < 0.9:
            k = c / 0.9; x0, y0 = 200 + 700 * k, 300 + 260 * k
            for j in range(14):
                d.line([x0 - j * 9, y0 - j * 3.4, x0 - (j + 1) * 9, y0 - (j + 1) * 3.4], fill=(255, 240, 220, int(200 * (1 - j / 14) * (1 - k))), width=3)
        im.alpha_composite(lay)

def road_layer():
    """밤길: 겹겹의 산 능선과 멀리 이어지는 길 (원본 그림)."""
    LW, LH = int(W * 1.12), int(H * 1.12)
    lay = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for _ in range(220):
        x, y = R.uniform(0, LW), R.uniform(0, LH * 0.45); r = R.choice([1, 1, 1.5])
        d.ellipse([x - r, y - r, x + r, y + r], fill=(235, 230, 255, int(R.uniform(50, 160))))
    for k, (base, amp, col) in enumerate([(LH * .66, 70, (34, 38, 56)), (LH * .74, 90, (26, 29, 44)), (LH * .84, 60, (18, 20, 31))]):
        pts = [(0, LH)]; ph = R.uniform(0, 6)
        for x in range(0, LW + 40, 40):
            pts.append((x, base - amp * (0.5 + 0.5 * math.sin(x / 210 + ph)) - 30 * math.sin(x / 77 + ph * 2)))
        pts.append((LW, LH)); d.polygon(pts, fill=col + (255,))
    road = []
    for i in range(60):
        t = i / 59; y = LH - t * (LH * .38); x = LW * .5 + math.sin(t * 5.5) * (260 * (1 - t) + 30)
        road.append((x, y, 120 * (1 - t) + 6))
    for (x1, y1, w1), (x2, y2, w2) in zip(road, road[1:]):
        d.polygon([(x1 - w1 / 2, y1), (x1 + w1 / 2, y1), (x2 + w2 / 2, y2), (x2 - w2 / 2, y2)], fill=(70, 62, 60, 255))
    glow = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
    g.ellipse([LW * .5 - 260, LH * .52, LW * .5 + 260, LH * .68], fill=(255, 210, 140, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(70))
    out = Image.alpha_composite(lay, glow); out.info['road'] = road
    hole = Image.new('L', (LW, LH), 0); hd = ImageDraw.Draw(hole); ox, oy = (LW - W) // 2, (LH - H) // 2
    hd.rectangle([ox - 100, oy + 640, ox + W + 100, oy + 1360], fill=120)
    hole = hole.filter(ImageFilter.GaussianBlur(90))
    out.putalpha(ImageChops.multiply(out.getchannel('A'), ImageChops.invert(hole)))
    ROAD.extend(road)
    return out
ROAD = []

class Travelers:
    """길을 따라 멀어지는 작은 불빛들 + 옆으로 흐르는 바람 먼지."""
    def __init__(s):
        s.l = [R.uniform(0, 1) for _ in range(7)]
        s.dust = [dict(x=R.uniform(0, W), y=R.uniform(300, H), v=R.uniform(30, 80), r=R.uniform(1.5, 3)) for _ in range(40)]
    def draw(s, im, t):
        lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        LW, LH = int(W * 1.12), int(H * 1.12); ox, oy = (LW - W) / 2, (LH - H) / 2
        for q in s.l:
            u = (q + t * 0.035) % 1; i = min(len(ROAD) - 2, int(u * (len(ROAD) - 1)))
            x, y, w = ROAD[i]; x -= ox; y -= oy; r = max(2, w / 14)
            a = int(230 * (1 - u * 0.7))
            d.ellipse([x - r * 3, y - r * 3, x + r * 3, y + r * 3], fill=(255, 210, 140, a // 5))
            d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 236, 200, a))
        for q in s.dust:
            x = (q['x'] + q['v'] * t) % W
            d.ellipse([x - q['r'], q['y'] - q['r'], x + q['r'], q['y'] + q['r']], fill=(240, 225, 200, 110))
        im.alpha_composite(lay)


def lamp_layer(chars='文昌學堂'):
    """등불 아래 원고지: 왼쪽 위 등불빛 + 옅은 원고지 칸 + 칸 속 文昌學堂 (원본 그림)."""
    LW, LH = int(W * 1.12), int(H * 1.12)
    lay = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    cell = 72; x0 = (LW % cell) // 2
    for top, rows in ([(120, 6), (LH - 6 * cell - 90, 6)] if chars else []):
        for r in range(rows):
            y = top + r * cell
            for c in range(x0, LW - cell, cell):
                d.rectangle([c, y + 6, c + cell, y + cell - 6], outline=(190, 120, 90, 70), width=2)
            d.line([x0, y + 3, LW - cell, y + 3], fill=(190, 120, 90, 40), width=1)
    f = F(52, True); top = LH - 6 * cell - 90
    for i, ch in enumerate(chars):
        c = x0 + (3 + i * 2) * cell; y = top + 2 * cell + 6
        d.text((c + 10, y + 4), ch, font=f, fill=(225, 205, 170, 120))
    glow = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
    g.ellipse([-260, -260, 700, 620], fill=(255, 196, 120, 120))
    g.ellipse([LW - 520, LH - 640, LW + 200, LH + 80], fill=(255, 190, 120, 55))
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    out = Image.alpha_composite(glow, lay)
    hole = Image.new('L', (LW, LH), 0); hd = ImageDraw.Draw(hole); ox, oy = (LW - W) // 2, (LH - H) // 2
    hd.rectangle([ox - 100, oy + 640, ox + W + 100, oy + 1360], fill=210)
    hole = hole.filter(ImageFilter.GaussianBlur(90))
    out.putalpha(ImageChops.multiply(out.getchannel('A'), ImageChops.invert(hole)))
    return out

class Motes:
    """등불빛 속에 천천히 떠오르는 먼지 + 가끔 넘어가는 종이 한 장의 그림자."""
    def __init__(s, n=46):
        s.p = [dict(x=R.uniform(0, W * 0.7), y=R.uniform(0, H), v=R.uniform(10, 28), sw=R.uniform(8, 26), ph=R.uniform(0, 6.3), r=R.uniform(1.5, 3.2)) for _ in range(n)]
    def draw(s, im, t):
        lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for q in s.p:
            y = (q['y'] - q['v'] * t) % H; x = q['x'] + math.sin(t * 0.6 + q['ph']) * q['sw']
            near = max(0.25, 1 - (x / W) * 0.9 - (y / H) * 0.5)
            a = int(200 * near * (0.6 + 0.4 * math.sin(t * 1.7 + q['ph'])))
            d.ellipse([x - q['r'], y - q['r'], x + q['r'], y + q['r']], fill=(255, 226, 170, max(0, a)))
        im.alpha_composite(lay)

def moon_layer():
    """달밤 언덕 위 홀로 선 나무: 큰 달 + 낮은 능선 + 나무 한 그루 실루엣 (원본 그림)."""
    LW, LH = int(W * 1.12), int(H * 1.12)
    lay = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for _ in range(160):
        x, y = R.uniform(0, LW), R.uniform(0, LH * 0.5); r = R.choice([1, 1, 1.5])
        d.ellipse([x - r, y - r, x + r, y + r], fill=(235, 230, 255, int(R.uniform(40, 130))))
    glow = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
    mx, my, mr = LW * 0.86, LH * 0.15, 110
    g.ellipse([mx - mr * 3, my - mr * 3, mx + mr * 3, my + mr * 3], fill=(240, 228, 200, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    d.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=(246, 238, 214, 235))
    pts = [(0, LH)]
    for x in range(0, LW + 40, 40):
        pts.append((x, LH * 0.80 - 120 * math.exp(-((x - LW * 0.3) / 380) ** 2) - 18 * math.sin(x / 90)))
    pts.append((LW, LH)); d.polygon(pts, fill=(16, 18, 28, 255))
    bx, by = LW * 0.3, LH * 0.80 - 120
    def grow(x, y, ang, length, width, depth):
        if depth == 0 or length < 14: return
        nx, ny = x + math.cos(ang) * length, y + math.sin(ang) * length
        d.line([(x, y), (nx, ny)], fill=(16, 18, 28, 255), width=max(2, int(width)))
        for da in (-0.45, 0.4) if depth > 1 else (-0.3,):
            grow(nx, ny, ang + da + R.uniform(-0.15, 0.15), length * R.uniform(0.66, 0.78), width * 0.68, depth - 1)
    grow(bx, by + 6, -math.pi / 2, 210, 26, 7)
    out = Image.alpha_composite(glow, lay)
    hole = Image.new('L', (LW, LH), 0); hd = ImageDraw.Draw(hole); ox, oy = (LW - W) // 2, (LH - H) // 2
    hd.rectangle([ox - 100, oy + 640, ox + W + 100, oy + 1360], fill=170)
    hole = hole.filter(ImageFilter.GaussianBlur(90))
    out.putalpha(ImageChops.multiply(out.getchannel('A'), ImageChops.invert(hole)))
    return out

class Snow:
    """천천히 내리는 첫눈."""
    def __init__(s, n=70):
        s.p = [dict(x=R.uniform(0, W), y=R.uniform(-H, H), v=R.uniform(35, 75), sw=R.uniform(10, 40), ph=R.uniform(0, 6.3), r=R.uniform(2, 4.5)) for _ in range(n)]
    def draw(s, im, t):
        lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for q in s.p:
            y = (q['y'] + q['v'] * t) % (H + 40) - 20; x = q['x'] + math.sin(t * 0.7 + q['ph']) * q['sw']
            d.ellipse([x - q['r'], y - q['r'], x + q['r'], y + q['r']], fill=(240, 244, 255, 190))
        im.alpha_composite(lay)

def earth_layer():
    """산과 밭: 겹겹의 산 능선 + 앞쪽 밭이랑 (토, 2026-11-18). 나무 없음."""
    LW, LH = int(W * 1.12), int(H * 1.12)
    lay = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for _ in range(120):
        x, y = R.uniform(0, LW), R.uniform(0, LH * 0.35); r = R.choice([1, 1, 1.5])
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 240, 200, int(R.uniform(40, 110))))
    for base, amp, col in [(LH * .52, 260, (92, 72, 30)), (LH * .62, 180, (70, 54, 22)), (LH * .72, 110, (52, 40, 16))]:
        pts = [(0, LH)]; ph = R.uniform(0, 6)
        for x in range(0, LW + 30, 30):
            pts.append((x, base - amp * math.exp(-((x - LW * R.uniform(.3, .7)) / 420) ** 2) * 0 - amp * (0.5 + 0.5 * math.sin(x / 260 + ph)) * 0.8 - 25 * math.sin(x / 70 + ph * 2)))
        pts.append((LW, LH)); d.polygon(pts, fill=col + (255,))
    top = LH * .80; vx = LW * .5
    d.rectangle([0, top, LW, LH], fill=(40, 30, 12, 255))
    for k in range(1, 12):
        y = top + (LH - top) * (k / 12) ** 1.5; ph = R.uniform(0, 6)
        pts = [(x, y + 6 * math.sin(x / 180 + ph)) for x in range(0, LW + 20, 20)]
        d.line(pts, fill=(120, 94, 40, 90), width=2)
    glow = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
    g.ellipse([LW * .5 - 420, LH * .30, LW * .5 + 420, LH * .62], fill=(255, 200, 80, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(90))
    out = Image.alpha_composite(glow, lay)
    hole = Image.new('L', (LW, LH), 0); hd = ImageDraw.Draw(hole); ox, oy = (LW - W) // 2, (LH - H) // 2
    hd.rectangle([ox - 100, oy + 640, ox + W + 100, oy + 1360], fill=150)
    hole = hole.filter(ImageFilter.GaussianBlur(90))
    out.putalpha(ImageChops.multiply(out.getchannel('A'), ImageChops.invert(hole)))
    return out

def water_layer():
    """비 오는 밤 물가: 아래쪽 넓은 수면 + 옅은 물결 줄 (수, 2026-11-18). 산·길 없음."""
    LW, LH = int(W * 1.12), int(H * 1.12)
    lay = Image.new('RGBA', (LW, LH), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    top = LH * .74
    d.rectangle([0, top, LW, LH], fill=(6, 6, 8, 255))
    for k in range(1, 22):
        y = top + (LH - top) * (k / 22) ** 1.4
        for _ in range(6):
            x = R.uniform(0, LW); w = R.uniform(60, 260)
            d.line([(x, y), (x + w, y)], fill=(230, 235, 245, int(R.uniform(30, 90))), width=2)
    out = lay
    hole = Image.new('L', (LW, LH), 0); hd = ImageDraw.Draw(hole); ox, oy = (LW - W) // 2, (LH - H) // 2
    hd.rectangle([ox - 100, oy + 640, ox + W + 100, oy + 1360], fill=150)
    hole = hole.filter(ImageFilter.GaussianBlur(90))
    out.putalpha(ImageChops.multiply(out.getchannel('A'), ImageChops.invert(hole)))
    return out

class Rain:
    """가늘게 내리는 비 + 수면에 퍼지는 동그라미 물결."""
    def __init__(s, n=90):
        s.p = [dict(x=R.uniform(0, W), y=R.uniform(0, H), v=R.uniform(700, 1100), l=R.uniform(26, 60)) for _ in range(n)]
        s.rip = [dict(x=R.uniform(60, W - 60), y=R.uniform(H * .78, H - 40), ph=R.uniform(0, 2.4)) for _ in range(14)]
    def draw(s, im, t):
        lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for q in s.p:
            y = (q['y'] + q['v'] * t) % (H + 80) - 40; x = q['x'] - (y * 0.06)
            d.line([(x, y), (x - q['l'] * 0.06, y + q['l'])], fill=(225, 232, 245, 110), width=2)
        for q in s.rip:
            u = ((t + q['ph']) % 2.4) / 2.4; rx, ry = 10 + 120 * u, 3 + 30 * u
            d.ellipse([q['x'] - rx, q['y'] - ry, q['x'] + rx, q['y'] + ry], outline=(235, 240, 250, int(170 * (1 - u))), width=2)
        im.alpha_composite(lay)

def build_audio(parts, out, xf=0.8):
    """parts: [{"file","start","dur"}] -> 이어 붙인 음원(크로스페이드)."""
    args=['ffmpeg','-v','error','-y']
    for p in parts: args+=['-ss',str(p['start']),'-t',str(p['dur']+xf),'-i',os.path.join(ROOT,p['file'])]
    n=len(parts); fl=''; last='[0:a]'
    for i in range(1,n):
        o=f'[a{i}]'; fl+=f'{last}[{i}:a]acrossfade=d={xf}:c1=tri:c2=tri{o};'; last=o
    total=sum(p['dur'] for p in parts)
    fl+=f'{last}afade=t=in:d=0.4,afade=t=out:st={total-1.4}:d=1.4,atrim=0:{total}[out]'
    subprocess.check_call(args+['-filter_complex',fl,'-map','[out]','-c:a','pcm_s16le',out])
    return total

def tint_layer(col, strength, ring=True):
    g=Image.new('L',(W,H),0); ImageDraw.Draw(g).ellipse([-200,250,W+200,1750],fill=int(110*strength))
    g=g.filter(ImageFilter.GaussianBlur(240)); lay=Image.new('RGBA',(W,H),col+(255,)); lay.putalpha(g)
    if col==(0,0,0) and not ring:
        g2=Image.new('L',(W,H),0); ImageDraw.Draw(g2).ellipse([-200,250,W+200,1750],fill=int(170*strength)); g2=g2.filter(ImageFilter.GaussianBlur(240)); lay.putalpha(g2)
    elif col==(0,0,0):  # 수는 흑색 + 얇은 흰 테두리 (미오 님 11/18)
        r=Image.new('L',(W,H),0); ImageDraw.Draw(r).ellipse([70,330,W-70,1670],outline=int(115*strength),width=3)
        r=r.filter(ImageFilter.GaussianBlur(1.2)); ring=Image.new('RGBA',(W,H),(255,255,255,255)); ring.putalpha(r)
        g2=Image.new('L',(W,H),0); ImageDraw.Draw(g2).ellipse([-200,250,W+200,1750],fill=int(170*strength)); g2=g2.filter(ImageFilter.GaussianBlur(240)); lay.putalpha(g2)
        lay=Image.alpha_composite(lay,ring)
    return lay

def mark_layer(ch, a):
    lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay); f=F(620,True)
    w=d.textlength(ch,font=f); d.text(((W-w)/2,560),ch,font=f,fill=(255,255,255,int(26*a))); return lay

def main():
    cfg=json.load(open(sys.argv[1])); out=sys.argv[2]
    chk=subprocess.run([sys.executable,os.path.join(ROOT,'tools','reel_check.py'),sys.argv[1]])
    if chk.returncode: sys.exit('곡 이름 점검 실패: 영상을 만들지 않았어요')
    wav=out+'.wav'; total=build_audio(cfg['audio_parts'],wav)
    scs=cfg['scenes']; scs[-1]['sec']=round(total-sum(s['sec'] for s in scs[:-1]),3)
    bg=gradient().convert('RGBA'); th=cfg.get('theme'); art={'stars':star_layer,'road':road_layer,'lamp':(lambda: lamp_layer(cfg.get('lamp_chars','文昌學堂'))),'moon':moon_layer,'earth':earth_layer,'water':water_layer}.get(th,branch_layer)(); petals={'stars':Twinkle,'road':Travelers,'lamp':Motes,'moon':Snow,'earth':Motes,'water':Rain}.get(th,Petals)(); LW,LH=art.size
    veil=Image.new('L',(W,H),0); ImageDraw.Draw(veil).ellipse([40,600,W-40,1340],fill=160)
    veil=veil.filter(ImageFilter.GaussianBlur(120)); dark=Image.new('RGBA',(W,H),(8,8,14,255)); dark.putalpha(veil)
    tints={k:tint_layer(tuple(v),cfg.get('tint_strength',1),cfg.get('water_ring',True)) for k,v in cfg.get('tints',{}).items()}
    marks={sc['mark']:None for sc in scs if sc.get('mark')}
    ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
        '-i',wav,'-map','0:v','-map','1:a','-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-c:a','aac','-b:a','192k',
        '-shortest','-movflags','+faststart',out],stdin=subprocess.PIPE)
    T=0.0
    for idx,sc in enumerate(scs):
        dur=sc['sec']; n=int(round(dur*FPS)); tl_cache={}
        for k in range(n):
            t=k/FPS; g=(T+t)/total; z=1.0+0.10*g
            bw,bh=int(W/z*1.0),int(H/z); cx,cy=LW/2-40*g,LH/2+30*g
            crop=art.crop((int(cx-bw/2),int(cy-bh/2),int(cx+bw/2),int(cy+bh/2))).resize((W,H),Image.BILINEAR)
            fr=bg.copy()
            if sc.get('tint') in tints:
                a=min(1,t/0.8,(dur-t)/0.5+0.0) if idx<len(scs)-1 else min(1,t/0.8)
                lay=tints[sc['tint']].copy(); lay.putalpha(lay.getchannel('A').point(lambda v:int(v*max(0,a)))); fr.alpha_composite(lay)
            fr.alpha_composite(crop); petals.draw(fr,T+t)
            if sc.get('mark'): fr.alpha_composite(mark_layer(sc['mark'],max(0,min(1,t/0.8))))
            fr.alpha_composite(dark)
            fade_out=1 if idx==len(scs)-1 else max(0,min(1,(dur-t)/0.35))
            tl=text_layer(cfg,sc,t)
            if fade_out<1: tl.putalpha(tl.getchannel('A').point(lambda v:int(v*fade_out)))
            fr.alpha_composite(tl)
            ff.stdin.write(fr.convert('RGB').tobytes())
        T+=dur
    ff.stdin.close(); ff.wait(); os.remove(wav); print('ok',out,round(total,1),'s')

if __name__ == '__main__':
    main()
