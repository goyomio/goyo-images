"""정미년 캐러셀 유튜브판: jeongmi/<MMDD>/slides.json → 「프로필 링크」 문구만 유튜브용으로 바꿔 렌더 → 1350 정사각형.
python3 jm_yt.py <repo> <MMDD> <outdir>"""
import json, os, sys
repo, d, out = sys.argv[1:4]
sys.path.insert(0, os.path.join(repo, 'tools/week_src'))
os.chdir(repo)
import example_saju as X
from PIL import Image, ImageChops
import numpy as np
REP = [('프로필 링크에서', '글에 있는 링크에서'), ('프로필 링크의', '글에 있는 링크의'), ('프로필 링크', '글에 있는 링크'),
       ('link in bio', 'link in this post'), ('Link in bio', 'Link in this post')]
cfg = json.load(open(f'jeongmi/{d}/slides.json', encoding='utf-8'))
os.makedirs(out, exist_ok=True)
X.W, X.H = 1080, 1350
n = len(cfg['slides'])
post = 'posts/2027-%s-%s' % (d[:2], d[2:4])
for k, s in enumerate(cfg['slides'], 1):
    raw = json.dumps(s, ensure_ascii=False); changed = any(a in raw for a, _ in REP)
    orig = X.draw_slide(s, k, n).convert('RGB')
    ref = os.path.join(post, '%02d.jpg' % k)
    diff = np.asarray(ImageChops.difference(orig, Image.open(ref).convert('RGB'))).astype(int).mean() if os.path.exists(ref) else -1
    for a, b in REP: raw = raw.replace(a, b)
    im = X.draw_slide(json.loads(raw), k, n).convert('RGB')
    sq = Image.new('RGB', (1350, 1350), X.BG); sq.paste(im, (135, 0)); sq.save(os.path.join(out, '%02d.jpg' % k), quality=93)
    print(d, k, 'yt문구' if changed else '-', '원본재현 평균차', round(diff, 2))
