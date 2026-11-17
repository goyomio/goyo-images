#!/usr/bin/env python3
"""고르기형 타로 릴스(1080x1920) 샘플 생성.
python3 tools/tarot_reel.py <config.json> <out.mp4>
config: {"audio": "shorts/...mp4", "hook": [...], "cards": [{"file","ko","lines":[..],"en"}x3], "end": [..]}
기존 쇼츠의 음악을 그대로 깔고, 그림은 deck_1909 원판만 쓴다."""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
W, H, FPS = 1080, 1920, 30
GOLD, SOFT, DIM = (231, 205, 150), (226, 220, 205), (150, 150, 160)
SERIF_B = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
SERIF_R = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
def F(size, bold=False):
    return ImageFont.truetype(SERIF_B if bold else SERIF_R, size, index=1)  # KR

def background():
    bg = Image.new('RGB', (W, H), (14, 17, 24))
    glow = Image.new('L', (W, H), 0)
    ImageDraw.Draw(glow).ellipse([-200, 200, W + 200, 1500], fill=70)
    glow = glow.filter(ImageFilter.GaussianBlur(220))
    bg.paste(Image.new('RGB', (W, H), (52, 60, 78)), mask=glow)
    return bg
BG = background()

def ctext(d, y, s, f, fill):
    w = d.textlength(s, font=f); d.text(((W - w) / 2, y), s, font=f, fill=fill)

def header(d):
    ctext(d, 200, "타로 · 오행음악 · 고요", F(40, True), SOFT)
    ctext(d, 258, "FIVE ELEMENTS MUSIC", F(28), DIM)

def card_back(w, h):
    im = Image.new('RGB', (w, h), (20, 26, 44)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], 18, outline=GOLD, width=4)
    d.rounded_rectangle([16, 16, w - 17, h - 17], 12, outline=GOLD, width=1)
    cx, cy = w // 2, h // 2
    for r in (90, 60):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=2)
    d.polygon([(cx, cy - 40), (cx + 12, cy - 12), (cx + 40, cy), (cx + 12, cy + 12),
               (cx, cy + 40), (cx - 12, cy + 12), (cx - 40, cy), (cx - 12, cy - 12)], fill=GOLD)
    f = F(30, True); t = "GOYO"; tw = d.textlength(t, font=f)
    d.text(((w - tw) / 2, h - 80), t, font=f, fill=GOLD)
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], 18, fill=255)
    return im, m

def scene_hook(cfg, t):
    im = BG.copy(); d = ImageDraw.Draw(im); header(d)
    y = 420
    for i, s in enumerate(cfg['hook']):
        ctext(d, y, s, F(66 if i else 46, bool(i)), GOLD if i else SOFT); y += 110 if i else 90
    cw, ch = 280, 480; back, m = card_back(cw, ch)
    gap = 40; x0 = (W - 3 * cw - 2 * gap) // 2
    for i in range(3):
        bob = int(10 * __import__('math').sin(t * 2.2 + i * 1.3))
        x = x0 + i * (cw + gap); yy = 820 + bob
        im.paste(back, (x, yy), m)
        ctext_x = x + cw / 2; f = F(56, True); s = str(i + 1)
        d.text((ctext_x - d.textlength(s, font=f) / 2, yy + ch + 40), s, font=f, fill=GOLD)
    ctext(d, 1520, cfg.get('hook_en', ''), F(34), DIM)
    return im

def scene_card(cfg, i, t, dur):
    c = cfg['cards'][i]
    im = BG.copy(); d = ImageDraw.Draw(im); header(d)
    ctext(d, 360, f"{i + 1}번을 고른 당신", F(46, True), SOFT)
    art = Image.open(os.path.join(ROOT, 'deck_1909', c['file'])).convert('RGB')
    s = 1.0 + 0.04 * (t / dur)  # 천천히 다가가기
    ch = int(760 * s); cw = int(art.width * ch / art.height)
    art = art.resize((cw, ch), Image.LANCZOS)
    im.paste(art, ((W - cw) // 2, 450 + (760 - ch) // 2))
    y = 1260
    ctext(d, y, c['ko'], F(60, True), GOLD); y += 110
    for line in c['lines']:
        ctext(d, y, line, F(44), SOFT); y += 72
    ctext(d, y + 24, c.get('en', ''), F(32), DIM)
    return im

def scene_end(cfg, t):
    im = BG.copy(); d = ImageDraw.Draw(im); header(d)
    y = 820
    for i, s in enumerate(cfg['end']):
        ctext(d, y, s, F(60 if i == 0 else 42, i == 0), GOLD if i == 0 else SOFT); y += 110
    return im

def main():
    cfg = json.load(open(sys.argv[1])); out = sys.argv[2]
    audio = os.path.join(ROOT, cfg['audio'])
    total = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                           '-of', 'csv=p=0', audio]).decode())
    hook, end = cfg.get('hook_sec', 4.6), cfg.get('end_sec', 1.8)
    per = (total - hook - end) / 3
    plan = [('hook', None, hook)] + [('card', i, per) for i in range(3)] + [('end', None, end)]
    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                           '-r', str(FPS), '-i', '-', '-i', audio, '-map', '0:v', '-map', '1:a',
                           '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'medium', '-crf', '20',
                           '-c:a', 'aac', '-b:a', '192k', '-af', f'afade=t=out:st={total - 1.2}:d=1.2',
                           '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    black = Image.new('RGB', (W, H), (0, 0, 0))
    for kind, i, dur in plan:
        n = int(round(dur * FPS))
        for k in range(n):
            t = k / FPS
            fr = scene_hook(cfg, t) if kind == 'hook' else scene_card(cfg, i, t, dur) if kind == 'card' else scene_end(cfg, t)
            fade = min(1, t / 0.35, (dur - t) / 0.35) if kind != 'hook' else min(1, (dur - t) / 0.35)
            if fade < 1: fr = Image.blend(black, fr, max(0, fade))
            ff.stdin.write(fr.tobytes())
    ff.stdin.close(); ff.wait(); print('ok', out, round(total, 1), 's')

if __name__ == '__main__':
    main()
