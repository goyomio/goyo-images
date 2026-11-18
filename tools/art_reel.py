#!/usr/bin/env python3
"""그림 읽기 릴스판. 그림을 천천히 훑는 화면 + 장면 글자 + 고요 무음편 소리.
python3 tools/art_reel.py 설정.json 출력.mp4

설정: {"image": 그림 경로, "audio": 무음편 mp4, "audio_start": 초,
       "scenes": [{"sec":3, "label":"..", "title":[".."], "sub":"..", "lines":[".."], "small":"..",
                   "view": [x0,y0,x1,y1](그림 안 0~1 비율, 시작), "view_to": [...](끝), "dim":0.0~1}]}
첫 장면은 0초부터 글자가 보이고(페이드 없음) 검은 바탕 + 큰 흰 제목.
수(水) 색은 흑색 + 얇은 흰 테두리로 그린다."""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from tarot_reel import F  # noqa: E402

W, H, FPS = 1080, 1920, 30
FG = (246, 243, 236); SUB = (205, 200, 190); DIM = (150, 145, 135); GOLD = (201, 169, 106)
COL = {'목': (47, 217, 107), '화': (255, 70, 55), '토': (255, 194, 26), '금': (235, 235, 240), '수': (0, 0, 0)}
CG = os.path.join(ROOT, 'tools', 'fonts', 'CormorantGaramond-500.ttf')


def ease(t):
    return t * t * (3 - 2 * t)


def ctext(d, y, s, f, fill, a=1.0):
    """가운데 정렬. [(글자, 색)] 목록이면 색을 나눠 그림. 수 색은 흰 테두리."""
    parts = s if isinstance(s, list) else [(s, fill)]
    w = sum(d.textlength(t, font=f) for t, _ in parts); x = (W - w) / 2
    for t, c in parts:
        c = COL.get(c, c) if isinstance(c, str) else tuple(c)
        al = int(255 * a)
        if c == (0, 0, 0):
            d.text((x, y), t, font=f, fill=(0, 0, 0, al), stroke_width=max(2, f.size // 36), stroke_fill=(255, 255, 255, al))
        else:
            d.text((x, y), t, font=f, fill=tuple(c) + (al,), stroke_width=max(1, round(f.size / 24)), stroke_fill=(10, 10, 14, int(al * 0.8)))  # 어두운 테두리 (미오 님 규칙 11/18)
        x += d.textlength(t, font=f)


def logo(d, y, a=1.0):
    f = ImageFont.truetype(CG, 54); sp = 22
    ws = [d.textlength(c, font=f) for c in 'GOYO']; x = (W - sum(ws) - sp * 3) / 2
    for c, w in zip('GOYO', ws):
        d.text((x, y), c, font=f, fill=DIM + (int(255 * a),)); x += w + sp


def view_crop(img, v):
    x0, y0, x1, y1 = v; iw, ih = img.size
    return img.crop((int(x0 * iw), int(y0 * ih), int(x1 * iw), int(y1 * ih)))


def frame(img, sc, t, first):
    d_sec = sc['sec']; p = min(1, t / d_sec)
    fr = Image.new('RGBA', (W, H), (10, 10, 12, 255))
    if sc.get('view'):
        v0, v1 = sc['view'], sc.get('view_to', sc['view'])
        e = ease(p); v = [a + (b - a) * e for a, b in zip(v0, v1)]
        cr = view_crop(img, v)
        box = sc.get('box', [0, 0, W, H])
        bw, bh = box[2] - box[0], box[3] - box[1]
        s = max(bw / cr.width, bh / cr.height)
        cr = cr.resize((int(cr.width * s) + 1, int(cr.height * s) + 1), Image.BILINEAR)
        cx, cy = (cr.width - bw) // 2, (cr.height - bh) // 2
        fr.paste(cr.crop((cx, cy, cx + bw, cy + bh)), (box[0], box[1]))
        if sc.get('dim'):
            sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).rectangle([0, 0, W, H], fill=int(255 * sc['dim']))
            fr = Image.alpha_composite(fr, Image.merge('RGBA', [Image.new('L', (W, H), 0)] * 3 + [sh]))
        if sc.get('shade', True) and not sc.get('box'):
            g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).rectangle([0, 1050, W, H], fill=225)
            g = g.filter(ImageFilter.GaussianBlur(160))
            fr = Image.alpha_composite(fr, Image.merge('RGBA', [Image.new('L', (W, H), 0)] * 3 + [g]))
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    a = 1.0 if (first or sc.get('instant')) else max(0, min(1, (t - 0.2) / 0.5))
    y = sc.get('y', 1180)
    if sc.get('label'):
        ctext(d, y, sc['label'], F(44, True), GOLD, a); y += 80
    if sc.get('title'):
        size = sc.get('title_size', 200)
        for ln in sc['title']:
            ctext(d, y, ln, F(size, True), FG, a); y += int(size * 1.22)
        y += 30
    if sc.get('sub'):
        ctext(d, y, sc['sub'], F(54), SUB, a); y += 90
    for ln in sc.get('lines', []):
        ctext(d, y, ln, F(sc.get('line_size', 72), True), FG, a); y += int(sc.get('line_size', 72) * 1.5)
    if sc.get('small'):
        y += 16
        for ln in sc['small'].split('\n'):
            ctext(d, y, ln, F(sc.get('small_size', 46)), SUB, a); y += int(sc.get('small_size', 46) * 1.45)
    if sc.get('en'):
        y += 6
        for ln in sc['en'].split('\n'):
            ctext(d, y, ln, F(sc.get('en_size', 38)), (236, 233, 226), a); y += int(sc.get('en_size', 38) * 1.45)
    if sc.get('credit'):
        ctext(d, sc.get('credit_y', 1700), sc['credit'], F(28), DIM, a)
    if sc.get('logo'):
        logo(d, 1760, a)
    fr = Image.alpha_composite(fr, lay)
    return fr.convert('RGB')


def main():
    cfg = json.load(open(sys.argv[1])); out = sys.argv[2]
    img = Image.open(os.path.join(ROOT, cfg['image'])).convert('RGB')
    total = sum(s['sec'] for s in cfg['scenes'])
    # 소리: audio(한 곡) 또는 audio_parts([{file,start,dur}...], 1초씩 겹쳐 이음)
    parts = cfg.get('audio_parts') or [{'file': cfg['audio'], 'start': cfg.get('audio_start', 1.0), 'dur': total}]
    wav = out + '.wav'; args = ['ffmpeg', '-loglevel', 'error', '-y']
    for q in parts: args += ['-ss', str(q['start']), '-t', str(q['dur']), '-i', os.path.join(ROOT, q['file'])]
    if len(parts) == 1: fl = '[0:a]anull[o]'
    else:
        fl = ''; last = '0:a'
        for k in range(1, len(parts)):
            fl += f'[{last}][{k}:a]acrossfade=d=1[x{k}];'; last = f'x{k}'
        fl += f'[{last}]anull[o]'
    subprocess.check_call(args + ['-filter_complex', fl, '-map', '[o]', '-ac', '2', '-ar', '48000', wav])
    p = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-i', wav,
                          '-map', '0:v', '-map', '1:a', '-af', f'afade=t=in:d=0.6,afade=t=out:st={total - 2}:d=2',
                          '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-shortest', out],
                         stdin=subprocess.PIPE)
    for i, sc in enumerate(cfg['scenes']):
        n = int(round(sc['sec'] * FPS))
        for k in range(n):
            p.stdin.write(frame(img, sc, k / FPS, i == 0).tobytes())
    p.stdin.close(); p.wait(); os.remove(wav)
    print(out, total)


if __name__ == '__main__':
    main()
