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
    if tint not in (None, '수'): tint = None  # 글자색이 묻히지 않게 바탕은 어둡게, 색은 글자로 (수만 검정+흰 테두리 바탕)
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


def grid(d, y, a):
    """사주 여덟 칸(시·일·월·연), 일간 자리에 '나'"""
    bw, gap = 150, 22; x0 = (W - (bw * 4 + gap * 3)) / 2; al = int(255 * a)
    for r in range(2):
        for c in range(4):
            x = x0 + c * (bw + gap); yy = y + r * (bw + gap); me = (r == 0 and c == 1)
            d.rounded_rectangle([x, yy, x + bw, yy + bw], 18, outline=(GOLD if me else (120, 116, 108)) + (al,), width=5 if me else 3,
                                fill=(60, 52, 38, al) if me else None)
            if me: draw_line_at(d, x + bw / 2, yy + 22, '나', F(84, True), a)
    for c, lab in enumerate(['시', '일', '월', '연']):
        draw_line_at(d, x0 + c * (bw + gap) + bw / 2, y + 2 * (bw + gap) + 4, lab, F(44, True), a, SOFT)
    return 2 * (bw + gap) + 70


def draw_line_at(d, cx, y, t, font, a, col=FG):
    w = d.textlength(t, font=font); al = int(255 * a)
    d.text((cx - w / 2, y), t, font=font, fill=col + (al,), stroke_width=2, stroke_fill=(10, 10, 14, int(al * .85)))


def frame(sc, a):
    im = bg(sc.get('tint')).convert('RGBA'); lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    header(d); layout(d, sc['items'], a)
    if sc.get('grid'): grid(d, sc['grid'], a)
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


def onechar(p):
    EN_ST = ['Yang Wood', 'Yin Wood', 'Yang Fire', 'Yin Fire', 'Yang Earth', 'Yin Earth', 'Yang Metal', 'Yin Metal', 'Yang Water', 'Yin Water']
    KO_ST = ['갑목', '을목', '병화', '정화', '무토', '기토', '경금', '신금', '임수', '계수']
    T = [4.5, 5.0, 6.0, 7.0, 7.5, 8.5, 9.0, 10.0, 11.0, 11.5, 12.5]
    st = [{'sec': round(T[i + 1] - T[i], 2), 'tint': k, 'items': [('k', [(h, C[k])], 360), ('gap', 20), ('k', f'{KO_ST[i]}({h})', 72), ('e', EN_ST[i], 50)]}
          for i, (h, k) in enumerate(STEM)]
    st1 = [(f' {h} ', C[k]) for h, k in STEM[:5]]; st2 = [(f' {h} ', C[k]) for h, k in STEM[5:]]
    link = '프로필 링크에서 들어 보세요' if p == 'ig' else '@goyo_mio 채널에서 들어 보세요'
    link_en = 'Then hear its music: link in bio' if p == 'ig' else 'Then hear its music: @goyo_mio'
    app = '프로필 링크 사주앱에서 바로 보여요' if p == 'ig' else '@goyo_mio 채널 상단 링크 사주앱에서'
    return [
        {'sec': 2.5, 'grid': 1180, 'items': [('k', '사주 여덟 글자 중,', 74), ('k', "'나'는 딱 한 글자예요", 74), ('e', 'Only one of your eight characters is you', 44), ('gap', 420)]},
        {'sec': 2.0, 'grid': 1180, 'items': [('k', '태어난 날의 천간,', 70), ('k', '일간', 120), ('e', 'Your day master: the stem of your birth day', 44), ('gap', 400)]},
    ] + st + [
        {'sec': 2.5, 'items': [('k', '그 한 글자를', 84), ('k', '음악으로 옮겼어요', 84), ('e', 'That one character, turned into music', 46)]},
        {'sec': 3.0, 'items': [('k', '일간마다 한 편씩,', 78), ('k', '내 글자의 소리', 78), ('e', 'One playlist for each day master', 44), ('gap', 40), ('k', st1, 90), ('k', st2, 90)]},
        {'sec': 2.0, 'items': [('k', '내 글자는?', 96), ('gap', 10), ('k', app, 54), ('e', 'Find your day master in the Saju app', 44)]},
        {'sec': 2.0, 'items': [('k', '찾았으면,', 84), ('k', link, 66), ('e', link_en, 44), ('gap', 30), ('e', [('GOYO', FG)], 96)]},
    ]


KO_EL = {'목': ('나무', '木', 'Wood'), '화': ('불', '火', 'Fire'), '토': ('흙', '土', 'Earth'), '금': ('금', '金', 'Metal'), '수': ('물', '水', 'Water')}
MANY = {
    '화': ('화가', ['밝다', '열정적이다', '표현이 솔직하다'], 'Bright. Passionate. Says what they feel.',
          [('뜨거운 불엔', '수', 'Blazing Fire'), ('넘치는 불엔', '토', 'Excess Fire')]),
    '금': ('금이', ['맺고 끊음이 분명하다', '원칙을 지킨다', '말이 직설적이다'], 'Clear-cut. Principled. Straight-talking.',
          [('너무 단단한 금엔', '화', 'Rigid Metal'), ('넘치는 금엔', '수', 'Excess Metal')]),
    '목': ('목이', ['추진력이 있다', '곧다', '성장 욕구가 크다'], 'Driven. Upright. Always wanting to grow.',
          [('무성한 나무엔', '금', 'Overgrown Wood'), ('넘치는 나무엔', '화', 'Excess Wood')]),
    '토': ('토가', ['듬직하다', '신중하다', '잘 흔들리지 않는다'], 'Steady. Careful. Hard to shake.',
          [('굳은 흙엔', '목', 'Hardened Earth'), ('넘치는 흙엔', '금', 'Excess Earth'), ('메마른 흙엔', '수', 'Dry Earth')]),
    '수': ('물이', ['생각이 많다', '감정이 깊다', '밤에 더 또렷하다'], 'Lots of thoughts. Deep feelings. Sharper at night.',
          [('넘치는 물엔', '목', 'Overflowing Water'), ('불어난 물엔', '토', 'Rising Water'), ('차가운 물엔', '화', 'Cold Water')]),
}


def many(el):
    def build(p):
        subj, traits, tr_en, ans = MANY[el]; name = KO_EL[el][2]
        hook = [(subj[0] if el != '수' else '물', C[el]), (subj[1:] + ' 많다는 말,', FG)]
        ko_row = [(f' {k} ', C[k]) for k in ['목', '화', '토', '금', '수']]
        hz_row = [(f' {KO_EL[k][1]} ', C[k]) for k in ['목', '화', '토', '금', '수']]
        link = '프로필 링크에서' if p == 'ig' else '채널 @goyo_mio에서'
        link_en = 'The sound your chart needs: link in bio' if p == 'ig' else 'The sound your chart needs: @goyo_mio'
        per = round(3.5 / len(ans), 2)
        A = [{'sec': per, 'tint': k, 'items': [('k', lead, 64), ('k', [('↓', SOFT)], 50), ('gap', 20), ('k', [(KO_EL[k][0], C[k])], 250),
              ('k', [(KO_EL[k][1], C[k])], 80), ('gap', 20), ('e', f'{en_} needs {KO_EL[k][2]}', 46)]} for lead, k, en_ in ans]
        A[-1]['sec'] = round(3.5 - per * (len(ans) - 1), 2)
        return [
            {'sec': 2.5, 'items': [('k', '사주에', 70), ('k', hook, 92), ('k', '들어 보셨어요?', 92), ('e', f'Ever been told your chart has a lot of {name}?', 46)]},
            {'sec': 2.5, 'items': [('k', [('흔히 이렇게 말해요', SOFT)], 54)] + [('k', t, 80) for t in traits] + [('e', tr_en, 46)]},
            {'sec': 2.0, 'items': [('k', '그럼,', 84), ('k', '무슨 기운이', 84), ('k', '필요할까요?', 84), ('e', 'So what does it need?', 48)]},
        ] + A + [
            {'sec': 2.0, 'items': [('k', '사주마다', 90), ('k', [('달라요', GOLD)], 130), ('e', 'It depends on your chart', 48)]},
            {'sec': 3.5, 'items': [('k', '그래서 고요엔', 78), ('k', '다섯 오행이 다 있어요', 78), ('e', 'So Goyo has music for all five elements', 44), ('gap', 40),
                                   ('k', ko_row, 110), ('k', hz_row, 54), ('gap', 20), ('k', [('일간마다 따로 만든 소리도 있어요', SOFT)], 46)]},
            {'sec': 3.4, 'items': [('k', '내 사주에 필요한 소리,', 74), ('k', link, 74), ('e', link_en, 44), ('gap', 30),
                                   ('e', [('GOYO', FG)], 96), ('gap', 20), ('k', [('※ 오행을 소리로 옮긴 해석이에요', DIMC)], 38, False)]},
        ]
    return build


def elsc(sec, top, k, big, hz, en, sub=None, top_en=None):
    """한 기운 장면: 위 라벨, 한글 크게(오행 색), 한자 작게 아래, 영어"""
    it = [('k', top, 72)] + ([('e', top_en, 40)] if top_en else []) + [('gap', 20), ('k', [(big, C[k])], 230 if len(big) < 3 else 180), ('k', [(hz, C[k])], 80)]
    if sub: it += [('gap', 10), ('k', sub, 58)]
    return {'sec': sec, 'tint': k, 'items': it + [('gap', 16), ('e', en, 46)]}


def ending(p, ko1, en1, sec=3.0):
    link = '프로필 링크에서' if p == 'ig' else '채널 @goyo_mio에서'
    return {'sec': sec, 'items': [('k', ko1, 74), ('k', link, 74), ('e', en1 + (': link in bio' if p == 'ig' else ': @goyo_mio'), 44), ('gap', 30),
                                  ('e', [('GOYO', FG)], 96), ('gap', 20), ('k', [('※ 오행을 소리로 옮긴 해석이에요', DIMC)], 38, False)]}


def el_rows():
    return [('k', [(f' {k} ', C[k]) for k in ['목', '화', '토', '금', '수']], 110), ('k', [(f' {KO_EL[k][1]} ', C[k]) for k in ['목', '화', '토', '금', '수']], 54)]


def stem_rows():
    ko = list('갑을병정무기경신임계')
    return [('k', [(f' {ko[i]} ', C[STEM[i][1]]) for i in range(5)], 96), ('k', [(f' {STEM[i][0]} ', C[STEM[i][1]]) for i in range(5)], 48), ('gap', 10),
            ('k', [(f' {ko[i]} ', C[STEM[i][1]]) for i in range(5, 10)], 96), ('k', [(f' {STEM[i][0]} ', C[STEM[i][1]]) for i in range(5, 10)], 48)]


def weekday(p):
    return [
        {'sec': 2.5, 'items': [('k', '제일 좋아하는 요일,', 84), ('k', '뭐예요?', 110), ('e', "What's your favorite day of the week?", 46)]},
        {'sec': 2.5, 'items': [('k', '그 요일 이름,', 84), ('k', '사실 오행이에요', 84), ('e', 'In Korean, its name is one of the five elements', 46)]},
        elsc(0.8, '화요일', '화', '불', '火', 'Tuesday · Fire'),
        elsc(0.8, '수요일', '수', '물', '水', 'Wednesday · Water'),
        elsc(0.8, '목요일', '목', '나무', '木', 'Thursday · Wood'),
        elsc(0.8, '금요일', '금', '쇠와 돌', '金', 'Friday · Metal'),
        elsc(0.8, '토요일', '토', '흙', '土', 'Saturday · Earth'),
        {'sec': 2.5, 'items': [('k', "금요일의 '금'은", 84), ('k', '돈이 아니에요', 84), ('e', "In Korean Friday, Geum (金) isn't gold. It means metal.", 44)]},
        {'sec': 2.5, 'items': [('k', '일주일 안에,', 84), ('k', '다섯 기운이 다 있어요', 84), ('e', 'Every week holds all five', 46), ('gap', 40)] + el_rows()},
        {'sec': 3.0, 'items': [('k', '요일마다,', 84), ('k', '그 요일의 소리를', 84), ('e', 'A sound for each day', 46)]},
        ending(p, '다섯 가지 고요,', 'Five kinds of quiet'),
    ]


def daytime(p):
    return [
        {'sec': 2.5, 'items': [('k', '아침형이에요,', 92), ('k', '저녁형이에요?', 92), ('e', 'Morning person or night owl?', 48)]},
        {'sec': 2.5, 'items': [('k', '오행에선 하루도', 80), ('k', '다섯 기운으로 흘러요', 80), ('e', 'In the five elements, a day moves through all five', 44)]},
        elsc(2.0, '아침은', '목', '나무', '木', 'Morning · Wood · growing', '자라는 시간'),
        elsc(2.0, '한낮은', '화', '불', '火', 'Noon · Fire · spreading', '번지는 시간'),
        elsc(2.0, '저녁은', '금', '쇠', '金', 'Evening · Metal · gathering', '거두는 시간'),
        elsc(2.0, '밤은', '수', '물', '水', 'Night · Water · settling', '가라앉는 시간'),
        elsc(2.0, '그 사이마다', '토', '흙', '土', 'In between · Earth · connecting', '이어 주는 시간'),
        {'sec': 2.5, 'items': [('k', '깨어 있는 시간에,', 84), ('k', '맞는 소리를', 84), ('e', 'A sound for every hour', 46)]},
        ending(p, '다섯 가지 고요,', 'Five kinds of quiet', 2.5),
    ]


def color(p):
    return [
        {'sec': 2.5, 'items': [('k', '좋아하는 색,', 92), ('k', '바로 떠오르죠?', 92), ('e', 'Got a favorite color?', 48)]},
        {'sec': 2.5, 'items': [('k', '색마다', 84), ('k', '오행이 있어요', 84), ('e', 'Every color belongs to an element', 46)]},
        elsc(2.0, '초록', '목', '나무', '木', 'Green → Wood'),
        elsc(2.0, '빨강', '화', '불', '火', 'Red → Fire'),
        elsc(2.0, '노랑', '토', '흙', '土', 'Yellow → Earth'),
        elsc(2.0, '하양', '금', '쇠와 돌', '金', 'White → Metal'),
        elsc(2.0, '검정', '수', '물', '水', 'Black → Water', [('깊은 물은 검어요', SOFT)]),
        {'sec': 2.5, 'items': [('k', '다섯 색의 소리,', 84), ('k', '다 있어요', 84), ('e', 'All five, in sound', 46), ('gap', 40)] + el_rows()},
        ending(p, '다섯 가지 고요,', 'Five kinds of quiet', 2.5),
    ]


def wood2(p):
    return [
        {'sec': 2.5, 'items': [('k', '갑목과 을목,', 84), ('k', '같은 나무일까요?', 84), ('e', 'Yang Wood and Yin Wood: the same tree?', 44), ('gap', 40),
                               ('k', [('갑목 · 을목', C['목'])], 120)]},
        elsc(3.0, '갑목은', '목', '갑목', '甲', 'Yang Wood · a tall, straight tree', '곧게 뻗는 큰 나무'),
        elsc(3.0, '을목은', '목', '을목', '乙', 'Yin Wood · a climbing vine', '감아 오르는 덩굴'),
        {'sec': 2.5, 'items': [('k', '그래서', 84), ('k', [('음악도 달라요', GOLD)], 100), ('e', 'So their music is different too', 46)]},
        {'sec': 3.0, 'items': [('k', '일간마다,', 80), ('k', '따로 만든 소리', 80), ('e', 'Music for each day master', 46), ('gap', 30)] + stem_rows()},
        ending(p, '내 일간의 소리,', 'Your day master\'s sound', 4.0),
    ]


def anymusic(p):
    return [
        {'sec': 2.3, 'items': [('k', '공부할 때,', 90), ('k', '아무 음악이나 틀어요?', 84), ('e', 'Do you play just any music while you study?', 46)]},
        {'sec': 2.3, 'items': [('k', '쉴 때도,', 96), ('k', '잠들 때도,', 96), ('e', 'While you rest. While you fall asleep.', 46)]},
        {'sec': 2.4, 'items': [('k', '하루에 몇 시간씩', 84), ('k', '듣는 소리예요', 84), ('e', "It's what you hear for hours every day", 46)]},
        {'sec': 3.5, 'items': [('k', '그렇게 오래', 80), ('k', '곁에 둘 소리라면,', 80), ('k', [('내 사주로 골라 보세요', GOLD)], 80), ('e', 'If it stays with you that long, choose it by your chart', 44)]},
        {'sec': 3.0, 'items': [('k', '오행마다, 일간마다', 80), ('k', '따로 만든 소리', 80), ('e', 'Music for each element and each day master', 44), ('gap', 30)] + el_rows()},
        {'sec': 3.5, 'items': [('k', '가사 없이,', 84), ('k', '곡이 바뀌어도 모르게', 80), ('k', '이어지는 연주곡', 80), ('e', 'No lyrics. Track after track, seamless.', 44)]},
        ending(p, '내 사주의 소리,', 'The sound of your chart', 3.0),
    ]


SRC = {'month': 'shorts/미끼편/몇월생 미끼 쇼츠.mp4', 'gaeun': 'shorts/미끼편/D 개운은 행동 쇼츠.mp4', 'onechar': 'shorts/미끼편/A 나는 한 글자 쇼츠.mp4',
       'fire': 'shorts/미끼편/I 화 많은 사주 쇼츠.mp4', 'metal': 'shorts/미끼편/G 금 많은 사주 쇼츠.mp4', 'wood': 'shorts/미끼편/J 목 많은 사주 쇼츠.mp4',
       'earth': 'shorts/미끼편/H 토 많은 사주 쇼츠.mp4', 'water': 'shorts/미끼편/F 물 많은 사주 쇼츠.mp4',
       'weekday': 'shorts/미끼편/K 요일 쇼츠.mp4', 'daytime': 'shorts/미끼편/L 아침형 저녁형 쇼츠.mp4', 'color': 'shorts/미끼편/M 좋아하는 색 쇼츠.mp4',
       'wood2': 'shorts/미끼편/C 갑목과 을목 쇼츠.mp4', 'anymusic': 'shorts/미끼편/E 아무 음악 쇼츠.mp4'}


def main():
    kind, plat, out = sys.argv[1], sys.argv[2], sys.argv[3]
    scenes = {'month': month, 'gaeun': gaeun, 'onechar': onechar, 'fire': many('화'), 'metal': many('금'), 'wood': many('목'),
              'earth': many('토'), 'water': many('수'),
              'weekday': weekday, 'daytime': daytime, 'color': color, 'wood2': wood2, 'anymusic': anymusic}[kind](plat)
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
