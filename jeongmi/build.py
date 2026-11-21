"""정미년 시리즈(1/1~2/7) 인스타 창 캐러셀·릴스 설정 만들기.
python3 jeongmi/build.py 0101  → jeongmi/0101/slides.json, reel.json, caption.txt
렌더: tools/week_src/example_saju.py (캐러셀), tools/week_src/example_reel.py (릴스 ig/yt)
원문: 사주 창 「2027 정미년 해석 + 함께할 것들」 인계(11/21) + 미오 님 결정 17건."""
import json, os, sys
FG = [236, 233, 226]; GOLD = [200, 180, 140]; EN = [214, 210, 202]
def T(t, sz, col=FG, bold=False, gap=24): return [t, sz, col, bold, gap]
def IL(name, body, gap): return [T(name, 34, GOLD, True, 0), T(body, 31, gap=12 if gap else 0)]
def S(items, tag=None, **kw):
    d = {'items': items}
    if tag: d['tag'] = tag
    d.update(kw); return d
P = {}

# ───────── 1/1 금 · 해석 본편 「큰 해 다음엔 가까운 등불」 (정화)
P['0101'] = dict(
 music='정화', audio='shorts/그림편/audio/정화_Lamplit Keys_60s.m4a',
 slides=[
  S([T('1월 1일 · 새해 첫날', 44, GOLD, gap=30), T('큰 해 다음엔\n가까운 등불', 104, bold=True, gap=36),
     T('2027년, 정미(丁未)', 48, gap=14), T('사주의 해는 입춘(2월 4일)에 바뀌어요.', 38, gap=30),
     T('After the big sun, a lamp close by', 38, EN, gap=4), T("In Saju, the year turns at\nthe start of spring (立春): Feb 4.", 32, EN, gap=0)]),
  S([T('큰 불이\n등불이 되어\n흙에 내려앉는 해예요.', 76, bold=True, gap=40),
     T('A great fire becomes a lamp\nand settles onto the earth.', 36, EN, gap=0)], tag='2027년을 한 문장으로'),
  S([T('2026년 병화는\n하늘의 해예요.', 58, gap=30), T('2027년 정화는\n가까운 곳을 오래 비추는 등불이에요.', 58, bold=True, gap=30),
     T('넓게 퍼지던 빛이\n가까운 자리를 오래 밝히는\n빛으로 옮겨 가요.', 44, gap=36),
     T('2026 was the sun in the sky. 2027 is a lamp that keeps lighting what is close.', 34, EN, gap=0)], tag='큰 불에서 등불로'),
  S([T('2025 을사 · 초여름\n2026 병오 · 한여름\n2027 정미 · 늦여름', 56, gap=36), T('세 해 이어진 여름이\n정미년에 다 익어요.', 60, bold=True, gap=24),
     T('불이 꺼지는 해라기보다\n불이 무르익는 해로 읽어요.', 44, gap=36),
     T('2025 early, 2026 high, 2027 late summer: summer ripens fully in 2027.', 34, EN, gap=0)], tag='세 해의 여름'),
  S([T('미(未)는 늦여름의 마른 흙,\n나무를 품어 두는\n창고 같은 흙이에요.', 54, gap=34), T('그동안 키운 것을\n조용히 넣어 두는 해예요.', 62, bold=True, gap=36),
     T('未 Afternoon Earth (Mito) is dry late-summer earth that stores what has grown. A year to keep what you raised.', 34, EN, gap=0)], tag='넣어 두는 흙'),
  S([
     *IL('갑목', '생각을 말과 손으로 꺼내, 눈에 보이는\n성과로 바꿔 가는 해로 읽을 수 있어요.', 20),
     *IL('을목', '좋아하는 것을 즐기다 보면,\n그것이 움직이는 기회로 이어질 수 있어요.', 20),
     *IL('병화', '곁의 사람과 몫을 나눌 일이 늘고,\n내 재주를 드러낼 기회도 생길 수 있어요.', 20),
     *IL('정화', '나와 닮은 불이 하나 더 켜지는 해여서, 내 색을\n또렷하게 표현하기 좋은 해로 읽을 수 있어요.', 20),
     *IL('무토', '따뜻하게 돌봐 주는 손길이 닿고,\n내 힘도 단단해지는 해로 읽을 수 있어요.', 0)], tag='내 일간으로 읽은 2027년 ①'),
  S([*IL('기토', '혼자 깊이 파고드는 공부와 직관이\n살아나는 해로 읽을 수 있어요.', 20),
     *IL('경금', '맡은 일을 단정하게 정돈하고,\n배움으로 안을 채워 가는 해로 읽을 수 있어요.', 20),
     *IL('신금', '조금 버거운 일이 오히려\n나를 단단하게 다듬는 해가 될 수 있어요.', 20),
     *IL('임수', '성실하게 들여 온 노력이 손에 잡히는\n모습으로 돌아오는 해로 읽을 수 있어요.', 20),
     *IL('계수', '바깥 기회는 넓어지지만,\n내 속도를 지키는 게 중요한 해로 읽을 수 있어요.', 34),
     T('내 일간은 프로필 링크의\n무료 앱에서 찾을 수 있어요.', 42, GOLD, gap=0)], tag='내 일간으로 읽은 2027년 ②'),
  S([T('다섯 가지 고요', 56, bold=True, gap=10), T('정화 편', 96, bold=True, gap=34),
     T('2027년의 글자 그대로,\n가까운 곳을 오래 비추는\n등불 같은 소리예요.', 50, gap=24), T('첫 곡은 『Lamplit Keys』예요.', 44, gap=30),
     T('음악은 프로필 링크에서', 46, GOLD, gap=30),
     T('Five Kinds of Quiet · 丁火 Yin Fire (Jeonghwa). The first track is Lamplit Keys. Music: link in bio', 32, EN, gap=0)], tag='틀어 두기 좋은 소리'),
 ],
 reel=[
  dict(sec=4.5, instant=True, items=[T('1월 1일', 50, GOLD, gap=34), T('큰 해 다음엔\n가까운 등불', 124, bold=True, gap=50), T('After the big sun, a lamp close by', 42, EN, gap=0)]),
  dict(sec=6.5, tag='2027년을 한 문장으로', step=1.0, items=[T('큰 불이\n등불이 되어\n흙에 내려앉는 해예요.', 86, bold=True, gap=50),
       T('A great fire becomes a lamp\nand settles onto the earth.', 40, EN, gap=0)]),
  dict(sec=6.0, step=1.0, items=[T('2026년은\n하늘의 해', 90, bold=True, gap=40), T('2027년은\n가까이 오래 비추는\n등불', 76, bold=True, gap=50),
       T('2026: the sun. 2027: a lamp.', 40, EN, gap=0)]),
  dict(sec=5.0, step=0.9,
       items_ig=[T('내 일간으로 읽으면\n어떤 해일까요?', 92, bold=True, gap=34), T('풀이는 @goyo_mio\n피드 게시물에서', 60, bold=True, gap=30),
                 T('What does 2027 mean for your day master?\nFull reading on our profile', 40, EN, gap=0)],
       items_yt=[T('내 일간으로 읽으면\n어떤 해일까요?', 92, bold=True, gap=34), T('풀이는\n채널 게시물에서', 60, bold=True, gap=30),
                 T('What does 2027 mean for your day master?\nFull reading in our Posts tab', 40, EN, gap=0)]),
  dict(sec=7.5, tag='지금 흐르는 소리',
       items_ig=[T('다섯 가지 고요', 60, bold=True, gap=10), T('정화 편', 100, bold=True, gap=36), T('첫 곡 『Lamplit Keys』', 56, gap=26),
                 T('음악은 프로필 링크에서', 48, GOLD, gap=30), T('Five Kinds of Quiet · 丁火 Yin Fire (Jeonghwa): Lamplit Keys\nMusic: link in bio', 36, EN, gap=0)],
       items_yt=[T('다섯 가지 고요', 60, bold=True, gap=10), T('정화 편', 100, bold=True, gap=36), T('첫 곡 『Lamplit Keys』', 56, gap=26),
                 T('음악은 아래 관련 영상', 48, GOLD, gap=30), T('Five Kinds of Quiet · 丁火 Yin Fire (Jeonghwa): Lamplit Keys\nMusic: related video below', 36, EN, gap=0)]),
 ],
 caption="""큰 해 다음엔, 가까운 등불.

2027년은 정미(丁未)년이에요. 큰 불이 등불이 되어 흙에 내려앉는 해예요. 2026년 병화가 하늘의 해였다면, 2027년 정화는 가까운 곳을 오래 비추는 등불이에요. 2025 을사, 2026 병오, 2027 정미로 이어진 초여름·한여름·늦여름이 정미년에 다 익어요. 미(未)는 나무를 품어 두는 늦여름의 흙이라, 그동안 키운 것을 조용히 넣어 두는 해로 읽어요.

사주의 해는 입춘에 바뀌어요. 2027년 입춘은 2월 4일 오전 10시 46분이에요.

내 일간으로 읽은 한 줄은 6·7장에 있어요. 내 일간은 프로필 링크의 무료 앱에서 찾을 수 있어요.

2027년의 글자 그대로, 『다섯 가지 고요｜정화(丁火)』. 첫 곡은 『Lamplit Keys』예요. 프로필 링크에서 들을 수 있어요.

· English ·
After the big sun, a lamp close by.

2027 is the 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth: a year when a great fire becomes a lamp and settles onto the earth. If 2026 was 丙火 Yang Fire (Byeonghwa), the sun in the sky, then 2027's Yin Fire is a lamp that keeps lighting what is close. Early summer in 2025, high summer in 2026, late summer in 2027: the three summer years ripen fully in 2027. Afternoon Earth is late-summer earth, a storehouse that holds Wood, so we read 2027 as a year to quietly keep what you have raised.

In Saju, the year turns at the start of spring (立春). In 2027, it falls on February 4 at 10:46 a.m. Korea Standard Time.

A one-line reading for each day master is on slides 6 and 7. Find your day master in our free app through the link in bio.

Music true to the year's own character: Five Kinds of Quiet · Yin Fire. The first track is Lamplit Keys. Listen through the link in bio.

#고요 #정미년 #2027년 #새해 #사주 #오행 #일간 #오행음악 #saju #fiveelements""",
 reel_caption="""큰 해 다음엔, 가까운 등불.

큰 불이 등불이 되어 흙에 내려앉는 해, 2027년 정미년이에요. 2026년이 하늘의 해였다면 2027년은 가까운 곳을 오래 비추는 등불이에요. 사주의 해는 입춘(2월 4일 오전 10시 46분)에 바뀌어요.

내 일간으로 읽은 2027년은 피드 게시물에 있어요. 지금 흐르는 음악은 『다섯 가지 고요｜정화(丁火)』의 첫 곡 『Lamplit Keys』, 프로필 링크에서 들을 수 있어요.

· English ·
After the big sun, a lamp close by. 2027, the 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth, is when a great fire becomes a lamp and settles onto the earth. If 2026 was the sun in the sky, 2027 is a lamp that keeps lighting what is close. In Saju, the year turns at the start of spring (立春), February 4, 10:46 a.m. Korea Standard Time.

A reading for each day master is in our feed post. The music is Lamplit Keys from Five Kinds of Quiet · Yin Fire. Listen through the link in bio.

#고요 #정미년 #2027년 #새해 #사주 #오행음악 #saju""",
)

# ───────── 1/4 월 · 소한 (정화) — 유튜브 창이 이 장면으로 21:00 영상판을 만듦(A안)
P['0104'] = dict(
 music='정화',
 slides=[
  S([T('1월 4일 · 이번 주 기운', 44, GOLD, gap=30), T('내일 밤,\n소한', 112, bold=True, gap=36),
     T('小寒 · 1월 5일 오후 11시 10분', 44, gap=30), T('Minor Cold (小寒) arrives tomorrow night', 38, EN, gap=0)]),
  S([T('1월 5일 오후 11시 10분,\n소한이 드는 순간부터\n사주의 달이 바뀌어요.', 54, gap=34), T('자월(子月)에서\n축월(丑月)로.', 70, bold=True, gap=36),
     T('At 11:10 p.m. on January 5, the Saju month turns from 子 Midnight Water (Jasu) to 丑 Deep Night Earth (Chukto).', 32, EN, gap=0)], tag='사주의 달이 바뀌는 밤'),
  S([T('소한부터는\n한겨울의 언 흙이 시작돼요.', 62, bold=True, gap=36), T('언 흙에는\n등불 같은 따뜻한 불이\n어울린다고 봐요.', 52, gap=36),
     T('Minor Cold brings the frozen earth of deep winter. A warm, lamp-like fire suits it.', 34, EN, gap=0)], tag='한겨울의 언 흙'),
  S([T('해는 아직 병오년이에요.\n사주의 해는 입춘(2월 4일)에 바뀌어요.', 46, gap=34), T('소한 뒤, 입춘 전에 태어나면\n병오년 축월생이에요.', 60, bold=True, gap=36),
     T('The year is still the 丙午 year (Byeong-o) · Yang Fire · Noon Fire. Born after Minor Cold, before the start of spring (立春)? Your month is Deep Night Earth.', 32, EN, gap=0)], tag='해는 아직 그대로'),
  S([T('월 계미 · 화 갑신 · 수 을유\n목 병술 · 금 정해 · 토 무자\n일 기축', 54, gap=34), T('날마다 앞 글자가\n물 → 나무 → 불 → 흙 순서로 흘러요.', 46, gap=30),
     T('화요일 밤 11시 10분부터 축월이에요.', 40, GOLD, gap=30),
     T('This week, the first characters run Water → Wood → Fire → Earth. Minor Cold starts Tuesday night.', 32, EN, gap=0)], tag='이번 주 일진'),
  S([T('다섯 가지 고요', 56, bold=True, gap=10), T('정화 편', 96, bold=True, gap=34),
     T('언 흙 곁에 켜 두는\n가까운 등불 같은 소리예요.', 52, gap=30), T('음악은 프로필 링크에서', 46, GOLD, gap=30),
     T('Five Kinds of Quiet · 丁火 Yin Fire (Jeonghwa): a lamp close by, beside frozen earth. Music: link in bio', 32, EN, gap=0)], tag='틀어 두기 좋은 소리'),
 ],
 caption="""내일 밤, 소한이에요.

1월 5일 오후 11시 10분, 소한(小寒)이 드는 순간부터 사주의 달이 자월에서 축월로 바뀌어요. 소한부터는 한겨울의 언 흙이 시작돼요. 언 흙에는 등불 같은 따뜻한 불이 어울린다고 봐요.

해는 아직 병오년이에요. 사주의 해는 입춘(2월 4일)에 바뀌어서, 소한 뒤 입춘 전에 태어나면 병오년 축월생이에요.

이번 주 일진은 계미 → 갑신 → 을유 → 병술 → 정해 → 무자 → 기축. 날마다 앞 글자가 물 → 나무 → 불 → 흙 순서로 흘러요.

언 흙 곁에 켜 두는 가까운 등불 같은 소리, 『다섯 가지 고요｜정화(丁火)』. 프로필 링크에서 들을 수 있어요.

· English ·
Minor Cold arrives tomorrow night.

At 11:10 p.m. on January 5 (Korea Standard Time), Minor Cold (小寒) begins and the Saju month turns from 子 Midnight Water (Jasu) to 丑 Deep Night Earth (Chukto). From here comes the frozen earth of deep winter, and a warm, lamp-like fire suits it.

The year is still the 丙午 year (Byeong-o) · Yang Fire · Noon Fire. In Saju, the year turns at the start of spring (立春) on February 4, so anyone born after Minor Cold and before then has a Deep Night Earth month in that year.

This week, the first characters of the day pillars flow Water → Wood → Fire → Earth.

A lamp close by, beside frozen earth: Five Kinds of Quiet · 丁火 Yin Fire (Jeonghwa). Listen through the link in bio.

#고요 #이번주기운 #소한 #절기 #일진 #사주 #오행 #saju #fiveelements""",
)

# ───────── 1/20 수 · 세 해의 여름 (병화) — 재배치(11/21 21:34)로 1/3에서 옮김 — 원문 Ⅰ 넷째 줄, Ⅲ-2
P['0103'] = dict(
 music='병화', audio='shorts/그림편/audio/병화_Noon Avenue_60s.m4a',
 slides=[
  S([T('1월 20일 · 고요 이야기', 44, GOLD, gap=30), T('여름이\n세 해 동안\n이어졌어요', 104, bold=True, gap=36),
     T('2025 · 2026 · 2027', 48, gap=30), T('Summer has lasted three years', 38, EN, gap=0)]),
  S([T('2025 을사 · 초여름\n2026 병오 · 한여름\n2027 정미 · 늦여름', 60, bold=True, gap=36),
     T('사(巳)는 초여름, 오(午)는 한여름,\n미(未)는 늦여름의 글자예요.', 46, gap=36),
     T('巳 Midmorning Fire (Sahwa) is early summer, 午 Noon Fire (Ohwa) is high summer, and 未 Afternoon Earth (Mito) is late summer.', 32, EN, gap=0)], tag='세 해의 여름'),
  S([T('2026년 병오는\n해(丙)와 한여름(午)이 겹친\n가장 뜨거운 자리예요.', 58, gap=36),
     T('In 2026, 丙火 Yang Fire (Byeonghwa), the sun, meets Noon Fire: the hottest point.', 34, EN, gap=0)], tag='한여름'),
  S([T('2027년 정미는\n여름의 마무리예요.', 64, bold=True, gap=34), T('불이 꺼지는 해라기보다\n불이 다 익는 해로 읽어요.', 50, gap=36),
     T('2027 closes the summer. We read it as a year when the fire ripens, not one when it goes out.', 34, EN, gap=0)], tag='늦여름'),
  S([T('1월인 지금은 아직 병오년,\n한여름의 끝자락이에요.', 54, gap=30), T('늦여름은\n입춘(2월 4일)부터.', 64, bold=True, gap=36),
     T('January is still the 丙午 year (Byeong-o), the tail end of high summer. The 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth begins Feb 4, at the start of spring (立春).', 32, EN, gap=0)], tag='지금은 어느 여름일까요'),
  S([T('다섯 가지 고요', 56, bold=True, gap=10), T('병화 편', 96, bold=True, gap=34),
     T('한여름의 끝자락에 듣는,\n한낮의 해 같은 소리예요.', 52, gap=24), T('첫 곡은 『Noon Avenue』예요.', 44, gap=30),
     T('음악은 프로필 링크에서', 46, GOLD, gap=30),
     T('Five Kinds of Quiet · Yang Fire. The first track is Noon Avenue. Music: link in bio', 32, EN, gap=0)], tag='틀어 두기 좋은 소리'),
 ],
 reel=[
  dict(sec=4.5, instant=True, items=[T('1월 20일', 50, GOLD, gap=34), T('여름이\n세 해 동안\n이어졌어요', 120, bold=True, gap=50), T('Summer has lasted three years', 42, EN, gap=0)]),
  dict(sec=6.5, tag='세 해의 여름', step=0.9, items=[T('2025 을사 · 초여름', 70, gap=20), T('2026 병오 · 한여름', 70, gap=20), T('2027 정미 · 늦여름', 70, bold=True, gap=44),
       T('Early, high, and late summer', 40, EN, gap=0)]),
  dict(sec=6.0, step=1.0, items=[T('2027년은\n여름의 마무리', 96, bold=True, gap=40), T('불이 다 익는 해', 72, gap=50), T('2027: the fire ripens', 40, EN, gap=0)]),
  dict(sec=5.0, step=0.9,
       items_ig=[T('1월인 지금은\n어느 여름일까요?', 92, bold=True, gap=34), T('풀이는 @goyo_mio\n피드 게시물에서', 60, bold=True, gap=30),
                 T('Which summer are we in now?\nFull reading on our profile', 40, EN, gap=0)],
       items_yt=[T('1월인 지금은\n어느 여름일까요?', 92, bold=True, gap=34), T('풀이는\n채널 게시물에서', 60, bold=True, gap=30),
                 T('Which summer are we in now?\nFull reading in our Posts tab', 40, EN, gap=0)]),
  dict(sec=7.5, tag='지금 흐르는 소리',
       items_ig=[T('다섯 가지 고요', 60, bold=True, gap=10), T('병화 편', 100, bold=True, gap=36), T('첫 곡 『Noon Avenue』', 56, gap=26),
                 T('음악은 프로필 링크에서', 48, GOLD, gap=30), T('Five Kinds of Quiet · 丙火 Yang Fire (Byeonghwa): Noon Avenue\nMusic: link in bio', 36, EN, gap=0)],
       items_yt=[T('다섯 가지 고요', 60, bold=True, gap=10), T('병화 편', 100, bold=True, gap=36), T('첫 곡 『Noon Avenue』', 56, gap=26),
                 T('음악은 아래 관련 영상', 48, GOLD, gap=30), T('Five Kinds of Quiet · 丙火 Yang Fire (Byeonghwa): Noon Avenue\nMusic: related video below', 36, EN, gap=0)]),
 ],
 caption="""여름이 세 해 동안 이어졌어요.

2025 을사는 초여름, 2026 병오는 한여름, 2027 정미는 늦여름이에요. 사(巳)·오(午)·미(未)가 여름의 세 글자라서, 세 해를 이어 보면 여름 한 철이 돼요. 2026년 병오는 해(丙)와 한여름(午)이 겹친 가장 뜨거운 자리고, 2027년 정미는 여름의 마무리예요. 불이 꺼지는 해라기보다 불이 다 익는 해로 읽어요.

1월인 지금은 아직 병오년, 한여름의 끝자락이에요. 사주의 해는 입춘(2월 4일)에 바뀌거든요.

한여름의 끝자락에는 한낮의 해 같은 『다섯 가지 고요｜병화(丙火)』. 첫 곡은 『Noon Avenue』예요. 프로필 링크에서 들을 수 있어요.

· English ·
Summer has lasted three years.

2025 was early summer, 2026 is high summer, and 2027 is late summer. The three summer characters are 巳 Midmorning Fire (Sahwa), 午 Noon Fire (Ohwa) and 未 Afternoon Earth (Mito), so the three years together make one summer season. 2026 is the hottest point, where 丙火 Yang Fire (Byeonghwa), the sun, met Noon Fire. 2027 closes the summer. We read it as a year when the fire ripens, not one when it goes out.

Right now, in January, it is still the 丙午 year (Byeong-o) · Yang Fire · Noon Fire, the tail end of high summer. In Saju, the year turns at the start of spring (立春) on February 4.

For the tail end of high summer, music like the midday sun: Five Kinds of Quiet · Yang Fire. The first track is Noon Avenue. Listen through the link in bio.

#고요 #고요이야기 #정미년 #병오년 #사주 #오행 #오행음악 #saju #fiveelements""",
 reel_caption="""여름이 세 해 동안 이어졌어요.

2025 을사는 초여름, 2026 병오는 한여름, 2027 정미는 늦여름. 2027년은 여름의 마무리, 불이 다 익는 해로 읽어요. 1월인 지금이 어느 여름인지는 피드 게시물에 있어요.

지금 흐르는 음악은 『다섯 가지 고요｜병화(丙火)』의 첫 곡 『Noon Avenue』, 프로필 링크에서 들을 수 있어요.

· English ·
Summer has lasted three years: early summer in 2025, high summer in 2026, and late summer in 2027. 2027 closes the summer, a year when the fire ripens. Which summer are we in now, in January? See our feed post.

The music is Noon Avenue from Five Kinds of Quiet · 丙火 Yang Fire (Byeonghwa). Listen through the link in bio.

#고요 #정미년 #병오년 #사주 #오행음악 #saju""",
)

# ───────── 1/17 일 (재배치로 1/6에서 옮김) · 넓게 비추는 빛, 가까이 오래 비추는 빛 (정화) — 원문 Ⅲ-1(적천수 병·정 구분), Ⅶ 라 투르
P['0106'] = dict(
 music='정화', audio='shorts/그림편/audio/정화_Lantern Room_60s.m4a',
 slides=[
  S([T('1월 17일 · 고요 이야기', 44, GOLD, gap=30), T('빛에도\n두 가지가\n있어요', 110, bold=True, gap=36),
     T('넓게 비추는 빛, 가까이 오래 비추는 빛', 42, gap=30), T('Two kinds of light', 38, EN, gap=0)]),
  S([T('병화는 하늘의 해.', 70, bold=True, gap=30), T('사방을 고루,\n멀리까지 비추는 빛이에요.', 54, gap=36),
     T('丙火 Yang Fire (Byeonghwa) is the sun in the sky,\nlighting everything, far and wide.', 34, EN, gap=0)], tag='넓게 비추는 빛'),
  S([T('정화는 등불.', 70, bold=True, gap=30), T('가까운 자리를\n오래 밝히는 빛이에요.', 54, gap=36),
     T('丁火 Yin Fire (Jeonghwa) is a lamp\nthat lights what is near, for a long time.', 34, EN, gap=0)], tag='가까이 오래 비추는 빛'),
  S([T('해는 멀리서 모두를 비추고,\n등불은 가까이에서\n한 사람의 얼굴과 손을 비춰요.', 54, gap=36),
     T('옛 명리 책 『적천수』도\n병화는 세차고, 정화는 부드럽다고\n두 불을 나눠 봐요.', 44, gap=36),
     T('The sun lights everyone from afar. A lamp lights one person\'s face and hands, up close.', 34, EN, gap=0)], tag='같은 불, 다른 빛'),
  S([T('2026년의 빛은 해,\n2027년의 빛은 등불이에요.', 58, bold=True, gap=30), T('넓게 퍼지는 빛이 입춘부터\n가까운 자리를 오래 밝히는\n빛으로 옮겨 가요.', 46, gap=30),
     T('사주에서는 입춘(2월 4일)에 한 해가 바뀌어요.', 38, gap=30), T('1월 7일 그림 읽기의 라 투르도\n등불 하나를 그렸어요.', 42, GOLD, gap=30),
     T('In 2026 the light is the sun; in 2027, a lamp.\nLa Tour painted one in our Jan 7 post.', 32, EN, gap=0)], tag='해에서 등불로'),
  S([T('다섯 가지 고요', 56, bold=True, gap=10), T('정화 편', 96, bold=True, gap=34),
     T('가까운 자리를 오래 밝히는\n등불 같은 소리예요.', 52, gap=24), T('지금 고른 곡은 『Lantern Room』이에요.', 42, gap=30),
     T('음악은 프로필 링크에서', 46, GOLD, gap=30),
     T('Five Kinds of Quiet · Yin Fire. Track: Lantern Room. Music: link in bio', 32, EN, gap=0)], tag='틀어 두기 좋은 소리'),
 ],
 reel=[
  dict(sec=4.5, instant=True, items=[T('1월 17일', 50, GOLD, gap=34), T('빛에도\n두 가지가\n있어요', 124, bold=True, gap=50), T('Two kinds of light', 42, EN, gap=0)]),
  dict(sec=6.5, step=1.0, items=[T('해는\n넓게 멀리', 96, bold=True, gap=40), T('등불은\n가까이 오래', 96, bold=True, gap=50),
       T('The sun: far and wide. A lamp: close and lasting.', 40, EN, gap=0)]),
  dict(sec=5.5, step=1.0, items=[T('2027년의 빛은', 76, gap=20), T('등불', 150, bold=True, gap=50), T('In 2027, the light is a lamp.', 40, EN, gap=0)]),
  dict(sec=5.0, step=0.9,
       items_ig=[T('옛 책은 두 불을\n어떻게 나눴을까요?', 92, bold=True, gap=34), T('풀이는 @goyo_mio\n피드 게시물에서', 60, bold=True, gap=30),
                 T('How did old texts tell the two fires apart?\nFull reading on our profile', 40, EN, gap=0)],
       items_yt=[T('옛 책은 두 불을\n어떻게 나눴을까요?', 92, bold=True, gap=34), T('풀이는\n채널 게시물에서', 60, bold=True, gap=30),
                 T('How did old texts tell the two fires apart?\nFull reading in our Posts tab', 40, EN, gap=0)]),
  dict(sec=7.5, tag='지금 흐르는 소리',
       items_ig=[T('다섯 가지 고요', 60, bold=True, gap=10), T('정화 편', 100, bold=True, gap=36), T('『Lantern Room』', 56, gap=26),
                 T('음악은 프로필 링크에서', 48, GOLD, gap=30), T('Five Kinds of Quiet · 丁火 Yin Fire (Jeonghwa): Lantern Room.\nMusic: link in bio', 36, EN, gap=0)],
       items_yt=[T('다섯 가지 고요', 60, bold=True, gap=10), T('정화 편', 100, bold=True, gap=36), T('『Lantern Room』', 56, gap=26),
                 T('음악은 아래 관련 영상', 48, GOLD, gap=30), T('Five Kinds of Quiet · 丁火 Yin Fire (Jeonghwa): Lantern Room.\nMusic: related video below', 36, EN, gap=0)]),
 ],
 caption="""빛에도 두 가지가 있어요.

병화는 하늘의 해예요. 사방을 고루, 멀리까지 비추는 빛이에요. 정화는 등불이에요. 가까운 자리를 오래 밝히는 빛이에요. 해는 멀리서 모두를 비추고, 등불은 가까이에서 한 사람의 얼굴과 손을 비춰요. 옛 명리 책 『적천수』도 병화는 세차고 정화는 부드럽다고 두 불을 나눠 봐요.

2026년의 빛이 해라면, 2027년의 빛은 등불이에요. 넓게 퍼지는 빛이 입춘부터 가까운 자리를 오래 밝히는 빛으로 옮겨 가요. 사주에서는 입춘(2월 4일)에 한 해가 바뀌어요.

1월 7일 고요의 그림 읽기에서 본 조르주 드 라 투르의 그림도 등불 하나를 그렸어요.

가까운 자리를 오래 밝히는 『다섯 가지 고요｜정화(丁火)』, 지금 고른 곡은 『Lantern Room』이에요. 프로필 링크에서 들을 수 있어요.

· English ·
There are two kinds of light.

丙火 Yang Fire (Byeonghwa) is the sun in the sky, lighting everything, far and wide. 丁火 Yin Fire (Jeonghwa) is a lamp that lights what is near, for a long time. The sun lights everyone from afar; a lamp lights one person's face and hands, up close. The old Saju classic Di Tian Sui (滴天髓) also tells the two fires apart: Yang Fire is fierce, Yin Fire is gentle.

If 2026's light is the sun, 2027's is a lamp. From the start of spring, the wide light turns to a close, steady one. In Saju, the year turns at the start of spring (立春), February 4.

Georges de La Tour, in our January 7 painting post, painted a single lamp.

Five Kinds of Quiet · Yin Fire, with the track Lantern Room. Listen through the link in bio.

#고요 #고요이야기 #정미년 #병화 #정화 #적천수 #사주 #오행음악 #saju #fiveelements""",
 reel_caption="""빛에도 두 가지가 있어요.

해(병화)는 넓게 멀리, 등불(정화)은 가까이 오래 비춰요. 2027년의 빛은 등불이에요. 옛 명리 책이 두 불을 어떻게 나눴는지는 피드 게시물에 있어요.

지금 흐르는 음악은 『다섯 가지 고요｜정화(丁火)』의 『Lantern Room』, 프로필 링크에서 들을 수 있어요.

· English ·
There are two kinds of light. The sun lights far and wide; a lamp lights what is close, for a long time. In 2027, the light is a lamp. Our feed post shows how an old Saju classic tells the two fires apart.

The music is Lantern Room from Five Kinds of Quiet · 丁火 Yin Fire (Jeonghwa). Listen through the link in bio.

#고요 #정미년 #병화 #정화 #사주 #오행음악 #saju""",
)

# ───────── 1/7 목 · 고요의 그림 읽기 #2 라 투르 (정화) — 원문 Ⅶ, LACMA M.77.73 (1635~37년경, 퍼블릭 도메인)
LT = 'art/라투르_막달라_연기나는불꽃.jpg'
P['0107'] = dict(
 music='정화',
 slides=[
  S([T('고요의 그림 읽기 #2', 40, GOLD, gap=10), T('등불 하나', 84, bold=True, gap=14),
     T('조르주 드 라 투르, 〈연기 나는 불꽃 앞의 막달라 마리아〉\n1635~37년경 · LACMA · 퍼블릭 도메인', 26, [150, 145, 135], gap=10),
     T('The Magdalen with the Smoking Flame · Georges de La Tour', 28, EN, gap=0)], card={'file': LT, 'h': 600}),
  S([T('어두운 방,\n등불 하나가\n얼굴과 손만 비춰요.', 66, bold=True, gap=36),
     T('그녀는 불꽃을 바라보고 있어요.\n등불 위로 연기 한 줄기가 올라가요.', 46, gap=36),
     T('In a dark room, one lamp lights only her face and hands.', 34, EN, gap=0)], tag='그림'),
  S([T('무릎 위 해골,\n쌓인 책과 채찍,\n그리고 바라보는 불꽃.', 60, bold=True, gap=34),
     T('해골과 책의 매끈한 표면, 치마와 피부가\n빛을 저마다 다르게 받도록 그렸어요.', 40, gap=34),
     T('A skull on her lap, books, a scourge, and the flame she watches.', 34, EN, gap=0)], tag='그림 속 물건'),
  S([T('라 투르는 1652년 세상을 떠난 뒤\n이름이 잊혔어요.', 54, gap=30), T('1915년, 독일 미술사학자\n헤르만 포스가 다시 찾아냈어요.', 58, bold=True, gap=30),
     T('이 그림도 한때는\n르냉 형제의 그림으로 전해졌어요.', 46, gap=36),
     T('Forgotten after his death in 1652, La Tour was rediscovered in 1915 by Hermann Voss.', 34, EN, gap=0)], tag='잊혔다가 다시 찾은 화가'),
  S([T('보이는 것', 40, GOLD, True, 6), T('어둠 속 불꽃 하나 → 불, 그중 등불', 44, gap=26),
     T('그리는 방식', 40, GOLD, True, 6), T('빛만 남기고 어둠에 묻음 → 불의 빛', 44, gap=26),
     T('화가의 사주', 40, GOLD, True, 6), T('세례 기록만 남아 있어\n생일을 확인하지 못해 보지 않았어요.', 40, gap=30),
     T('제 해석이에요.', 34, [150, 145, 135], gap=24),
     T('Seen: one flame in the dark. Painted: only the light, the rest left in shadow. We read it as 丁火 Yin Fire (Jeonghwa).', 32, EN, gap=0)], tag='고요의 읽기 · 화(火)'),
  S([T('넓게 퍼지는 해가 아니라\n가까운 것을 오래 비추는 등불.', 58, bold=True, gap=34),
     T('2027년의 빛을\n그림 한 장으로 보면 이래요.', 50, gap=36),
     T('Not the wide sun, but a lamp that lights what is near. This is 2027 in a single painting.', 34, EN, gap=0)], tag='정미년과 이어서'),
  S([T('다섯 가지 고요', 56, bold=True, gap=10), T('정화 편', 96, bold=True, gap=34),
     T('심지 하나로 오래 타는\n등불 같은 소리예요.', 52, gap=24), T('오늘 밤 9시 릴스에 흐르는 곡은\n『Soft Wick』이에요.', 42, gap=30),
     T('음악은 프로필 링크에서', 46, GOLD, gap=30),
     T('Five Kinds of Quiet · Yin Fire.\nTonight\'s reel: Soft Wick. Music: link in bio', 32, EN, gap=0)], tag='이 그림 옆에 둘 소리'),
 ],
 caption="""고요의 그림 읽기 #2 · 조르주 드 라 투르 〈연기 나는 불꽃 앞의 막달라 마리아〉

어두운 방, 등불 하나가 얼굴과 손만 비춰요. 무릎 위에는 해골, 곁에는 쌓인 책과 채찍, 그리고 그녀가 바라보는 불꽃이 있어요. 라 투르는 1652년 세상을 떠난 뒤 이름이 잊혔다가, 1915년 독일 미술사학자 헤르만 포스가 다시 찾아냈어요. 이 그림도 한때는 르냉 형제의 그림으로 전해졌어요.

고요의 읽기로는 화(火), 그중 등불 정화예요. 넓게 퍼지는 해가 아니라 가까운 것을 오래 비추는 빛이라, 2027년의 빛을 그림 한 장으로 보면 이래요. 화가는 세례 기록만 남아 있어 생일을 확인하지 못해 사주는 보지 않았어요. 제 해석이에요.

이 그림 옆에는 『다섯 가지 고요｜정화(丁火)』. 오늘 밤 9시 릴스에는 『Soft Wick』이 흘러요. 프로필 링크에서 들을 수 있어요.

그림: LACMA(로스앤젤레스 카운티 미술관), 1635~37년경, 퍼블릭 도메인

· English ·
Goyo Reads a Painting #2 · Georges de La Tour, The Magdalen with the Smoking Flame

In a dark room, one lamp lights only her face and hands. A skull rests on her lap, with books, a scourge, and the flame she watches. After his death in 1652, La Tour was forgotten until the German art historian Hermann Voss rediscovered him in 1915. This painting, too, was once attributed to the Le Nain brothers.

We read it as Fire, and within Fire, the lamp: 丁火 Yin Fire (Jeonghwa). Not the wide sun, but a light that stays close. This is 2027 in a single painting. Only his baptism record survives, so his birth date is unknown and we did not read his Saju. This is our own reading.

Beside it: Five Kinds of Quiet · Yin Fire. Tonight's 9 p.m. reel plays Soft Wick. Listen through the link in bio.

Image: LACMA (Los Angeles County Museum of Art), c. 1635 to 1637, public domain

#고요 #고요의그림읽기 #라투르 #GeorgesdeLaTour #막달라마리아 #정미년 #오행 #명화 #fiveelements""",
)

# ───────── 1/3 일 · 여행: 진주 남강유등 (임수) — 원문 Ⅷ. 재배치(11/21 21:34)로 1/20에서 옮김
# 근거: 문화체육관광부 축제 정보(2026. 10. 3.~10. 18.), 한국관광공사 소개(임진왜란 진주성 전투 유래)
P['0103j'] = dict(
 music='임수', audio='shorts/그림편/audio/임수_Wide Water_60s.m4a',
 slides=[
  S([T('1월 3일 · 정미년에 갈 만한 곳', 44, GOLD, gap=30), T('강물 위의\n등불', 116, bold=True, gap=36),
     T('경남 진주 남강유등축제', 48, gap=30), T('Lamps on the river · Jinju, Korea', 38, EN, gap=0)]),
  S([T('가을이면\n진주 남강 위에\n등이 떠요.', 66, bold=True, gap=34), T('해마다 10월 초~중순에 열려요.\n2026년은 10월 3일부터 18일까지였어요.', 42, gap=26),
     T('2027년 날짜는 아직 발표 전이에요.', 36, [150, 145, 135], gap=30),
     T('Every fall, lamps float on the Namgang River. Held in early to mid October.', 32, EN, gap=0)], tag='강물 위에 등을 띄우는 축제'),
  S([T('임진왜란 진주성 전투 때', 50, gap=20), T('남강에 등을 띄워\n강을 건너려는 적을 막고,\n성 밖 가족에게\n안부를 전했다고 해요.', 58, bold=True, gap=36),
     T('It began with a 1590s battle at Jinju Fortress: river lamps held back the enemy and carried word home.', 32, EN, gap=0)], tag='왜 강에 등을 띄웠을까요'),
  S([T('2027년의 글자는\n가까운 곳을 오래 비추는 등불.', 54, gap=30), T('그 등불이\n넓은 강물 위에\n떠 있는 곳이에요.', 60, bold=True, gap=36),
     T('2027 is the year of the lamp. Here, the lamps float on a wide river.', 34, EN, gap=0)], tag='등불과 강물이 한 장면에'),
  S([T('다섯 가지 고요', 56, bold=True, gap=10), T('임수 편', 96, bold=True, gap=34),
     T('등불을 싣고 흐르는\n넓은 강물 같은 소리예요.', 52, gap=24), T('첫 곡은 『Wide Water』예요.', 44, gap=30),
     T('음악은 프로필 링크에서', 46, GOLD, gap=30),
     T('Five Kinds of Quiet · 壬水 Yang Water (Imsu).\nThe first track is Wide Water. Music: link in bio', 32, EN, gap=0)], tag='틀어 두기 좋은 소리'),
 ],
 reel=[
  dict(sec=4.5, instant=True, items=[T('1월 3일 · 갈 만한 곳', 50, GOLD, gap=34), T('강물 위의\n등불', 130, bold=True, gap=50), T('Lamps on the river', 42, EN, gap=0)]),
  dict(sec=6.0, step=1.0, items=[T('가을, 진주 남강에\n등이 떠요', 92, bold=True, gap=40), T('해마다 10월 초~중순', 60, gap=50), T('Jinju, every October', 40, EN, gap=0)]),
  dict(sec=6.5, step=1.0, items=[T('임진왜란 때\n강을 건너려는 적을 막고', 78, bold=True, gap=30), T('성 밖 가족에게\n안부를 전한 등불', 78, bold=True, gap=50),
       T('Lamps that held back the enemy\nand carried word home', 40, EN, gap=0)]),
  dict(sec=5.0, step=0.9,
       items_ig=[T('왜 2027년에\n어울리는 곳일까요?', 92, bold=True, gap=34), T('풀이는 @goyo_mio\n피드 게시물에서', 60, bold=True, gap=30),
                 T('Why does it suit 2027?\nFull reading on our profile', 40, EN, gap=0)],
       items_yt=[T('왜 2027년에\n어울리는 곳일까요?', 92, bold=True, gap=34), T('풀이는\n채널 게시물에서', 60, bold=True, gap=30),
                 T('Why does it suit 2027?\nFull reading in our Posts tab', 40, EN, gap=0)]),
  dict(sec=7.5, tag='지금 흐르는 소리',
       items_ig=[T('다섯 가지 고요', 60, bold=True, gap=10), T('임수 편', 100, bold=True, gap=36), T('첫 곡 『Wide Water』', 56, gap=26),
                 T('음악은 프로필 링크에서', 48, GOLD, gap=30), T('Five Kinds of Quiet · 壬水 Yang Water (Imsu): Wide Water.\nMusic: link in bio', 36, EN, gap=0)],
       items_yt=[T('다섯 가지 고요', 60, bold=True, gap=10), T('임수 편', 100, bold=True, gap=36), T('첫 곡 『Wide Water』', 56, gap=26),
                 T('음악은 아래 관련 영상', 48, GOLD, gap=30), T('Five Kinds of Quiet · 壬水 Yang Water (Imsu): Wide Water.\nMusic: related video below', 36, EN, gap=0)]),
 ],
 caption="""강물 위의 등불, 진주 남강유등축제예요.

가을이면 경남 진주 남강 위에 수많은 등이 떠요. 해마다 10월 초~중순에 열리고, 2026년은 10월 3일부터 18일까지였어요. 2027년 날짜는 아직 발표 전이라 가기 전에 진주시 공지를 확인해 주세요.

임진왜란 진주성 전투 때 남강에 등을 띄워 강을 건너려는 적을 막고, 성 밖 가족에게 안부를 전했다고 해요. 축제는 그 이야기에서 시작됐어요.

2027년의 글자는 가까운 곳을 오래 비추는 등불이에요. 그 등불이 넓은 강물 위에 떠 있는 곳이라, 정미년에 한 번 가 볼 만한 곳으로 골랐어요.

등불을 싣고 흐르는 강물 같은 소리, 『다섯 가지 고요｜임수(壬水)』. 첫 곡은 『Wide Water』예요. 프로필 링크에서 들을 수 있어요.

· English ·
Lamps on the river: the Jinju Namgang Yudeung Festival.

Every fall, countless lamps float on the Namgang River in Jinju, Korea. The festival runs in early to mid October; in 2026 it ran October 3 to 18. The 2027 dates are not out yet, so check the city's notice before you go.

The custom goes back to the 1590s and a battle at Jinju Fortress: lamps floated on the river held back the enemy and carried word to families outside the walls.

2027 is the year of the lamp, a light that stays close. Here, those lamps float on a wide river, so we picked it as a place to visit this year.

Music like a wide river carrying lamps: Five Kinds of Quiet · 壬水 Yang Water (Imsu). The first track is Wide Water. Listen through the link in bio.

#고요 #정미년 #진주남강유등축제 #진주 #유등 #국내여행 #오행음악 #fiveelements""",
 reel_caption="""강물 위의 등불, 진주 남강유등축제예요.

가을이면 진주 남강에 등이 떠요. 임진왜란 진주성 전투 때 강을 건너려는 적을 막고 성 밖 가족에게 안부를 전한 등불에서 시작된 축제예요. 2027년에 어울리는 이유는 피드 게시물에 있어요.

지금 흐르는 음악은 『다섯 가지 고요｜임수(壬水)』의 첫 곡 『Wide Water』, 프로필 링크에서 들을 수 있어요.

· English ·
Lamps on the river: every fall in Jinju, Korea, lamps float on the Namgang River. The festival began with a battle in the 1590s, when river lamps held back the enemy and carried word to families. Why it suits 2027 is in our feed post.

The music is Wide Water from Five Kinds of Quiet · 壬水 Yang Water (Imsu). Listen through the link in bio.

#고요 #정미년 #진주남강유등축제 #유등 #오행음악""",
)

def build(key):
    p = P[key]; out = os.path.join(os.path.dirname(os.path.abspath(__file__)), key); os.makedirs(out, exist_ok=True)
    json.dump({'music': p['music'], 'slides': p['slides']}, open(f'{out}/slides.json', 'w'), ensure_ascii=False, indent=1)
    if p.get('reel'):
        json.dump({'audio': p['audio'], 'scenes': p['reel']}, open(f'{out}/reel.json', 'w'), ensure_ascii=False, indent=1)
    open(f'{out}/caption.txt', 'w').write(p['caption'])
    if not p.get('reel') and os.path.exists(f'{out}/reel.json'): os.remove(f'{out}/reel.json')
    if p.get('reel_caption'): open(f'{out}/reel_caption.txt', 'w').write(p['reel_caption'])
    print('built', key)

DATES = {'0101': '2027-01-01', '0103': '2027-01-20', '0104': '2027-01-04', '0106': '2027-01-17', '0107': '2027-01-07', '0103j': '2027-01-03'}
def pack(key):
    """렌더된 캐러셀·릴스를 posts/날짜(18:00), posts/날짜-1820(18:20)에 넣음. 모두 approved:false."""
    import shutil
    p = P[key]; d = DATES[key]; root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src = os.path.join(root, 'jeongmi', key); dst = os.path.join(root, 'posts', d); os.makedirs(dst, exist_ok=True)
    def keep(path):  # 이미 승인된 폴더는 다시 넣어도 승인 유지(바뀐 내용은 미오 님께 다시 알릴 것)
        try: return json.load(open(path)).get('approved', False)
        except Exception: return False
    n = len(p['slides']); files = []
    for i in range(1, n + 1):
        shutil.copy(f'{src}/{i:02d}.jpg', f'{dst}/{i:02d}.jpg'); files.append(f'posts/{d}/{i:02d}.jpg')
    json.dump({'type': 'carousel', 'via': 'api', 'approved': keep(f'{dst}/post.json'), 'files': files, 'caption': p['caption'],
               'note': f'정미년 시리즈 {key} (인스타 창 11/21). 설정 jeongmi/build.py · 렌더 example_saju.py. 미오 님 확인 뒤 approved true'},
              open(f'{dst}/post.json', 'w'), ensure_ascii=False, indent=1)
    if p.get('reel'):
        rd = dst + '-1820'; os.makedirs(rd, exist_ok=True)
        json.dump({'type': 'reel', 'via': 'api', 'approved': keep(f'{rd}/post.json'), 'video_file': f'jeongmi/{key}/reel_ig.mp4', 'caption': p['reel_caption'],
                   'thumb_offset': 1000, 'note': f'정미년 시리즈 {key} 릴스 18:20. 유튜브 쇼츠판 jeongmi/{key}/short_yt.mp4 (끝 「음악은 아래 관련 영상」)'},
                  open(f'{rd}/post.json', 'w'), ensure_ascii=False, indent=1)
    print('packed', key, d)

if __name__ == '__main__':
    if sys.argv[1:2] == ['pack']:
        for k in sys.argv[2:]: pack(k)
        sys.exit()
    for k in sys.argv[1:] or P: build(k)
