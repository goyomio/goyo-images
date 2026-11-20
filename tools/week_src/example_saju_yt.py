"""예시 사주 풀이 유튜브판: 마지막 장 _yt 렌더 + 정사각형 1350x1350 세트 + 쇼츠 썸네일.
python3 tools/week_src/example_saju_yt.py example_saju/02/slides.json
결과: example_saju/NN/yt/01.jpg~NN.jpg (정사각형, 마지막 장은 yt_last), yt/쇼츠_썸네일.jpg"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import example_saju as X
from PIL import Image, ImageDraw

SQ = 1350


def slide(s, k, n):
    W, H, M = X.W, X.H, X.M
    im = Image.new('RGBA', (W, H), X.BG + (255,)); d = ImageDraw.Draw(im); X.frame(im, d)
    if s.get('tag'):
        f = X.F(34); w = d.textlength(s['tag'], font=f); d.text(((W - w) / 2, M + 90), s['tag'], font=f, fill=X.GOLD)
    if s.get('pillars'):
        y = X.pillars(d, 330, s['pillars'])
        X.block(d, [('k', *it) for it in s['items']], top=y + 30)
    else:
        X.block(d, [('k', *it) for it in s['items']])
    pg = '%02d / %02d' % (k, n); f = X.F(24); w = d.textlength(pg, font=f)
    d.text((W - M - 90 - w, H - M - 58), pg, font=f, fill=(110, 106, 100))
    return im.convert('RGB')


def square(im):
    out = Image.new('RGB', (SQ, SQ), X.BG); out.paste(im, ((SQ - im.width) // 2, (SQ - im.height) // 2)); return out


def thumb(no, path):
    W, H = 1080, 1920
    X.W, X.H = W, H
    im = Image.new('RGBA', (W, H), X.BG + (255,)); d = ImageDraw.Draw(im); X.frame(im, d)
    f = X.F(190, True); lines = ['예시 사주', '풀이 #%d' % no]
    lh = 260
    top = d.textbbox((0, 0), lines[0], font=f)[1]; bot = lh + d.textbbox((0, 0), lines[1], font=f)[3]
    y = 781 - top                              # 1편 썸네일(맥 쇼츠_썸네일_큰글자.jpg)과 같은 자리
    for t in lines:
        w = d.textlength(t, font=f); d.text(((W - w) / 2, y), t, font=f, fill=(236, 233, 226)); y += lh
    im.convert('RGB').save(path, quality=92)


def main(js):
    cfg = json.load(open(js, encoding='utf-8')); out = os.path.join(os.path.dirname(js), 'yt'); os.makedirs(out, exist_ok=True)
    slides = cfg['slides'][:-1] + [cfg['yt_last']]; n = len(slides)
    X.W, X.H = 1080, 1350
    for k, s in enumerate(slides, 1):
        im = slide(s, k, n)
        if k == n: im.save(os.path.join(os.path.dirname(js), '%02d_yt.jpg' % k), quality=92)
        square(im).save(os.path.join(out, '%02d.jpg' % k), quality=92)
    thumb(cfg['no'], os.path.join(out, '쇼츠_썸네일.jpg'))
    print('ok yt', n)


if __name__ == '__main__': main(sys.argv[1])
