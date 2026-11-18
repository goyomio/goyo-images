#!/usr/bin/env python3
"""고정 캐러셀 2종 (2026-11-18). 새 디자인 규칙: 검은 바탕, 큰 흰 제목, GOYO 로고, 색 하나.
python3 tools/week_src/pin_carousel.py find|intro"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from tarot_reel import F
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
BG = (10, 10, 12); FG = (250, 248, 242); SUB = (220, 215, 205); DIMC = (150, 145, 135); GOLD = (201, 169, 106)
OH = [('木', '목', (47, 217, 107)), ('火', '화', (255, 59, 47)), ('土', '토', (255, 194, 26)), ('金', '금', (255, 255, 255)), ('水', '수', (0, 0, 0))]
CG = os.path.join(os.path.dirname(__file__), '..', 'fonts', 'CormorantGaramond-500.ttf')
ENC = (175, 170, 160)


EN = {'EN1_1': 'Find the five elements in your Saju', 'EN1_2': 'Four pillars, two characters each: eight in all', 'EN1_2b': 'Each one carries an element', 'EN1_3': 'See which elements you have more or less of', 'EN1_3b': 'Example only. Every chart is different', 'EN1_4': 'See yours right away: link in bio', 'EN1_5': "Having less doesn't always mean you need more", 'EN1_6': 'Your day master: the character for your birth day', 'EN1_6b': 'Each one has its own Goyo music', 'EN2_1': 'Goyo: choose the sound of your Saju', 'EN2_2a': 'I believe changing small daily habits', 'EN2_2b': 'is the easiest, surest way to work with your chart', 'EN2_3': 'So I chose something effortless to keep close: sound', 'EN2_4': 'A different sound for each element', 'EN2_5a': "Every morning: Today's Tarot", 'EN2_5b': 'Saju reels: symbolic stars and their sounds', 'EN2_5c': 'Link in bio: your five elements and day master', 'EN2_6': 'Find your five elements: link in bio'}


def en(d, y, t, size=40, fill=ENC):
    f = ImageFont.truetype(CG, size); ct(d, y, EN.get(t, t), f, fill)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def new():
    im = Image.new('RGB', (W, H), BG); return im, ImageDraw.Draw(im)


def ct(d, y, t, f, fill):
    w = d.textlength(t, font=f); d.text(((W - w) / 2, y), t, font=f, fill=fill)


def logo(d, y=1210, size=50, fill=DIMC):
    f = ImageFont.truetype(CG, size); sp = int(size * 0.42)
    ws = [d.textlength(c, font=f) for c in 'GOYO']; x = (W - sum(ws) - sp * 3) / 2
    for c, w in zip('GOYO', ws): d.text((x, y), c, font=f, fill=fill); x += w + sp


def lines(d, y, arr, f, fill, gap):
    for t in arr: ct(d, y, t, f, fill); y += gap
    return y


def hanja_row(d, y, size=96, sp=40):
    f = F(size, True); ws = [d.textlength(h, font=f) for h, _, _ in OH]; x = (W - sum(ws) - sp * 4) / 2
    for (h, _, c), w in zip(OH, ws):
        d.text((x, y), h, font=f, fill=c, stroke_width=3 if h == '水' else 0, stroke_fill=(255, 255, 255)); x += w + sp


def page_no(d, i, n):
    pass  # 쪽 번호는 넣지 않음(인스타 점 표시로 충분)


def find(out):
    os.makedirs(out, exist_ok=True); S = []
    # 1 표지
    im, d = new()
    lines(d, 330, ['내 사주의', '오행 찾기'], F(150, True), FG, 190)
    hanja_row(d, 760)
    ct(d, 930, '생년월일시만 있으면 돼요', F(56), SUB)
    en(d, 1020, 'EN1_1', 50)
    logo(d); S.append(im)
    # 2 사주팔자란
    im, d = new()
    ct(d, 130, '사주팔자란?', F(110, True), FG)
    y = lines(d, 300, ['태어난 해 · 달 · 날 · 시,', '네 기둥(사주)에 두 글자씩', '모두 여덟 글자(팔자)예요.'], F(58), SUB, 84)
    bw, bh, gap = 190, 250, 26; x0 = (W - (bw * 4 + gap * 3)) / 2
    for i, lab in enumerate(['시', '일', '월', '년']):
        x = x0 + i * (bw + gap); d.rounded_rectangle([x, 590, x + bw, 590 + bh], 22, outline=(80, 78, 74), width=3)
        lw = d.textlength(lab, font=F(44, True)); d.text((x + (bw - lw) / 2, 610), lab, font=F(44, True), fill=GOLD)
        for k in range(2):
            q = '○'; qw = d.textlength(q, font=F(64)); d.text((x + (bw - qw) / 2, 685 + k * 75), q, font=F(64), fill=(120, 118, 112))
    lines(d, 860, ['여덟 글자는 저마다', '목 · 화 · 토 · 금 · 수 가운데', '하나의 기운을 가져요.'], F(58, True), FG, 84)
    en(d, 1108, 'EN1_2'); en(d, 1156, 'EN1_2b')
    logo(d, 1240, 44); S.append(im)
    # 3 오행으로 나누면
    im, d = new()
    lines(d, 130, ['오행으로', '나눠 보면'], F(110, True), FG, 140)
    ct(d, 430, '어떤 기운이 많고 적은지 보여요', F(56), SUB)
    en(d, 505, 'EN1_3')
    vals = [3, 1, 2, 2, 0]
    for i, ((h, k, c), v) in enumerate(zip(OH, vals)):
        y = 580 + i * 110
        d.text((150, y - 8), h, font=F(76, True), fill=c, stroke_width=3 if h == '水' else 0, stroke_fill=(255, 255, 255))
        d.rounded_rectangle([280, y + 18, 880, y + 58], 20, fill=(30, 30, 34))
        if v: d.rounded_rectangle([280, y + 18, 280 + 200 * v, y + 58], 20, fill=c, outline=(255, 255, 255) if h == '水' else None, width=3 if h == '水' else 0)
        d.text((910, y + 2), str(v), font=F(58), fill=SUB)
    ct(d, 1130, '예시예요. 사람마다 달라요.', F(44), DIMC)
    en(d, 1183, 'EN1_3b', 34, DIMC)
    logo(d, 1230, 44); S.append(im)
    # 4 프로필 링크에서
    im, d = new()
    lines(d, 90, ['프로필 링크에서', '바로 볼 수 있어요'], F(96, True), FG, 125)
    en(d, 330, 'EN1_4')
    shot = Image.open('/tmp/page_out.png').convert('RGB')
    shot = shot.crop((0, 0, shot.width, min(shot.height, int(shot.width * 1.05))))
    s = 690 / shot.height; shot = shot.resize((int(shot.width * s), 690))
    fr = Image.new('RGB', (shot.width + 12, shot.height + 12), (70, 68, 64)); fr.paste(shot, (6, 6))
    im.paste(fr, ((W - fr.width) // 2, 410))
    ct(d, 1135, '생년월일시만 넣으면 여덟 글자와 오행이 나와요', F(42), SUB)
    logo(d, 1230, 44); S.append(im)
    # 5 적다고 꼭 필요한 건 아니에요
    im, d = new()
    lines(d, 200, ['적다고', '꼭 필요한', '기운은 아니에요'], F(110, True), FG, 145)
    lines(d, 690, ['같은 "목이 없는 사주"라도', '목이 필요한 사람이 있고,', '덜어야 하는 사람도 있어요.'], F(56), SUB, 82)
    lines(d, 970, ['일간의 힘(억부)과', '태어난 계절(조후)까지 함께 봐요.'], F(56, True), GOLD, 82)
    en(d, 1150, 'EN1_5')
    logo(d, 1240, 44); S.append(im)
    # 6 내 일간 편
    im, d = new()
    lines(d, 220, ['나를 뜻하는 글자,', '일간'], F(110, True), FG, 150)
    lines(d, 600, ['태어난 날의 천간이 일간이에요.', '고요에는 일간마다', '따로 만든 음악이 있어요.'], F(58), SUB, 86)
    lines(d, 920, ['내 일간 편 듣기는', '프로필 링크에서'], F(66, True), FG, 96)
    en(d, 1108, 'EN1_6'); en(d, 1156, 'EN1_6b')
    logo(d, 1240, 44); S.append(im)
    for i, im in enumerate(S, 1): im.save(os.path.join(out, f'{i:02d}.jpg'), quality=93)
    return S


def intro(out):
    os.makedirs(out, exist_ok=True); S = []
    im, d = new()
    lines(d, 360, ['내 사주의', '소리를', '고르는 곳'], F(140, True), FG, 170)
    en(d, 930, 'EN2_1', 54)
    logo(d, 1080, 64, (200, 190, 170)); S.append(im)
    # 2 시작한 이유
    im, d = new()
    ct(d, 150, '고요를 시작한 이유', F(90, True), FG)
    lines(d, 370, ['사주를 풀다 보면', '"내게 필요한 기운을', '어떻게 곁에 둘 수 있을까요?"', '라는 질문을 자주 받아요.'], F(58), SUB, 86)
    lines(d, 770, ['저는 생활 습관을 바꾸는 것이', '가장 부담 없고 정확한', '개운이라고 생각해요.'], F(58, True), FG, 86)
    en(d, 1060, 'EN2_2a', 38); en(d, 1108, 'EN2_2b', 38)
    logo(d, 1240, 44); S.append(im)
    # 3
    im, d = new()
    lines(d, 260, ['그런데 습관은', '매일 마음을 먹어야 해서', '오래 이어 가기가 어렵더라고요.'], F(66), SUB, 100)
    lines(d, 660, ['그래서', '마음먹지 않아도', '곁에 있는 것,'], F(90, True), FG, 120)
    ct(d, 1010, '소리를 골랐어요.', F(90, True), GOLD)
    en(d, 1140, 'EN2_3')
    logo(d, 1240, 44); S.append(im)
    # 4 오행 다섯 소리
    im, d = new()
    lines(d, 110, ['오행마다', '다른 소리'], F(110, True), FG, 140)
    en(d, 392, 'EN2_4')
    gen = ['실내악', '재즈', '로파이', '피아노 독주', '앰비언트 피아노']
    gen_en = ['Wood · chamber music', 'Fire · jazz', 'Earth · lo-fi', 'Metal · solo piano', 'Water · ambient piano']
    for i, ((h, k, c), g) in enumerate(zip(OH, gen)):
        y = 470 + i * 140
        d.text((200, y), h, font=F(96, True), fill=c, stroke_width=3 if h == '水' else 0, stroke_fill=(255, 255, 255))
        d.text((340, y + 8), f'{k} · {g}', font=F(62), fill=SUB)
        d.text((342, y + 88), gen_en[i], font=ImageFont.truetype(CG, 36), fill=ENC)
    logo(d, 1230, 44); S.append(im)
    # 5 고요에서 할 수 있는 것
    im, d = new()
    ct(d, 140, '고요에서는', F(110, True), FG)
    items = [('매일 아침', '오늘의 타로'), ('사주 릴스', '신살과 귀인, 내 글자의 소리'), ('프로필 링크', '내 사주 오행과 일간 찾기')]
    for i, (a, b) in enumerate(items):
        y = 400 + i * 230
        ct(d, y, a, F(56), GOLD); ct(d, y + 80, b, F(70, True), FG); en(d, y + 165, ['EN2_5a', 'EN2_5b', 'EN2_5c'][i], 36)
    logo(d); S.append(im)
    # 6
    im, d = new()
    lines(d, 360, ['내 사주에', '필요한 소리는?'], F(120, True), FG, 160)
    lines(d, 740, ['프로필 링크에서', '내 오행부터 찾아보세요'], F(66), SUB, 96)
    en(d, 950, 'EN2_6', 46)
    logo(d, 1080, 64, (200, 190, 170)); S.append(im)
    for i, im in enumerate(S, 1): im.save(os.path.join(out, f'{i:02d}.jpg'), quality=93)
    return S


def sheet(S, path):
    c = Image.new('RGB', (6 * 270 + 50, 338), (255, 255, 255))
    for i, im in enumerate(S): c.paste(im.resize((270, 338)), (i * 280, 0))
    c.save(path)


if __name__ == '__main__':
    k = sys.argv[1]
    out = os.path.join(ROOT, 'posts', f'pin-{k}')
    S = {'find': find, 'intro': intro}[k](out)
    sheet(S, f'/tmp/pin_{k}.jpg')
