#!/usr/bin/env python3
"""1909 원판 덱에서 무작위 3장 (역방향 포함, 디지털 추첨). 출력: JSON [{"id","ko","rev","file"}]"""
import json, random, os, sys
MAJ=[("Fool","바보"),("Magician","마법사"),("High Priestess","여사제"),("Empress","여황제"),("Emperor","황제"),("Hierophant","교황"),("Lovers","연인"),("Chariot","전차"),("Strength","힘"),("Hermit","은둔자"),("Wheel of Fortune","운명의 수레바퀴"),("Justice","정의"),("Hanged Man","매달린 사람"),("Death","죽음"),("Temperance","절제"),("Devil","악마"),("Tower","탑"),("Star","별"),("Moon","달"),("Sun","태양"),("Judgement","심판"),("World","세계")]
SU=[("wands","완드"),("cups","컵"),("swords","소드"),("pents","펜타클")]
RK=["에이스","2","3","4","5","6","7","8","9","10","시종","기사","여왕","왕"]
deck=[{"id":f"m{i:02d}","ko":ko,"file":f"m{i:02d}_{en.lower().replace(' ','-')}.jpg"} for i,(en,ko) in enumerate(MAJ)]
deck+=[{"id":f"{k}{r:02d}","ko":f"{ko} {RK[r-1]}","file":f"{k}{r:02d}.jpg"} for k,ko in SU for r in range(1,15)]
here=os.path.dirname(os.path.abspath(__file__)); dd=os.path.join(here,'..','..','deck_1909')
assert all(os.path.exists(os.path.join(dd,c['file'])) for c in deck), 'deck file missing'
rng=random.SystemRandom(); picks=rng.sample(deck,3)
print(json.dumps([dict(c,rev=rng.random()<0.5) for c in picks],ensure_ascii=False))
