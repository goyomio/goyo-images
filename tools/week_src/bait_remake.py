#!/usr/bin/env python3
"""저녁 6시 릴스(미끼편) 다시 만들기 (2026-11-18 미오 님 규칙 반영).
- 수(水)는 검정 + 얇은 흰 테두리, 오행 색은 앱과 같은 색
- 흰 글씨에는 어두운 테두리, 장면마다 영어 줄, 운세 말(luck) 쓰지 않음, 편 수·시간 같은 숫자 없음
- 음악은 원래 영상의 소리를 그대로 씀
python3 tools/week_src/bait_remake.py month|gaeun ig|yt <out.mp4>"""
import os, sys, subprocess
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from tarot_reel import F
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
W, H, FPS = 1080, 1920, 30
CG = os.path.join(ROOT, 'tools', 'fonts', 'CormorantGaramond-500.ttf')
FG, SOFT, EN, GOLD, DIMC = (250, 248, 242), (226, 220, 205), (236, 233, 226), (231, 205, 150), (165, 160, 152)
C = {'목': (47, 217, 107), '화': (255, 59, 47), '토': (255, 194, 26), '금': (255, 255, 255), '수': (0, 0, 0)}
SC = {'k': 1.62, 'e': 1.6}
STEM = [('甲', '목'), ('乙', '목'), ('丙', '화'), ('丁', '화'), ('戊', '토'), ('己', '토'), ('庚', '금'), ('辛', '금'), ('壬', '수'), ('癸', '수')]


def bg(tint=None):
    im = Image.new('RGB', (W, H), (14, 13, 15))
    g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).ellipse([-260, 260, W + 260, 1660], fill=150)
    g = g.filter(ImageFilter.GaussianBlur(260))
    glow = (70, 58, 40) if tint is None else tuple(int(c * 0.32) for c in C[tint])
    if tint == '수': glow = (2, 2, 4)
    im.paste(Image.new('RGB', (W, H), glow), (0, 0), g)
    if tint == '수':  # 수: 검정 바탕 + 얇은 흰 테두리 원
        r = Image.new('L', (W, H), 0); ImageDraw.Draw(r).ellipse([90, 380, W - 90, 1620], outline=120, width=3)
        im.paste(Image.new('RGB', (W, H), (255, 255, 255)), (0, 0), r.filter(ImageFilter.GaussianBlur(1)))
    return im


def draw_line(d, y, parts, font, a=1.0):
    """parts: [(글자, 색)] 가운데 정렬. 검정은 흰 테두리, 나머지는 어두운 테두리."""
    if isinstance(parts, str): parts = [(parts, FG)]
    w = sum(d.textlength(t, font=font) for t, _ in parts)
    while w > W - 90 and font.size > 24:
        font = font.font_variant(size=font.size - 2); w = sum(d.textlength(t, font=font) for t, _ in parts)
    x = (W - w) / 2
    al = int(255 * a)
    for t, c in parts:
        if c == (0, 0, 0):
            d.text((x, y), t, font=font, fill=(0, 0, 0, al), stroke_width=max(2, font.size // 32), stroke_fill=(255, 255, 255, al))
        else:
            d.text((x, y), t, font=font, fill=tuple(c) + (al,), stroke_width=max(1, round(font.size / 24)), stroke_fill=(10, 10, 14, int(al * 0.85)))
        x += d.textlength(t, font=font)


def header(d):
    draw_line(d, 200, '사주 · 오행음악 · 고요', F(40, True))
    draw_line(d, 258, [('FIVE ELEMENTS MUSIC', DIMC)], ImageFont.truetype(CG, 30))


def _font(it):
    z = int(it[2] * SC[it[0]])
    if it[0] == 'e': return ImageFont.truetype(CG, int(z * 1.25)) if it[1] == [('GOYO', FG)] else F(z, False)
    return F(z, it[3] if len(it) > 3 and isinstance(it[3], bool) else True)


def wrap(d, items):
    """영어 줄·작은 안내 줄이 화면보다 길면 글씨를 줄이지 않고 줄을 나눔(휴대폰에서 크게 보이게)."""
    out = []
    for it in items:
        if it[0] == 'gap': out.append(it); continue
        parts = it[1] if isinstance(it[1], list) else [(it[1], None)]
        small = it[0] == 'e' or (len(it) > 3 and it[3] is False)
        if not small or len(parts) != 1:
            out.append(it); continue
        txt, col = parts[0]; f = _font(it)
        if d.textlength(txt, font=f) <= W - 110:
            out.append(it); continue
        words, line, lines = txt.split(' '), '', []
        for w_ in words:
            t = (line + ' ' + w_).strip()
            if d.textlength(t, font=f) > W - 110 and line: lines.append(line); line = w_
            else: line = t
        lines.append(line)
        # 줄 길이를 고르게 (한 단어만 다음 줄로 넘어가지 않게)
        n = len(lines); target = d.textlength(txt, font=f) / n * 1.06
        lines, line = [], ''
        for w_ in words:
            t = (line + ' ' + w_).strip()
            if line and d.textlength(t, font=f) > target and len(lines) < n - 1: lines.append(line); line = w_
            else: line = t
        lines.append(line)
        for ln in lines:
            out.append((it[0], [(ln, col)] if col is not None else ln) + tuple(it[2:]))
    return out


def layout(d, items, a):
    """items: (종류, 내용, 크기[, 색]) — 종류 k(한글/한자), e(영어), gap"""
    items = wrap(d, items)
    hs = []
    for it in items:
        if it[0] == 'gap': hs.append(it[1]); continue
        hs.append(int(it[2] * SC[it[0]] * (1.5 if it[0] == 'e' else 1.32)))
    y = (H - sum(hs)) // 2 + 40
    for it, h in zip(items, hs):
        if it[0] != 'gap':
            font = _font(it)
            parts = it[1] if isinstance(it[1], list) else [(it[1], EN if it[0] == 'e' else (it[4] if len(it) > 4 else FG))]
            draw_line(d, y, parts, font, a)
        y += h


def frame(sc, a):
    im = bg(sc.get('tint')).convert('RGBA'); lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    header(d); layout(d, sc['items'], a)
    return Image.alpha_composite(im, lay).convert('RGB')


def dots():
    return [(' ● ', C[k]) for k in ['목', '화', '토', '금', '수']]


def month(p):
    li = lambda lab, k, h: [(f'{lab} · ', FG), (f'{k}({h})', C[k])]
    LIST = [('k', li('5·6월생', '화', '火'), 54), ('k', li('8·9월생', '금', '金'), 54), ('k', li('11·12월생', '수', '水'), 54),
            ('k', li('2·3월생', '목', '木'), 54), ('k', li('1·4·7·10월생', '토', '土'), 54)]
    def el(lab, en_m, k, h, ko, en):
        return {'sec': 3.0, 'tint': k, 'items': [('k', lab, 76), ('e', en_m, 40), ('gap', 30), ('k', [(h, C[k])], 300), ('gap', 10),
                ('k', f'{k}({h}) · {ko}', 58), ('e', en, 42)]}
    last_link = '오행별 곡은 프로필 링크에서' if p == 'ig' else '오행별 곡은 @goyo_mio 채널에서'
    last_en = 'Your element: link in bio' if p == 'ig' else 'Your element: @goyo_mio'
    return [
        {'sec': 1.6, 'items': [('k', '몇 월에', 96), ('k', '태어나셨어요?', 96), ('e', 'What month were you born?', 46), ('gap', 20), ('k', dots(), 50)]},
        {'sec': 2.4, 'items': [('k', '태어난 달마다', 72), ('k', '소리가 달라요', 72), ('e', 'Each birth month has its own sound', 42), ('gap', 30)] + LIST},
        el('5·6월생', 'Born in May or June', '화', '火', '햇살처럼 번지는 재즈', 'Fire · jazz that spreads like sunlight'),
        el('8·9월생', 'Born in August or September', '금', '金', '또렷하게 울리는 피아노 독주', 'Metal · clear solo piano'),
        el('11·12월생', 'Born in November or December', '수', '水', '물결처럼 흐르는 피아노', 'Water · ambient piano that flows'),
        el('2·3월생', 'Born in February or March', '목', '木', '새순처럼 자라는 실내악', 'Wood · chamber music that grows'),
        el('1·4·7·10월생', 'Born in January, April, July, or October', '토', '土', '포근하게 감싸는 로파이', 'Earth · soft lo-fi'),
        {'sec': 3.0, 'items': [('k', '한 장 정리', 66), ('e', 'Save this to find your element', 38), ('gap', 16)] + [(i[0], i[1], 48) for i in LIST] +
            [('gap', 24), ('k', last_link, 46), ('e', last_en, 40), ('gap', 14), ('k', [('※ 절기 기준이라 달 초(4~8일 무렵)생은 앞 달로 보세요', DIMC)], 36, False)]},
    ]


def gaeun(p):
    row = [(f' {h} ', C[k]) for h, k in [('木', '목'), ('火', '화'), ('土', '토'), ('金', '금'), ('水', '수')]]
    st1 = [(f' {h} ', C[k]) for h, k in STEM[:5]]; st2 = [(f' {h} ', C[k]) for h, k in STEM[5:]]
    last_link = '프로필 링크에서 들어 보세요' if p == 'ig' else '채널 고요에서 들어 보세요'
    last_en = 'Hear the element your chart needs: link in bio' if p == 'ig' else 'Hear the element your chart needs: @goyo_mio'
    return [
        {'sec': 2.6, 'items': [('k', '운은 기다리는 게 아니라,', 68), ('k', '여는 거예요', 68), ('e', "Don't wait for your path to open. Open it.", 40), ('gap', 40), ('k', [('개운', GOLD)], 200), ('k', [('開運', SOFT)], 56, False)]},
        {'sec': 3.2, 'items': [('k', '개운은', 80), ('k', '행동이에요', 104), ('e', 'Opening Your Path (Gaeun) is something you do', 46)]},
        {'sec': 4.0, 'items': [('k', '①', 52), ('k', '먹는 것', 76), ('e', 'What you eat', 42), ('gap', 50), ('k', '②', 52), ('k', '가까이 두는 것', 76), ('e', 'What you keep close', 42)]},
        {'sec': 3.2, 'items': [('k', '고요는 세 번째,', 76), ('k', '감상하는 개운이에요', 76), ('e', 'Goyo is the third way: open it by listening', 42)]},
        {'sec': 3.5, 'items': [('k', '오행마다, 일간마다', 70), ('k', '따로 만든 소리', 70), ('e', 'Music for each element and each day master', 40), ('gap', 40),
            ('k', row, 96), ('gap', 20), ('k', st1, 72), ('k', st2, 72)]},
        {'sec': 3.5, 'items': [('k', '내 사주에 필요한 기운,', 70), ('k', last_link, 70), ('e', last_en, 40), ('gap', 30),
            ('e', [('GOYO', FG)], 96), ('gap', 20), ('k', [('※ 오행을 소리로 옮긴 해석이에요', DIMC)], 38, False)]},
    ]


SRC = {'month': 'shorts/미끼편/몇월생 미끼 쇼츠.mp4', 'gaeun': 'shorts/미끼편/D 개운은 행동 쇼츠.mp4'}


def main():
    kind, plat, out = sys.argv[1], sys.argv[2], sys.argv[3]
    scenes = {'month': month, 'gaeun': gaeun}[kind](plat)
    src = os.path.join(ROOT, SRC[kind]); wav = out + '.m4a'
    total = sum(s['sec'] for s in scenes)
    subprocess.check_call(['ffmpeg', '-v', 'error', '-y', '-i', src + '.orig.mp4' if os.path.exists(src + '.orig.mp4') else src, '-vn', '-t', str(total), '-c:a', 'aac', '-b:a', '192k', wav])
    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                           '-i', wav, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-c:a', 'copy',
                           '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    for i, sc in enumerate(scenes):
        n = int(round(sc['sec'] * FPS)); full = frame(sc, 1.0).tobytes()
        for k in range(n):
            t = k / FPS
            if i == 0 or t >= 0.3: ff.stdin.write(full)
            else: ff.stdin.write(frame(sc, max(0.15, t / 0.3)).tobytes())
    ff.stdin.close(); ff.wait(); os.remove(wav); print('ok', out, total)


if __name__ == '__main__':
    main()
