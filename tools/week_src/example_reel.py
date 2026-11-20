"""예시 사주 풀이 릴스/쇼츠 (1080x1920, 캐러셀과 같은 액자).
python3 tools/week_src/example_reel.py example_saju/01/reel.json ig|yt out.mp4"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import example_saju as X
from PIL import Image, ImageDraw

X.W, X.H = 1080, 1920
W, H, FPS = X.W, X.H, 30
TOP, BOT = 260, 1385          # 글자는 이 사이 (쇼츠·릴스 아래 UI 피하기)


def layers(scene):
    """장면 하나를 [배경(액자+태그), 글 묶음1, 글 묶음2...] RGBA로."""
    base = Image.new('RGBA', (W, H), X.BG + (255,)); d = ImageDraw.Draw(base); X.frame(base, d)
    if scene.get('tag'):
        f = X.F(40); w = d.textlength(scene['tag'], font=f)
        d.text(((W - w) / 2, TOP + 10), scene['tag'], font=f, fill=X.GOLD)
    # 전체 높이 계산 → 가운데 정렬
    tmp = ImageDraw.Draw(Image.new('RGBA', (W, H)))
    hs = []
    for t, sz, col, bold, gap in scene['items']:
        n = len(X.wrap(tmp, t, X.F(sz, bold), W - 2 * X.M - 120))
        hs.append(n * int(sz * 1.42) + gap)
    top0 = TOP + 90 if scene.get('tag') else TOP
    outs = []
    if scene.get('pillars'):
        P = Image.new('RGBA', (W, H), (0, 0, 0, 0)); pd = ImageDraw.Draw(P)
        ph = 56 + 2 * 132 + 20 + 40
        y0 = top0 + (BOT - top0 - ph - sum(hs)) // 2
        top0 = X.pillars(pd, y0, scene['pillars']) + 40
        outs.append(P); y = top0
    else:
        y = top0 + (BOT - top0 - sum(hs)) // 2
    for (t, sz, col, bold, gap), h in zip(scene['items'], hs):
        L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(L)
        X.block(ld, [('k', t, sz, col, bold, 0)], top=y)
        outs.append(L); y += h
    assert y <= BOT + 5, ('글이 아래로 넘침', y)
    return base, outs


def ease(t): return max(0.0, min(1.0, t))


def render(cfg, which, out):
    # 장면마다 플랫폼별 글 묶음(items_ig / items_yt)이 있으면 그것을 씀. end가 없으면 끝 장면 없음(11/21 새 순서).
    scenes = [dict(s, items=s.get('items_' + which, s.get('items'))) for s in cfg['scenes']]
    if cfg.get('end'): scenes.append(cfg['end'][which])
    total = sum(s['sec'] for s in scenes)
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                           '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                           '-ss', str(cfg.get('audio_start', 0)), '-i', cfg['audio'],
                           '-filter_complex', f"[1:a]atrim=0:{total},afade=t=in:d=1,afade=t=out:st={total-2}:d=2,asetpts=PTS-STARTPTS[a]",
                           '-map', '0:v', '-map', '[a]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20',
                           '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-t', str(total), out],
                          stdin=subprocess.PIPE)
    black = Image.new('RGB', (W, H), X.BG)
    for si, s in enumerate(scenes):
        base, ls = layers(s); n = int(s['sec'] * FPS)
        last = None
        for k in range(n):
            t = k / FPS
            fr = base.copy()
            for i, L in enumerate(ls):
                a = ease((t - 0.3 - i * s.get('step', 0.7)) / 0.6)
                if a > 0:
                    if a < 1:
                        L2 = L.copy(); L2.putalpha(L.getchannel('A').point(lambda v, a=a: int(v * a)))
                        fr.alpha_composite(L2)
                    else:
                        fr.alpha_composite(L)
            fr = fr.convert('RGB')
            fade = ease((s['sec'] - t) / 0.4) if si < len(scenes) - 1 else 1.0
            if fade < 1: fr = Image.blend(black, fr, fade)
            ff.stdin.write(fr.tobytes()); last = fr
        if si == len(scenes) - 1: last.save(out + '.last.jpg', quality=90)
    ff.stdin.close(); ff.wait()
    print('ok', out, total)


if __name__ == '__main__':
    render(json.load(open(sys.argv[1], encoding='utf-8')), sys.argv[2], sys.argv[3])
