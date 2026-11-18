import asyncio, base64, os, sys
src = open('/home/claude/goyo/make_slides.py').read().split('post1 = [')[0]
src=src.replace('position:relative}','position:relative;word-break:keep-all;overflow-wrap:break-word}',1)
exec(src)
OUT = '/home/claude/week3/out'; os.makedirs(OUT, exist_ok=True)
b64 = lambda p: 'data:image/jpeg;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
E = lambda e, t=None: f'<span style="{tc(e)}">{t or e}</span>'
P = 'style="font-size:42px;line-height:1.65"'
SM = 'style="font-size:30px;color:#9a9a9a;margin-top:26px;line-height:1.6"'
MUSIC = lambda title, body, link='프로필 링크에서 들을 수 있어요.': (
    '<div class="step">틀어 두기 좋은 소리</div><div class="rule"></div>'
    f'<h1 style="font-size:100px">고요<br>{title} 편</h1><br><p>{body}</p><br><p>{link}</p>', "")
def bg(img, text, h=620):
    return (f'<div style="position:absolute;inset:0;background:url({img}) center/cover"></div>'
            f'<div style="position:absolute;left:0;right:0;bottom:0;height:{h}px;background:linear-gradient(transparent,rgba(0,0,0,.93))"></div>'
            f'<div style="position:absolute;left:96px;right:96px;bottom:150px">{text}</div>')

# ── 11/23 월 · 하원 · 이번 주 기운
DAYS = [('월', '신', '축', '금'), ('화', '임', '인', '수'), ('수', '계', '묘', '수'), ('목', '갑', '진', '목'),
        ('금', '을', '사', '목'), ('토', '병', '오', '화'), ('일', '정', '미', '화')]
dayrows = ''.join(f'<tr><th style="text-align:left;width:120px">{d}</th><td style="font-size:56px;width:auto;text-align:left;padding:2px 0">'
                  f'<span style="{tc(e)}">{g}</span>{z}</td></tr>' for d, g, z, e in DAYS)
mon = [
 ('<div class="step">11월 23일 · 음력 10월 15일</div><div class="rule"></div>'
  '<h1 style="font-size:120px">상달의<br>보름</h1><p class="sub">이번 주 기운</p>', SWIPE),
 ('<div class="step">일 년에 보름이 세 번</div><div class="rule"></div>'
  f'<p {P}>옛사람들은 세 번의 보름을<br>특별히 여겼어요.</p><br>'
  '<h2 style="font-size:60px;line-height:1.7">정월 대보름 · 상원(上元)<br>칠월 백중 · 중원(中元)<br>시월 보름 · 하원(下元)</h2><br>'
  '<p>셋을 묶어 삼원(三元)이라 불렀고,<br>오늘이 그 마지막, 하원이에요.</p>', ""),
 ('<div class="step">열두 달 가운데 으뜸</div><div class="rule"></div>'
  '<h1 style="font-size:120px">상달<br>上月</h1><br>'
  f'<p {P}>음력 10월은 농사를 마치고<br>햇곡식으로 시루떡을 쪄서<br>집집마다 고사를 지내던 달이에요.<br>그래서 열두 달 중 으뜸이라는 뜻으로<br>"상달"이라 불렀어요.</p>', ""),
 ('<div class="step">개천절도 원래 이 달이었어요</div><div class="rule"></div>'
  f'<p {P}>고구려의 동맹, 동예의 무천,<br>하늘에 올리던 이 큰 제사들은<br>모두 10월에 열렸어요.</p><br>'
  '<h2 style="font-size:60px">개천절도 원래<br>음력 10월 3일이었어요.</h2><br>'
  f'<p {P}>1949년 국경일 법을 만들면서<br>지금의 양력 10월 3일이 됐어요.</p>', ""),
 ('<div class="step">이번 주 일진</div><div class="rule" style="margin:28px 0"></div>'
  f'<table style="margin:0">{dayrows}</table>'
  f'<p style="font-size:38px;line-height:1.6;margin-top:28px">천간이 {E("금")} → {E("수")} → {E("목")} → {E("화")}로 흘러요.<br>열 개의 천간은 원래 상생 순서로 줄 서 있거든요.</p>'
  f'<p {SM}>토요일은 병오일, 올해(병오년)와 같은 기둥이에요.<br>이번 달은 기해월이에요. 왜 "기"인지는 금요일에.</p>', ""),
 MUSIC(E('수', '계수(癸水)'), '보름밤, 이슬처럼 잔잔한 소리.<br>하루를 닫는 밤에 틀어 두기 좋아요.'),
]
mon_cap = ("오늘은 음력 10월 15일, 하원(下元)이에요.\n\n"
 "정월 대보름(상원), 칠월 백중(중원)과 함께 옛사람들이 특별히 여긴 세 보름, 삼원(三元)의 마지막이에요. "
 "음력 10월은 농사를 마치고 햇곡식으로 고사를 지내던 달이라 열두 달 중 으뜸, \"상달\"이라 불렀어요. "
 "고구려의 동맹, 동예의 무천도 10월 제사였고, 개천절도 원래 음력 10월 3일이었다가 1949년에 양력이 됐어요.\n\n"
 "이번 주 일진은 신축 → 임인 → 계묘 → 갑진 → 을사 → 병오 → 정미. 천간이 금 → 수 → 목 → 화, 상생 순서로 흘러가요.\n\n"
 "보름밤엔 『다섯 가지 고요｜계수(癸水)』. 프로필 링크에서 들을 수 있어요.\n\n"
 "#고요 #이번주기운 #상달 #하원 #일진 #오행 #사주 #절기")

# ── 11/25 수 · 고요의 이야기 #1 이름
row = lambda L, w, h, e=None: (f'<div class="row" style="margin:30px 0"><span class="el logo" style="width:110px;font-size:80px;color:#c4a066">{L}</span>'
                               f'<span class="tx" style="font-size:64px;font-weight:700">{w}</span><span class="tx" style="font-size:40px;margin-left:24px;color:#9a9a9a">{h}</span></div>')
wed = [
 ('<div class="step">고요의 이야기 #1</div><div class="rule"></div>'
  '<h1 style="font-size:104px">고요라는<br>이름에 숨긴<br>네 단어</h1><p class="sub">처음 꺼내는 이야기</p>', SWIPE),
 ('<div class="step">사실 GOYO는 줄임말이에요</div><div class="rule"></div>'
  + row('G', '고요', '') + row('O', '온기', '溫氣') + row('Y', '여운', '餘韻') + row('O', '오행', '五行') +
  f'<br><p {P}>유치한가 싶어서<br>한 번도 말한 적이 없어요.</p>', ""),
 ('<div class="step">G · 고요</div><div class="rule"></div>'
  '<h2>고요는 한자가 없는<br>순우리말이에요.</h2><br>'
  f'<p {P}>조용하다는 말과 조금 달라요.<br>소리가 없어서가 아니라<br>마음이 가라앉아서 고요해요.<br>음악이 흐르는데도 고요할 수 있어요.</p>', ""),
 ('<div class="step">O · 온기</div><div class="rule"></div>'
  '<h2 style="font-size:60px">차갑게 비어 있는 고요 말고,<br>곁에 누가 있는 고요.</h2><br>'
  f'<p {P}>온기(溫氣)는 따뜻한 기운이에요.<br>혼자 듣는 음악이어도<br>혼자인 느낌은 들지 않았으면 해요.</p>', ""),
 ('<div class="step">Y · 여운</div><div class="rule"></div>'
  '<h1 style="font-size:120px">餘韻</h1><br>'
  f'<p {P}>남을 여(餘), 운 운(韻), 곧 울림.<br>소리가 그친 뒤에도<br>남아 있는 울림이라는 뜻이에요.</p><br>'
  '<h2 style="font-size:58px">곡이 끝나도<br>방 안에 남는 것.</h2>', ""),
 ('<div class="step">O · 오행</div><div class="rule"></div>'
  f'<h1 style="font-size:96px">{E("목")} {E("화")} {E("토")} {E("금")} {E("수")}</h1><br>'
  f'<p {P}>그리고 이 모든 걸<br>다섯 갈래로 나눠 담는 틀이 오행이에요.</p><br>'
  '<h2 style="font-size:58px">고요, 온기, 여운, 오행.<br>제가 만들고 싶은 소리예요.</h2><br>'
  '<p>프로필 링크 → GOYO</p>', ""),
]
wed_cap = ("GOYO는 사실 줄임말이에요.\n\n"
 "고요, 온기(溫氣), 여운(餘韻), 오행(五行). 유치한가 싶어서 한 번도 말한 적이 없어요.\n"
 "고요는 한자가 없는 순우리말이고, 여운은 남을 여(餘)에 운 운(韻), 곧 소리가 그친 뒤에도 남는 울림이라는 뜻이에요. "
 "곡이 끝나도 방 안에 남는 것, 혼자 들어도 혼자인 느낌이 들지 않는 것. 그걸 다섯 갈래의 오행으로 나눠 담고 있어요.\n\n"
 "고요의 이야기, 매주 수요일에 하나씩 꺼낼게요.\n\n"
 "#고요 #고요의이야기 #GOYO #오행음악 #플레이리스트 #브랜드이야기")

# ── 11/26 목 · 고요의 그림 읽기 #2 세한도
SP = b64('se_paint.jpg'); SPN = b64('se_pine.jpg'); ST = b64('se_title.jpg')
CR = '<p style="font-size:30px;color:#9a9a9a;margin-top:34px;line-height:1.6">김정희, 〈세한도(歲寒圖)〉 1844 · 국보<br>국립중앙박물관 · 이미지 위키미디어 공용(퍼블릭 도메인)</p>'
thu = [
 ('<div class="step">고요의 그림 읽기 #2</div><div class="rule" style="margin-bottom:40px"></div>'
  f'<img src="{SP}" style="width:100%;display:block">' + CR, SWIPE),
 (bg(SPN, '<h2 style="font-size:66px;line-height:1.5">날이 추워진 뒤에야<br>안다.</h2>'), ""),
 ('<div class="step">제주, 유배 5년째</div><div class="rule"></div>'
  f'<p {P}>1844년, 김정희는 제주에 유배된 지<br>5년째였어요. 권세를 잃은 그에게<br>제자인 역관 이상적이<br>북경에서 120권짜리 책을 구해<br>바다 건너 보내 줬어요.</p><br>'
  '<h2>이 그림은<br>그 답례예요.</h2>', ""),
 ('<div class="step">제목은 논어에서</div><div class="rule"></div>'
  '<h2 style="font-size:54px;line-height:1.6">歲寒然後<br>知松柏之後凋也</h2><br>'
  f'<p {P}>"날이 추워진 뒤에야 소나무와 잣나무가<br>늦게 시든다는 걸 안다."<br>어려울 때도 변하지 않은 제자를<br>그 나무에 빗댔어요.</p>'
  f'<img src="{ST}" style="height:250px;display:block;margin-top:34px">'
  f'<p {SM}>제목 옆 "우선시상(藕船是賞)"<br>우선(이상적의 호)이 보라고 그린 그림이라는 뜻이에요.</p>', ""),
 ('<div class="step">23센티 그림, 14미터 두루마리</div><div class="rule"></div>'
  f'<p {P}>그림 자체는 세로 23cm, 가로 69cm.<br>이상적이 이듬해 정월 북경에서<br>청나라 문인 16명의 감상글을 받았고,<br>뒤에 오세창·정인보 등의 글이 더해져<br>지금은 14m에 이르는 두루마리예요.</p><br>'
  '<h2 style="font-size:58px">그림 오른쪽 아래 도장,<br>장무상망(長毋相忘).<br>"오래도록 서로 잊지 말자."</h2>', ""),
 ('<div class="step">바다를 건너갔다 돌아온 그림</div><div class="rule"></div>'
  f'<p {P}>일제강점기에 일본인 학자<br>후지쓰카 지카시의 손에 들어가<br>일본으로 건너갔어요.</p><br>'
  f'<p {P}>1944년 서예가 손재형이 찾아가<br>두 달 동안 설득한 끝에 되찾아 왔고,<br>2020년 손창근 선생이<br>국립중앙박물관에 기증했어요.</p>', ""),
 (f'<div class="step">고요의 그림 읽기 · {E("목","목(木)")}</div><div class="rule"></div>'
  f'<p style="font-size:38px;line-height:1.7"><b>보이는 것</b><br>한겨울, 위로 곧게 선 나무 네 그루 → {E("목")}<br><br>'
  f'<b>그리는 방식</b><br>물기를 뺀 마른 붓(갈필), 깎아 낸 듯한 선 → {E("금")}<br><br>'
  f'<b>화가의 사주</b><br>1786년 음력 6월 3일생<br>병오년 갑오월 을해일, 일간 {E("목","을목(乙木)")}</p>'
  '<p style="font-size:30px;color:#9a9a9a;margin-top:22px;line-height:1.6">목을 금의 방식으로 그렸어요. 금은 목을 다듬는 기운이라<br>시련에 깎이고도 서 있는 나무로 읽혀요.<br>한여름에 태어난 을목이 그린 한겨울 나무예요.<br>공교롭게 올해와 같은 병오년생이에요.<br>태어난 시는 기록이 없어 일주까지만 봤어요. 제 해석이에요.</p>', ""),
 MUSIC(E('목', '갑목(甲木)'), '곧게 선 큰 나무 같은 소리.<br>찬 아침, 마음을 다잡고 싶을 때<br>틀어 두기 좋아요.'),
]
thu_cap = ("고요의 그림 읽기 #2 · 김정희 〈세한도〉\n\n"
 "1844년, 제주 유배 5년째의 김정희는 북경에서 120권짜리 책을 구해 보내 준 제자 이상적에게 이 그림을 그려 줬어요. "
 "제목은 논어의 \"날이 추워진 뒤에야 소나무와 잣나무가 늦게 시든다는 걸 안다\"에서 왔어요. "
 "그림은 가로 69cm지만, 청나라 문인 16명과 오세창·정인보 등의 글이 더해져 지금은 14m에 이르는 두루마리예요. "
 "일본으로 건너갔다가 1944년 손재형이 되찾아 왔고, 2020년 국립중앙박물관에 기증됐어요.\n\n"
 "고요의 읽기로는 목(木). 겨울의 나무를, 물기를 뺀 마른 붓으로 깎듯이 그렸어요. 화가의 일간도 을목이에요.\n\n"
 "이 그림 옆에는 『다섯 가지 고요｜갑목(甲木)』. 프로필 링크에서 들을 수 있어요.\n\n"
 "#고요 #고요의그림읽기 #세한도 #김정희 #추사 #국보 #오행 #명화")

# ── 11/27 금 · 기해월 · 월두법
YR = [('갑·기', '병인'), ('을·경', '무인'), ('병·신', '경인'), ('정·임', '임인'), ('무·계', '갑인')]
yrows = ''.join(f'<tr><td style="font-size:52px;width:300px;text-align:left;padding:10px 0;font-weight:400">{a} 년</td>'
                f'<td style="font-size:52px;width:auto;text-align:left;padding:10px 0;{"color:#c4a066" if a=="병·신" else ""}">→ {b}월</td></tr>' for a, b in YR)
fri = [
 (f'<h1 style="font-size:100px">겨울인데<br>왜 하늘에<br>{E("토","흙")}이 있을까요?</h1><div class="rule"></div><p class="sub">이번 달은 기해월(己亥月)</p>', SWIPE),
 ('<div class="step">월주는 두 글자</div><div class="rule"></div>'
  f'<p {P}>입동(11월 7일)부터 대설(12월 7일) 전까지는<br>사주로 해월(亥月)이에요.<br>해(亥)는 겨울의 시작, {E("수","물")}이에요.</p><br>'
  f'<h2>그런데 올해 해월의 천간은<br>{E("토","기(己)")}, 밭의 흙이에요.</h2>', ""),
 ('<div class="step">달의 천간은 그해가 정해요</div><div class="rule"></div>'
  f'<p {P}>달의 지지는 절기로 늘 같지만,<br>달의 천간은 그해 천간에 따라 정해져요.<br>이걸 월두법(月頭法)이라고 해요.</p><br>'
  '<p style="font-size:38px;color:#9a9a9a">그해 천간 → 첫 달(인월)의 천간</p>'
  f'<table style="margin-top:6px">{yrows}</table>', ""),
 ('<div class="step">올해는 병오년</div><div class="rule"></div>'
  f'<p {P}>병년은 첫 달이 경인월이고,<br>거기서 한 달에 한 칸씩 가요.</p><br>'
  '<p style="font-size:42px;line-height:1.9">경인 · 신묘 · 임진 · 계사 · 갑오 · 을미<br>병신 · 정유 · 무술 · <span style="color:#c4a066;font-weight:700">기해</span></p><br>'
  '<h2>열 번째 달이<br>기해월이에요.</h2>', ""),
 ('<div class="step">5년마다 같은 달</div><div class="rule"></div>'
  f'<p {P}>달의 기둥이 60갑자를 한 바퀴 도는 데<br>60달, 딱 5년이 걸려요.</p><br>'
  '<h2>5년 전 2021년(신축년)<br>이맘때도 기해월이었어요.</h2><br>'
  f'<p {P}>그래서 다섯 살 차이 나는 사람끼리는<br>같은 절기 달에 태어나면<br>월주가 같아요.</p>', ""),
 (f'<div class="step">기해, 겨울 밭</div><div class="rule"></div>'
  f'<h1 style="font-size:110px">{E("토","己")}<br>{E("수","亥")}</h1><br>'
  f'<p {P}>기토는 밭의 흙, 해수는 겨울의 물.<br>눈 녹은 물을 머금고 쉬는<br>겨울 밭 같은 달이에요.<br>다음 해를 위해 땅이 물을 모아 두는 때.</p>'
  f'<p {SM}>제 해석이에요.</p>', ""),
 MUSIC(E('토', '기토(己土)'), '고요히 쉬는 밭 같은 소리.<br>차분히 정리하는 저녁에<br>틀어 두기 좋아요.'),
]
fri_cap = ("겨울인데 왜 하늘에 흙(己)이 있을까요?\n\n"
 "지금은 사주로 해월(亥月), 겨울의 물이 시작되는 달이에요. 그런데 올해 이 달의 천간은 기(己), 밭의 흙이에요. "
 "달의 지지는 절기로 늘 같지만 천간은 그해 천간이 정하거든요. 이걸 월두법이라고 해요. "
 "병년과 신년은 첫 달이 경인월이라, 열 번째 달이 기해월이 돼요. 달의 기둥은 60달, 5년마다 한 바퀴 돌아서 2021년 이맘때도 기해월이었어요.\n\n"
 "기해는 눈 녹은 물을 머금고 쉬는 겨울 밭 같은 달. 『다섯 가지 고요｜기토(己土)』를 프로필 링크에서 들을 수 있어요.\n\n"
 "#고요 #사주 #월주 #월두법 #기해월 #명리학 #사주공부 #오행")

# ── 11/29 일 · 정화 · 일찍 지는 해
sun = [
 ('<h1 style="font-size:96px">해가 가장<br>일찍 지는 날은<br>동지가<br>아니에요</h1><div class="rule"></div><p class="sub">등불을 켜는 계절</p>', SWIPE),
 ('<div class="step">서울의 해 지는 시각</div><div class="rule"></div>'
  f'<p {P}>밤이 가장 긴 날은 동지(12월 22일)지만,<br>해가 가장 일찍 지는 날은 따로 있어요.</p><br>'
  '<h2 style="font-size:60px;line-height:1.6">12월 6~7일 무렵<br>오후 5시 13분쯤</h2><br>'
  f'<p {P}>동짓날 해는 그보다 4~5분 늦게 져요.<br>오늘 해도 5시 14분쯤 지니까,<br>지금이 1년 중 가장 일찍 어두워지는 때예요.</p>', ""),
 ('<div class="step">왜 그럴까요?</div><div class="rule"></div>'
  f'<p {P}>해가 가장 높이 뜨는 "진짜 정오"는<br>날마다 조금씩 움직여요.<br>지구가 타원 궤도를 돌고,<br>축이 기울어 있기 때문이에요.</p><br>'
  f'<p {P}>12월에는 이 정오가 하루 몇십 초씩<br>늦어져서, 낮은 계속 짧아지는데도<br>해 지는 시각은 먼저 바닥을 쳐요.</p>', ""),
 ('<div class="step">오늘은 정미일</div><div class="rule"></div>'
  f'<h1 style="font-size:120px">{E("화","丁")}未</h1><br>'
  f'<p {P}>정화(丁火)는 해 같은 큰불(병화)이 아니라<br>등불, 촛불처럼<br>작고 오래가는 불이에요.</p><br>'
  '<h2>해가 일찍 지는 이 주에<br>가장 어울리는 불이에요.</h2>', ""),
 MUSIC(E('화', '정화(丁火)'), '해가 지고 불을 켜 두는 저녁,<br>책을 읽거나 하루를 정리할 때<br>틀어 두기 좋아요. 22곡이에요.', '프로필 링크 → GOYO 유튜브'),
 ('<div class="step">다섯 가지 고요, 열 편</div><div class="rule"></div>'
  f'<p style="font-size:48px;line-height:1.9">{E("목","갑목")} · {E("목","을목")} · {E("화","병화")} · {E("화","정화")} · {E("토","무토")}<br>'
  f'{E("토","기토")} · {E("금","경금")} · {E("금","신금")} · {E("수","임수")} · {E("수","계수")}</p><br>'
  f'<p {P}>일간 열 개마다 한 편씩 만들었어요.<br>내 일간은 사주 앱 「일주」의 첫 글자예요.<br>(예: 을묘 → 을)</p><br>'
  '<p>프로필 링크 → GOYO 유튜브</p>', ""),
]
sun_cap = ("해가 가장 일찍 지는 날은 동지가 아니에요.\n\n"
 "밤이 가장 긴 날은 동지(12월 22일)지만, 서울에서 해가 가장 일찍 지는 날은 12월 6~7일 무렵, 오후 5시 13분쯤이에요. "
 "12월엔 해가 가장 높이 뜨는 정오가 날마다 조금씩 늦어져서, 해 지는 시각이 동지보다 먼저 바닥을 치거든요. "
 "오늘도 해는 5시 14분쯤 져요.\n\n"
 "오늘은 정미일. 정화(丁火)는 해 같은 큰불이 아니라 등불처럼 작고 오래가는 불이에요. "
 "불을 켜 두는 저녁엔 『다섯 가지 고요｜정화(丁火)』, 프로필 링크 → GOYO 유튜브에서 들을 수 있어요.\n\n"
 "#고요 #정화 #동지 #일몰 #오행음악 #플레이리스트 #책읽을때듣는음악 #저녁음악")

tue_cap = ("사주 여덟 글자 중 '나'는 딱 한 글자예요.\n\n"
 "태어난 날의 천간, 일간(日干)이에요. 갑·을·병·정·무·기·경·신·임·계 열 가지라 대략 열 명 중 한 명은 나와 일간이 같아요. "
 "날의 천간은 열흘마다 돌아오고, 오늘 11월 24일은 임인일이라 오늘 낮에 태어난 아기의 일간은 임수예요.\n\n"
 "내 일간은 사주 앱 「일주」의 첫 글자로 확인할 수 있어요(예: 을묘 → 을). 고요에는 일간 열 개마다 한 편씩 플레이리스트가 있어요. 프로필 링크에서 들을 수 있어요.\n\n"
 "#고요 #사주 #일간 #오행음악 #천간 #사주공부")
sat_cap = ("사주에 화가 많다는 말, 들어 보셨어요?\n\n"
 "오늘 11월 28일은 병오일이에요. 올해가 병오년이라 해와 날의 기둥이 같은 날이고, 이런 날은 60일마다 돌아와요. 병오는 천간도 지지도 불인 기둥이에요.\n\n"
 "일본에선 \"병오년에 태어난 여자는 기가 세다\"는 미신 때문에 1966년 출생아 수가 전년보다 25% 줄었어요. "
 "60년이 지난 올해는 1월 출생아 수가 오히려 조금 늘었다는 집계가 나왔고요. 사주에서 병오는 뜨거운 기둥일 뿐, 좋고 나쁨을 정하지 않아요.\n\n"
 "불이 많을 땐 물이 필요할 수도, 흙이 필요할 수도 있어요. 사주마다 달라서 고요에는 다섯 오행이 다 있어요. 프로필 링크에서 들을 수 있어요.\n\n"
 "#고요 #사주 #병오년 #화많은사주 #오행 #오행음악")

POSTS = {'2026-11-23': (mon, mon_cap, 'windsor'), '2026-11-25': (wed, wed_cap, 'windsor'),
         '2026-11-26': (thu, thu_cap, 'api'), '2026-11-27': (fri, fri_cap, 'windsor'),
         '2026-11-29': (sun, sun_cap, 'windsor')}
REELS = {'2026-11-24': ('shorts/미끼편/A 나는 한 글자 쇼츠.mp4', tue_cap),
         '2026-11-28': ('shorts/미끼편/I 화 많은 사주 쇼츠.mp4', sat_cap)}

async def main():
    from playwright.async_api import async_playwright
    only = sys.argv[1:]
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for d, (sl, _, _) in POSTS.items():
            if only and d not in only: continue
            os.makedirs(f'{OUT}/{d}', exist_ok=True)
            for i, (body, extra) in enumerate(sl, 1):
                html = BASE.replace("{body}", body).replace("{extra}", extra).replace("{page}", f"{i:02d} / {len(sl):02d}")
                await pg.set_content(html); await pg.wait_for_timeout(300)
                await pg.screenshot(path=f"{OUT}/{d}/{i:02d}.jpg", type='jpeg', quality=92)
        await b.close()
if __name__ == '__main__':
    asyncio.run(main())
