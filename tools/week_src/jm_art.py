"""정미년 시리즈 선 그림 도구 (금색 선, 투명 PNG). 2배로 그리고 줄임."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import example_saju as X
from PIL import Image, ImageDraw

GOLD = (200, 180, 140, 255); FG = (236, 233, 226, 255); DIM = (150, 146, 138, 255); HI = (232, 205, 150, 255)
EARTH = (150, 120, 85, 255); ICE = (200, 210, 220, 255); WATER = (150, 175, 195, 255); WOOD = (150, 180, 130, 255)
S = 2
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'shorts', '정미년', 'art')


class Pic:
    def __init__(self, w, h):
        self.w, self.h = w, h; self.im = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0)); self.d = ImageDraw.Draw(self.im)

    def p(self, *xy): return [v * S for v in xy]
    def line(self, pts, col=GOLD, w=3): self.d.line([(x * S, y * S) for x, y in pts], fill=col, width=w * S)
    def poly(self, pts, col=GOLD, w=3, fill=None): self.d.polygon([(x * S, y * S) for x, y in pts], outline=col, width=w * S, fill=fill)
    def rect(self, x0, y0, x1, y1, col=GOLD, w=3, r=8, fill=None): self.d.rounded_rectangle(self.p(x0, y0, x1, y1), radius=r * S, outline=col, width=w * S, fill=fill)
    def circ(self, cx, cy, r, col=GOLD, w=3, fill=None): self.d.ellipse(self.p(cx - r, cy - r, cx + r, cy + r), outline=col, width=w * S, fill=fill)
    def text(self, cx, y, t, sz=26, col=FG, bold=False):
        f = X.F(sz * S, bold); tw = self.d.textlength(t, font=f); self.d.text((cx * S - tw / 2, y * S), t, font=f, fill=col)
    def vtext(self, cx, y, t, sz=30, col=FG, bold=True, gap=4):
        for i, ch in enumerate(t): self.text(cx, y + i * (sz + gap), ch, sz, col, bold)
    def arrow(self, x0, y0, x1, y1, col=GOLD, w=4):
        self.line([(x0, y0), (x1, y1)], col, w); a = math.atan2(y1 - y0, x1 - x0)
        self.poly([(x1, y1), (x1 - 18 * math.cos(a - 0.4), y1 - 18 * math.sin(a - 0.4)), (x1 - 18 * math.cos(a + 0.4), y1 - 18 * math.sin(a + 0.4))], col, 1, fill=col)
    def sun(self, cx, cy, r, col=HI):
        self.circ(cx, cy, r, col, 4)
        for i in range(12):
            a = math.radians(i * 30); self.line([(cx + math.cos(a) * (r + 8), cy + math.sin(a) * (r + 8)), (cx + math.cos(a) * (r + 22), cy + math.sin(a) * (r + 22))], col, 3)
    def flame(self, cx, cy, s=1.0, col=HI):
        pts = [(cx, cy - 40 * s), (cx + 16 * s, cy - 8 * s), (cx + 12 * s, cy + 10 * s), (cx, cy + 16 * s), (cx - 12 * s, cy + 10 * s), (cx - 16 * s, cy - 8 * s)]
        self.poly(pts, col, 3, fill=col)
    def snow(self, cx, cy, r, col=ICE):
        for i in range(6):
            a = math.radians(i * 60); self.line([(cx, cy), (cx + math.cos(a) * r, cy + math.sin(a) * r)], col, 3)
    def tree(self, cx, base, h, col=WOOD, bare=False):
        self.line([(cx, base), (cx, base - h)], col, 5)
        for k in range(1, 4):
            y = base - h * k / 4; L = h * (0.45 - k * 0.08)
            self.line([(cx, y), (cx - L, y - L * 0.6)], col, 3); self.line([(cx, y), (cx + L, y - L * 0.6)], col, 3)
            if not bare: self.circ(cx - L, y - L * 0.6, 5, col, 2, fill=col)
    def ground(self, x0, x1, y, col=EARTH, n=3):
        for k in range(n): self.line([(x0 + k * 16, y + k * 12), (x1 - k * 16, y + k * 12)], col, 4)
    def waves(self, x0, x1, y, col=WATER, n=3):
        for k in range(n):
            pts = [(x, y + k * 16 + 6 * math.sin((x - x0) / 22)) for x in range(int(x0), int(x1), 6)]; self.line(pts, col, 3)
    def save(self, name):
        os.makedirs(OUT, exist_ok=True); p = os.path.join(OUT, name + '.png')
        self.im.resize((self.w, self.h), Image.LANCZOS).save(p); return 'shorts/정미년/art/' + name + '.png'
