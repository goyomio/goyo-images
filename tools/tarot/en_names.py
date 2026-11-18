#!/usr/bin/env python3
"""python3 tools/tarot/en_names.py posts/<date>-tarot/tarot.json → 영어 캡션에 쓸 자리·카드 영어 이름 (카드 이름은 여기 것만 씀)"""
import json, sys
MAJ_EN=['The Fool','The Magician','The High Priestess','The Empress','The Emperor','The Hierophant','The Lovers','The Chariot','Strength','The Hermit','Wheel of Fortune','Justice','The Hanged Man','Death','Temperance','The Devil','The Tower','The Star','The Moon','The Sun','Judgement','The World']
SU_EN={'wands':'Wands','cups':'Cups','swords':'Swords','pents':'Pentacles'}
RK_EN=['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Page','Knight','Queen','King']
POS_EN=["Today's flow","What to keep","What to let go"]
cfg=json.load(open(sys.argv[1]))
for p,c in zip(POS_EN,cfg['cards']):
    i=c['id']; n=MAJ_EN[int(i[1:])] if i.startswith('m') else f"{RK_EN[int(i[-2:])-1]} of {SU_EN[i[:-2]]}"
    print(f"{p}: {n}{' (reversed)' if c.get('rev') else ''}")
