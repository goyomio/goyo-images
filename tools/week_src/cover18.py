#!/usr/bin/env python3
"""저녁 6시 캐러셀 첫 장 다시 만들기 (2026-11-18 새 디자인 규칙).
검은 바탕 · 큰 흰 제목 · GOYO 로고(Cormorant) · 색 하나.
python3 tools/week_src/cover18.py [날짜 ...]   (없으면 전부)
원래 첫 장은 01_old.jpg 로 남긴다. 그림 읽기는 원래 첫 장에서 그림과 출처 줄을 잘라 쓴다."""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from tarot_reel import F
from PIL import Image, ImageDraw, ImageFont
import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
W, H = 1080, 1350
BG = (10, 10, 12); FG = (250, 248, 242); SUB = (205, 200, 190); DIMC = (150, 145, 135)
GOLD = (201, 169, 106); MOK = (47, 217, 107); HWA = (255, 70, 55); TO = (255, 194, 26); GEUM = (235, 235, 240); SU = (0, 0, 0)  # 수는 흑색, 얇은 흰 테두리 (미오 님 11/18)
CG = os.path.join(ROOT, 'tools', 'fonts', 'CormorantGaramond-500.ttf')
FIVE = [('화', HWA), ('·', FG), ('수', SU), ('·', FG), ('목', MOK), ('·', FG), ('금', GEUM), ('·', FG), ('토', TO)]

S = {
 '2026-11-18': dict(label='고요 이야기', title=['고요는', '이렇게', '만들어요'], sub='같은 곡이 되풀이되지 않게', acc=GOLD),
 '2026-11-19': dict(label='고요의 그림 읽기 #1', title=['빈 방의 햇빛'], sub='빌헬름 함메르쇠이', acc=GOLD, paint=True),
 '2026-11-20': dict(label='몰랐던 오행 이야기', title=[FIVE, '요일 이름이', '오행이에요'], sub='화요일부터 토요일까지', acc=None),
 '2026-11-22': dict(label='11월 22일 · 이번 주 기운', title=['소설', '小雪'], sub='첫눈이 온다는 날', acc=SU),
 '2026-11-23': dict(label='11월 23일 · 음력 10월 15일', title=['상달의', '보름'], sub='하원(下元)이에요', acc=SU),
 '2026-11-25': dict(label='고요 이야기', title=['고요라는', '이름에 숨긴', '네 단어'], sub='처음 꺼내는 이야기', acc=GOLD),
 '2026-11-26': dict(label='고요의 그림 읽기 #2', title=['세한도'], sub='김정희', acc=GOLD, paint=True),
 '2026-11-27': dict(label='사주 · 오행 정보', title=['겨울인데', '왜 하늘에', '흙이 있을까요?'], sub='이번 달은 기해월(己亥月)', acc=TO),
 '2026-11-29': dict(label='고요 이야기', title=['해가 가장', '일찍 지는 날은', '동지가 아니에요'], sub='등불을 켜는 계절', acc=HWA),
 '2026-11-30': dict(label='11월 30일 · 음력 10월 22일', title=['12월인데', '사주로는', '아직 10월'], sub='이번 주 기운', acc=SU),
 '2026-12-02': dict(label='고요 이야기', title=['곡 이름만 봐도', '천간이 보여요'], sub='고요의 곡 이름 이야기', acc=GOLD),
 '2026-12-03': dict(label='고요의 그림 읽기 #3', title=['인왕제색도'], sub='정선', acc=GOLD, paint=True),
 '2026-12-04': dict(label='사주 · 오행 정보', title=['자정과 정오', '"정"은', '무슨 뜻일까요?'], sub='하루를 열둘로 나누던 시간', acc=GOLD),
 '2026-12-06': dict(label='고요 이야기', title=['고요,', '어느 편부터', '들으면 될까요?'], sub='처음 오셨다면', acc=GOLD),
 '2026-12-07': dict(label='12월 7일 · 대설', title=['오늘부터', '사주는', '자월(子月)'], sub='이번 주 기운', acc=SU),
 '2026-12-09': dict(label='고요의 그림 읽기 · 특별판', title=['수련'], sub='클로드 모네', acc=GOLD, paint=True),
 '2026-12-10': dict(label='고요의 그림 읽기 #4', title=['막달라 마리아'], sub='조르주 드 라 투르', acc=GOLD, paint=True),
 '2026-12-11': dict(label='사주 · 오행 정보', title=['사주 앱마다', '결과가', '다른 이유'], sub='세 가지만 확인하세요', acc=GOLD),
 '2026-12-13': dict(label='고요 이야기', title=['무지개가', '일곱 색인 건', '음계 때문'], sub='프리즘 이야기', acc=GOLD),
 '2026-12-14': dict(label='12월 14일 · 이번 주 기운', title=['동짓달', '기나긴 밤'], sub='음력 11월 6일', acc=SU),
 '2026-12-16': dict(label='고요 이야기', title=['다섯 가지 고요', '다섯 개의 시간'], sub='썸네일에 담긴 것', acc=None, five_bar=True),
 '2026-12-17': dict(label='고요의 그림 읽기 #5', title=['만종'], sub='장프랑수아 밀레', acc=GOLD, paint=True),
 '2026-12-18': dict(label='사주 · 오행 정보', title=['환갑은 왜', '61살일까요?'], sub='60갑자 이야기', acc=GOLD),
 '2026-12-20': dict(label='토(土)의 장르 이야기', title=['로파이는', '원래', '"저음질"'], sub='lo-fi, low fidelity', acc=TO),
 '2026-12-21': dict(label='12월 21일 · 이번 주 기운', title=['내일은', '동지'], sub='음력 11월 13일', acc=SU),
 '2026-12-23': dict(label='고요 이야기', title=['운은', '바꾸는 게 아니라', '여는 거예요'], sub='개운(開運) 이야기', acc=GOLD),
 '2026-12-24': dict(label='고요의 그림 읽기 #6', title=['간바라 밤눈'], sub='우타가와 히로시게', acc=GOLD, paint=True),
 '2026-12-25': dict(label='사주 · 오행 정보', title=['태어난 시간을', '모르면', '사주를 못 볼까요?'], sub='여섯 글자로도 볼 수 있어요', acc=GOLD),
 '2026-12-27': dict(label='사주 · 오행 정보', title=['제야의 종은', '왜 33번', '칠까요?'], sub='한 해의 마지막 밤', acc=GOLD),
 '2026-12-30': dict(label='고요 이야기', title=['고요,', '한 장의', '지도'], sub='올해의 마지막 이야기', acc=None, five_bar=True),
 '2026-12-31': dict(label='12월 31일 · 한 해의 끝에서', title=['2027년은', '정미년'], sub='정(丁)은 등불, 미(未)는 흙', acc=HWA),  # 11/21 12/28에서 옮김
 '보류-까치': dict(label='고요의 그림 읽기', title=['까치'], sub='클로드 모네', acc=GOLD, paint=True),  # 11/21 보류, 다시 풀 때 번호·날짜 새로
}

PAINT = {'2026-12-09': ('wl_full.jpg', ['클로드 모네, 〈수련(Water Lilies)〉 1906', '시카고 미술관 · 퍼블릭 도메인(CC0)']), '2026-11-19': (None, ['빌헬름 함메르쇠이, 〈스트란가데의 실내, 바닥의 햇빛〉', '1901 · 덴마크 국립미술관(SMK)']), '2026-11-26': ('se_paint.jpg', ['김정희, 〈세한도(歲寒圖)〉 1844 · 국보', '국립중앙박물관 · 이미지 위키미디어 공용(퍼블릭 도메인)']), '2026-12-03': ('inwang_full.jpg', ['정선, 〈인왕제색도(仁王霽色圖)〉 1751 · 국보', '국립중앙박물관 · 이미지 위키미디어 공용(퍼블릭 도메인)']), '2026-12-10': ('latour_full.jpg', ['조르주 드 라 투르, 〈연기 나는 불꽃 앞의 막달라 마리아〉', '1635~1637년 무렵 · LACMA · 위키미디어 공용(퍼블릭 도메인)']), '2026-12-17': ('millet_full.jpg', ["장프랑수아 밀레, 〈만종(L'Angélus)〉 1857~1859", '오르세 미술관 · 이미지 위키미디어 공용(퍼블릭 도메인)']), '2026-12-24': ('hiro_full.jpg', ['우타가와 히로시게, 〈간바라 밤눈〉 「도카이도 53역참」 중, 1833~1834', '메트로폴리탄 미술관 · 이미지 위키미디어 공용(퍼블릭 도메인)']), '보류-까치': ('monet_full.jpg', ['클로드 모네, 〈까치(La Pie)〉 1868~1869', '오르세 미술관 · 이미지 위키미디어 공용(퍼블릭 도메인)'])}

EN = {'2026-11-18': 'How Goyo makes its music', '2026-11-19': 'Interior in Strandgade, Sunlight on the Floor', '2026-11-20': 'In Korean, five weekdays are named for the elements', '2026-11-22': 'Light Snow (小雪): when first snow is said to fall', '2026-11-23': 'The full moon of the tenth lunar month', '2026-11-25': 'Four words hidden in the name Goyo', '2026-11-26': 'Sehando (Winter Scene) · Kim Jeong-hui', '2026-11-27': 'Why is there Earth in a winter sky?', '2026-11-29': "The earliest sunset isn't on the winter solstice", '2026-11-30': "December, yet in Saju it's still the tenth month", '2026-12-02': 'Each Goyo track title names its heavenly stem', '2026-12-03': 'Clearing After Rain on Mount Inwang · Jeong Seon', '2026-12-04': "What 'jeong' means in Korean midnight and noon", '2026-12-06': 'New to Goyo? Where to start listening', '2026-12-07': 'Today Saju enters the Midwinter Water month (子)', '2026-12-09': 'Water Lilies · Claude Monet', '2026-12-10': 'Magdalene with the Smoking Flame · Georges de La Tour', '2026-12-11': 'Why Saju apps give different results', '2026-12-13': 'Why the rainbow has seven colors: the musical scale', '2026-12-14': 'The long nights of the eleventh lunar month', '2026-12-16': 'Five Goyo playlists, five times of day', '2026-12-17': 'The Angelus · Jean-François Millet', '2026-12-18': "Why Korea's 60th birthday falls at 61", '2026-12-20': 'Lo-fi first meant low fidelity', '2026-12-21': 'Tomorrow is the winter solstice', '2026-12-23': 'Gaeun (開運) means opening, not changing', '2026-12-24': 'Kambara: Night Snow · Utagawa Hiroshige', '2026-12-25': 'No birth time? You can still read your Saju', '2026-12-27': "Why does Korea's New Year bell ring 33 times?", '2026-12-30': 'Goyo on one map: our last story of the year', '2026-12-31': '2027 is the 丁未 year: lamp and earth', '보류-까치': 'The Magpie · Claude Monet', '2026-11-21': "Saju's new year starts in early February", '2026-11-24': 'Of your eight characters, one is you', '2026-11-28': 'Lots of Fire in your chart?', '2026-12-01': 'Lots of Metal in your chart?', '2026-12-05': 'Morning person or night owl?', '2026-12-08': "What's your favorite color?", '2026-12-12': 'Lots of Wood in your chart?', '2026-12-15': 'Lots of Earth in your chart?', '2026-12-19': 'Gaeun (開運) means opening, not waiting', '2026-12-22': 'Yang Wood and Yin Wood: the same tree?', '2026-12-26': 'Do you play just any music when you study?', '2026-12-29': "What's your favorite day of the week?"}


def ct(d, y, t, f, fill):
    w = d.textlength(t, font=f)
    if fill == SU: d.text(((W - w) / 2, y), t, font=f, fill=SU, stroke_width=max(1, f.size // 40), stroke_fill=(255, 255, 255))
    else: d.text(((W - w) / 2, y), t, font=f, fill=fill)


def ct_en(d, y, t, size, fill):
    """영어 줄: 라틴 글자는 Cormorant, 한자는 본문 글꼴로 섞어 그림(한자 네모 깨짐 방지)."""
    fe = ImageFont.truetype(CG, size); fk = F(int(size * 0.86))
    segs = []
    for ch in t:
        k = ord(ch) >= 0x2E80
        if segs and segs[-1][0] == k: segs[-1][1] += ch
        else: segs.append([k, ch])
    w = sum(d.textlength(s_, font=fk if k else fe) for k, s_ in segs); x = (W - w) / 2
    for k, s_ in segs:
        d.text((x, y + (int(size * 0.12) if k else 0)), s_, font=fk if k else fe, fill=fill); x += d.textlength(s_, font=fk if k else fe)


def logo(d, y=1230, size=56, fill=DIMC, im=None):
    """GOYO 워드마크: tools/assets/goyo_letters 글자 그림만 씀(글꼴로 치지 않음, 미오 님 11/21 규칙)."""
    if im is None: raise ValueError('logo needs im')
    gh = int(size * 0.82)
    gl = [Image.open(os.path.join(ROOT, 'tools', 'assets', 'goyo_letters', f'{i}_{c}.png')).convert('RGBA') for i, c in enumerate('GOYO')]
    gl = [g.resize((max(1, int(g.width * gh / g.height)), gh), Image.LANCZOS) for g in gl]
    a = int(255 * 0.62)  # 예전 회색(DIMC) 느낌으로 살짝 낮춤
    gl = [Image.merge('RGBA', (*g.split()[:3], g.split()[3].point(lambda v: v * a // 255))) for g in gl]
    sp = int(size * 0.42); x = (W - sum(g.width for g in gl) - sp * 3) // 2
    for g in gl: im.paste(g, (x, y + 8), g); x += g.width + sp


def fit(d, t, size, maxw):
    while True:
        f = F(size, True)
        w = sum(d.textlength(s, font=f) for s, _ in t) if isinstance(t, list) else d.textlength(t, font=f)
        if w <= maxw or size <= 60: return f, size, w
        size -= 4


def crop_painting(old):
    a = np.asarray(old.convert('L')).astype(int)
    rows = (a > 35).sum(1); runs = []; s = None
    for y, v in enumerate(rows):
        if v > W * 0.25 and s is None: s = y
        if v <= W * 0.25 and s is not None: runs.append((s, y)); s = None
    if s is not None: runs.append((s, len(rows)))
    y0, y1 = max(runs, key=lambda r: r[1] - r[0])
    cols = (a[y0:y1] > 35).sum(0); xs = np.where(cols > (y1 - y0) * 0.5)[0]
    pic = old.crop((int(xs.min()), y0, int(xs.max()) + 1, y1))
    # 출처 줄: 그림 바로 아래 왼쪽 글자
    cy0 = y1 + 8; cy1 = cy0; blank = 0
    for y in range(cy0, min(cy0 + 140, H)):
        if (a[y, 90:620] > 70).any(): cy1 = y; blank = 0
        else:
            blank += 1
            if blank > 30 and cy1 > cy0: break
    credit = old.crop((90, cy0, 620, cy1 + 6)) if cy1 > cy0 else None
    return pic, credit


def make(date):
    sp = S[date]; pdir = os.path.join(ROOT, 'posts', date)
    post = json.load(open(os.path.join(pdir, 'post.json')))
    first = os.path.join(ROOT, post['files'][0]); old_p = os.path.join(pdir, '01_old.jpg')
    if not os.path.exists(old_p): Image.open(first).convert('RGB').save(old_p, quality=95)
    old = Image.open(old_p).convert('RGB')
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    acc = sp['acc'] or GOLD
    paint = sp.get('paint')
    # 라벨 + 제목: 모든 줄을 같은 크기로, 화면 가운데에
    fl = F(42, True)
    base = 150 if paint else (180 if len(sp['title']) <= 2 else 160)
    z = min(fit(d, t, base, W - 130)[1] for t in sp['title']); f = F(z, True)
    block = 90 + len(sp['title']) * int(z * 1.18) + (84 if sp.get('five_bar') else 0) + 34 + 70
    y = 150 if paint else max(170, (1180 - block) // 2)
    ct(d, y, sp['label'], fl, acc); y += 90
    for t in sp['title']:
        if isinstance(t, list):
            w = sum(d.textlength(s_, font=f) for s_, _ in t); x = (W - w) / 2
            for s_, c in t:
                d.text((x, y), s_, font=f, fill=c, **({'stroke_width': max(2, f.size // 40), 'stroke_fill': (255, 255, 255)} if c == SU else {})); x += d.textlength(s_, font=f)
        else:
            ct(d, y, t, f, FG)
        y += int(z * 1.18)
    if sp.get('five_bar'):
        y += 24; bw = 120; x0 = (W - bw * 5 - 20 * 4) / 2
        for i, c in enumerate([MOK, HWA, TO, GEUM, SU]):
            d.rounded_rectangle([x0 + i * (bw + 20), y + 20, x0 + i * (bw + 20) + bw, y + 34], 7, fill=c, outline=(255, 255, 255) if c == SU else None, width=2)
        y += 60
    y += 34
    ct(d, y, sp['sub'], F(54), SUB); y += 90
    if EN.get(date):
        ct_en(d, y - 14, EN[date], 44, DIMC); y += 52
    if paint:
        src, cred = PAINT[date]
        pic = Image.open(os.path.join(ROOT, 'tools', 'week_src', src)).convert('RGB') if src else crop_painting(old)[0]
        top, bot = y + 10, 1085
        sc = min((W - 160) / pic.width, (bot - top) / pic.height)
        pw, ph = int(pic.width * sc), int(pic.height * sc)
        pic = pic.resize((pw, ph), Image.LANCZOS); px = (W - pw) // 2
        im.paste(pic, (px, top)); cy = top + ph + 16
        for ln in cred:
            fc = F(26)
            while d.textlength(ln, font=fc) > W - 120: fc = F(fc.size - 1)
            ct(d, cy, ln, fc, DIMC); cy += 36
    logo(d, im=im)
    im.save(first, quality=93)
    return first

# 저녁 6시 릴스: 영상은 그대로 두고 피드 표지(cover_url)만 새 규칙으로
RS = {
 '2026-11-21': dict(label='사주 · 오행 정보', title=['몇 월에', '태어나셨어요?'], sub='사주의 새해는 입춘부터', acc=None, five_bar=True),
 '2026-11-24': dict(label='사주 · 오행 정보', title=['여덟 글자 중', '"나"는', '한 글자'], sub='일간 이야기', acc=GOLD),
 '2026-11-28': dict(label='사주 · 오행 정보', title=['사주에', '화가 많다면?'], sub='화(火) 많은 사주', acc=HWA),
 '2026-12-01': dict(label='사주 · 오행 정보', title=['사주에', '금이 많다면?'], sub='금(金) 많은 사주', acc=GEUM),
 '2026-12-05': dict(label='사주 · 오행 정보', title=['아침형이에요,', '저녁형이에요?'], sub='하루의 오행', acc=GOLD),
 '2026-12-08': dict(label='사주 · 오행 정보', title=['좋아하는 색,', '바로 떠오르죠?'], sub='색의 오행', acc=None, five_bar=True),
 '2026-12-12': dict(label='사주 · 오행 정보', title=['사주에', '목이 많다면?'], sub='목(木) 많은 사주', acc=MOK),
 '2026-12-15': dict(label='사주 · 오행 정보', title=['사주에', '토가 많다면?'], sub='토(土) 많은 사주', acc=TO),
 '2026-12-19': dict(label='고요 이야기', title=['운은', '기다리는 게 아니라', '여는 거예요'], sub='개운(開運)', acc=GOLD),
 '2026-12-22': dict(label='사주 · 오행 정보', title=['갑목과 을목,', '같은 나무일까요?'], sub='갑(甲) · 을(乙)', acc=MOK),
 '2026-12-26': dict(label='고요 이야기', title=['공부할 때,', '아무 음악이나', '틀어요?'], sub='내 사주로 고르는 소리', acc=GOLD),
 '2026-12-29': dict(label='사주 · 오행 정보', title=['제일 좋아하는', '요일, 뭐예요?'], sub='요일의 오행', acc=None, five_bar=True),
}


def reel_cover(date):
    sp = RS[date]; pdir = os.path.join(ROOT, 'posts', date)
    im = Image.new('RGB', (W, 1920), BG); d = ImageDraw.Draw(im)
    acc = sp['acc'] or GOLD
    z = min(fit(d, t, 170, W - 130)[1] for t in sp['title']); f = F(z, True)
    block = 90 + len(sp['title']) * int(z * 1.18) + (84 if sp.get('five_bar') else 0) + 34 + 70
    y = 285 + max(120, (1180 - block) // 2)
    ct(d, y, sp['label'], F(42, True), acc); y += 90
    for t in sp['title']:
        ct(d, y, t, f, FG); y += int(z * 1.18)
    if sp.get('five_bar'):
        y += 24; bw = 120; x0 = (W - bw * 5 - 20 * 4) / 2
        for i, c in enumerate([MOK, HWA, TO, GEUM, SU]):
            d.rounded_rectangle([x0 + i * (bw + 20), y + 20, x0 + i * (bw + 20) + bw, y + 34], 7, fill=c, outline=(255, 255, 255) if c == SU else None, width=2)
        y += 60
    y += 34; ct(d, y, sp['sub'], F(54), SUB)
    if EN.get(date): ct_en(d, y + 80, EN[date], 46, DIMC)
    logo(d, 285 + 1230, im=im)
    out = os.path.join(pdir, 'cover.jpg'); im.save(out, quality=93)
    pj = os.path.join(pdir, 'post.json'); post = json.load(open(pj))
    post['cover_file'] = os.path.relpath(out, ROOT)
    json.dump(post, open(pj, 'w'), ensure_ascii=False, indent=1)
    return out


if __name__ == '__main__':
    ds = sys.argv[1:] or sorted(list(S) + list(RS))
    for dt in ds:
        print(make(dt) if dt in S else reel_cover(dt))
