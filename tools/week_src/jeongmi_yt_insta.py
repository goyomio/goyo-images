import json,os,subprocess,datetime,shutil,sys
R='/home/claude/goyo-images'; os.chdir(R)
OUT='/home/claude/jm/ytout'; shutil.rmtree(OUT,ignore_errors=True)
V={'병화':'oIt-DzA96Bw','무토':'q8w4WV76ah4','기토':'8hLmKk8ag08','정화':'xDGOypKeG_s','경금':'VzDuEs2i5es','임수':'m_t33eB1bkc','계수':'wzt4ETUmOto','갑목':'g3Eeu8QVaJY','신금':'6p_X4z3terE','을목':'jtYiLzQkUJs','토1':'VxV9ePEWoj4'}
NM={'병화':'병화(丙火) 편','무토':'무토(戊土) 편','기토':'기토(己土) 편','정화':'정화(丁火) 편','경금':'경금(庚金) 편','임수':'임수(壬水) 편','계수':'계수(癸水) 편','갑목':'갑목(甲木) 편','신금':'신금(辛金) 편','을목':'을목(乙木) 편','토1':'토(土) 본편'}
PL='https://www.youtube.com/playlist?list=PLRm375HI5ZcA'
WD='월화수목금토일'
def fold(m,d):
    dt=datetime.date(2027,m,d); n=(dt-datetime.date(2026,12,31)).days+1
    return '%02d_%02d-%02d(%s)'%(n,m,d,WD[dt.weekday()])
def links(p):
    v=V[p]
    ko=f"{NM[p]} 음악 ▶ https://youtu.be/{v}\n고요 오행음악 전체 듣기 ▶ {PL}\n무료 사주앱 (내 일간 찾기) ▶ https://goyomio.com\n매일 아침 오늘의 타로 보기 (인스타그램) ▶ https://www.instagram.com/goyo_mio"
    en=f"Music ▶ https://youtu.be/{v}\nAll GOYO five-element music ▶ {PL}\nFree Saju app (find your Day Master) ▶ https://goyomio.com\nDaily tarot on Instagram ▶ https://www.instagram.com/goyo_mio"
    return ko,en
KO_REP=[('프로필 링크에 있어요','아래 링크에 있어요'),('프로필 링크의 무료 앱','아래 링크의 무료 앱'),('프로필 링크에서','아래 링크에서'),('프로필 링크','아래 링크'),('피드 게시물','채널 게시물'),('9시 릴스','9시 쇼츠'),('릴스','쇼츠')]
EN_REP=[('(link in bio)','(link below)'),('Listen at the link in bio','Listen at the links below'),('9 p.m. reel','9 p.m. Short'),('linked in our bio','linked below'),('Listen through the link in bio','Listen through the links below'),('link in bio','links below'),('in our bio','below'),("today's feed post",'today’s channel post'),('our feed post','our channel post'),('feed post','channel post')]
def conv(c,p,shorts):
    ko,en=c.split('\n\n· English ·\n')
    for a,b in KO_REP: ko=ko.replace(a,b)
    for a,b in EN_REP: en=en.replace(a,b)
    en_body,hs=en.rsplit('\n\n',1)
    hs=' '.join(hs.split()[:3]) if shorts else hs
    lk,le=links(p)
    d=f"{ko}\n\n{lk}\n\n· English ·\n{en_body}\n\n{le}\n\n{hs}"
    for bad in ['프로필','피드','bio','feed post','릴스',' reel']: assert bad not in d,(bad,d[:80])
    return d
# 캐러셀 (월 일, 음악 편)
CAR={'0113':'경금','0114':'기토','0115':'병화','0118':None,'0121':'경금','0122':'계수','0124':'토1','0125':None,'0127':'계수','0128':'기토','0129':'을목','0131':'기토','0201':None,'0203':'신금','0204':'계수','0205':'기토','0207':'갑목'}
# 쇼츠: key -> (영상, 편, 제목, 태그)
SH={
'0113-1820':('jeongmi/0113/short_yt.mp4','경금','정미년 곁에 둘 소리, 바위와 비｜Stone and Rain for 2027',['정미년','경금','계수','오행','오행음악']),
'0114-2100':('shorts/그림편/유튜브/그림03 밀레 이삭줍기.mp4','기토','밀레 〈이삭줍기〉, 거둔 뒤에 남은 것｜Millet’s The Gleaners',['밀레','이삭줍기','명화','오행','오행음악']),
'0115-1820':('jeongmi/0115/short_yt.mp4','병화','바다를 바라보는 절, 김제 망해사의 해넘이｜Manghaesa, Gimje',['망해사','김제','병화','오행','오행음악']),
'0121-2100':('shorts/그림편/유튜브/그림04 정선 인왕제색도.mp4','경금','정선 〈인왕제색도〉, 비 갠 뒤의 바위｜After Rain at Mt. Inwang',['인왕제색도','정선','명화','오행','오행음악']),
'0122-1820':('jeongmi/0122/short_yt.mp4','계수','그림 속 그 산으로, 인왕산 수성동 계곡｜Mt. Inwang, Seoul',['인왕산','수성동계곡','계수','오행','오행음악']),
'0124-1820':('jeongmi/0124/short_yt.mp4','토1','지평선이 보이는 들, 전북 김제｜Gimje, Where Land Meets Sky',['김제','지평선','정미년','오행','오행음악']),
'0127-1820':('jeongmi/0127/short_yt.mp4','계수','보름밤 물과 하늘에 띄우는 불, 치앙마이 이펭｜Yi Peng, Chiang Mai',['치앙마이','이펭','정화','오행','오행음악']),
'0128-2100':('shorts/그림편/유튜브/그림05 모네 건초더미.mp4','기토','모네 〈건초더미(여름의 끝)〉, 쌓아 둔 수확｜Monet’s Stacks of Wheat',['모네','건초더미','명화','오행','오행음악']),
'0129-1820':('jeongmi/0129/short_yt.mp4','을목','같은 정미년, 일간마다 열 가지 얼굴｜One Year, Ten Day Masters',['정미년','일간','2027년운세','오행','오행음악']),
'0131-1820':('jeongmi/0131/short_yt.mp4','기토','책상 위 정미년, 작은 등 하나와 흙 화분｜A Lamp and a Clay Pot',['정미년','토분','정화','오행','오행음악']),
'0203-1820':('jeongmi/0203/short_yt.mp4','신금','마른 해 곁에 둘 것, 유리 물병과 놋그릇·풍경｜Water, Brass and a Wind Bell',['풍경','놋그릇','정미년','오행','오행음악']),
'0204-2100':('shorts/그림편/유튜브/그림06 히로시게 소나기.mp4','계수','히로시게 〈아타케의 소나기〉, 하늘의 물｜Hiroshige’s Sudden Shower',['히로시게','우키요에','명화','오행','오행음악']),
'0205-1820':('jeongmi/0205/short_yt.mp4','기토','모네의 마을 지베르니, 그 들판에 가면｜Giverny, Monet’s Village',['지베르니','모네','여행','오행','오행음악']),
'0207-1820':('jeongmi/0207/short_yt.mp4','갑목','설날 윷놀이, 단단한 나무 네 가락｜Yut on Seollal',['윷놀이','설날','갑목','오행','오행음악']),
}
FN={'0113-1820': '바위의 소리 비의 소리', '0114-2100': '밀레 이삭줍기', '0115-1820': '김제 망해사', '0121-2100': '정선 인왕제색도', '0122-1820': '서울 인왕산', '0124-1820': '전북 김제', '0127-1820': '치앙마이 이펭', '0128-2100': '모네 건초더미', '0129-1820': '같은 해 열 가지 얼굴', '0131-1820': '작은 등 하나 흙 화분 하나', '0203-1820': '유리 물병 놋그릇 풍경', '0204-2100': '히로시게 소나기', '0205-1820': '지베르니', '0207-1820': '설날 윷'}
log=[]
for d,p in CAR.items():
    m,dd=int(d[:2]),int(d[2:]); f=fold(m,dd); out=f'{OUT}/{f}/18시00분 게시물'
    r=subprocess.run(['python3','tools/week_src/jeongmi_yt.py',R,d,out],capture_output=True,text=True)
    assert r.returncode==0,r.stderr
    diffs=[float(l.split()[-1]) for l in r.stdout.strip().split('\n')]
    c=json.load(open(f'posts/2027-{d[:2]}-{d[2:]}/post.json'))['caption']
    if p is None:  # 음악 없는 캐러셀: 링크 묶음은 재생목록 기준
        ko,en=c.split('\n\n· English ·\n')
        for a,b in KO_REP: ko=ko.replace(a,b)
        for a,b in EN_REP: en=en.replace(a,b)
        eb,hs=en.rsplit('\n\n',1)
        desc=f"{ko}\n\n고요 오행음악 전체 듣기 ▶ {PL}\n무료 사주앱 (내 일간 찾기) ▶ https://goyomio.com\n매일 아침 오늘의 타로 보기 (인스타그램) ▶ https://www.instagram.com/goyo_mio\n\n· English ·\n{eb}\n\nAll GOYO five-element music ▶ {PL}\nFree Saju app (find your Day Master) ▶ https://goyomio.com\nDaily tarot on Instagram ▶ https://www.instagram.com/goyo_mio\n\n{hs}"
    else: desc=conv(c,p,False)
    n=len(os.listdir(out))
    txt=f"[유튜브 채널 게시물(이미지) 업로드 안내 · 2027-{d[:2]}-{d[2:]} 18:00]\n올릴 사진: 이 폴더의 01.jpg ~ {n:02d}.jpg ({n}장, 번호 순서대로)\n예약 시각: 2027-{d[:2]}-{d[2:]} 18:00 (KST)\n\n■ 게시물 글\n{desc}\n"
    open(f'{out}/업로드 안내.txt','w').write(txt); log.append((d,'게시물',n,max(diffs)))
for k,(src,p,title,tags) in SH.items():
    d,s=k.split('-'); m,dd=int(d[:2]),int(d[2:]); f=fold(m,dd)
    slot=f'{s[:2]}시{s[2:]}분 쇼츠'; out=f'{OUT}/{f}/{slot}'; os.makedirs(out,exist_ok=True)
    c=json.load(open(f'posts/2027-{d[:2]}-{d[2:]}-{s}/post.json'))['caption']
    name=FN[k] #.rstrip('.').replace('〈','').replace('〉','').replace(',','').replace('/','·')[:30].strip()
    mp=f'{out}/쇼츠_{name}.mp4'; shutil.copy(src,mp)
    subprocess.run(['ffmpeg','-v','error','-y','-ss','1.5','-i',mp,'-frames:v','1','-q:v','2',f'{out}/쇼츠_썸네일.jpg'],check=True)
    assert len(title)<=100
    desc=conv(c,p,True); v=V[p]
    txt=f"""[유튜브 쇼츠 업로드 안내 · {k}]
올릴 파일: {f}/{slot}/{os.path.basename(mp)} (썸네일: 같은 폴더 쇼츠_썸네일.jpg)
예약 시각: 2027-{d[:2]}-{d[2:]} {s[:2]}:{s[2:]} (KST)
붙일 음악 영상(관련 동영상): {NM[p]} — https://youtu.be/{v}
설정: 아동용 아님 · AI 사용 「예」 · 언어 한국어 · 재생목록 GOYO 오행음악

■ 제목 ({len(title)}자)
{title}

■ 설명
{desc}

■ 태그 (5개)
{', '.join(tags)}
"""
    open(f'{out}/업로드 안내.txt','w').write(txt); log.append((k,'쇼츠',os.path.basename(mp),len(title)))
for l in log: print(l)
