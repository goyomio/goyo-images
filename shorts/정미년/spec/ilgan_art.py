import sys, math; sys.path.insert(0,'tools/week_src'); from jm_art import *
W,H=620,340
def year(p,x=0):
    p.flame(470+x,120,1.3); p.text(470+x,165,'丁',40,HI,True)
    p.ground(400+x,540+x,240,EARTH,3); p.text(470+x,190,'',1); p.text(470+x,282,'未',40,EARTH,True)
def drop(p,cx,cy,s=1,col=WATER):
    p.poly([(cx,cy-18*s),(cx+10*s,cy),(cx+8*s,cy+8*s),(cx,cy+12*s),(cx-8*s,cy+8*s),(cx-10*s,cy)],col,2,fill=col)
def mountain(p,x0,x1,base,top,col=EARTH):
    m=(x0+x1)/2; p.poly([(x0,base),(m-40,top+30),(m,top),(m+50,top+40),(x1,base)],col,4)
def ore(p,cx,cy,s=1,col=GOLD):
    p.poly([(cx-70*s,cy+20*s),(cx-50*s,cy-40*s),(cx-5*s,cy-60*s),(cx+55*s,cy-35*s),(cx+75*s,cy+15*s),(cx+25*s,cy+50*s),(cx-35*s,cy+48*s)],col,4)
    p.line([(cx-50*s,cy-40*s),(cx-10*s,cy),(cx+55*s,cy-35*s)],col,2); p.line([(cx-10*s,cy),(cx+25*s,cy+50*s)],col,2)
def lamp(p,cx,cy):
    p.rect(cx-40,cy-50,cx+40,cy+50,GOLD,3,10); p.flame(cx,cy+12,0.9); p.line([(cx-30,cy-62),(cx+30,cy-62)],GOLD,3); p.line([(cx,cy-62),(cx,cy-80)],GOLD,3)
out={}
# 병화
p=Pic(W,H); p.sun(310,150,70); p.line([(80,290),(540,290)],DIM,2); out['병화_sym']=p.save('일간_병화_해')
p=Pic(W,H); p.sun(310,80,45)
for k,x in enumerate([150,240,380,470]): p.arrow(310+(x-310)*0.25,140,x,225,HI,3)
p.ground(90,530,240,EARTH,4); out['병화_ex']=p.save('일간_병화_흙많으면')
p=Pic(W,H); p.sun(150,150,55); p.text(150,250,'丙',40,HI,True); year(p); out['병화_yr']=p.save('일간_병화_정미')
# 무토
p=Pic(W,H); mountain(p,90,530,290,60); out['무토_sym']=p.save('일간_무토_산')
p=Pic(W,H); mountain(p,140,480,240,50); p.waves(80,540,262,WATER,3)
for x in [220,300,390]: p.tree(x,215,60,WOOD)
out['무토_ex']=p.save('일간_무토_물적심')
p=Pic(W,H); mountain(p,60,280,280,90); p.text(170,295,'',1); year(p); drop(p,360,200,1.4); out['무토_yr']=p.save('일간_무토_정미')
# 기토
p=Pic(W,H); 
for k in range(4): p.line([(70+k*20,140+k*45),(550-k*20,140+k*45)],EARTH,4)
for k in range(4):
    for j in range(5): p.circ(130+j*90+k*8,165+k*45,5,WOOD,2,fill=WOOD)
out['기토_sym']=p.save('일간_기토_밭흙')
p=Pic(W,H); p.ground(90,530,110,EARTH,5)
for j in range(6): p.circ(140+j*68,190,7,WOOD,2,fill=WOOD)
p.line([(310,40),(310,300)],GOLD,2); p.text(310,8,'中',30,GOLD,True); out['기토_ex']=p.save('일간_기토_가운데품음')
p=Pic(W,H); p.flame(120,140,1.3); p.text(120,185,'丁',40,HI,True); p.arrow(170,150,300,150,GOLD,4)
p.ground(330,560,150,EARTH,3); p.text(445,200,'己',44,EARTH,True); p.text(445,255,'未 속에도 己',26,FG); out['기토_yr']=p.save('일간_기토_정미')
# 정화
p=Pic(W,H); lamp(p,310,170); out['정화_sym']=p.save('일간_정화_등불')
p=Pic(W,H); lamp(p,390,170); p.tree(190,290,200,WOOD,bare=True); p.text(190,300,'甲',30,WOOD,True)
for x,y in [(80,60),(540,70),(500,260),(90,200)]: p.snow(x,y,14)
out['정화_ex']=p.save('일간_정화_나무와겨울')
p=Pic(W,H); lamp(p,200,170); p.text(200,250,'나',30,FG,True); lamp(p,420,170); p.text(420,250,'丁',36,HI,True); out['정화_yr']=p.save('일간_정화_두등불')
# 경금
p=Pic(W,H); ore(p,310,170,1.6); out['경금_sym']=p.save('일간_경금_원석')
p=Pic(W,H); ore(p,170,150,0.9); p.flame(170,270,1.0); p.arrow(260,160,360,160,GOLD,4)
p.poly([(390,200),(560,120),(570,135),(400,215)],GOLD,3); p.line([(390,200),(370,230)],GOLD,6); out['경금_ex']=p.save('일간_경금_불과날')
p=Pic(W,H); ore(p,160,170,0.9); p.text(160,265,'庚',40,GOLD,True); p.flame(430,170,1.5); p.text(430,230,'丁',44,HI,True); p.arrow(380,170,260,170,HI,4); out['경금_yr']=p.save('일간_경금_정미')
# 임수
p=Pic(W,H); p.waves(60,560,130,WATER,5); out['임수_sym']=p.save('일간_임수_큰물')
p=Pic(W,H); p.flame(150,150,1.4); p.text(150,200,'丁',40,HI,True); p.waves(380,560,120,WATER,3); p.text(470,200,'壬',40,WATER,True)
p.arrow(220,140,300,140,GOLD,3); p.arrow(370,170,290,170,GOLD,3); p.text(310,240,'丁壬合',32,GOLD,True); out['임수_ex']=p.save('일간_임수_합')
p=Pic(W,H); p.waves(60,560,190,WATER,3)
for x in [140,260,380,500]: p.rect(x-22,140,x+22,180,GOLD,2,6); p.flame(x,170,0.5)
out['임수_yr']=p.save('일간_임수_등불강물')
# 계수
p=Pic(W,H)
for x,y in [(150,80),(260,140),(370,60),(470,150),(200,230),(420,250),(310,210)]: drop(p,x,y,1.3)
out['계수_sym']=p.save('일간_계수_비')
p=Pic(W,H); p.flame(250,140,1.3); p.ground(150,350,210,EARTH,2)
pts=[(560,40)]+[(560-k*20, 40+k*14+30*math.sin(k/2)) for k in range(1,18)]
p.line([(x,y) for x,y in pts],WATER,4); drop(p,220,290,1.0); drop(p,560,40,1.0); out['계수_ex']=p.save('일간_계수_흐름따라')
p=Pic(W,H); year(p,-160)
for x,y in [(460,80),(520,150),(420,200),(540,260)]: drop(p,x,y,1.2)
out['계수_yr']=p.save('일간_계수_정미')
import json; json.dump(out,open('/tmp/ilgan_art.json','w'),ensure_ascii=False); print(len(out))
