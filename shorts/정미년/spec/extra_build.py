import json, subprocess, sys, os
A=json.load(open('/tmp/extra_art.json'))
FG=[236,233,226]; EN=[214,210,202]; GD=[200,180,140]; DM=[190,186,178]
K='/home/claude/goyo-keys/audio/'; U='/mnt/user-data/uploads/Desktop/고요음악/쇼츠/_릴스음원/'
def sc(main,en,art=None,sub=None,size=58,sec=5.5,h=280,instant=False,tag=None,step=None,big=None):
    it=[]
    if big: it.append([big,110,GD,True,30])
    it.append([main,size,FG,True,24])
    if sub: it.append([sub,40,GD,False,24])
    it.append([en,28,EN,False,0])
    s={'sec':sec,'items':it}
    if art: s['art']={'file':A[art],'h':h}
    if instant: s['instant']=True
    if tag: s['tag']=tag
    if step: s['step']=step
    return s
P={}
P['0113-2100']=dict(date='2027-01-13',slot='2100',name='겨울나무는 쉬지 않아요',
 audio=dict(pyeon='갑목',title='Quiet Trunk',file=U+'갑목/09 Quiet Trunk.m4a',start_hms='21:37',근거='원곡: 맥 _릴스음원/catalog.json 갑목 09 21:37 Quiet Trunk (60초)'),
 music_ko='갑목(甲木)',music_en='Yang Wood',end_tag='오늘 밤의 소리',end_art='0113_겨울나무',
 scenes=[sc('잎을 다 떨군 겨울나무,\n그냥 쉬고 있는 걸까요?','A bare winter tree:\nis it simply resting?','0113_겨울나무',size=70,sec=4.0,instant=True,h=260),
  sc('가지 끝을 보면\n겨울눈이 달려 있어요.','Look at the tips of the branches:\nwinter buds, with spring’s leaves or flowers folded inside.','0113_겨울눈',sub='봄에 펼 잎이나 꽃이 접혀 든 눈이에요.'),
  sc('이 눈은 겨울에 만든 게 아니에요.\n지난여름과 가을에\n미리 지어 둔 거예요.','These buds weren’t made in winter.\nThe tree built them last summer and autumn.','0113_눈에서봄',sec=6.0),
  sc('많은 나무는 추위를\n일정 시간 겪어야\n봄에 제대로 싹을 틔워요.','Many trees need a certain stretch of cold\nbefore they can bud properly in spring.\nBotanists call it a chilling requirement.','0113_눈에서봄',sub='이걸 저온 요구라고 해요.',sec=6.0,tag='저온 요구'),
  sc('사주에서 겨울은 물(水)의 철.\n물은 나무를 낳는다(水生木)고 봐요.','In Saju, winter is the season of Water,\nand Water is said to nourish Wood (水生木).','0113_수생목',size=52,sec=6.0),
  sc('그래서 갑목(甲木) 일간에게 겨울은\n드러나지 않는 준비가\n쌓이는 철로 읽을 수 있어요.','So for a 甲木 Yang Wood (Gapmok) Day Master,\nwinter can be read as a season of quiet preparation.\nThe start of spring (立春) is just over three weeks away.',None,sub='입춘(2월 4일)까지 3주 남짓 남았어요.',size=54,sec=7.0,step=0.9)],
 caption='''잎을 다 떨군 겨울나무, 그냥 쉬고 있는 걸까요?

가지 끝을 보면 겨울눈이 달려 있어요. 봄에 펼 잎이나 꽃이 접혀 든 눈이에요. 이 눈은 겨울에 만든 게 아니라, 지난여름과 가을에 미리 지어 둔 거예요. 그리고 많은 나무는 추위를 일정 시간 겪어야 봄에 제대로 싹을 틔워요. 이걸 저온 요구라고 해요.

사주에서 겨울은 물(水)의 철이고, 물은 나무를 낳는다(水生木)고 봐요. 그래서 갑목(甲木) 일간에게 겨울은 드러나지 않는 준비가 쌓이는 철로 읽을 수 있어요. 입춘(2월 4일 오전 10시 46분)까지 3주 남짓 남았어요.

이 영상의 소리는 다섯 가지 고요의 『Quiet Trunk』(갑목 편)예요. 내 일간을 찾는 무료 앱과 음악은 프로필 링크에서 볼 수 있어요.

· English ·
A bare winter tree: is it simply resting? Look at the tips of the branches: winter buds, with spring’s leaves or flowers folded inside. These buds weren’t made in winter; the tree built them last summer and autumn. Many trees also need a certain stretch of cold before they can bud properly in spring, which botanists call a chilling requirement. In Saju, winter is the season of Water, and Water is said to nourish Wood (水生木). So for a 甲木 Yang Wood (Gapmok) Day Master, winter can be read as a season of quiet preparation. The start of spring (立春) is just over three weeks away: Feb 4, 2027, 10:46 a.m. KST.
Music in this video: Five Kinds of Quiet · Yang Wood · “Quiet Trunk”. Find your Day Master with our free app, and the music: link in bio.

#고요 #갑목 #겨울나무 #정미년 #오행음악''')
P['0116-2100']=dict(date='2027-01-16',slot='2100',name='잠들기 전 피아노',
 audio=dict(pyeon='수1',title='Night Tide',file=K+'수1/02 Night Tide.m4a',start_hms=''),
 music_ko='수(水)',music_en='Water',end_tag='오늘 밤의 소리',end_art='0116_달과물',
 scenes=[sc('잠들기 전에 틀어 두는 피아노,\n고요는 이렇게 만들어요','Bedtime piano:\nhow GOYO makes it','0116_달과물',size=64,sec=4.0,instant=True,h=260),
  sc('고요의 물(水) 편은\n밤을 위해 만든\n피아노 연주예요.','GOYO’s Water series is piano music\nmade for the night.','0116_건반'),
  sc('빠르기는 1분에 52~60박.\n서두르지 않는 속도예요.','The tempo is 52 to 60 beats per minute:\nno hurry.','0116_메트로놈'),
  sc('북이나 드럼 같은 타악기는\n하나도 넣지 않았어요.','No drums, no percussion at all.','0116_건반'),
  sc('화음에서 3도를 비워 두었어요.\n밝지도 슬프지도 않은,\n맑고 찬 소리예요.','We leave the third out of the chords:\nneither bright nor sad, just clear and cool.','0116_3도비움',sub='3도가 장조와 단조를 가르거든요.',sec=6.0,tag='3도'),
  sc('사주에서 물은 겨울과 밤,\n모으고 쉬는 기운이에요.','In Saju, Water is winter and night:\nthe energy of gathering and resting.\nWe won’t promise it puts you to sleep.\nWe just chose sounds that don’t grab your ear.',None,sub='잠이 온다고 말하진 않을게요.\n귀를 붙잡지 않는 소리를 골랐어요.',size=56,sec=7.0,step=0.9)],
 caption='''잠들기 전에 틀어 두는 피아노, 고요는 이렇게 만들어요.

고요의 물(水) 편은 밤을 위해 만든 피아노 연주예요. 빠르기는 1분에 52~60박, 서두르지 않는 속도예요. 북이나 드럼 같은 타악기는 하나도 넣지 않았어요. 그리고 화음에서 3도를 비워 두었어요. 3도가 장조와 단조를 가르거든요. 그래서 밝지도 슬프지도 않은, 맑고 찬 소리가 나요.

사주에서 물은 겨울과 밤, 모으고 쉬는 기운이에요. 잠이 온다고 말하진 않을게요. 다만 귀를 붙잡지 않는 소리를 골랐어요.

이 영상의 소리는 다섯 가지 고요의 『Night Tide』(수1 편)예요. 음악은 프로필 링크에서 들을 수 있어요.

· English ·
Bedtime piano: how GOYO makes it. GOYO’s Water series is piano music made for the night. The tempo is 52 to 60 beats per minute: no hurry. No drums, no percussion at all. And we leave the third out of the chords, since the third is what makes a chord major or minor. So the sound is neither bright nor sad, just clear and cool. In Saju, Water is winter and night: the energy of gathering and resting. We won’t promise it puts you to sleep. We just chose sounds that don’t grab your ear.
Music in this video: Five Kinds of Quiet · Water · “Night Tide”. Music: link in bio.

#고요 #수면음악 #피아노 #오행음악 #수''')
P['0122-2100']=dict(date='2027-01-22',slot='2100',name='모두에게 좋은 해는 없어요',
 audio=dict(pyeon='목1',title='Tree Rings',file=U+'목1_TreeRings_60s.m4a',start_hms='38:44',근거='원곡: 맥 고요음악/목/목1/목1 영상 최종 v2.mp4 38:44부터 60초 (설명란 38:42 Tree Rings, 2초 겹침 뒤부터), 맥 _릴스음원/목1_TreeRings_60s.m4a'),
 music_ko='목(木)',music_en='Wood',end_tag='오늘 밤의 소리',end_art='0122_나이테',
 scenes=[sc('2027년은\n좋은 해일까요?','Will 2027 be a good year?','0122_나이테',size=80,sec=3.5,instant=True,h=260),
  sc('나무의 나이테를 보면\n해마다 폭이 달라요.','Look at a tree’s rings: their width changes from year to year.\nWide in good growing years, narrow in hard ones.','0122_나이테',sub='자라기 좋은 해엔 넓게,\n힘든 해엔 좁게 자라요.',sec=6.0),
  sc('같은 해라도\n물가의 나무와 마른 언덕의 나무는\n나이테가 다르게 남아요.','Even in the same year, a tree by the water\nand a tree on a dry hill leave different rings.','0122_나이테',sec=5.5),
  sc('사주도 그래요.\n정미년은 불(丁)과 흙(未)의 해.','Saju works the same way.\nThe 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth:\na year of fire and earth.',None,size=60,sec=5.0),
  sc('한겨울생처럼 차가운 사주엔\n반가운 온기로 읽고,\n불이 이미 많은 사주엔\n조금 덥게 읽기도 해요.','For a cold chart, say someone born in deep winter,\nit reads as welcome warmth.\nFor a chart already full of fire,\nit may read as a little too warm.','0122_겨울과여름',size=52,sec=7.0),
  sc('그래서 한 해가 모두에게\n똑같이 좋을 수는 없어요.','So no year is good for everyone in the same way.\nThat’s why GOYO has all five elements.','0122_다섯',sub='고요에 다섯 오행 편이\n다 있는 이유예요.',sec=6.5,step=0.9)],
 caption='''2027년은 좋은 해일까요?

나무의 나이테를 보면 해마다 폭이 달라요. 자라기 좋은 해엔 넓게, 힘든 해엔 좁게 자라요. 같은 해라도 물가의 나무와 마른 언덕의 나무는 나이테가 다르게 남아요.

사주도 그래요. 다가오는 정미년은 불(丁)과 흙(未)의 해예요. 한겨울생처럼 차가운 사주엔 반가운 온기로 읽고, 불이 이미 많은 사주엔 조금 덥게 읽기도 해요. 그래서 한 해가 모두에게 똑같이 좋을 수는 없어요. 고요에 다섯 오행 편이 다 있는 이유예요.

사주의 해는 입춘(2027년 2월 4일 오전 10시 46분)에 바뀌어요.

이 영상의 소리는 다섯 가지 고요의 『Tree Rings』(목1 편)예요. 내 일간을 찾는 무료 앱과 음악은 프로필 링크에서 볼 수 있어요.

· English ·
Will 2027 be a good year? Look at a tree’s rings: their width changes from year to year, wide in good growing years and narrow in hard ones. Even in the same year, a tree by the water and a tree on a dry hill leave different rings. Saju works the same way. The coming 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth is a year of fire and earth. For a cold chart, say someone born in deep winter, it reads as welcome warmth. For a chart already full of fire, it may read as a little too warm. So no year is good for everyone in the same way. That’s why GOYO has all five elements. In Saju, the year turns at the start of spring (立春): Feb 4, 2027, 10:46 a.m. KST.
Music in this video: Five Kinds of Quiet · Wood · “Tree Rings”. Find your Day Master with our free app, and the music: link in bio.

#고요 #정미년 #나이테 #오행 #오행음악''')
P['0127-2100']=dict(date='2027-01-27',slot='2100',name='재 속에 묻어 둔 불씨',
 audio=dict(pyeon='화1',title='Ember Walk',file=K+'화1/03 Ember Walk.m4a',start_hms=''),
 music_ko='화(火)',music_en='Fire',end_tag='오늘 밤의 소리',end_art='0127_화로',
 scenes=[sc('옛날 집에선\n불씨를 꺼뜨리지 않았대요','In old Korean homes,\nthe fire was never allowed to go out.','0127_화로',size=72,sec=4.0,instant=True,h=260),
  sc('화로에 담은 숯불을\n재로 덮고 돌을 얹어\n오래 살려 두었어요.','Embers in the brazier were covered with ash\nand weighted with a stone to keep them alive.','0127_재속불씨',sec=6.0),
  sc('불씨를 지키는 건\n집안의 큰일이었고,\n이사할 때도 꼭 살려서 옮겼어요.','Keeping the ember was a household duty,\nand when a family moved, they carried it, still alive.','0127_화로',sub='불씨는 살림을 지키는 불로 여겼거든요.',size=54,sec=6.5),
  sc('그런데 정미년의 미(未) 속에도\n정화(丁火), 작은 불이 들어 있어요.','Inside 未 Afternoon Earth (Mito),\nthe second character of the 丁未 year (Jeongmi),\nthere is a small fire too: 丁火 Yin Fire (Jeonghwa).','0127_미속정',sub='未 속 글자(지장간): 丁 · 乙 · 己\n丁은 여름 불이 남은 기운이에요.',size=54,sec=6.0,tag='未 속의 丁'),
  sc('흙 속에 묻어 둔 불씨처럼,\n피운 불을 꺼뜨리지 않고\n이어 가는 해로 읽을 수 있어요.','Like an ember kept under ash,\none way to read the year:\nkeeping the fire you’ve lit burning.\nThe start of spring (立春) is eight days away.',None,sub='입춘까지 여드레 남았어요.',size=56,sec=7.0,step=0.9)],
 caption='''옛날 집에선 불씨를 꺼뜨리지 않았대요.

화로에 담은 숯불을 재로 덮고 돌을 얹어 오래 살려 두었어요. 불씨를 지키는 건 집안의 큰일이었고, 이사할 때도 불씨를 꼭 살려서 옮겼어요. 불씨를 살림을 지키는 불로 여겼거든요.

그런데 다가오는 정미년의 미(未) 속에도 정화(丁火), 작은 불이 들어 있어요. 未 속 글자(지장간)는 정(丁)·을(乙)·기(己)예요. 그래서 정미년은 흙 속에 묻어 둔 불씨처럼, 피운 불을 꺼뜨리지 않고 이어 가는 해로 읽을 수 있어요.

입춘(2월 4일 오전 10시 46분)까지 여드레 남았어요.

이 영상의 소리는 다섯 가지 고요의 『Ember Walk』(화1 편)예요. 내 일간을 찾는 무료 앱과 음악은 프로필 링크에서 볼 수 있어요.

· English ·
In old Korean homes, the fire was never allowed to go out. Embers in the brazier were covered with ash and weighted with a stone to keep them alive. Keeping the ember was a household duty, and when a family moved, they carried it, still alive; the ember was seen as the fire that guarded the household. Inside 未 Afternoon Earth (Mito), the second character of the coming 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth, there is a small fire too: 丁火 Yin Fire (Jeonghwa), along with 乙 and 己 (its hidden stems). So, like an ember kept under ash, one way to read the year is keeping the fire you’ve lit burning. The start of spring (立春) is eight days away: Feb 4, 2027, 10:46 a.m. KST.
Music in this video: Five Kinds of Quiet · Fire · “Ember Walk”. Find your Day Master with our free app, and the music: link in bio.

#고요 #정미년 #불씨 #오행 #오행음악''')
P['0129-2100']=dict(date='2027-01-29',slot='2100',name='날짜에도 이름이 있어요',
 audio=dict(pyeon='금1',title='Pale Ring',file=K+'금1/04 Pale Ring.m4a',start_hms=''),
 music_ko='금(金)',music_en='Metal',end_tag='오늘 밤의 소리',end_art='0129_60',
 scenes=[sc('어제 1월 28일은\n정미(丁未)일이었어요','Yesterday, January 28,\nwas a 丁未 (Jeongmi) day.','0129_달력',size=72,sec=4.0,instant=True,h=260),
  sc('날마다 60갑자 이름이\n하나씩 붙어요.\n60일이 지나면 같은 이름이 돌아와요.','Every day carries one of sixty names.\nAfter sixty days, the same name comes back.','0129_60',size=54,sec=6.0),
  sc('이 날짜 셈은 『춘추』의 기록부터\n2,700년 넘게\n끊기지 않고 이어져 왔다고 봐요.','This day count is thought to have run unbroken\nfor more than 2,700 years,\nsince the days of the Spring and Autumn Annals.','0129_60',sub='그 책의 일식 기록과 날짜가 들어맞거든요.',size=54,sec=6.5,tag='2,700년'),
  sc('60일마다 돌아오니\n한 해에 같은 날 이름을\n여섯 번쯤 만나요.','Since names return every sixty days,\neach comes round about six times a year.\nToday, January 29, is a 戊申 (Musin) day.','0129_60',sub='오늘 1월 29일은 무신(戊申)일이에요.',sec=6.0),
  sc('다음 정미일은 3월 29일.\n정미년은 입춘, 2월 4일에 시작돼요.','The next 丁未 day is March 29.\nThe 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth begins at the start of spring (立春), February 4.',None,sub='입춘 날의 일진은 갑인(甲寅)이에요.',size=56,sec=6.5,step=0.9)],
 caption='''어제 1월 28일은 정미(丁未)일이었어요.

날마다 60갑자 이름이 하나씩 붙어요. 60일이 지나면 같은 이름이 돌아와요. 이 날짜 셈은 『춘추』의 기록부터 2,700년 넘게 끊기지 않고 이어져 왔다고 봐요. 그 책의 일식 기록과 날짜가 들어맞거든요.

60일마다 돌아오니 한 해에 같은 날 이름을 여섯 번쯤 만나요. 오늘 1월 29일은 무신(戊申)일이에요.

다음 정미일은 3월 29일이에요. 정미년은 입춘(2월 4일 오전 10시 46분)에 시작되고, 그날의 일진은 갑인(甲寅)이에요.

이 영상의 소리는 다섯 가지 고요의 『Pale Ring』(금1 편)이에요. 내 일간을 찾는 무료 앱과 음악은 프로필 링크에서 볼 수 있어요.

· English ·
Yesterday, January 28, was a 丁未 (Jeongmi) day. Every day carries one of sixty names, and after sixty days the same name comes back. This day count is thought to have run unbroken for more than 2,700 years, since the Spring and Autumn Annals, whose eclipse records match the count. Since names return every sixty days, each comes round about six times a year. Today, January 29, is a 戊申 (Musin) day. The next 丁未 day is March 29. The 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth begins at the start of spring (立春): Feb 4, 2027, 10:46 a.m. KST, on a 甲寅 (Gabin) day.
Music in this video: Five Kinds of Quiet · Metal · “Pale Ring”. Find your Day Master with our free app, and the music: link in bio.

#고요 #일진 #60갑자 #정미년 #오행음악''')
P['0131-2100']=dict(date='2027-01-31',slot='2100',name='입춘대길 건양다경',
 audio=dict(pyeon='갑목',title='Pine at Dawn',file=U+'갑목/10 Pine at Dawn.m4a',start_hms='24:39',근거='원곡: 맥 _릴스음원/catalog.json 갑목 10 24:39 Pine at Dawn (60초)'),
 music_ko='갑목(甲木)',music_en='Yang Wood',end_tag='오늘 밤의 소리',end_art='0131_동쪽',
 scenes=[sc('나흘 뒤 대문에 붙이는\n여덟 글자','Eight characters for the front gate,\nfour days from now','0131_입춘첩',big='立春大吉\n建陽多慶',size=52,sec=5.0,instant=True,h=240),
  sc('입춘대길: 봄이 서니 크게 길하기를.\n건양다경: 볕이 일어 경사가 많기를.','“As spring begins, may great fortune come.\nAs the warm light rises, may there be much to celebrate.”','0131_입춘첩',size=50,sec=6.0),
  sc('입춘 무렵 대문이나 기둥에\n써 붙이는 입춘첩이에요.','These are ipchuncheop, spring couplets\nposted on gates and pillars at the start of spring.','0131_입춘첩',sec=5.5),
  sc('오행에서 봄은 나무(木),\n방향은 해가 뜨는 동쪽이에요.','In the five elements, spring is Wood,\nand its direction is east, where the sun rises.','0131_동쪽',sec=5.5),
  sc('갑목(甲木)은 그 동쪽의 큰 나무.\n2월 4일 오전 10시 46분,\n사주의 해도 바뀌어요.','甲木 Yang Wood (Gapmok) is the tall tree of the east.\nOn Feb 4, 2027, at 10:46 a.m. KST, the Saju year turns too.',None,size=56,sec=6.5,step=0.9)],
 caption='''나흘 뒤 대문에 붙이는 여덟 글자, 立春大吉 建陽多慶.

입춘대길(立春大吉)은 봄이 서니 크게 길하기를, 건양다경(建陽多慶)은 볕이 일어 경사가 많기를 바라는 말이에요. 입춘 무렵 대문이나 기둥에 써 붙이는 입춘첩이에요.

오행에서 봄은 나무(木), 방향은 해가 뜨는 동쪽이에요. 갑목(甲木)은 그 동쪽의 큰 나무예요. 2월 4일 오전 10시 46분, 사주의 해도 정미년으로 바뀌어요.

이 영상의 소리는 다섯 가지 고요의 『Pine at Dawn』(갑목 편)이에요. 내 일간을 찾는 무료 앱과 음악은 프로필 링크에서 볼 수 있어요.

· English ·
Eight characters for the front gate, four days from now: 立春大吉 建陽多慶. “As spring begins, may great fortune come. As the warm light rises, may there be much to celebrate.” These are ipchuncheop, spring couplets posted on gates and pillars at the start of spring (立春). In the five elements, spring is Wood, and its direction is east, where the sun rises. 甲木 Yang Wood (Gapmok) is the tall tree of the east. On Feb 4, 2027, at 10:46 a.m. KST, the Saju year turns too, to the 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth.
Music in this video: Five Kinds of Quiet · Yang Wood · “Pine at Dawn”. Find your Day Master with our free app, and the music: link in bio.

#고요 #입춘 #입춘대길 #갑목 #오행음악''')
P['0201-2100']=dict(date='2027-02-01',slot='2100',name='청자 한 점에 다섯 기운',
 audio=dict(pyeon='신금',title='Silver Thread',file=K+'신금/08 Silver Thread.m4a',start_hms='31:24'),
 music_ko='신금(辛金)',music_en='Yin Metal',end_tag='오늘 밤의 소리',end_art='0201_청자',
 scenes=[sc('청자 한 점에\n다섯 기운이 다 들어 있어요','One piece of celadon\nholds all five elements.','0201_청자',size=72,sec=4.0,instant=True,h=270),
  sc('흙(土)을 곱게 걸러\n물(水)로 반죽해 빚어요.','Fine clay (Earth) is mixed\nwith water (Water) and shaped.','0201_흙물',sec=5.0),
  sc('나무(木)를 때서\n가마 불(火)을 1,200℃ 넘게 올려요.','Burning wood (Wood)\ntakes the kiln fire (Fire) past 1,200°C.','0201_나무불',sec=5.5),
  sc('푸른빛은 쇠(金)에서 나와요.\n유약 속 1~3%의 철분이\n불 속에서 푸르게 바뀌어요.','The blue-green comes from Metal:\n1–3% iron in the glaze\nturns that color in the kiln.','0201_철분',size=54,sec=6.5,tag='金'),
  sc('다섯이 다 모여야\n비색(翡色)이 나와요.','Only with all five\ndoes the jade-green color appear.\nGOYO has all five elements, too.','0201_청자',sub='고요에도 다섯 오행 편이 다 있어요.',sec=6.0,step=0.9)],
 caption='''청자 한 점에 다섯 기운이 다 들어 있어요.

흙(土)을 곱게 걸러 물(水)로 반죽해 빚어요. 나무(木)를 때서 가마 불(火)을 1,200℃ 넘게 올려요. 그리고 그 푸른빛은 쇠(金)에서 나와요. 유약 속 1~3%의 철분이 불 속에서 푸르게 바뀌거든요.

다섯이 다 모여야 고려청자의 비색(翡色)이 나와요. 고요에도 다섯 오행 편이 다 있어요.

이 영상의 소리는 다섯 가지 고요의 『Silver Thread』(신금 편)예요. 내 일간을 찾는 무료 앱과 음악은 프로필 링크에서 볼 수 있어요.

· English ·
One piece of celadon holds all five elements. Fine clay (Earth) is mixed with water (Water) and shaped. Burning wood (Wood) takes the kiln fire (Fire) past 1,200°C. And the blue-green comes from Metal: 1–3% iron in the glaze turns that color in the kiln. Only with all five does the jade-green of Goryeo celadon appear. GOYO has all five elements, too.
Music in this video: Five Kinds of Quiet · Yin Metal · “Silver Thread”. Find your Day Master with our free app, and the music: link in bio.

#고요 #청자 #오행 #다섯가지고요 #오행음악''')
P['0203-2100']=dict(date='2027-02-03',slot='2100',name='흙의 18일이 끝나는 날',
 audio=dict(pyeon='무토',title='Earthen Path',file=K+'무토/06 Earthen Path.m4a',start_hms='11:29'),
 music_ko='무토(戊土)',music_en='Yang Earth',end_tag='오늘 밤의 소리',end_art='0203_사계토',
 scenes=[sc('내일이 입춘,\n오늘은 흙의 18일이\n끝나는 날이에요','Tomorrow is the start of spring.\nToday, earth’s eighteen days come to an end.','0203_18일',size=64,sec=4.5,instant=True,h=240),
  sc('옛 달력은 네 계절에\n다섯 기운을 나눴어요.','The old calendar split five elements\nacross four seasons:\nspring Wood, summer Fire, autumn Metal, winter Water.','0203_사계토',sub='봄 나무, 여름 불, 가을 쇠, 겨울 물.',sec=6.0),
  sc('남은 흙(土)은\n계절이 바뀌기 전 18일씩\n나눠 받았어요.','Earth took the eighteen days\nbefore each season turns.\nThis is called 土旺用事 (Towang-yongsa), earth in charge.','0203_18일',sub='이걸 토왕용사(土旺用事)라고 해요.',sec=6.5,tag='土旺用事'),
  sc('입춘·입하·입추·입동 앞\n18일씩, 한 해 72일이에요.','Eighteen days before each season’s start,\n72 days a year.','0203_사계토',sec=5.0),
  sc('흙은 한 계절을 거두어\n다음 계절로 넘겨주는\n자리로 봐요.','Earth is seen as the place\nthat gathers one season\nand hands it to the next.\nAn old custom avoids major digging at this time.',None,sub='이 무렵엔 흙을 크게 파헤치는 일을\n삼가는 풍습도 동아시아에 전해져요.',size=56,sec=6.5),
  sc('내일 오전 10시 46분, 입춘.\n사주의 해가\n정미년으로 바뀌어요.','Tomorrow at 10:46 a.m. KST, the start of spring (立春).\nThe Saju year turns to the 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth.',None,size=58,sec=5.5,step=0.9)],
 caption='''내일이 입춘, 오늘은 흙의 18일이 끝나는 날이에요.

옛 달력은 네 계절에 다섯 기운을 나눴어요. 봄은 나무, 여름은 불, 가을은 쇠, 겨울은 물. 남은 흙(土)은 계절이 바뀌기 전 18일씩 나눠 받았어요. 입춘·입하·입추·입동 앞 18일씩, 한 해 72일이에요. 이걸 토왕용사(土旺用事)라고 해요.

흙은 한 계절을 거두어 다음 계절로 넘겨주는 자리로 봐요. 그래서 이 무렵엔 흙을 크게 파헤치는 일을 삼가는 풍습도 동아시아에 전해져요.

내일 오전 10시 46분이 입춘이에요. 사주의 해가 정미년으로 바뀌어요.

이 영상의 소리는 다섯 가지 고요의 『Earthen Path』(무토 편)예요. 내 일간을 찾는 무료 앱과 음악은 프로필 링크에서 볼 수 있어요.

· English ·
Tomorrow is the start of spring (立春). Today, earth’s eighteen days come to an end. The old calendar split five elements across four seasons: spring Wood, summer Fire, autumn Metal, winter Water. Earth took the eighteen days before each of the four season-starts: 72 days a year. This is called 土旺用事 (Towang-yongsa), earth in charge. Earth is seen as the place that gathers one season and hands it to the next, and there is an old custom of avoiding major digging at this time. Tomorrow at 10:46 a.m. KST, the Saju year turns to the 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth.
Music in this video: Five Kinds of Quiet · Yang Earth · “Earthen Path”. Find your Day Master with our free app, and the music: link in bio.

#고요 #토왕용사 #입춘 #무토 #오행음악''')
P['0204-1300']=dict(date='2027-02-04',slot='1300',name='정미년 첫 글자의 소리',
 audio=dict(pyeon='정화',title='Little Lamp',file=U+'정화/16 Little Lamp.m4a',start_hms='',근거='원곡: 맥 고요음악/쇼츠/_릴스음원/정화/16 Little Lamp.m4a (60초 클립)'),
 music_ko='정화(丁火)',music_en='Yin Fire',end_tag='정미년 첫날의 소리',end_art='0204_해와등불',
 scenes=[sc('오늘 오전 10시 46분부터 정미년.\n첫 글자 정화(丁火)는\n어떤 소리일까요?','From 10:46 this morning (KST): the 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth.\nWhat does 丁火 Yin Fire (Jeonghwa) sound like?','0204_해와등불',size=62,sec=4.5,instant=True,h=240),
  sc('고요의 정화 편은 재즈예요.\n로즈와 우리처, 두 전자 피아노가\n따뜻한 화음을 길게 눌러 줘요.','GOYO’s Yin Fire album is jazz:\ntwo vintage electric pianos, Rhodes and Wurlitzer,\nholding long, warm chords.','0204_전자피아노',size=54,sec=6.0),
  sc('빠르기는 1분에 98~100박.\n고요의 불 가운데\n조금 느린 쪽이에요.','The tempo is 98 to 100 beats per minute,\nthe slower side of GOYO’s Fire music.\nThe 丙火 Yang Fire (Byeonghwa) album runs 102 to 104.','0204_메트로놈',sub='병화 편은 102~104박이에요.',sec=6.0,tag='98–100'),
  sc('선율은 긴 음으로 천천히 내려앉고,\n일렉 베이스가 둥글게 받쳐요.','The melody settles in long notes,\nand a round electric bass holds it up.','0204_전자피아노',size=54,sec=5.5),
  sc('병화가 사방을 비추는 해라면,\n정화는 가까이 오래 비추는 등불.\n그 차이를 빠르기와 음의 길이로 옮겼어요.','If Yang Fire is the sun lighting everything,\nYin Fire is a lamp that lights what is near, and keeps burning.\nWe turned that difference into tempo and note length.','0204_해와등불',size=50,sec=7.0,step=0.9)],
 caption='''오늘 오전 10시 46분부터 정미년이에요. 첫 글자 정화(丁火)는 어떤 소리일까요?

고요의 정화 편은 재즈예요. 로즈와 우리처, 두 전자 피아노가 따뜻한 화음을 길게 눌러 줘요. 빠르기는 1분에 98~100박으로, 고요의 불 가운데 조금 느린 쪽이에요. 병화 편은 102~104박이에요. 선율은 긴 음으로 천천히 내려앉고, 일렉 베이스가 둥글게 받쳐요.

병화가 사방을 비추는 해라면, 정화는 가까이 오래 비추는 등불이에요. 그 차이를 빠르기와 음의 길이로 옮겼어요.

※ 오행을 공부해 온 제작자가 각 기운의 성질을 템포·선율·화음으로 옮겨 본 해석 시리즈예요.

이 영상의 소리는 다섯 가지 고요의 『Little Lamp』(정화 편)예요. 내 일간을 찾는 무료 앱과 음악은 프로필 링크에서 볼 수 있어요.

· English ·
From 10:46 this morning (KST), it’s the 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth. What does its first character, 丁火 Yin Fire (Jeonghwa), sound like? GOYO’s Yin Fire album is jazz: two vintage electric pianos, Rhodes and Wurlitzer, holding long, warm chords. The tempo is 98 to 100 beats per minute, the slower side of GOYO’s Fire music; the 丙火 Yang Fire (Byeonghwa) album runs 102 to 104. The melody settles in long notes, and a round electric bass holds it up. If Yang Fire is the sun lighting everything, Yin Fire is a lamp that lights what is near, and keeps burning. We turned that difference into tempo and note length.
Music in this video: Five Kinds of Quiet · Yin Fire · “Little Lamp”. Find your Day Master with our free app, and the music: link in bio.

#고요 #정미년 #정화 #재즈 #오행음악''')
P['0206-1800']=dict(date='2027-02-06',slot='1800',name='섣달그믐 밤의 불',
 audio=dict(pyeon='정화',title='Golden Hush',file=U+'정화/17 Golden Hush.m4a',start_hms='',근거='원곡: 맥 고요음악/쇼츠/_릴스음원/정화/17 Golden Hush.m4a (60초 클립)'),
 music_ko='정화(丁火)',music_en='Yin Fire',end_tag='그믐밤의 소리',end_art='0206_불밝힌집',
 scenes=[sc('오늘은 섣달그믐.\n옛날엔 오늘 밤 잠들면\n눈썹이 센다고 했대요.','Today is the last night of the lunar year.\nPeople used to say: fall asleep tonight,\nand your eyebrows turn white.','0206_눈썹',size=62,sec=4.5,instant=True,h=220),
  sc('그래서 밤새 잠들지 않고\n묵은해를 지켰어요.','So people stayed up all night\nto see the old year out.\nIt was called 守歲 (suse), keeping the year.','0206_불밝힌집',sub='이걸 수세(守歲), 해지킴이라고 해요.',sec=6.0,tag='守歲'),
  sc('방, 마루, 부엌, 곳간, 장독대까지\n집 안 곳곳에 불을 밝혀 두고\n새벽닭이 울 때까지 기다렸어요.','Lamps were lit all through the house:\nrooms, hall, kitchen, storeroom, even the crock terrace,\nuntil the first rooster crowed.','0206_불밝힌집',size=52,sec=6.5),
  sc('그래도 잠든 아이 눈썹엔\n흰 가루를 발라 두고,\n아침에 「눈썹 셌다」며 놀리기도 했어요.','Children who dozed off got white powder on their brows,\nand were teased in the morning that they had turned white.','0206_눈썹',size=52,sec=6.5),
  sc('정미년의 첫 글자도 불, 정화(丁火).\n불 밝힌 그믐밤을 지나\n내일은 설날이에요.','The first character of the 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth\nis a fire too: 丁火 Yin Fire (Jeonghwa).\nPast this lamp-lit night, tomorrow is Seollal.',None,size=56,sec=6.0,step=0.9)],
 caption='''오늘은 섣달그믐. 옛날엔 오늘 밤 잠들면 눈썹이 센다고 했대요.

그래서 밤새 잠들지 않고 묵은해를 지켰어요. 이걸 수세(守歲), 해지킴이라고 해요. 방, 마루, 부엌, 곳간, 장독대까지 집 안 곳곳에 불을 밝혀 두고 새벽닭이 울 때까지 기다렸어요. 그래도 잠든 아이 눈썹엔 흰 가루를 발라 두고, 아침에 「눈썹 셌다」며 놀리기도 했어요.

정미년의 첫 글자도 불, 정화(丁火)예요. 불 밝힌 그믐밤을 지나 내일은 설날이에요.

이 영상의 소리는 다섯 가지 고요의 『Golden Hush』(정화 편)예요. 내 일간을 찾는 무료 앱과 음악은 프로필 링크에서 볼 수 있어요.

참고: 한국민족문화대백과사전 「수세」·「제석」

· English ·
Today is the last night of the lunar year. People used to say: fall asleep tonight, and your eyebrows turn white. So people stayed up all night to see the old year out. It was called 守歲 (suse), keeping the year. Lamps were lit all through the house: rooms, hall, kitchen, storeroom, even the crock terrace, until the first rooster crowed. Children who dozed off got white powder on their brows, and were teased in the morning that they had turned white. The first character of the 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth is a fire too: 丁火 Yin Fire (Jeonghwa). Past this lamp-lit night, tomorrow is Seollal, the Lunar New Year.
Music in this video: Five Kinds of Quiet · Yin Fire · “Golden Hush”. Find your Day Master with our free app, and the music: link in bio.

#고요 #섣달그믐 #수세 #설날 #오행음악''')
P['0206-2100']=dict(date='2027-02-06',slot='2100',name='떡국 한 그릇, 한 살',
 audio=dict(pyeon='수1',title='Quiet Harbor',file=K+'수1/05 Quiet Harbor.m4a',start_hms=''),
 music_ko='수(水)',music_en='Water',end_tag='오늘 밤의 소리',end_art='0206_떡국',
 scenes=[sc('떡국 먹으면 한 살 더 먹는다던데,\n지금도 그럴까요?','Eat a bowl of tteokguk, gain a year:\nis that still true?','0206_떡국',size=60,sec=4.5,instant=True,h=240),
  sc('예전 세는 나이로는\n새해가 오면 다 같이\n한 살씩 늘었어요.','In the old Korean way of counting,\neveryone gained a year together\nwhen the new year came.','0206_나이',sec=5.5),
  sc('2023년 6월 28일부터\n법과 공문서의 나이는\n만 나이로 통일됐어요.','Since June 28, 2023, Korean law and official documents\nuse international age.','0206_나이',sub='내 생일이 지나야 한 살이 늘어요.',size=54,sec=6.0,tag='만 나이'),
  sc('병역이나 청소년 보호처럼\n연 나이를 쓰는 법도 아직 있어요.','A few laws, such as military service and youth protection,\nstill count by calendar year.',None,size=48,sec=5.0),
  sc('떡국은 그대로,\n나이 세는 법만 바뀌었어요.','The tteokguk stays.\nOnly the way we count has changed.','0206_떡국',sub='내일 아침 떡국은 맛있게 드세요.',size=60,sec=5.5,step=0.9)],
 caption='''떡국 먹으면 한 살 더 먹는다던데, 지금도 그럴까요?

예전 세는 나이로는 새해가 오면 다 같이 한 살씩 늘었어요. 그런데 2023년 6월 28일부터 법과 공문서의 나이는 만 나이로 통일됐어요. 내 생일이 지나야 한 살이 늘어요. 병역이나 청소년 보호처럼 연 나이를 쓰는 법도 아직 있어요.

떡국은 그대로, 나이 세는 법만 바뀌었어요. 내일 아침 떡국은 맛있게 드세요.

이 영상의 소리는 다섯 가지 고요의 『Quiet Harbor』(수1 편)예요. 음악은 프로필 링크에서 들을 수 있어요.

· English ·
Eat a bowl of tteokguk (rice cake soup), gain a year: is that still true? In the old Korean way of counting, everyone gained a year together when the new year came. Since June 28, 2023, ages in Korean law and official documents use international age: you gain a year on your birthday. A few laws, such as military service and youth protection, still count by calendar year. The tteokguk stays; only the way we count has changed. Enjoy your bowl tomorrow morning.
Music in this video: Five Kinds of Quiet · Water · “Quiet Harbor”. Music: link in bio.

#고요 #떡국 #만나이 #설날 #오행음악''')
for k,v in P.items(): v['key']=k; v['end_art']={'file':A[v['end_art']],'h':200}; v['note']='정미년 시리즈 · '+v['name']
json.dump(P,open('/tmp/extra_specs.json','w'),ensure_ascii=False,indent=1)
only=sys.argv[1:]
if only==['dry']: sys.exit()
for k,v in P.items():
    if only and k not in only: continue
    p=f'shorts/정미년/spec/{k}.json'; json.dump(v,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    r=subprocess.run([sys.executable,'tools/week_src/jm_make.py',p],capture_output=True,text=True); print(k,r.returncode,r.stdout[-300:],r.stderr[-600:])
