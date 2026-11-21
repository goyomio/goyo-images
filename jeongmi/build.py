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
  S([T('사주의 달은 1일이 아니라\n절기가 드는 순간 바뀌어요.', 50, gap=32), T('소한은 사주의 달을 여는\n열두 절기 가운데 마지막이에요.', 58, bold=True, gap=34),
     T('입춘에 인월(寅月)로 한 해의 달을 열고,\n소한에 축월(丑月)로 마지막 달을 열어요.\n스물네 절기 전체의 마지막은\n보름 뒤 대한이에요.', 38, GOLD, gap=30),
     T('In Saju, a month begins not on the 1st but at one of twelve solar terms. The Saju year opens at the start of spring (立春) with 寅 Predawn Wood (Inmok). Minor Cold (小寒) is the last of the twelve, opening the final month: Deep Night Earth.', 32, EN, gap=0)], tag='사주의 달력은 절기로 넘어가요'),
  S([T('소한부터는\n한겨울의 언 흙이 시작돼요.', 62, bold=True, gap=36), T('언 흙에는\n등불 같은 따뜻한 불이\n어울린다고 봐요.', 52, gap=36),
     T('Minor Cold brings the frozen earth of deep winter. A warm, lamp-like fire suits it.', 34, EN, gap=0)], tag='한겨울의 언 흙'),
  S([T('소한(小寒)은 작은 추위,\n대한(大寒)은 큰 추위.', 48, gap=28), T('그런데 옛말에\n「대한이 소한의 집에 가서\n얼어 죽었다」고 해요.', 52, bold=True, gap=30),
     T('소한 무렵이 대한 무렵보다\n더 춥게 느껴질 때가 많아 생겼다고 해요.\n올해 대한은 1월 20일 오후 4시 30분이에요.', 38, GOLD, gap=26),
     T('Minor Cold is the "small cold"; Major Cold (大寒), the "great cold." Yet an old Korean saying goes: "Major Cold went to Minor Cold\'s house and froze to death." The days around Minor Cold are said to feel even colder. This year, Major Cold arrives on January 20 at 4:30 p.m. KST.', 30, EN, gap=0)], tag='이름은 작은 추위인데'),
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

사주의 달은 1일이 아니라 절기가 드는 순간 바뀌어요. 소한은 사주의 달을 여는 열두 절기 가운데 마지막이에요. 입춘에 인월로 열린 한 해가 소한에 축월로 마지막 달을 맞아요. 스물네 절기 전체의 마지막은 보름 뒤 대한(1월 20일 오후 4시 30분)이에요. 이름은 작은 추위지만, 옛말에 「대한이 소한의 집에 가서 얼어 죽었다」고 할 만큼 소한 무렵이 대한 무렵보다 더 춥게 느껴질 때가 많다고 해요.

해는 아직 병오년이에요. 사주의 해는 입춘(2월 4일)에 바뀌어서, 소한 뒤 입춘 전에 태어나면 병오년 축월생이에요.

이번 주 일진은 계미 → 갑신 → 을유 → 병술 → 정해 → 무자 → 기축. 날마다 앞 글자가 물 → 나무 → 불 → 흙 순서로 흘러요.

언 흙 곁에 켜 두는 가까운 등불 같은 소리, 『다섯 가지 고요｜정화(丁火)』. 프로필 링크에서 들을 수 있어요.

· English ·
Minor Cold arrives tomorrow night.

At 11:10 p.m. on January 5 (Korea Standard Time), Minor Cold (小寒) begins and the Saju month turns from 子 Midnight Water (Jasu) to 丑 Deep Night Earth (Chukto). From here comes the frozen earth of deep winter, and a warm, lamp-like fire suits it.

In Saju, a month begins not on the 1st but at one of twelve solar terms. The Saju year opens at the start of spring (立春) with 寅 Predawn Wood (Inmok), and Minor Cold is the last of the twelve, opening the final month. The last of all twenty-four solar terms is Major Cold (大寒), fifteen days later, on January 20 at 4:30 p.m. Its name means the "great cold," yet an old Korean saying goes: "Major Cold went to Minor Cold's house and froze to death." The days around Minor Cold are said to feel even colder.

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
     T('The sun lights everyone from afar.\nA lamp lights one person\'s\nface and hands, up close.', 34, EN, gap=0)], tag='같은 불, 다른 빛'),
  S([T('옛 명리 책 『적천수』는 병화를 두고', 42, gap=26), T('세차고 사나워서\n서리와 눈도\n업신여긴다고 했어요.', 62, bold=True, gap=30),
     T('丙火猛烈 欺霜侮雪', 40, GOLD, gap=26), T('겨울 추위에도\n기세가 꺾이지 않는 불이라는 뜻이에요.', 44, gap=34),
     T('Di Tian Sui (滴天髓), a classic Saju text, on Yang Fire:\n"Fierce and blazing, it scorns frost and snow."', 32, EN, gap=0)], tag='옛 책이 본 해'),
  S([T('같은 책은 정화를 두고', 42, gap=26), T('부드럽고 치우치지 않으며\n속은 환하게 밝다고 했어요.', 56, bold=True, gap=24),
     T('세져도 사납게 타지 않고,\n약해져도 다하지 않는다고요.', 52, bold=True, gap=26),
     T('丁火柔中 內性昭融 … 旺而不烈 衰而不窮', 34, GOLD, gap=26), T('등불이 오래 비추는 빛인 까닭이 여기 있어요.', 40, gap=34),
     T('On Yin Fire: "Gentle and centered, bright within.\nStrong, it does not rage; weak, it does not run out."', 32, EN, gap=0)], tag='옛 책이 본 등불'),
  S([T('2026년의 빛은 해,\n2027년의 빛은 등불이에요.', 58, bold=True, gap=30), T('넓게 퍼지는 빛이 입춘부터\n가까운 자리를 오래 밝히는\n빛으로 옮겨 가요.', 46, gap=30),
     T('사주에서는 입춘(2월 4일)에 한 해가 바뀌어요.', 38, gap=30), T('1월 7일 그림 읽기의 라 투르도\n등불 하나를 그렸어요.', 42, GOLD, gap=30),
     T('In 2026 the light is the sun; in 2027, a lamp.\nLa Tour, from our Jan 7 post, painted one.', 32, EN, gap=0)], tag='해에서 등불로'),
  S([T('다섯 가지 고요', 56, bold=True, gap=10), T('정화 편', 96, bold=True, gap=34),
     T('가까운 자리를 오래 밝히는\n등불 같은 소리예요.', 52, gap=24), T('지금 고른 곡은 『Lantern Room』이에요.', 42, gap=30),
     T('음악은 프로필 링크에서', 46, GOLD, gap=30),
     T('Five Kinds of Quiet · Yin Fire. Track: Lantern Room.\nListen through the link in bio.', 32, EN, gap=0)], tag='틀어 두기 좋은 소리'),
 ],
 reel=[
  dict(sec=4.5, instant=True, items=[T('1월 17일', 50, GOLD, gap=34), T('빛에도\n두 가지가\n있어요', 124, bold=True, gap=50), T('Two kinds of light', 42, EN, gap=0)]),
  dict(sec=6.5, step=1.0, items=[T('해는\n넓게 멀리', 96, bold=True, gap=40), T('등불은\n가까이 오래', 96, bold=True, gap=50),
       T('The sun: far and wide. A lamp: close and lasting.', 40, EN, gap=0)]),
  dict(sec=5.5, step=1.0, items=[T('2027년의 빛은', 76, gap=20), T('등불', 150, bold=True, gap=50), T('In 2027, the light is a lamp.', 40, EN, gap=0)]),
  dict(sec=5.0, step=0.9,
       items_ig=[T('옛 책은 두 불을\n어떻게 나눴을까요?', 92, bold=True, gap=34), T('자세한 이야기는\n@goyo_mio 피드 게시물에서', 56, bold=True, gap=30),
                 T('How did old texts tell the two fires apart?\nMore in our feed post', 40, EN, gap=0)],
       items_yt=[T('옛 책은 두 불을\n어떻게 나눴을까요?', 92, bold=True, gap=34), T('자세한 이야기는\n채널 게시물에서', 56, bold=True, gap=30),
                 T('How did old texts tell the two fires apart?\nMore in our Posts tab', 40, EN, gap=0)]),
  dict(sec=7.5, tag='지금 흐르는 소리',
       items_ig=[T('다섯 가지 고요', 60, bold=True, gap=10), T('정화 편', 100, bold=True, gap=36), T('『Lantern Room』', 56, gap=26),
                 T('음악은 프로필 링크에서', 48, GOLD, gap=30), T('Five Kinds of Quiet · 丁火 Yin Fire (Jeonghwa)\nLantern Room · Listen through the link in bio.', 36, EN, gap=0)],
       items_yt=[T('다섯 가지 고요', 60, bold=True, gap=10), T('정화 편', 100, bold=True, gap=36), T('『Lantern Room』', 56, gap=26),
                 T('음악은 아래 관련 영상', 48, GOLD, gap=30), T('Five Kinds of Quiet · 丁火 Yin Fire (Jeonghwa)\nLantern Room · Music: related video below', 36, EN, gap=0)]),
 ],
 caption="""빛에도 두 가지가 있어요.

병화는 하늘의 해예요. 사방을 고루, 멀리까지 비추는 빛이에요. 정화는 등불이에요. 가까운 자리를 오래 밝히는 빛이에요. 해는 멀리서 모두를 비추고, 등불은 가까이에서 한 사람의 얼굴과 손을 비춰요. 옛 명리 책 『적천수』는 병화를 두고 「세차고 사나워서 서리와 눈도 업신여긴다(丙火猛烈 欺霜侮雪)」고 했어요. 겨울 추위에도 기세가 꺾이지 않는 불이라는 뜻이에요. 같은 책은 정화를 두고 「부드럽고 치우치지 않으며 속은 환하게 밝다(丁火柔中 內性昭融)」, 「세져도 사납게 타지 않고 약해져도 다하지 않는다(旺而不烈 衰而不窮)」고 했어요. 등불이 오래 비추는 빛인 까닭이 여기 있어요. 1월 3일 진주 편에서 말한 등불(정화)과 강물(임수)의 짝도 이 책의 같은 대목(合壬而忠)에 나와요.

2026년의 빛이 해라면, 2027년의 빛은 등불이에요. 넓게 퍼지는 빛이 입춘부터 가까운 자리를 오래 밝히는 빛으로 옮겨 가요. 사주에서는 입춘(2월 4일)에 한 해가 바뀌어요.

1월 7일 고요의 그림 읽기에서 본 조르주 드 라 투르의 그림도 등불 하나를 그렸어요.

가까운 자리를 오래 밝히는 『다섯 가지 고요｜정화(丁火)』, 지금 고른 곡은 『Lantern Room』이에요. 프로필 링크에서 들을 수 있어요.

· English ·
There are two kinds of light.

丙火 Yang Fire (Byeonghwa) is the sun in the sky, lighting everything, far and wide. 丁火 Yin Fire (Jeonghwa) is a lamp that lights what is near, for a long time. The sun lights everyone from afar; a lamp lights one person's face and hands, up close. The old Saju classic Di Tian Sui (滴天髓) tells the two fires apart. Of Yang Fire: "fierce and blazing, it scorns frost and snow," a fire whose force holds even in winter. Of Yin Fire: "gentle and centered, bright within; strong, it does not rage; weak, it does not run out." That is why we call the lamp a lasting light. The lamp-and-river pair from our January 3 Jinju post, Yin Fire with 壬水 Yang Water (Imsu), comes from the same passage.

If 2026's light is the sun, 2027's is a lamp. From the start of spring, the wide light turns to a close, steady one. In Saju, the year turns at the start of spring (立春), February 4.

The Georges de La Tour painting in our January 7 post shows a single lamp.

From Five Kinds of Quiet · Yin Fire, today's track is Lantern Room. Listen through the link in bio.

#고요 #고요이야기 #정미년 #병화 #정화 #적천수 #사주 #오행음악 #saju #fiveelements""",
 reel_caption="""빛에도 두 가지가 있어요.

해(병화)는 넓게 멀리, 등불(정화)은 가까이 오래 비춰요. 2027년의 빛은 등불이에요. 옛 명리 책 『적천수』가 두 불을 어떻게 나눴는지는 피드 게시물에 있어요.

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
  S([T('가을이면\n진주 남강 위에\n등이 떠요.', 66, bold=True, gap=34), T('해마다 10월 초~중순, 진주성과 남강 일대.\n입장은 무료예요.', 40, gap=26),
     T('2026년은 10월 3일~18일, 낮 1시~밤 11시.\n2027년 일정은 아직 발표 전이에요.', 34, [150, 145, 135], gap=30),
     T('Every year in early to mid-October,\nlamps float on the Namgang River.\nEntry is free. In 2026: Oct 3–18, 1 to 11 p.m.', 32, EN, gap=0)], tag='강물 위에 등을 띄우는 축제'),
  S([T('임진왜란, 1592년 10월', 50, GOLD, gap=20), T('김시민 장군과 군사 약 3,800명이\n왜군 약 2만 명을 막아 낸\n진주성 전투예요.', 54, bold=True, gap=32),
     T('캄캄한 밤 남강에 등을 띄워\n강을 건너려는 적을 살피고 막았고,\n성 밖 가족에게 안부도 전했다고 해요.', 42, gap=34),
     T('October 1592: about 3,800 defenders under Kim Si-min\nheld Jinju Fortress against some 20,000 invaders.\nRiver lamps showed crossings and carried news out.', 30, EN, gap=0)], tag='시작은 진주대첩'),
  S([T('이듬해 1593년', 50, GOLD, gap=20), T('다시 쳐들어온 대군에\n성이 무너지고, 민관군\n7만여 명이 목숨을 잃었어요.', 54, bold=True, gap=32),
     T('그 뒤로 강에 띄우는 등에는\n그때 스러진 이들을\n기리는 뜻이 이어져 왔어요.', 44, gap=34),
     T('In 1593 the fortress fell, and some 70,000\nsoldiers and townspeople died.\nSince then, the lamps have also honored the dead.', 30, EN, gap=0)], tag='등불에 담긴 또 하나의 뜻'),
  S([T('축제 기간에는\n진주성이 무료로 열려요.', 58, bold=True, gap=30),
     T('성 안 남강 절벽 위 촉석루는\n우리나라 3대 누각으로 꼽혀요.', 44, gap=24),
     T('물에 띄운 다리(부교)로 강을 걸어서 건너고,\n소망등을 달 수 있어요(둘 다 유료).', 40, gap=34),
     T('During the festival, Jinju Fortress is free to enter. Chokseongnu Pavilion stands on a cliff above the river.\nCross on floating bridges, hang a wish lamp (both paid).', 30, EN, gap=0)], tag='갈 때 알아 둘 것'),
  S([T('축제가 아닐 때도\n유등을 볼 수 있어요.', 58, bold=True, gap=30),
     T('소망진산 유등테마공원은\n늘 열려 있고 무료예요.\n밤이면 유등에 불이 켜져요.', 44, gap=24),
     T('바로 옆 남강유등전시관은 월요일에 쉬고,\n겨울(12~2월)엔 저녁 6시까지 열어요.', 38, gap=34),
     T('Outside the festival, Somangjinsan Lantern Park\nis open year-round, free, and lit at night.\nThe lantern museum next door is closed Mondays\nand closes at 6 p.m. from December to February.', 30, EN, gap=0)], tag='겨울에 간다면'),
  S([T('다가오는 정미년의 첫 글자는\n가까운 곳을 오래 비추는 등불(정화).', 46, gap=30),
     T('옛 책은 등불(정화)과\n넓은 강물(임수)을\n서로 끌어당기는 짝으로 묶어요.', 56, bold=True, gap=30),
     T('그 짝이 한 장면에 담긴 곳이에요.', 44, gap=34),
     T('The first character of the coming Saju year\n(from Feb 4, 2027) is a lamp: 丁火 Yin Fire (Jeonghwa).\nOld Saju texts pair it with 壬水 Yang Water (Imsu),\na wide river. Here, the two share one scene.', 28, EN, gap=0)], tag='등불과 강물이 한 장면에'),
  S([T('다섯 가지 고요', 56, bold=True, gap=10), T('임수 편', 96, bold=True, gap=34),
     T('등불을 싣고 흐르는\n넓은 강물 같은 소리예요.', 52, gap=24), T('첫 곡은 『Wide Water』예요.', 44, gap=30),
     T('음악은 프로필 링크에서', 46, GOLD, gap=30),
     T('Five Kinds of Quiet · Yang Water.\nThe first track is Wide Water.\nListen through the link in bio.', 32, EN, gap=0)], tag='틀어 두기 좋은 소리'),
 ],
 reel=[
  dict(sec=4.5, instant=True, items=[T('1월 3일 · 갈 만한 곳', 50, GOLD, gap=34), T('강물 위의\n등불', 130, bold=True, gap=50), T('Lamps on the river', 42, EN, gap=0)]),
  dict(sec=6.0, step=1.0, items=[T('가을, 진주 남강에\n등이 떠요', 92, bold=True, gap=40), T('해마다 10월 초~중순', 60, gap=50), T('Jinju, every October', 40, EN, gap=0)]),
  dict(sec=6.5, step=1.0, items=[T('임진왜란 때\n강을 건너려는 적을 막고', 78, bold=True, gap=30), T('성 밖 가족에게\n안부를 전한 등불', 78, bold=True, gap=50),
       T('Lamps that helped hold back the enemy\nand carried word home', 40, EN, gap=0)]),
  dict(sec=5.0, step=0.9,
       items_ig=[T('왜 2027년에\n어울리는 곳일까요?', 92, bold=True, gap=34), T('자세한 이야기는\n@goyo_mio 피드 게시물에서', 56, bold=True, gap=30),
                 T('Why does it suit 2027?\nMore in our feed post', 40, EN, gap=0)],
       items_yt=[T('왜 2027년에\n어울리는 곳일까요?', 92, bold=True, gap=34), T('자세한 이야기는\n채널 게시물에서', 56, bold=True, gap=30),
                 T('Why does it suit 2027?\nMore in our Posts tab', 40, EN, gap=0)]),
  dict(sec=7.5, tag='지금 흐르는 소리',
       items_ig=[T('다섯 가지 고요', 60, bold=True, gap=10), T('임수 편', 100, bold=True, gap=36), T('첫 곡 『Wide Water』', 56, gap=26),
                 T('음악은 프로필 링크에서', 48, GOLD, gap=30), T('Five Kinds of Quiet · 壬水 Yang Water (Imsu)\nWide Water · Listen through the link in bio.', 36, EN, gap=0)],
       items_yt=[T('다섯 가지 고요', 60, bold=True, gap=10), T('임수 편', 100, bold=True, gap=36), T('첫 곡 『Wide Water』', 56, gap=26),
                 T('음악은 아래 관련 영상', 48, GOLD, gap=30), T('Five Kinds of Quiet · 壬水 Yang Water (Imsu)\nWide Water · Music: related video below', 36, EN, gap=0)]),
 ],
 caption="""강물 위의 등불, 진주 남강유등축제예요.

가을이면 경남 진주 남강 위에 수많은 등이 떠요. 해마다 10월 초~중순 진주성과 남강 일대에서 열리고, 입장은 무료예요. 2026년은 10월 3일부터 18일까지, 낮 1시부터 밤 11시까지였어요(유등 점등은 저녁부터). 2027년 날짜는 아직 발표 전이라 가기 전에 진주시 공지를 확인해 주세요.

시작은 1592년 10월 진주성 전투예요. 김시민 장군과 군사 약 3,800명이 왜군 약 2만 명을 막아 냈고, 캄캄한 밤 남강에 등을 띄워 강을 건너려는 적을 살피고 막았고, 성 밖 가족에게 안부도 전했다고 해요.

이듬해 1593년에는 다시 쳐들어온 대군에 성이 무너지고, 민관군 7만여 명이 목숨을 잃었어요. 그 뒤로 강에 띄우는 등에는 그때 스러진 이들을 기리는 뜻이 이어져 왔어요.

축제 기간에는 진주성이 무료로 열려요. 성 안 남강 절벽 위 촉석루는 우리나라 3대 누각으로 꼽히고, 물에 띄운 다리(부교)로 강을 걸어서 건너거나 소망등을 달 수 있어요(둘 다 유료). 축제가 아닐 때도 소망진산 유등테마공원은 늘 열려 있고 무료예요. 밤이면 유등에 불이 켜져요. 바로 옆 남강유등전시관은 월요일에 쉬고 겨울(12~2월)엔 저녁 6시까지 열어요.

다가오는 정미년(2027년 2월 4일 입춘부터)의 첫 글자는 가까운 곳을 오래 비추는 등불, 정화(丁火)예요. 옛 책은 등불(정화)과 넓은 강물(임수)을 서로 끌어당기는 짝으로 묶어요. 그 짝이 한 장면에 담긴 곳이라, 정미년에 한 번 가 볼 만한 곳으로 골랐어요.

등불을 싣고 흐르는 강물 같은 소리, 『다섯 가지 고요｜임수(壬水)』. 첫 곡은 『Wide Water』예요. 프로필 링크에서 들을 수 있어요.

· English ·
Lamps on the river: the Jinju Namgang Yudeung Festival.

Every fall, countless lamps float on the Namgang River in Jinju, Korea. The festival runs in early to mid-October around Jinju Fortress and the river, and entry is free. In 2026 it ran October 3 to 18, 1 to 11 p.m. The 2027 dates are not out yet, so check the city's notice before you go.

It began in October 1592, when about 3,800 defenders under Kim Si-min held Jinju Fortress against some 20,000 invaders. Lamps set afloat on the dark river, it is said, revealed enemy troops trying to cross, helped hold them back, and carried word to families outside the walls.

The next year, 1593, a larger army returned. The fortress fell, and some 70,000 soldiers and townspeople died. Since then, the river lamps have also honored the dead.

During the festival, the fortress is free to enter. Chokseongnu, the pavilion on a cliff above the river, is counted among Korea's three great pavilions. You can cross the river on floating bridges and hang a wish lamp (both paid). Outside the festival, Somangjinsan Lantern Park is open year-round, free, and lit at night; the lantern museum next door is closed on Mondays and closes at 6 p.m. from December to February.

The first character of the coming Saju year (from February 4, 2027) is a lamp: 丁火 Yin Fire (Jeonghwa). Old Saju texts pair it with 壬水 Yang Water (Imsu), a wide river. Here the two share one scene, so we picked it as a place to visit in 2027.

Music like a wide river carrying lamps: Five Kinds of Quiet · Yang Water. The first track is Wide Water. Listen through the link in bio.

#고요 #정미년 #진주남강유등축제 #진주 #유등 #진주성 #촉석루 #국내여행 #오행음악 #fiveelements""",
 reel_caption="""강물 위의 등불, 진주 남강유등축제예요.

가을이면 진주 남강에 등이 떠요. 임진왜란 진주성 전투 때 강을 건너려는 적을 막고 성 밖 가족에게 안부를 전한 등불에서 시작된 축제예요. 2027년에 어울리는 이유와 갈 때 알아 둘 것은 피드 게시물에 있어요.

지금 흐르는 음악은 『다섯 가지 고요｜임수(壬水)』의 첫 곡 『Wide Water』, 프로필 링크에서 들을 수 있어요.

· English ·
Lamps on the river: every fall in Jinju, Korea, lamps float on the Namgang River. The festival began with the 1592 Battle of Jinju, during the Imjin War, when river lamps held back the enemy and carried word to families. Why it suits 2027, and tips for visiting, are in our feed post.

The music is Wide Water from Five Kinds of Quiet · 壬水 Yang Water (Imsu). Listen through the link in bio.

#고요 #정미년 #진주남강유등축제 #유등 #오행음악""",
)

# ───────── 1/6 수 · 닮은 것 vs 식혀 주는 것 (계수) — 원문 Ⅳ, 결정 9·13 (분류 이름으로만, 판정 안 함)
P['0106v'] = dict(
 music='계수', audio='shorts/그림편/audio/계수_Drizzle_95s.m4a',
 slides=[
  S([T('1월 6일 · 고요 이야기', 44, GOLD, gap=30), T('닮은 것,\n식혀 주는 것', 104, bold=True, gap=36),
     T('2027년과 함께할 것을 고르는 두 갈래', 42, gap=30), T('Two ways to keep company with 2027', 38, EN, gap=0)]),
  S([T('2027년은\n등불이 늦여름의 마른 흙을\n데우는 해예요.', 60, bold=True, gap=34), T('2026년의 큰 불이 이어지는\n뜨겁고 마른 때예요.', 46, gap=26), T('사주로는 2월 4일 입춘부터 정미년이에요.', 36, GOLD, gap=34),
     T('2027: a lamp warming the dry earth of late summer. A hot, dry year that carries on from 2026. In Saju, 2027 begins on February 4.', 32, EN, gap=0)], tag='2027년은 어떤 해'),
  S([T('2027년의 모양을\n그대로 담은 것', 62, bold=True, gap=34), T('등불, 늦여름 들판,\n거둔 것을 품는 흙.', 52, gap=36),
     T('What echoes the year: a lamp, late-summer fields, earth that holds the harvest.', 32, EN, gap=0)], tag='닮은 것'),
  S([T('2027년의 열기 곁에 둘\n서늘한 것', 62, bold=True, gap=34), T('물,\n그리고 흙의 열을 받아\n흘려보내는 쇠와 바위.', 52, gap=36),
     T('What sits beside its heat: water, and metal and stone that take in the earth\'s warmth and let it go.', 32, EN, gap=0)], tag='식혀 주는 것'),
  S([T('불은 흙을 낳고,\n흙은 쇠를 낳아요.', 62, bold=True, gap=34), T('그래서 옛 책은\n불과 흙이 많아 덥고 마른 때에\n쇠와 물을 함께 봐요.', 46, gap=36),
     T('Fire feeds Earth, and Earth feeds Metal. In hot, dry times, old texts look to Metal and Water too.', 32, EN, gap=0)], tag='명리로 보면'),
  S([T('1~2월 고요에서 이어서 볼', 42, gap=10), T('닮은 것', 72, bold=True, gap=30),
     T('그림 · 등불 하나를 그린 라 투르,\n늦여름 건초더미를 그린 모네,\n이삭 줍는 들판을 그린 밀레', 40, gap=20),
     T('곳 · 지평선이 보이는 김제 들녘', 40, gap=20), T('곁에 둘 것 · 책상 위 등 하나, 흙 화분 하나', 40, gap=20),
     T('소리 · 정화 편, 토 편', 40, gap=34),
     T('Coming up, echoing the year: La Tour, Monet, Millet,\nthe fields of Gimje, a desk lamp, a clay pot,\nand 丁火 Yin Fire (Jeonghwa) and Earth music.', 30, EN, gap=0)], tag='시리즈 안내'),
  S([T('1~2월 고요에서 이어서 볼', 40, gap=8), T('식혀 주는 것', 68, bold=True, gap=26),
     T('그림 · 비 갠 인왕산 바위를 그린 정선,\n다리 위 소나기를 그린 히로시게', 38, gap=16),
     T('곳 · 서울 인왕산과 수성동 계곡', 38, gap=16), T('곁에 둘 것 · 유리 물병, 놋그릇, 처마 풍경(風磬)', 38, gap=16),
     T('소리 · 계수 편, 경금 편, 금 편, 수 편', 38, gap=20),
     T('둘이 한 장면에 있는 곳은\n1월 3일의 진주 남강유등이에요.', 38, GOLD, gap=24),
     T('Coming up, beside its heat: Jeong Seon, Hiroshige,\nInwangsan and its valley, a glass carafe, brassware,\na wind chime, and 癸水 Yin Water (Gyesu),\n庚金 Yang Metal (Gyeonggeum), Metal and Water music.\nThe two share one scene in Jinju (our Jan 3 post).', 30, EN, gap=0)], tag='시리즈 안내'),
  S([T('불과 물이 내 사주에\n얼마나 있는지는\n무료 앱에서 볼 수 있어요.', 54, gap=34), T('어느 쪽이 더 어울리는지는\n사주 전체를 봐야 알 수 있어요.', 52, bold=True, gap=36),
     T('Your chart\'s Fire and Water: see our free app.\nWhich side suits you depends on your whole chart.', 30, EN, gap=0)], tag='내게는 어느 쪽일까요'),
  S([T('다섯 가지 고요', 56, bold=True, gap=10), T('계수 편', 96, bold=True, gap=34),
     T('마른 흙에 조용히 스미는\n비 같은 소리예요.', 52, gap=24), T('첫 곡은 『Drizzle』이에요.', 44, gap=30),
     T('음악은 프로필 링크에서', 46, GOLD, gap=30),
     T('Five Kinds of Quiet · Yin Water.\nThe first track is Drizzle.\nListen through the link in bio.', 32, EN, gap=0)], tag='틀어 두기 좋은 소리'),
 ],
 reel=[
  dict(sec=4.5, instant=True, items=[T('1월 6일', 50, GOLD, gap=34), T('닮은 것,\n식혀 주는 것', 118, bold=True, gap=50), T('Two ways to keep company with 2027', 40, EN, gap=0)]),
  dict(sec=6.0, step=1.0, items=[T('2027년은', 70, gap=16), T('등불이\n마른 흙을 데우는 해', 92, bold=True, gap=50), T('A lamp warming dry earth', 40, EN, gap=0)]),
  dict(sec=7.0, step=1.0, items=[T('닮은 것', 80, bold=True, gap=10), T('등불 · 들판 · 흙', 64, gap=40), T('식혀 주는 것', 80, bold=True, gap=10), T('물 · 쇠 · 바위', 64, gap=50),
       T('What echoes it: lamp, fields, earth.\nWhat sits beside it: water, metal, stone.', 38, EN, gap=0)]),
  dict(sec=5.0, step=0.9,
       items_ig=[T('내게는\n어느 쪽일까요?', 96, bold=True, gap=34), T('자세한 이야기는\n@goyo_mio 피드 게시물에서', 56, bold=True, gap=30),
                 T('Which side suits you?\nMore in our feed post', 40, EN, gap=0)],
       items_yt=[T('내게는\n어느 쪽일까요?', 96, bold=True, gap=34), T('자세한 이야기는\n채널 게시물에서', 56, bold=True, gap=30),
                 T('Which side suits you?\nMore in our Posts tab', 40, EN, gap=0)]),
  dict(sec=7.5, tag='지금 흐르는 소리',
       items_ig=[T('다섯 가지 고요', 60, bold=True, gap=10), T('계수 편', 100, bold=True, gap=36), T('첫 곡 『Drizzle』', 56, gap=26),
                 T('음악은 프로필 링크에서', 48, GOLD, gap=30), T('Five Kinds of Quiet · 癸水 Yin Water (Gyesu)\nDrizzle · Listen through the link in bio.', 36, EN, gap=0)],
       items_yt=[T('다섯 가지 고요', 60, bold=True, gap=10), T('계수 편', 100, bold=True, gap=36), T('첫 곡 『Drizzle』', 56, gap=26),
                 T('음악은 아래 관련 영상', 48, GOLD, gap=30), T('Five Kinds of Quiet · 癸水 Yin Water (Gyesu)\nDrizzle · Music: related video below', 36, EN, gap=0)]),
 ],
 caption="""닮은 것, 식혀 주는 것.

2027년은 등불이 늦여름의 마른 흙을 데우는 해예요. 2026년의 큰 불이 이어지는 뜨겁고 마른 해라서, 2027년과 함께할 것을 두 갈래로 나눠 봤어요. 사주로는 2월 4일 입춘부터가 정미년이에요.

닮은 것은 2027년의 모양을 그대로 담은 것이에요. 등불, 늦여름 들판, 거둔 것을 품는 흙. 식혀 주는 것은 그 열기 곁에 둘 서늘한 것이에요. 물, 그리고 흙의 열을 받아 흘려보내는 쇠와 바위. 불은 흙을 낳고 흙은 쇠를 낳아서, 옛 책은 불과 흙이 많아 덥고 마른 때에 쇠와 물을 함께 봐요.

1~2월 고요에서는 두 갈래를 하나씩 이어서 볼 거예요. 닮은 것으로는 등불 하나를 그린 라 투르, 늦여름 건초더미를 그린 모네, 이삭 줍는 들판을 그린 밀레의 그림, 지평선이 보이는 김제 들녘, 책상 위 등 하나와 흙 화분 하나, 정화 편과 토 편의 소리가 있어요. 식혀 주는 것으로는 비 갠 인왕산 바위를 그린 정선과 다리 위 소나기를 그린 히로시게의 그림, 서울 인왕산과 수성동 계곡, 유리 물병과 놋그릇과 처마 풍경(風磬), 계수·경금·금·수 편의 소리가 있어요. 둘이 한 장면에 있는 곳은 1월 3일에 소개한 진주 남강유등이에요.

불과 물이 내 사주에 얼마나 있는지는 무료 앱에서 볼 수 있어요. 어느 쪽이 더 어울리는지는 사주 전체를 봐야 알 수 있어요. 앱은 프로필 링크에 있어요.

마른 흙에 조용히 스미는 비 같은 소리, 『다섯 가지 고요｜계수(癸水)』. 첫 곡은 『Drizzle』이에요. 프로필 링크에서 들을 수 있어요.

· English ·
What echoes 2027, and what sits beside its heat.

2027 is a lamp warming the dry earth of late summer, a hot, dry year that carries on from 2026's big fire. So we sorted what to keep close this year into two groups. In Saju, 2027 begins on February 4.

What echoes the year: a lamp, late-summer fields, earth that holds the harvest. What sits beside its heat: water, and metal and stone that take in the earth's warmth and let it go. Fire feeds Earth and Earth feeds Metal, so in hot, dry times the old texts look to Metal and Water too.

Over January and February we'll look at each side in turn. Echoing the year: La Tour's lamp, Monet's haystacks, Millet's gleaners, the open fields of Gimje, a desk lamp and a clay pot, and 丁火 Yin Fire (Jeonghwa) and Earth music. Beside its heat: Jeong Seon's Inwangsan after the rain, Hiroshige's sudden shower over a bridge, Inwangsan and its valley, a glass carafe, brassware and a wind chime, and Water and Metal music. The two share one scene at the Jinju lantern festival, from our January 3 post.

You can see how much Fire and Water your chart holds in our free app. Which side suits you better depends on your whole chart. The app is linked in our bio.

Music like rain soaking quietly into dry earth: Five Kinds of Quiet · 癸水 Yin Water (Gyesu). The first track is Drizzle. Listen through the link in bio.

#고요 #정미년 #2027년 #사주 #오행 #오행음악 #saju #fiveelements""",
 reel_caption="""닮은 것, 식혀 주는 것.

2027년은 등불이 마른 흙을 데우는 해예요. 그래서 함께할 것을 두 갈래로 나눴어요. 닮은 것은 등불·들판·흙, 식혀 주는 것은 물·쇠·바위. 이 시리즈에서 이어서 볼 그림·곳·소리와 어느 쪽이 내게 어울리는지에 대한 이야기는 피드 게시물에 있어요.

지금 흐르는 음악은 『다섯 가지 고요｜계수(癸水)』의 첫 곡 『Drizzle』, 프로필 링크에서 들을 수 있어요.

· English ·
2027 is a lamp warming dry earth, so we split what to keep close into two groups. What echoes it: lamp, fields, earth. What sits beside its heat: water, metal, stone. Our feed post lists the paintings, places and music coming up, and more on which side suits you.

The music is Drizzle from Five Kinds of Quiet · 癸水 Yin Water (Gyesu). Listen through the link in bio.

#고요 #정미년 #사주 #오행 #오행음악""",
)

P['0108'] = dict(
 music='토', audio='shorts/그림편/audio/토_Warm Soil_60s.m4a',
 slides=[
  S([T('1월 8일 · 고요 이야기', 44, GOLD, gap=30), T('등불의 소리,\n데워진 흙의 소리', 96, bold=True, gap=36),
     T('다가오는 해와 닮은 두 갈래', 44, gap=30), T('The sound of a lamp, the sound of warm earth', 36, EN, gap=0)]),
  S([T('입춘(2월 4일)부터 시작되는\n정미년은', 46, gap=28), T('등불이 늦여름의\n마른 흙을 데우는\n해예요.', 64, bold=True, gap=32),
     T('그 모양을 그대로 닮은 소리를\n두 갈래로 골랐어요.', 46, gap=34),
     T('The 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth\nbegins Feb 4. It\'s a lamp warming the dry earth\nof late summer, and here is music that echoes it.', 30, EN, gap=0)], tag='다가오는 해의 모양'),
  S([T('정화 편', 96, bold=True, gap=20), T('첫 곡 『Lamplit Keys』', 50, gap=34),
     T('해처럼 넓게 퍼지기보다\n가까운 곳을 오래 비추는\n등불의 소리예요.', 50, gap=30), T('정미년의 첫 글자, 정화 그대로예요.', 42, GOLD, gap=34),
     T('Five Kinds of Quiet · 丁火 Yin Fire (Jeonghwa),\nfirst track Lamplit Keys: the sound of a lamp\nthat lights what is near, for a long time.', 30, EN, gap=0)], tag='닮은 소리 하나 · 등불'),
  S([T('토 편', 96, bold=True, gap=20), T('첫 곡 『Warm Soil』', 50, gap=34),
     T('늦여름 햇볕에 데워진 마른 흙.\n느리고 담백하게 쌓이는\n로파이 리듬이 그 흙과 닮았어요.', 50, gap=34),
     T('Five Kinds of Quiet · Earth, first track Warm Soil.\nSlow, unfussy lo-fi beats that build in layers,\nlike earth warmed by the late-summer sun.', 30, EN, gap=0)], tag='닮은 소리 둘 · 데워진 흙'),
  S([T('토 편의 곡 이름에는\n흙과 불이 함께 있어요.', 56, bold=True, gap=34),
     T('『Warm Soil』 따뜻한 흙', 46, gap=18), T('『Hearth Light』 화로 불빛', 46, gap=18), T('『Quiet Harvest』 조용한 수확', 46, gap=34),
     T('데워진 흙, 거둔 것을 품는 흙.\n정미년의 흙 모양 그대로예요.', 44, GOLD, gap=34),
     T('Track names on the Earth album hold earth and fire\ntogether: Warm Soil, Hearth Light, Quiet Harvest.', 30, EN, gap=0)], tag='곡 이름에 담긴 것'),
  S([T('로파이(lo-fi)는\n일부러 살짝 바랜 듯한 따뜻한 질감을\n남겨 둔 소리예요.', 52, bold=True, gap=30),
     T('앞에 또렷이 나서기보다\n뒤에서 천천히 쌓여서,\n틀어 두고 일하거나 쉬기 좋아요.', 44, gap=30),
     T('흙 쪽에는 무토 편(집중할 때)과\n기토 편(쉬어 갈 때)도 있어요.', 42, GOLD, gap=34),
     T('Lo-fi keeps a faded, warm texture on purpose and stays\nin the background. For earth, there\'s also 戊土 Yang Earth\n(Muto) for focus and 己土 Yin Earth (Gito) for rest.', 28, EN, gap=0)], tag='로파이는 어떤 소리'),
  S([T('불과 물이 내 사주에\n얼마나 있는지는\n무료 앱에서 볼 수 있어요.', 52, gap=30), T('어느 쪽이 더 어울리는지는\n사주 전체를 봐야 알 수 있어요.', 50, bold=True, gap=30),
     T('1월 13일에는\n식혀 주는 소리로 이어 갈게요.', 42, GOLD, gap=34),
     T('Your chart\'s Fire and Water: see our free app.\nWhich side suits you depends on your whole chart.\nOn Jan 13: music from the cooling side.', 30, EN, gap=0)], tag='내게는 어느 쪽일까요'),
  S([T('다섯 가지 고요', 56, bold=True, gap=10), T('토 편', 96, bold=True, gap=34),
     T('늦여름 햇볕에 데워진\n흙 같은 소리예요.', 52, gap=24), T('첫 곡은 『Warm Soil』이에요.', 44, gap=30),
     T('음악은 프로필 링크에서', 46, GOLD, gap=30),
     T('Five Kinds of Quiet · Earth.\nThe first track is Warm Soil.\nListen through the link in bio.', 32, EN, gap=0)], tag='틀어 두기 좋은 소리'),
 ],
 reel=[
  dict(sec=4.5, instant=True, items=[T('1월 8일', 50, GOLD, gap=34), T('등불의 소리,\n데워진 흙의 소리', 100, bold=True, gap=50), T('The sound of a lamp,\nthe sound of warm earth', 40, EN, gap=0)]),
  dict(sec=6.0, step=1.0, items=[T('등불이\n마른 흙을 데우는 해', 88, bold=True, gap=40), T('입춘(2월 4일)부터', 56, gap=50), T('A lamp warming dry earth, from Feb 4', 40, EN, gap=0)]),
  dict(sec=7.0, step=1.0, items=[T('등불의 소리', 76, bold=True, gap=10), T('정화 편', 60, gap=40), T('데워진 흙의 소리', 76, bold=True, gap=10), T('토 편', 60, gap=50),
       T('Lamp: 丁火 Yin Fire (Jeonghwa)\nWarm earth: Five Kinds of Quiet · Earth', 36, EN, gap=0)]),
  dict(sec=5.5, step=0.9,
       items_ig=[T('곡 이름에 숨은\n흙과 불은?', 92, bold=True, gap=34), T('자세한 이야기는\n@goyo_mio 피드 게시물에서', 56, bold=True, gap=30),
                 T('Earth and fire hidden in the track names?\nMore in our feed post', 40, EN, gap=0)],
       items_yt=[T('곡 이름에 숨은\n흙과 불은?', 92, bold=True, gap=34), T('자세한 이야기는\n채널 게시물에서', 56, bold=True, gap=30),
                 T('Earth and fire hidden in the track names?\nMore in our Posts tab', 40, EN, gap=0)]),
  dict(sec=7.5, tag='지금 흐르는 소리',
       items_ig=[T('다섯 가지 고요', 60, bold=True, gap=10), T('토 편', 100, bold=True, gap=36), T('첫 곡 『Warm Soil』', 56, gap=26),
                 T('음악은 프로필 링크에서', 48, GOLD, gap=30), T('Five Kinds of Quiet · Earth\nWarm Soil · Listen through the link in bio.', 36, EN, gap=0)],
       items_yt=[T('다섯 가지 고요', 60, bold=True, gap=10), T('토 편', 100, bold=True, gap=36), T('첫 곡 『Warm Soil』', 56, gap=26),
                 T('음악은 아래 관련 영상', 48, GOLD, gap=30), T('Five Kinds of Quiet · Earth\nWarm Soil · Music: related video below', 36, EN, gap=0)]),
 ],
 caption="""등불의 소리, 데워진 흙의 소리.

입춘(2월 4일)부터 시작되는 정미년은 등불이 늦여름의 마른 흙을 데우는 해예요. 그 모양을 그대로 닮은 소리를 두 갈래로 골랐어요.

하나는 등불의 소리, 『다섯 가지 고요｜정화(丁火)』의 첫 곡 『Lamplit Keys』예요. 해처럼 넓게 퍼지기보다 가까운 곳을 오래 비추는 등불의 소리라서, 정미년의 첫 글자 정화 그대로예요.

다른 하나는 데워진 흙의 소리, 『다섯 가지 고요｜토(土)』예요. 느리고 담백하게 쌓이는 로파이 리듬이 늦여름 햇볕에 데워진 마른 흙과 닮았어요. 토 편의 곡 이름에는 흙과 불이 함께 있어요. 첫 곡 『Warm Soil』(따뜻한 흙), 『Hearth Light』(화로 불빛), 『Quiet Harvest』(조용한 수확). 데워진 흙, 거둔 것을 품는 흙이라 정미년의 흙 모양 그대로예요.

로파이(lo-fi)는 일부러 살짝 바랜 듯한 따뜻한 질감을 남겨 둔 소리예요. 앞에 또렷이 나서기보다 뒤에서 천천히 쌓여서 틀어 두고 일하거나 쉬기 좋아요. 흙 쪽에는 집중할 때 듣는 무토(戊土) 편과 쉬어 갈 때 듣는 기토(己土) 편도 있어요.

불과 물이 내 사주에 얼마나 있는지는 무료 앱에서 볼 수 있어요. 어느 쪽이 더 어울리는지는 사주 전체를 봐야 알 수 있어요. 앱은 프로필 링크에 있어요. 1월 13일에는 식혀 주는 소리로 이어 갈게요.

지금 흐르는 음악은 『다섯 가지 고요｜토(土)』의 첫 곡 『Warm Soil』이에요. 프로필 링크에서 들을 수 있어요.

· English ·
The sound of a lamp, the sound of warm earth.

The 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth begins at Ipchun (立春), the start of spring, on February 4. It is a lamp warming the dry earth of late summer, so we picked two kinds of music that echo it.

The sound of a lamp: Lamplit Keys, the first track of Five Kinds of Quiet · 丁火 Yin Fire (Jeonghwa). Rather than spreading wide like the sun, it lights what's close for a long time, just like Yin Fire, the year's first character.

The sound of warm earth: Five Kinds of Quiet · Earth, slow, unfussy lo-fi that builds in layers like earth warmed by the late-summer sun. Its track names hold earth and fire together: Warm Soil, Hearth Light, Quiet Harvest.

Lo-fi keeps a faded, warm texture on purpose and stays in the background, so it works well for focus or rest. For earth, there's also 戊土 Yang Earth (Muto) for focus and 己土 Yin Earth (Gito) for rest.

You can see how much Fire and Water your chart holds in our free app. Which side suits you depends on your whole chart. The app is linked in our bio. On January 13, we'll turn to the cooling side.

The music playing is Warm Soil, the first track of Five Kinds of Quiet · Earth. Listen through the link in bio.

#고요 #정미년 #오행음악 #로파이 #토 #정화 #사주 #saju #fiveelements #lofi""",
 reel_caption="""등불의 소리, 데워진 흙의 소리.

등불이 마른 흙을 데우는 정미년(입춘 2월 4일부터). 닮은 소리는 등불의 소리인 정화(丁火) 편과 데워진 흙의 소리인 토(土) 편이에요. 불과 물이 내 사주에 얼마나 있는지는 무료 앱에서 볼 수 있어요. 어느 쪽이 더 어울리는지는 사주 전체를 봐야 알 수 있어요. 곡 이름에 숨은 흙과 불, 로파이가 어떤 소리인지는 피드 게시물에 있어요.

지금 흐르는 음악은 『다섯 가지 고요｜토(土)』의 첫 곡 『Warm Soil』, 프로필 링크에서 들을 수 있어요.

· English ·
The coming year, from February 4, is a lamp warming dry earth. Two kinds of music echo it: 丁火 Yin Fire (Jeonghwa) for the lamp, and Five Kinds of Quiet · Earth for the warm soil. You can see how much Fire and Water your chart holds in our free app; which side suits you depends on your whole chart. More on the track names and lo-fi in our feed post.

The music is Warm Soil from Five Kinds of Quiet · Earth. Listen through the link in bio.

#고요 #정미년 #오행음악 #로파이 #saju""",
)

P['0110'] = dict(
 music='을목', audio='shorts/그림편/audio/을목_Morning Tendril_60s.m4a',
 slides=[
  S([T('1월 10일 · 고요 이야기', 44, GOLD, gap=30), T('넣어 두는\n흙', 116, bold=True, gap=36),
     T('늦여름 흙이 품고 있는 것', 44, gap=30), T('The earth that keeps', 38, EN, gap=0)]),
  S([T('미(未)는\n늦여름의 흙이에요.', 64, bold=True, gap=30),
     T('해마다 7월 초 소서부터\n8월 초 입추 전까지가 미의 달이에요.', 44, gap=26),
     T('한여름 열기가 남아\n아직 뜨겁고 말라 있어요.', 46, gap=34),
     T('未 Afternoon Earth (Mito) is late-summer earth.\nIts month runs from early July to early August,\nwhen the ground is still hot and dry.', 30, EN, gap=0)], tag='늦여름의 흙'),
  S([T('옛 책은 미(未) 안에', 46, gap=24), T('불씨(정화),\n덩굴 같은 나무(을목),\n흙(기토)이', 58, bold=True, gap=24),
     T('함께 들어 있다고 봐요.', 46, gap=26), T('未 · 丁 乙 己', 40, GOLD, gap=26),
     T('불이 데운 흙이\n나무를 품고 있는 모양이에요.', 44, gap=34),
     T('Old Saju texts see three things inside Afternoon Earth:\nan ember, a vine-like tree, and earth.\nFire-warmed earth holding a tree.', 30, EN, gap=0)], tag='흙 속에 든 것'),
  S([T('봄에 자란 나무의 기운이\n늦여름 흙으로 돌아와\n쌓이는 자리.', 56, bold=True, gap=30),
     T('그래서 옛 책은\n미(未)를 나무의 창고로 봐요.', 48, gap=34),
     T('Spring\'s growth returns to the late-summer earth\nand is stored there, so old texts call\nAfternoon Earth the storehouse of Wood.', 30, EN, gap=0)], tag='나무의 창고'),
  S([T('흙의 모양으로 보면\n다가오는 정미년은', 46, gap=24), T('새로 여는 해보다\n그동안 키운 것을\n조용히 넣어 두는\n해로 읽을 수 있어요.', 56, bold=True, gap=30),
     T('한 해가 내게 어떻게 닿는지는 사주마다 달라요.\n사주로는 2월 4일 입춘부터 정미년이에요.', 36, GOLD, gap=30),
     T('The coming year is the 丁未 year (Jeongmi) · Yin Fire ·\nAfternoon Earth. We read it as a year to quietly keep\nwhat you\'ve grown. How it touches you depends\non your own Saju. It begins on Feb 4.', 30, EN, gap=0)], tag='넣어 두는 해'),
  S([T('미토는\n나무를 품어 두는 흙이에요.', 56, bold=True, gap=30),
     T('옹기나 토분에\n작은 식물 하나를\n곁에 두어도 좋아요.', 50, gap=30),
     T('곁에 둘 것은 1월 31일에 더 이어 갈게요.', 38, GOLD, gap=34),
     T('Afternoon Earth holds a tree. A small plant in an onggi\ncrock or a terracotta pot is a nice thing to keep nearby.\nMore on things to keep close on Jan 31.', 30, EN, gap=0)], tag='곁에 두기'),
  S([T('흙이 품어 두는 나무는\n덩굴처럼 휘어 자라는\n을목이에요.', 56, bold=True, gap=30),
     T('을목 편 첫 곡 『Morning Tendril』은\n아침의 덩굴손이라는 뜻이에요.', 44, gap=34),
     T('The tree the earth keeps is 乙木 Yin Wood (Eulmok),\nwhich bends and climbs like a vine. Our Yin Wood\nalbum opens with Morning Tendril, named for\na vine\'s curling shoot.', 30, EN, gap=0)], tag='왜 을목 편'),
  S([T('다섯 가지 고요', 56, bold=True, gap=10), T('을목 편', 96, bold=True, gap=34),
     T('흙에 기대어 천천히 감아 오르는\n덩굴 같은 소리예요.', 50, gap=24), T('첫 곡은 『Morning Tendril』이에요.', 44, gap=30),
     T('음악은 프로필 링크에서', 46, GOLD, gap=30),
     T('Five Kinds of Quiet · Yin Wood.\nThe first track is Morning Tendril.\nListen through the link in bio.', 32, EN, gap=0)], tag='틀어 두기 좋은 소리'),
 ],
 reel=[
  dict(sec=4.5, instant=True, items=[T('1월 10일', 50, GOLD, gap=34), T('넣어 두는\n흙', 130, bold=True, gap=50), T('The earth that keeps', 42, EN, gap=0)]),
  dict(sec=6.0, step=1.0, items=[T('미(未)는', 70, gap=16), T('늦여름의\n마른 흙', 100, bold=True, gap=50), T('未 Afternoon Earth (Mito):\ndry, late-summer earth', 38, EN, gap=0)]),
  dict(sec=6.5, step=1.0, items=[T('그 흙 안에', 70, gap=16), T('덩굴 같은 나무가\n들어 있다고 봐요', 88, bold=True, gap=50), T('Inside it: a vine-like tree', 40, EN, gap=0)]),
  dict(sec=5.5, step=0.9,
       items_ig=[T('왜 나무의\n창고일까요?', 96, bold=True, gap=34), T('자세한 이야기는\n@goyo_mio 피드 게시물에서', 56, bold=True, gap=30),
                 T('Why a storehouse of Wood?\nMore in our feed post', 40, EN, gap=0)],
       items_yt=[T('왜 나무의\n창고일까요?', 96, bold=True, gap=34), T('자세한 이야기는\n채널 게시물에서', 56, bold=True, gap=30),
                 T('Why a storehouse of Wood?\nMore in our Posts tab', 40, EN, gap=0)]),
  dict(sec=7.5, tag='지금 흐르는 소리',
       items_ig=[T('다섯 가지 고요', 60, bold=True, gap=10), T('을목 편', 100, bold=True, gap=36), T('첫 곡 『Morning Tendril』', 56, gap=26),
                 T('음악은 프로필 링크에서', 48, GOLD, gap=30), T('Five Kinds of Quiet · 乙木 Yin Wood (Eulmok)\nMorning Tendril · Listen through the link in bio.', 34, EN, gap=0)],
       items_yt=[T('다섯 가지 고요', 60, bold=True, gap=10), T('을목 편', 100, bold=True, gap=36), T('첫 곡 『Morning Tendril』', 56, gap=26),
                 T('음악은 아래 관련 영상', 48, GOLD, gap=30), T('Five Kinds of Quiet · 乙木 Yin Wood (Eulmok)\nMorning Tendril · Music: related video below', 34, EN, gap=0)]),
 ],
 caption="""넣어 두는 흙.

미(未)는 늦여름의 흙이에요. 해마다 7월 초 소서부터 8월 초 입추 전까지가 미의 달이고, 한여름 열기가 남아 아직 뜨겁고 말라 있어요.

옛 책은 미 안에 불씨(정화), 덩굴 같은 나무(을목), 흙(기토)이 함께 들어 있다고 봐요. 불이 데운 흙이 나무를 품고 있는 모양이에요. 봄에 자란 나무의 기운이 늦여름 흙으로 돌아와 쌓이는 자리라서, 옛 책은 미를 나무의 창고로 봐요.

흙의 모양으로 보면, 다가오는 정미년은 새로 여는 해보다 그동안 키운 것을 조용히 넣어 두는 해로 읽을 수 있어요. 한 해가 내게 어떻게 닿는지는 사주마다 달라요. 사주로는 2월 4일 입춘부터 정미년이에요.

미토는 나무를 품어 두는 흙이에요. 옹기나 토분에 작은 식물 하나를 곁에 두어도 좋아요. 불과 물이 내 사주에 얼마나 있는지는 무료 앱에서 볼 수 있어요. 어느 쪽이 더 어울리는지는 사주 전체를 봐야 알 수 있어요. 곁에 둘 것은 1월 31일에 더 이어 갈게요.

흙이 품어 두는 나무는 덩굴처럼 휘어 자라는 을목이에요. 흙에 기대어 천천히 감아 오르는 덩굴 같은 소리, 『다섯 가지 고요｜을목(乙木)』의 첫 곡 『Morning Tendril』(아침의 덩굴손)이에요. 프로필 링크에서 들을 수 있어요.

· English ·
The earth that keeps.

未 Afternoon Earth (Mito) is late-summer earth. Its month runs from early July to early August, when the ground is still hot and dry.

Old Saju texts see three things inside it: an ember, a vine-like tree, and earth. It is fire-warmed earth holding a tree. Spring's growth returns to the late-summer earth and is stored there, so old texts call Afternoon Earth the storehouse of Wood.

The coming year is the 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth. Seen through its earth, we read it less as a year to open new things and more as one to quietly keep what you have grown. How a year touches you depends on your own Saju. It begins on February 4.

Afternoon Earth holds a tree. A small plant in an onggi crock or a terracotta pot is a nice thing to keep nearby. You can see how much Fire and Water your chart holds in our free app; which side suits you depends on your whole chart. We'll say more about things to keep close on January 31.

The tree the earth keeps is 乙木 Yin Wood (Eulmok), which bends and climbs like a vine. Music like a vine slowly winding up, leaning on the earth: Morning Tendril, the first track of Five Kinds of Quiet · Yin Wood. Listen through the link in bio.

#고요 #정미년 #미토 #을목 #사주 #오행 #오행음악 #saju #fiveelements""",
 reel_caption="""넣어 두는 흙.

미(未)는 늦여름의 마른 흙이고, 그 안에 덩굴 같은 나무(을목)가 들어 있다고 봐요. 옛 책이 왜 미를 나무의 창고로 보는지, 다가오는 정미년을 어떻게 읽는지는 피드 게시물에 있어요.

지금 흐르는 음악은 『다섯 가지 고요｜을목(乙木)』의 첫 곡 『Morning Tendril』, 프로필 링크에서 들을 수 있어요.

· English ·
未 Afternoon Earth (Mito) is dry, late-summer earth, and old Saju texts see a vine-like tree inside it. Our feed post explains why it is called the storehouse of Wood, and what that means for the coming year.

The music is Morning Tendril from Five Kinds of Quiet · 乙木 Yin Wood (Eulmok). Listen through the link in bio.

#고요 #정미년 #을목 #사주 #오행음악""",
)

P['0111'] = dict(
 music='임수',
 slides=[
  S([T('1월 11일 · 고요 이야기', 44, GOLD, gap=30), T('하늘의\n물', 120, bold=True, gap=36),
     T('두 해가 함께 받은 옛 이름', 44, gap=30), T('Water from the sky', 38, EN, gap=0)]),
  S([T('옛사람들은\n예순 개의 해 이름을\n둘씩 묶어', 58, bold=True, gap=26),
     T('한 쌍마다 이름을 하나씩 붙였어요.\n모두 서른 가지, 쇠·나무·물·불·흙의\n모습을 빌린 이름이에요.', 42, gap=34),
     T('Long ago, the sixty year-names were paired two by two,\nand each pair was given a name drawn from\nmetal, wood, water, fire or earth.', 30, EN, gap=0)], tag='해 이름에 붙은 또 하나의 이름'),
  S([T('병오(2026)와 정미(2027)는\n한 쌍이에요.', 56, bold=True, gap=30),
     T('둘이 함께 받은 이름은', 46, gap=20), T('천하수, 하늘의 물', 64, bold=True, gap=26),
     T('丙午 · 丁未  天河水', 40, GOLD, gap=34),
     T('2026, the 丙午 year (Byeong-o) · Yang Fire · Noon Fire,\nand 2027, the 丁未 year (Jeongmi)\n· Yin Fire · Afternoon Earth,\nshare one name: Cheonhasu, water from the sky.', 28, EN, gap=0)], tag='2026과 2027'),
  S([T('하늘의 물은\n더위가 만든 비예요.', 60, bold=True, gap=30),
     T('한여름 달궈진 땅에서\n더운 공기가 올라가 구름이 되고,\n그 구름이 소나기로 쏟아져요.', 46, gap=26),
     T('미(未)의 달, 7월 초~8월 초는\n장마와 소나기가 몰리는 때이기도 해요.', 40, GOLD, gap=34),
     T('Water from the sky is rain made by heat. Air rising\nfrom sun-baked ground forms clouds that break into\nsudden showers. The month of 未 Afternoon Earth (Mito),\nearly July to early August, is also monsoon season.', 28, EN, gap=0)], tag='하늘의 물이란'),
  S([T('가장 뜨거운 여름의 두 해에\n물의 이름이 붙은 건,', 50, gap=22),
     T('열이 끝까지 차오르면\n비로 내려오기 때문이라고\n읽을 수 있어요.', 58, bold=True, gap=30),
     T('그래도 두 해의 글자는 모두 불과 흙이라,\n물의 해라는 뜻은 아니에요.\n옛 이름 하나로만 봐요.', 40, gap=34),
     T('Two years of high and late summer carry a water name,\nperhaps because heat, once it peaks, comes down as rain.\nTheir characters are still fire and earth, so this is not\na year of water. We keep it as an old name only.', 28, EN, gap=0)], tag='불의 해에 붙은 물의 이름'),
  S([T('더위 끝의 소나기를\n그림으로 본다면', 58, bold=True, gap=30),
     T('다리 위로 갑자기 쏟아지는 비,\n히로시게의 「오하시 다리의 소나기」예요.', 44, gap=26),
     T('2월 4일 그림 읽기에서 이어 갈게요.', 42, GOLD, gap=34),
     T('Such a shower in a painting: Hiroshige\'s\nSudden Shower over Shin-Ōhashi Bridge and Atake.\nMore in our Feb 4 painting post.', 30, EN, gap=0)], tag='그림으로 본다면'),
  S([T('다섯 가지 고요', 56, bold=True, gap=10), T('임수 편', 96, bold=True, gap=34),
     T('넓게 고여 천천히 흐르는\n큰 물 같은 소리예요.', 52, gap=24), T('오늘은 『Morning Haze』를 골랐어요.', 42, gap=30),
     T('음악은 프로필 링크에서', 46, GOLD, gap=30),
     T('Five Kinds of Quiet · 壬水 Yang Water (Imsu).\nToday\'s pick: Morning Haze.\nListen through the link in bio.', 32, EN, gap=0)], tag='틀어 두기 좋은 소리'),
 ],
 caption="""하늘의 물.

옛사람들은 예순 개의 해 이름을 둘씩 묶고, 한 쌍마다 이름을 하나씩 붙였어요. 모두 서른 가지, 쇠·나무·물·불·흙의 모습을 빌린 이름이에요.

병오(2026)와 정미(2027)는 한 쌍이에요. 둘이 함께 받은 이름은 천하수(天河水), 하늘의 물이에요.

하늘의 물은 더위가 만든 비예요. 한여름 달궈진 땅에서 더운 공기가 올라가 구름이 되고, 그 구름이 소나기로 쏟아져요. 미(未)의 달인 7월 초부터 8월 초까지는 장마와 소나기가 몰리는 때이기도 해요. 가장 뜨거운 여름의 두 해에 물의 이름이 붙은 건, 열이 끝까지 차오르면 비로 내려오기 때문이라고 읽을 수 있어요. 그래도 두 해의 글자는 모두 불과 흙이라, 물의 해라는 뜻은 아니에요. 옛 이름 하나로만 봐요. 사주로는 2월 4일 입춘부터 정미년이에요.

더위 끝의 소나기를 그림으로 본다면, 다리 위로 갑자기 쏟아지는 비를 그린 히로시게의 「오하시 다리의 소나기」예요. 2월 4일 그림 읽기에서 이어 갈게요.

넓게 고여 천천히 흐르는 큰 물 같은 소리, 『다섯 가지 고요｜임수(壬水)』. 오늘은 『Morning Haze』를 골랐어요. 프로필 링크에서 들을 수 있어요.

· English ·
Water from the sky.

Long ago, the sixty year-names were paired two by two, and each pair was given a name drawn from metal, wood, water, fire or earth.

2026, the 丙午 year (Byeong-o) · Yang Fire · Noon Fire, and 2027, the 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth, are one such pair. Their shared name is 天河水 Water from the Sky (Cheonhasu).

Water from the sky is rain made by heat. Air rising from sun-baked ground forms clouds that break into sudden showers, and the month of 未 Afternoon Earth (Mito), early July to early August, is also monsoon season. Two years of high and late summer may carry a water name because heat, once it peaks, comes down as rain. Their characters are still fire and earth, so this is not a year of water; we keep it as an old name only. In Saju, the 丁未 year begins on February 4.

Seen in a painting, a summer shower like that looks like Hiroshige's Sudden Shower over Shin-Ōhashi Bridge and Atake (1857). More in our February 4 painting post.

Music like wide, slow water: Five Kinds of Quiet · 壬水 Yang Water (Imsu). Today's pick is Morning Haze. Listen through the link in bio.

#고요 #정미년 #병오년 #천하수 #하늘의물 #사주 #오행음악 #saju #fiveelements""",
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

DATES = {'0101': '2027-01-01', '0103': '2027-01-20', '0104': '2027-01-04', '0106': '2027-01-17', '0107': '2027-01-07', '0103j': '2027-01-03', '0106v': '2027-01-06', '0108': '2027-01-08', '0110': '2027-01-10', '0111': '2027-01-11'}
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
