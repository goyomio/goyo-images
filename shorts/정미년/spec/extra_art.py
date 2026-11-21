import sys, math, json; sys.path.insert(0,'tools/week_src'); from jm_art import *
W,H=620,340; A={}
def drop(p,cx,cy,s=1,col=WATER): p.poly([(cx,cy-18*s),(cx+10*s,cy),(cx+8*s,cy+8*s),(cx,cy+12*s),(cx-8*s,cy+8*s),(cx-10*s,cy)],col,2,fill=col)
def moon(p,cx,cy,r,col=ICE): p.circ(cx,cy,r,col,3); p.circ(cx+r*0.45,cy-r*0.25,r*0.85,(0,0,0,0),0,fill=None)
def crescent(p,cx,cy,r,col=ICE):
    pts=[(cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a))) for a in range(60,301,10)]
    pts2=[(cx+r*0.55+r*0.8*math.cos(math.radians(a)),cy+r*0.8*math.sin(math.radians(a))) for a in range(300,59,-10)]
    p.poly(pts+pts2,col,3)
# 1/13 겨울나무
p=Pic(W,H); p.tree(310,300,240,WOOD,bare=True); [p.snow(x,y,12) for x,y in [(110,70),(500,60),(540,200),(90,230)]]; A['0113_겨울나무']=p.save('0113_겨울나무')
p=Pic(W,H); p.line([(80,250),(540,120)],WOOD,6)
for t in [0.3,0.55,0.8]:
    x=80+460*t; y=250-130*t; p.poly([(x,y-6),(x+16,y-40),(x+30,y-8)],HI,3,fill=(232,205,150,90))
p.text(470,260,'겨울눈',28,FG,True); A['0113_겨울눈']=p.save('0113_겨울눈')
p=Pic(W,H); p.text(130,40,'여름 · 가을',26,FG,True); p.poly([(100,200),(130,120),(160,200)],HI,3); p.arrow(220,160,390,160,GOLD,4); p.text(305,190,'겨울을 지나',24,DIM)
p.snow(305,110,18); p.line([(480,260),(480,170)],WOOD,5); p.poly([(480,170),(450,130),(480,145),(510,120)],WOOD,3,fill=WOOD); p.text(480,280,'봄',28,FG,True); A['0113_눈에서봄']=p.save('0113_눈에서봄')
p=Pic(W,H); p.waves(70,300,200,WATER,3); p.text(185,270,'水',44,WATER,True); p.arrow(320,190,420,190,GOLD,4); p.tree(500,290,180,WOOD); p.text(500,300,'',1); A['0113_수생목']=p.save('0113_수생목')
# 1/16 잠들기 전 피아노
p=Pic(W,H); crescent(p,440,110,60); p.waves(60,560,250,WATER,3); A['0116_달과물']=p.save('0116_달과물')
p=Pic(W,H)
for i in range(14): p.rect(60+i*36,120,92+i*36,300,FG,2,3)
for i in [0,1,3,4,5,7,8,10,11,12]: p.rect(84+i*36,120,104+i*36,220,FG,1,2,fill=(236,233,226,255))
A['0116_건반']=p.save('0116_건반')
p=Pic(W,H); p.poly([(260,300),(360,300),(330,60),(290,60)],GOLD,3); p.line([(310,280),(370,110)],HI,4); p.circ(355,150,10,HI,2,fill=HI); p.text(470,150,'52–60',40,FG,True); p.text(470,200,'BPM',24,DIM); A['0116_메트로놈']=p.save('0116_메트로놈')
p=Pic(W,H); p.text(310,40,'',1)
for k,(lab,y) in enumerate([('5도',90),('3도 (비움)',170),('1도',250)]):
    col=DIM if k==1 else HI
    if k==1: p.circ(200,y,22,col,2)
    else: p.circ(200,y,22,col,3,fill=col)
    p.text(360,y-16,lab,28,col,True)
A['0116_3도비움']=p.save('0116_3도비움')
# 1/22 나이테
p=Pic(W,H)
rs=[18,34,44,70,80,92,120,128]
for r in rs: p.circ(310,170,r*1.2,WOOD,2)
A['0122_나이테']=p.save('0122_나이테')
p=Pic(W,H); p.tree(160,290,170,WOOD,bare=True); [p.snow(x,y,10) for x,y in [(70,80),(250,60)]]; p.flame(160,320-0,0.01,(0,0,0,0)); p.flame(260,240,1.0); p.text(160,300,'',1); p.text(200,20,'',1)
p.sun(480,90,30); p.tree(480,290,170,WOOD); p.flame(560,240,1.0); p.flame(400,240,1.0); A['0122_겨울과여름']=p.save('0122_겨울과여름')
p=Pic(W,H); cols=[WOOD,HI,EARTH,GOLD,WATER]; labs=['木','火','土','金','水']
for i in range(5):
    a=math.radians(-90+i*72); x=310+120*math.cos(a); y=170+120*math.sin(a); p.circ(x,y,34,cols[i],3); p.text(x,y-22,labs[i],34,cols[i],True)
A['0122_다섯']=p.save('0122_다섯오행')
# 1/27 불씨
def hwaro(p,cx,cy,emb=True):
    p.poly([(cx-110,cy-30),(cx+110,cy-30),(cx+80,cy+60),(cx-80,cy+60)],EARTH,4); p.line([(cx-90,cy+60),(cx-100,cy+90)],EARTH,4); p.line([(cx+90,cy+60),(cx+100,cy+90)],EARTH,4)
    if emb: p.flame(cx,cy-40,0.8)
p=Pic(W,H); hwaro(p,310,200); A['0127_화로']=p.save('0127_화로')
p=Pic(W,H); hwaro(p,310,200,False); p.ground(220,400,150,DIM,3); p.circ(310,190,12,HI,2,fill=HI); p.circ(310,120,22,DIM,3); p.text(470,100,'재로 덮고',24,FG); p.text(470,135,'돌을 얹어',24,FG); A['0127_재속불씨']=p.save('0127_재속불씨')
p=Pic(W,H); p.rect(200,40,420,300,EARTH,4,14); p.text(310,60,'未',56,EARTH,True)
for i,(c,col) in enumerate([('丁',HI),('乙',WOOD),('己',EARTH)]): p.text(250+i*60,200,c,40,col,True)
p.circ(250,222,34,HI,3); A['0127_미속정']=p.save('0127_미속정')
# 1/29 일진
p=Pic(W,H); p.rect(200,30,420,310,GOLD,3,14); p.line([(200,90),(420,90)],GOLD,3); p.text(310,45,'1월 28일',28,FG,True); p.vtext(310,110,'丁未',72,HI,True,10); A['0129_달력']=p.save('0129_달력')
p=Pic(W,H)
for i in range(60):
    a=math.radians(-90+i*6); x=310+130*math.cos(a); y=170+130*math.sin(a); p.circ(x,y,4 if i%10 else 7,HI if i==0 else GOLD,1,fill=HI if i==0 else GOLD)
p.text(310,140,'60',52,FG,True); A['0129_60']=p.save('0129_60갑자')
p=Pic(W,H); labs=['시','일','월','연']
for k,l in enumerate(labs):
    x=60+k*125
    for r in range(2):
        y=40+r*110; hl=(l=='일' and r==0); p.rect(x,y,x+100,y+95,HI if hl else GOLD,5 if hl else 3,12,fill=(232,205,150,60) if hl else None)
    p.text(x+50,250,l,30,FG,True)
p.text(60+125+50,70,'나',30,FG,True); A['0129_네기둥']=p.save('0129_네기둥')
# 1/31 입춘첩
p=Pic(W,H); p.rect(150,20,470,330,EARTH,4,4); p.line([(310,20),(310,330)],EARTH,3)
def tag(p,cx,cy,ang,txt):
    import math as m
    w,h=50,170; a=m.radians(ang); pts=[(-w/2,-h/2),(w/2,-h/2),(w/2,h/2),(-w/2,h/2)]
    p.poly([(cx+x*m.cos(a)-y*m.sin(a),cy+x*m.sin(a)+y*m.cos(a)) for x,y in pts],HI,3)
    p.vtext(cx,cy-74,txt,30,HI,True,6)
tag(p,250,160,12,'建陽多慶'); tag(p,370,160,-12,'立春大吉'); A['0131_입춘첩']=p.save('0131_입춘첩')
p=Pic(W,H); p.line([(80,250),(540,250)],DIM,2); p.sun(470,200,40); p.text(470,280,'동(東)',30,FG,True); p.tree(160,250,170,WOOD); p.text(160,280,'봄 · 木',30,WOOD,True); A['0131_동쪽']=p.save('0131_동쪽')
# 2/1 청자
def vase(p,cx,cy,s=1,col=(150,190,180,255)):
    prof=[(0,14),(12,16),(22,40),(40,72),(60,78),(110,62),(170,42),(220,34),(232,36)]
    top=cy-120*s; R=[(cx+r*s,top+y*s) for y,r in prof]; L=[(cx-r*s,top+y*s) for y,r in reversed(prof)]
    p.poly(R+L,col,4); p.line([(cx-14*s,top),(cx+14*s,top)],col,4)
    p.line([(cx-55*s,top+90*s),(cx+55*s,top+90*s)],col,1)
p=Pic(W,H); vase(p,310,190); A['0201_청자']=p.save('0201_청자')
p=Pic(W,H); p.ground(80,300,220,EARTH,3); p.text(190,250,'土',40,EARTH,True); p.waves(340,560,200,WATER,3); p.text(450,250,'水',40,WATER,True); A['0201_흙물']=p.save('0201_흙물')
p=Pic(W,H); p.tree(140,290,170,WOOD,bare=True); p.text(140,300,'',1); p.arrow(220,200,320,200,GOLD,4); p.flame(420,200,1.8); p.text(420,250,'1,200℃ 넘게',28,FG,True); A['0201_나무불']=p.save('0201_나무불')
p=Pic(W,H); vase(p,200,190,0.8); p.text(430,120,'Fe',50,GOLD,True); p.text(430,190,'유약 속 철분',26,FG); p.text(430,225,'약 1%',30,HI,True); A['0201_철분']=p.save('0201_철분')
# 2/3 토왕용사
p=Pic(W,H); p.circ(310,170,120,GOLD,3)
for i,(lab,col) in enumerate([('春 木',WOOD),('夏 火',HI),('秋 金',GOLD),('冬 水',WATER)]):
    a=math.radians(-90+i*90+45); p.text(310+80*math.cos(a),170+80*math.sin(a)-16,lab,26,col,True)
for i in range(4):
    a=math.radians(-90+i*90); p.circ(310+120*math.cos(a),170+120*math.sin(a),16,EARTH,3,fill=EARTH)
p.text(310,155,'土',36,EARTH,True); A['0203_사계토']=p.save('0203_사계토')
p=Pic(W,H); p.line([(60,170),(560,170)],DIM,3)
for i in range(18): p.circ(120+i*22,170,6,EARTH,1,fill=EARTH)
p.text(310,100,'입춘 앞 18일',30,FG,True); p.circ(530,170,14,WOOD,3,fill=WOOD); p.text(530,200,'입춘',24,WOOD,True); A['0203_18일']=p.save('0203_18일')
# 2/4 입춘
p=Pic(W,H); p.circ(310,170,130,GOLD,2); p.circ(310,170,30,DIM,2); p.text(310,155,'地',26,DIM,True)
a=math.radians(-90+315); x=310+130*math.cos(a); y=170+130*math.sin(a); p.sun(x,y,16); p.text(500,40,'315°',34,HI,True); A['0204_황경']=p.save('0204_황경315')
p=Pic(W,H); p.text(170,60,'丙午',50,DIM,True); p.text(170,130,'10:46 전',28,DIM); p.arrow(260,110,360,110,GOLD,4); p.text(450,60,'丁未',50,HI,True); p.text(450,130,'10:46 이후',28,FG); p.flame(450,250,1.4); A['0204_바뀜']=p.save('0204_병오정미')
# 2/6 설날
p=Pic(W,H); p.sun(170,150,50); p.text(170,250,'입춘 2/4',28,FG,True); crescent(p,450,150,55); p.text(450,250,'설날 2/7',28,FG,True); A['0206_해와달']=p.save('0206_해와달')
p=Pic(W,H); 
for i,(d,lab,col) in enumerate([('2/4','입춘',HI),('2/5','',DIM),('2/6','',DIM),('2/7','설날',ICE)]):
    x=110+i*130; p.rect(x-50,80,x+50,220,col,3,10); p.text(x,100,d,30,FG,True); p.text(x,170,lab,26,col,True)
p.line([(60,260),(450,260)],HI,4); p.text(255,275,'사주로는 이미 정미년',24,HI,True); A['0206_나흘']=p.save('0206_나흘')
# 2/6 떡국
p=Pic(W,H); p.d.ellipse(p.p(170,150,450,200),outline=GOLD,width=6); p.line([(175,175),(220,290),(400,290),(445,175)],GOLD,4)
for x in [240,290,340,380]: p.d.ellipse(p.p(x-20,160,x+20,182),outline=FG,width=4)
A['0206_떡국']=p.save('0206_떡국')
p=Pic(W,H); p.text(170,60,'세는 나이',30,DIM,True); p.text(170,110,'설에 다 같이 +1',24,DIM); p.arrow(280,110,350,110,GOLD,4); p.text(460,60,'만 나이',30,HI,True); p.text(460,110,'내 생일에 +1',24,FG); p.text(310,220,'2023. 6. 28.',40,FG,True); A['0206_나이']=p.save('0206_나이')
json.dump(A,open('/tmp/extra_art.json','w'),ensure_ascii=False); print(len(A))
