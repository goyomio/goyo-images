#!/usr/bin/env python3
"""사주 릴스 → 유튜브 쇼츠 썸네일(1080x1920, 흰 글자).
python3 tools/saju_thumb.py <영상.mp4> <출력.jpg> "<큰 제목>" "<작은 줄>"
배경은 영상 첫 프레임(글자가 뜨기 전)을 쓰고, 제목은 가운데 정사각형 안에 둔다(인스타 격자 잘림 대비)."""
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarot_reel import F, W, H
from PIL import Image, ImageDraw, ImageFilter

def main(video, out, big, small):
    tmp = out + '.bg.png'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-ss', '0.05', '-i', video, '-frames:v', '1', '-y', tmp], check=True)
    bg = Image.open(tmp).convert('RGB'); os.remove(tmp)
    veil = Image.new('L', (W, H), 0)
    ImageDraw.Draw(veil).ellipse([0, 640, W, 1300], fill=150)
    veil = veil.filter(ImageFilter.GaussianBlur(110))
    bg.paste(Image.new('RGB', (W, H), (6, 6, 10)), mask=veil)
    d = ImageDraw.Draw(bg)
    size = 190
    while True:
        fb = F(size, True)
        if d.textlength(big, font=fb) <= W - 140 or size <= 90: break
        size -= 8
    fs = F(64, False)
    bb = d.textbbox((0, 0), big, font=fb); bh = bb[3] - bb[1]
    sb = d.textbbox((0, 0), small, font=fs); shh = sb[3] - sb[1]
    gap = 46; total = bh + gap + shh; y0 = 960 - total // 2
    def ctext(y, t, f, fill, sw=0):
        w = d.textlength(t, font=f)
        d.text(((W - w) / 2, y), t, font=f, fill=fill, stroke_width=sw, stroke_fill=(0, 0, 0))
    ctext(y0 - bb[1], big, fb, (255, 255, 255), 3)
    ctext(y0 + bh + gap - sb[1], small, fs, (240, 240, 240), 2)
    bg.save(out, quality=92)

if __name__ == '__main__':
    main(*sys.argv[1:5])
