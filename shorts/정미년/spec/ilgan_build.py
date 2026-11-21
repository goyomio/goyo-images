import os
import json, re, subprocess, sys
D=json.load(open('/home/claude/jm/ilgan_reviewed.json')); A=json.load(open('/tmp/ilgan_art.json'))
D['1/30 임수']['tie_en']="The 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth opens with that very partner, 丁, like the lamps on the river in our January 3 post."
FG=[236,233,226]; EN=[214,210,202]; GD=[200,180,140]; DM=[190,186,178]
META={
'병화':dict(date='2027-01-12',hj='丙火',en='Yang Fire',ro='Byeonghwa',pyeon='병화',title='Rooftop Glow',file='/home/claude/goyo-keys/audio/병화/08 Rooftop Glow.m4a',hms='24:23',mk='병화(丙火)',gl='Much earth makes it kind.'),
'무토':dict(date='2027-01-16',hj='戊土',en='Yang Earth',ro='Muto',pyeon='무토',title='Quiet Ridge',file='/home/claude/goyo-keys/audio/무토/05 Quiet Ridge.m4a',hms='9:39',mk='무토(戊土)',gl='Moistened by water, all things live.'),
'기토':dict(date='2027-01-19',hj='己土',en='Yin Earth',ro='Gito',pyeon='기토',title='Kitchen Garden',file='/home/claude/goyo-keys/audio/기토/05 Kitchen Garden.m4a',hms='12:52',mk='기토(己土)',gl='Centered and upright, it stores and holds.'),
'정화':dict(date='2027-01-23',hj='丁火',en='Yin Fire',ro='Jeonghwa',pyeon='정화',title='Warm Wax',file='/home/claude/goyo-keys/audio/정화/10 Warm Wax.m4a',hms='39:39',mk='정화(丁火)',gl='With its mother near, it lasts through autumn and winter.'),
'경금':dict(date='2027-01-26',hj='庚金',en='Yang Metal',ro='Gyeonggeum',pyeon='경금',title='Quiet Quarry',file='/home/claude/goyo-keys/audio/경금/03 Quiet Quarry.m4a',hms='8:57',mk='경금(庚金)',gl='Meeting fire, it grows keen.'),
'임수':dict(date='2027-01-30',hj='壬水',en='Yang Water',ro='Imsu',pyeon='임수',title='Mirror Water',file='/mnt/user-data/uploads/Desktop/고요음악/쇼츠/_릴스음원/임수/16 Mirror Water.m4a',hms='',mk='임수(壬水)',gl='Transformed, it has feeling.'),
'계수':dict(date='2027-02-02',hj='癸水',en='Yin Water',ro='Gyesu',pyeon='계수',title='Rain Garden',file='/home/claude/goyo-keys/audio/계수/09 Rain Garden.m4a',hms='19:58',mk='계수(癸水)',gl='It does not worry over fire or earth.'),
}
def flat(s): return s.replace('\n',' ')
def wrap(t,n):
    return '\n'.join(wrap1(x,n) for x in t.split('\n'))
def wrap1(t,n):
    out=[];cur=''
    for w in t.split(' '):
        if cur and len(cur)+1+len(w)>n: out.append(cur);cur=w
        else: cur=(cur+' '+w).strip()
    out.append(cur);return '\n'.join(out)
def strip_book(e): return re.sub(r'^(The old Saju classic )?Di Tian Sui \(滴天髓\) ','The book ',e)
only=sys.argv[1:]
for k,d in D.items():
    st=k.split()[1]
    if only and st not in only: continue
    m=META[st]; key=m['date'][5:7]+m['date'][8:10]
    sc=[
     {'sec':4.0,'instant':True,'art':{'file':A[st+'_sym'],'h':260},'items':[[d['hook'],76,FG,True,26],[d['hook_en'],34,EN,False,0]]},
     {'sec':4.5,'art':{'file':A[st+'_sym'],'h':300},'items':[[d['image'].replace(', ',',\n'),66,FG,True,26],[d['image_en'],34,EN,False,0]]},
     {'sec':5.5,'step':0.9,'items':[['옛 책 『적천수』의 한 구절',48,FG,False,30],[d['quote'].replace(' ','\n'),110,GD,True,30],[d['quote_ko'],44,FG,False,26],[f"From Di Tian Sui (滴天髓), an old Saju classic:\n“{m['gl']}”",28,EN,False,0]]},
     {'sec':6.0,'art':{'file':A[st+'_ex'],'h':280},'tag':d['quote'],'items':[[wrap(d['explain'],16),50,FG,True,26],[strip_book(d['explain_en']),28,EN,False,0]]},
     {'sec':6.0,'art':{'file':A[st+'_yr'],'h':280},'items':[[wrap(d['tie'],16),50,FG,True,26],[d['tie_en'],28,EN,False,0]]},
     {'sec':7.0,'step':0.9,'items':[['그래서 정미년은',44,DM,False,24],[wrap(d['line'],15),56,FG,True,30],['사주의 해는 입춘(2027년 2월 4일 오전 10시 46분)에 바뀌어요.',30,DM,False,24],[d['line_en']+"\nIn Saju, the year turns at the start of spring (立春): Feb 4, 2027, 10:46 a.m. KST.",26,EN,False,0]]},
    ]
    en_first=d['hook_en'].replace('\n',' ')
    cap=(f"{flat(d['hook'])}\n\n{flat(d['image'])}. 옛 명리 책 『적천수』에는 「{d['quote']}」, {d['quote_ko']}라는 구절이 있어요. {flat(d['explain']).replace('옛 책 『적천수』는','책은')}\n\n"
         f"{flat(d['tie'])} 그래서 다가오는 정미년은 {flat(d['line'])} 어떻게 닿을지는 사주 전체를 봐야 해요.\n\n사주의 해는 입춘(2027년 2월 4일 오전 10시 46분)에 바뀌어요.\n\n"
         f"이 영상의 소리는 다섯 가지 고요의 『{m['title']}』({st} 편){'이에요' if m['title'].endswith('Garden') else '예요'}. 내 일간을 찾는 무료 앱과 음악은 프로필 링크에서 볼 수 있어요.\n\n· English ·\n"
         f"{en_first} {d['image_en']}. Di Tian Sui (滴天髓), an old Saju classic, says: {d['quote']}, “{m['gl']}” {strip_book(d['explain_en'])} {d['tie_en']} {d['line_en']} How it lands depends on the whole chart. In Saju, the year turns at the start of spring (立春), Feb 4, 2027, 10:46 a.m. KST.\n"
         f"Music in this video: Five Kinds of Quiet · {m['en']} · “{m['title']}”. Find your Day Master with our free app, and the music: link in bio.\n\n#고요 #{st} #정미년 #일간 #오행음악")
    spec={'key':key+'-1800','date':m['date'],'slot':'1800','name':'일간 '+st,
      'audio':{'pyeon':m['pyeon'],'title':m['title'],'file':m['file'],'start_hms':m['hms'],'근거':(f"원곡: goyo-keys/audio/catalog.json {m['pyeon']} {m['hms']} {m['title']} (곡 시작부터 60초)" if m['hms'] else f"원곡: 맥 고요음악/쇼츠/_릴스음원/{m['pyeon']}/{os.path.basename(m['file'])} (60초 클립)")},
      'music_ko':m['mk'],'music_en':m['en'],'end_tag':'이 영상의 소리','end_art':{'file':A[st+'_sym'],'h':200},
      'scenes':sc,'caption':cap,'note':f"정미년 시리즈 · 일간 {st} · 적천수 「{d['quote']}」 · 명리·영어 에이전트 검토 반영(11/22)"}
    p=f'shorts/정미년/spec/{key}-1800.json'; json.dump(spec,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    r=subprocess.run([sys.executable,'tools/week_src/jm_make.py',p],capture_output=True,text=True); print(st,r.returncode,r.stdout[-700:],r.stderr[-800:])
