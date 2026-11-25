#!/usr/bin/env python3
"""오늘의 타로 릴스 (2026-11-21 미오 님: 캐러셀 06:00 + 릴스 06:20).
python3 tools/tarot/reel.py posts/<date>-tarot/tarot.json [ig|yt]  → 같은 폴더 reel.mp4(인스타) 또는 short_yt.mp4(유튜브), 1080x1920 약 18초
0초: 「오늘의 타로」+날짜+「오늘 고요를 찾으시는 분들을 위해 뽑은 세 장」+카드 뒷면 → 한 장씩 뒤집힘(자리·카드 이름)
→ 연결 장면 「세 장이 건네는 말」(tarot.json reel_line 두 줄, reel_line_en) → 끝: 피드 게시물·프로필 링크 안내.
음악: tarot.json music.title_html 의 천간 편. 음원은 저장소 shorts/무음편/<천간> 무음편.mp4 의 소리."""
import json, os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, '..', '..'))
sys.path.insert(0, os.path.join(root, 'tools'))
from tarot_reel import F  # 한글 명조

VARIANT = sys.argv[2] if len(sys.argv) > 2 else 'ig'
cfg_path = sys.argv[1]; d = os.path.dirname(cfg_path); cfg = json.load(open(cfg_path, encoding='utf-8'))
W, H, FPS = 1080, 1920, 30
BG = (10, 10, 12); GOLD = (201, 169, 106); FG = (250, 248, 242); SUB = (200, 195, 185)
EN = lambda s: ImageFont.truetype(os.path.join(root, 'tools', 'fonts', 'CormorantGaramond-500.ttf'), s)

MAJ_EN = ['The Fool','The Magician','The High Priestess','The Empress','The Emperor','The Hierophant','The Lovers','The Chariot','Strength','The Hermit','Wheel of Fortune','Justice','The Hanged Man','Death','Temperance','The Devil','The Tower','The Star','The Moon','The Sun','Judgement','The World']
SU_EN = {'wands': 'Wands', 'cups': 'Cups', 'swords': 'Swords', 'pents': 'Pentacles'}
RK_EN = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Page','Knight','Queen','King']
POS_EN = ["Today's flow", "What to keep", "What to let go"]
MON_EN = ['January','February','March','April','May','June','July','August','September','October','November','December']
def card_en(c):
    i = c['id']; n = MAJ_EN[int(i[1:])] if i.startswith('m') else f"{RK_EN[int(i[-2:]) - 1]} of {SU_EN[i[:-2]]}"
    return n + (' (reversed)' if c.get('rev') else '')

m = re.search(r'(\d{4})-(\d{2})-(\d{2})', os.path.abspath(d))
date_en = f"{MON_EN[int(m.group(2)) - 1]} {int(m.group(3))}" if m else ''
date_ko = cfg['label'].split('·')[0].strip()
stem = re.search(r'(갑목|을목|병화|정화|무토|기토|경금|신금|임수|계수)', cfg['music']['title_html']).group(1)
HZ = re.search(r'\((.{2})\)', cfg['music']['title_html']); HZ = HZ.group(1) if HZ else ''
STEM_EN = {'갑목': '甲木 Yang Wood (Gapmok)', '을목': '乙木 Yin Wood (Eulmok)', '병화': '丙火 Yang Fire (Byeonghwa)', '정화': '丁火 Yin Fire (Jeonghwa)',
           '무토': '戊土 Yang Earth (Muto)', '기토': '己土 Yin Earth (Gito)', '경금': '庚金 Yang Metal (Gyeonggeum)', '신금': '辛金 Yin Metal (Singeum)',
           '임수': '壬水 Yang Water (Imsu)', '계수': '癸水 Yin Water (Gyesu)'}

# 카드
CH = 570; CW = int(CH * 0.58); GAP = 24; X0 = (W - 3 * CW - 2 * GAP) // 2; CY = 570
faces = []
for c in cfg['cards']:
    im = Image.open(os.path.join(root, 'deck_1909', c['file'])).convert('RGB')
    if c.get('rev'): im = im.rotate(180)
    faces.append(im.resize((CW, CH), Image.LANCZOS))

# 2026-11-23 미오 님 결정: 11/21 유튜브 쇼츠가 악마 카드 그림으로 「과도한 노출」 삭제 → 이의신청 중.
# 유튜브판(yt)에서만 노출 그림 카드는 그림 대신 글(번호·이름·사유)로 뒤집힌다. 인스타판(ig)은 그림 그대로.
# 2026-11-26: 이의신청 인용 → 꺼 둠(NUDE_TEXT=False). 썸네일은 0초 장면(카드 뒷면)이라 그림이 들어가지 않음.
NUDE = {'m06', 'm15', 'm17', 'm19', 'm20', 'm21'}   # 연인·악마·별·태양·심판·세계
ROMAN = ['0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI']
def make_text_face(c):
    b = Image.new('RGB', (CW, CH), (24, 22, 30)); dr = ImageDraw.Draw(b)
    dr.rectangle([6, 6, CW - 7, CH - 7], outline=GOLD, width=3); dr.rectangle([18, 18, CW - 19, CH - 19], outline=(120, 100, 64), width=1)
    cx = CW // 2
    ctext(dr, 38, ROMAN[int(c['id'][1:])], EN(96), GOLD, cx)
    y = 168
    for ln in wrap(dr, c['title'], F(40, True), CW - 40): ctext(dr, y, ln, F(40, True), FG, cx); y += 52
    for ln in wrap(dr, card_en(c), EN(30), CW - 40): ctext(dr, y + 4, ln, EN(30), SUB, cx); y += 36
    y += 20; dr.line([(cx - 60, y), (cx + 60, y)], fill=(120, 100, 64), width=1); y += 20
    for ln in ['이 카드 그림은', '유튜브가 노출로 판단해', '지금 이의신청 중이에요.', '결과가 나올 때까지', '글로 보여 드려요.']:
        ctext(dr, y, ln, F(26), SUB, cx); y += 34
    y += 6
    for ln in ['Image under YouTube review,', 'shown as text for now.']:
        ctext(dr, y, ln, EN(24), SUB, cx); y += 26
    assert y < CH - 24, y
    return b
def make_back():
    b = Image.new('RGB', (CW, CH), (24, 22, 30)); dr = ImageDraw.Draw(b)
    dr.rectangle([6, 6, CW - 7, CH - 7], outline=GOLD, width=3); dr.rectangle([18, 18, CW - 19, CH - 19], outline=(120, 100, 64), width=1)
    gl = [Image.open(os.path.join(root, 'tools', 'assets', 'goyo_letters', f'{i}_{ch}.png')).convert('RGBA') for i, ch in enumerate('GOYO')]
    gh = 34; gl = [g.resize((max(1, int(g.width * gh / g.height)), gh), Image.LANCZOS) for g in gl]
    tw = sum(g.width for g in gl) + 12 * 3; x = (CW - tw) // 2; bb = b.convert('RGBA')
    for g in gl: bb.alpha_composite(g, (x, CH // 2 - gh // 2)); x += g.width + 12
    return bb.convert('RGB')
BACK = make_back()

T0, STEP, FLIP = 1.2, 2.0, 0.5          # 첫 카드 뒤집기 시작, 간격, 뒤집는 시간
FLIPS = [T0 + i * STEP for i in range(3)]
END = FLIPS[-1] + FLIP + 1.8             # 끝 장면 시작
BRIDGE = 6.0                             # 연결 장면: 채널 소개 두 장면(각 3초)
CTA = END + BRIDGE
TOT = CTA + 6.5                          # 끝 장면 약 6초 머묾(11/21 미오 님: 너무 짧음)

def ctext(dr, y, t, f, fill, cx=W // 2, stroke=0):
    w = dr.textlength(t, font=f); dr.text((cx - w / 2, y), t, font=f, fill=fill, stroke_width=stroke, stroke_fill=(0, 0, 0))

def wrap(dr, t, f, maxw):
    if dr.textlength(t, font=f) <= maxw: return [t]
    if ', ' in t:
        a, b = t.split(', ', 1); return [a + ',', b]
    ws = t.split(' '); best = None
    for k in range(1, len(ws)):
        l1, l2 = ' '.join(ws[:k]), ' '.join(ws[k:]); s = max(dr.textlength(l1, font=f), dr.textlength(l2, font=f))
        if best is None or s < best[0]: best = (s, [l1, l2])
    return best[1] if best else [t]

NUDE_TEXT = False   # 11/26 이의신청 인용(콘텐츠 복구) → 권미오님 결정으로 그림으로 되돌림. 다시 필요하면 True.
if VARIANT == 'yt' and NUDE_TEXT:
    faces = [make_text_face(c) if c['id'] in NUDE else f for c, f in zip(cfg['cards'], faces)]

def frame(t):
    im = Image.new('RGB', (W, H), BG); dr = ImageDraw.Draw(im)
    endk = max(0.0, min(1.0, (t - END) / 0.6))
    ctext(dr, 230, '오늘의 타로', F(124, True), FG)
    ctext(dr, 392, date_ko, F(52), GOLD)
    ctext(dr, 470, '오늘 고요를 찾으시는 분들을 위해 뽑은 세 장', F(42), FG)
    for i, c in enumerate(cfg['cards']):
        x = X0 + i * (CW + GAP); p = (t - FLIPS[i]) / FLIP
        if p <= 0: img, sx = BACK, 1.0
        elif p >= 1: img, sx = faces[i], 1.0
        elif p < 0.5: img, sx = BACK, 1 - p * 2
        else: img, sx = faces[i], (p - 0.5) * 2
        w = max(1, int(CW * sx)); im.paste(img.resize((w, CH)), (x + (CW - w) // 2, CY))
        a = max(0.0, min(1.0, (t - FLIPS[i] - FLIP) / 0.4))
        if a > 0:
            L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(L); cx = x + CW // 2
            ctext(ld, CY + CH + 24, cfg['positions'][i], F(40, True), GOLD + (255,), cx)
            title = c['title']; lines = wrap(ld, title, F(38), CW + GAP - 6); y = CY + CH + 82
            for ln in lines: ctext(ld, y, ln, F(38), FG + (255,), cx); y += 48
            for ln in wrap(ld, card_en(c), EN(32), CW + GAP - 6): ctext(ld, y + 4, ln, EN(32), SUB + (255,), cx); y += 36
            L.putalpha(L.getchannel('A').point(lambda v: int(v * a * (1 - endk))))
            im.paste(L, (0, 0), L)
    if endk > 0:
        ov = Image.new('RGBA', (W, H), BG + (int(248 * endk),)); im.paste(ov, (0, 0), ov); dr = ImageDraw.Draw(im)
        INTRO = [(['고요는 매일 아침', '이렇게 세 장을 뽑아', '풀어드려요'],
                  ['Every morning, GOYO draws three cards like these', 'and reads them for you.']),
                 (['무료 사주 앱에서 내 오행을 찾고', '그 오행의 음악을 들을 수 있어요'],
                  ['Find your element in our free saju app', 'and listen to its music.'])]
        for i, (ko_l, en_l) in enumerate(INTRO):
            s0 = END + i * BRIDGE / 2; s1 = s0 + BRIDGE / 2
            bk = max(0.0, min(1.0, (t - s0 - 0.15) / 0.45)) * (1 - max(0.0, min(1.0, (t - s1 + 0.35) / 0.35)))
            if bk <= 0: continue
            B = Image.new('RGBA', (W, H), (0, 0, 0, 0)); bd = ImageDraw.Draw(B)
            y = 760 - 43 * (len(ko_l) - 2)
            for ln in ko_l: ctext(bd, y, ln, F(64, True), FG + (255,)); y += 92
            y += 34
            for ln in en_l: ctext(bd, y, ln, EN(40), SUB + (255,)); y += 50
            B.putalpha(B.getchannel('A').point(lambda v: int(v * bk))); im.paste(B, (0, 0), B)
        ck = max(0.0, min(1.0, (t - CTA) / 0.5))
        if ck <= 0: return im
        L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(L)
        if VARIANT == 'yt':
            ctext(ld, 680, '내 오행과 오행음악은', F(72, True), FG + (255,)); ctext(ld, 775, '@goyo_mio 채널에서', F(72, True), FG + (255,))
            ctext(ld, 920, '무료 사주 앱 goyomio.com', F(52, True), GOLD + (255,))
            ctext(ld, 1010, '오늘 세 장의 풀이는 인스타 @goyo_mio', F(42), SUB + (255,))
            ctext(ld, 1120, 'Your element and its music: @goyo_mio channel', EN(38), SUB + (255,))
            ctext(ld, 1168, 'Free saju app: goyomio.com', EN(38), SUB + (255,))
            ctext(ld, 1216, "Today's reading: Instagram @goyo_mio", EN(38), SUB + (255,))
        else:
            ctext(ld, 720, '오늘 세 장의 풀이는', F(72, True), FG + (255,)); ctext(ld, 815, '피드 게시물에서', F(72, True), FG + (255,))
            ctext(ld, 975, '앱과 음악은 프로필 링크에서', F(44), SUB + (255,))
            ctext(ld, 1035, 'goyomio.com', EN(40), GOLD + (255,))
            ctext(ld, 1140, "Today's reading is in our feed post.", EN(38), SUB + (255,))
            ctext(ld, 1188, 'App and music: link in bio', EN(38), SUB + (255,))
        L.putalpha(L.getchannel('A').point(lambda v: int(v * ck))); im.paste(L, (0, 0), L)
    return im

def main():
    audio = os.path.join(root, 'shorts', '무음편', f'{stem} 무음편.mp4')
    out = os.path.join(d, 'reel.mp4' if VARIANT == 'ig' else 'short_yt.mp4')
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                           '-i', audio, '-filter_complex', f"[1:a]atrim=0:{TOT},asetpts=PTS-STARTPTS,afade=t=in:d=0.6,afade=t=out:st={TOT - 1.5}:d=1.5[a]",
                           '-map', '0:v', '-map', '[a]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p',
                           '-c:a', 'aac', '-b:a', '192k', '-t', str(TOT), '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    for k in range(int(TOT * FPS)):
        ff.stdin.write(frame(k / FPS).tobytes())
    ff.stdin.close(); ff.wait()
    if VARIANT == 'ig': frame(0).save(os.path.join(d, 'reel_first.jpg'), quality=88)
    print('ok', out, round(TOT, 1))

if __name__ == '__main__':
    main()
