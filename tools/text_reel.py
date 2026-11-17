#!/usr/bin/env python3
"""글자 장면형 사주 릴스(1080x1920) 생성. 기존 쇼츠 음악을 그대로 깐다.
python3 tools/text_reel.py <config.json> <out.mp4>
config: {"audio": "shorts/...mp4", "header": "사주 · 오행음악 · 고요",
 "scenes": [{"sec": 3.5, "small": "윗줄", "big": ["큰 줄", ...], "after": ["아랫줄", ...], "en": "영문"} ...]}
마지막 장면 sec 는 남은 시간에 맞춰 자동 조정."""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarot_reel import BG, F, ctext, W, H, FPS, GOLD, SOFT, DIM, ROOT
from PIL import Image, ImageDraw

def wrap_h(lines, size, gap):
    return len(lines) * (size + gap)

def scene(cfg, sc):
    im = BG.copy(); d = ImageDraw.Draw(im)
    ctext(d, 200, cfg.get('header', '사주 · 오행음악 · 고요'), F(40, True), SOFT)
    ctext(d, 258, "FIVE ELEMENTS MUSIC", F(28), DIM)
    small, big, after, en = sc.get('small'), sc.get('big', []), sc.get('after', []), sc.get('en')
    bs = sc.get('big_size', 92)
    h = (70 if small else 0) + wrap_h(big, bs, 40) + (30 + wrap_h(after, 44, 28) if after else 0) + (90 if en else 0)
    y = max(420, (H - h) // 2 - 80)
    if small: ctext(d, y, small, F(46, True), SOFT); y += 110
    for s in big: ctext(d, y, s, F(bs, True), GOLD); y += bs + 40
    if after:
        y += 30
        for s in after: ctext(d, y, s, F(44), SOFT); y += 72
    if en: ctext(d, y + 40, en, F(32), DIM)
    return im

def main():
    cfg = json.load(open(sys.argv[1])); out = sys.argv[2]
    audio = os.path.join(ROOT, cfg['audio'])
    total = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                           '-of', 'csv=p=0', audio]).decode())
    scs = cfg['scenes']; scs[-1]['sec'] = total - sum(s['sec'] for s in scs[:-1])
    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                           '-r', str(FPS), '-i', '-', '-i', audio, '-map', '0:v', '-map', '1:a',
                           '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-c:a', 'aac', '-b:a', '192k',
                           '-af', f'afade=t=out:st={total - 1.2}:d=1.2', '-shortest', '-movflags', '+faststart', out],
                          stdin=subprocess.PIPE)
    black = Image.new('RGB', (W, H), (0, 0, 0))
    for idx, sc in enumerate(scs):
        base = scene(cfg, sc); n = int(round(sc['sec'] * FPS)); dur = sc['sec']
        for k in range(n):
            t = k / FPS
            fade = min(1, (dur - t) / 0.3) if idx == 0 else min(1, t / 0.3, (dur - t) / 0.3)
            fr = base if fade >= 1 else Image.blend(black, base, max(0, fade))
            ff.stdin.write(fr.tobytes())
    ff.stdin.close(); ff.wait(); print('ok', out, round(total, 1), 's')

if __name__ == '__main__':
    main()
