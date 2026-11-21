import sys; sys.path.insert(0,'tools/week_src'); from jm_art import *
# 만세력 네 기둥, 오른쪽부터
p=Pic(600,340); labs=['시','일','월','연']
for k,l in enumerate(labs):
    x=60+k*125
    for r in range(2):
        y=40+r*110; hl=(l=='일' and r==0)
        p.rect(x,y,x+100,y+95,HI if hl else GOLD,5 if hl else 3,12,fill=(232,205,150,60) if hl else None)
    p.text(x+50,250,l,30,FG,True)
p.text(60+125+50,70,'나',30,FG,True)
p.arrow(560,310,90,310,GOLD,3); p.text(330,318,'',1)
a1=p.save('0111_네기둥')
# 열 천간 → 열 편
p=Pic(620,330); stems=[('甲','갑목'),('乙','을목'),('丙','병화'),('丁','정화'),('戊','무토'),('己','기토'),('庚','경금'),('辛','신금'),('壬','임수'),('癸','계수')]
cols=[WOOD,WOOD,HI,HI,EARTH,EARTH,GOLD,GOLD,WATER,WATER]
for i,(h,k) in enumerate(stems):
    r,c=divmod(i,5); x=70+c*120; y=60+r*150
    p.circ(x,y,40,cols[i],3); p.text(x,y-24,h,34,cols[i],True); p.text(x,y+48,k+' 편',22,FG)
a2=p.save('0111_열편')
print(a1,a2)
