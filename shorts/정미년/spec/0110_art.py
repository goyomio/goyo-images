import sys; sys.path.insert(0,'tools/week_src'); from jm_art import *
# 성문 + 세로 현판
p=Pic(520,330)
p.poly([(60,150),(260,70),(460,150)],GOLD,4); p.poly([(100,150),(260,95),(420,150)],GOLD,3)
p.rect(110,150,410,190,GOLD,3,4); p.rect(80,190,440,300,GOLD,3,6)
p.d.arc(p.p(205,215,315,330),180,360,fill=GOLD,width=4*S)
p.rect(240,105,280,175,HI,3,4); p.vtext(260,108,'崇禮',sz=26,col=HI,gap=2)
a1=p.save('0110_성문')
# 오행-오상
p=Pic(560,330); pts=[('木','仁',280,50),('火','禮',470,150),('土','信',400,290),('金','義',160,290),('水','智',90,150)]
for i,(e,v,x,y) in enumerate(pts):
    col=HI if e=='火' else GOLD; p.circ(x,y,40,col,4 if e=='火' else 3); p.text(x,y-30,e,30,col,True); p.text(x,y+4,v,24,FG)
a2=p.save('0110_오상')
# 도성 지도
p=Pic(560,340); p.circ(280,170,130,DIM,2)
for t,x,y,col in [('흥인지문 · 仁',280+150,160,GOLD),('돈의문 · 義',280-150,160,GOLD),('숭례문 · 禮',280,300,HI)]:
    p.text(x,y,t,24,col,True)
p.circ(280,170,10,GOLD,3,fill=GOLD); p.text(280,185,'보신각 · 信',22,FG,True)
p.arrow(280,180,280,285,HI,3)
a3=p.save('0110_도성')
# 관악산 + 세로 현판
p=Pic(560,330)
p.line([(40,280),(120,200),(160,230),(230,120),(300,220),(350,170),(420,280)],HI,4)
p.text(230,290,'관악산',24,DIM)
p.rect(470,40,520,250,HI,3,6); p.vtext(495,55,'崇禮門',sz=40,col=HI,gap=16)
p.arrow(440,150,330,150,GOLD,3)
a4=p.save('0110_관악산')
# 남지 연못
p=Pic(560,300); p.rect(170,40,390,150,GOLD,3,6); p.d.arc(p.p(250,95,310,175),180,360,fill=GOLD,width=4*S)
p.d.ellipse(p.p(130,190,430,270),outline=WATER,width=4*S); p.waves(170,390,215,WATER,2)
p.text(280,272,'남지(南池)',22,DIM)
a5=p.save('0110_남지')
print(a1,a2,a3,a4,a5)
