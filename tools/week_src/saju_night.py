#!/usr/bin/env python3
"""사주 릴스 7~18회 일괄 제작 (2026-11-18 밤).
python3 tools/week_src/saju_night.py <회번호...>   → 설정·캡션·post.json(approved:false)·영상·유튜브판·미리보기
"""
import json, os, re, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SD = os.path.join(ROOT, 'shorts', '사주편')
FIX = '학파마다 기준은 다를 수 있어요'
T = {'목': [90, 200, 130], '화': [255, 120, 80], '토': [220, 180, 110], '금': [225, 225, 245], '수': [80, 120, 230]}

def A(name, dur, start=1.0):
    return {'file': f'shorts/무음편/{name} 무음편.mp4', 'start': start, 'dur': dur}

R = {}

# ---------------- 7 양인 (연결형) ----------------
R[7] = dict(date='2026-12-01', name='살04 양인', theme='stars', kind='연결형',
 audio=[A('화', 9.5, 0.3), A('갑목', 4.5), A('병화', 4.5), A('무토', 4.5), A('경금', 4.5), A('임수', 9.5)],
 scenes=[
  dict(sec=4.5, instant=True, big=['양인'], big_size=150, after=['있으면 기가 세다는 말, 들어 보셨어요?'], en='Yangin: strength at its peak.'),
  dict(sec=5.0, small='양간에서는 록(祿)의 바로 다음 글자', big=['일간의 힘이', '가장 세게 차오른 자리'], big_size=80, after=['요즘은 주체성과 추진력으로 읽기도 해요']),
  dict(sec=4.5, tint='목', small='갑(甲) 일간이라면', big=['묘(卯) 양인'], big_size=100, after=['내 힘으로 밀고 나가는 아침에', '『Morning Oak』(갑목 편)']),
  dict(sec=4.5, tint='화', small='병(丙) 일간이라면', big=['오(午) 양인'], big_size=100, after=['사람들 앞에 서는 한낮에', '『Noon Avenue』(병화 편)']),
  dict(sec=4.5, tint='토', small='무(戊) 일간이라면', big=['오(午) 양인'], big_size=100, after=['묵직하게 버텨야 하는 날에', '무토 편']),
  dict(sec=4.5, tint='금', small='경(庚) 일간이라면', big=['유(酉) 양인'], big_size=100, after=['매듭을 지어야 하는 저녁에', '『Stone Bridge』(경금 편)']),
  dict(sec=4.5, tint='수', small='임(壬) 일간이라면', big=['자(子) 양인'], big_size=100, after=['생각이 넘치는 밤에', '『Wide Water』(임수 편)']),
  dict(sec=5.0, tint='수', small='이 글자가 내 사주 지지에 있으면 양인', big=['내 사주에는', '양인이 있을까요?'], big_size=88, after=['내 일간의 곡은 프로필 링크에서'], en=FIX),
 ],
 caption="""양인(羊刃)이 있으면 기가 세다는 말, 들어 보셨어요?

양인은 태어난 날의 천간(일간)이 가장 세게 차오른 자리예요. 록(祿)의 바로 다음 글자라서, 록보다 힘이 더 차오른 상태로 봐요. 예전에는 지나친 힘이라 조심하는 글자로 읽었고, 요즘은 주체성과 추진력으로 읽기도 해요.

보는 법은 일간을 기준으로, 사주 네 기둥의 지지에 그 글자가 있는지 살피는 거예요.
갑(甲): 묘(卯)
병(丙)·무(戊): 오(午)
경(庚): 유(酉)
임(壬): 자(子)
음간(을乙·정丁·기己·신辛·계癸)은 양인을 따로 보지 않는 쪽과 다른 글자로 잡는 쪽이 있어요.

양인 하나로 성격이 정해지지는 않아요. 사주는 원국 전체로 봐요.
학파마다 기준은 다를 수 있어요.

장면마다 그 일간의 곡을 골랐어요.
『Morning Oak』(갑목 편) · 『Noon Avenue』(병화 편) · 무토 편 · 『Stone Bridge』(경금 편) · 『Wide Water』(임수 편)

내 일간의 곡은 프로필 링크에서 들을 수 있어요.

#고요 #사주 #양인 #양인살 #신살 #오행음악""")

# ---------------- 8 천덕·월덕 (정보형) ----------------
R[8] = dict(date='2026-12-03', name='귀인04 천덕월덕', theme='blossom', kind='정보형',
 audio=[A('을목', 18.0), A('정화', 18.0)],
 scenes=[
  dict(sec=4.5, instant=True, big=['천덕 · 월덕'], big_size=130, after=['덕을 쌓으면 생기는 귀인일까?'], en='Virtue stars set by your birth month.'),
  dict(sec=5.5, small='태어난 달로 정해지는 귀인', big=['하늘의 덕, 달의 덕'], big_size=88, after=['옛 책은 험한 일을', '누그러뜨리는 글자로 풀이했어요']),
  dict(sec=4.5, tint='화', small='인(寅)·오(午)·술(戌)월생이라면', big=['월덕은 병(丙)'], big_size=96),
  dict(sec=4.5, tint='수', small='신(申)·자(子)·진(辰)월생이라면', big=['월덕은 임(壬)'], big_size=96),
  dict(sec=4.5, tint='목', small='해(亥)·묘(卯)·미(未)월생이라면', big=['월덕은 갑(甲)'], big_size=96),
  dict(sec=5.5, tint='금', small='사(巳)·유(酉)·축(丑)월생이라면', big=['월덕은 경(庚)'], big_size=96, after=['이 글자가 사주 천간에 있으면 월덕']),
  dict(sec=5.0, tint='화', small='천덕 열두 달 표는 아래 글에 적어 둘게요', big=['내 사주에는', '덕이 있을까요?'], big_size=88, after=['천덕·월덕이 없는 사주도 흔해요'], en=FIX),
 ],
 caption="""덕을 쌓으면 생기는 귀인일까요?

천덕(天德)과 월덕(月德)은 태어난 달로 정해지는 귀인이에요. 하늘의 덕, 달의 덕이라는 뜻이고, 옛 책에서는 험한 일을 누그러뜨리는 글자로 풀이했어요.

보는 법은 태어난 달의 지지(월지)를 기준으로, 그 글자가 사주에 있는지 살피는 거예요. 천간 글자는 천간에서, 지지 글자는 지지에서 찾아요. 월은 절기로 바뀌어서, 인(寅)월은 입춘부터예요.

월덕
인(寅)·오(午)·술(戌)월: 병(丙)
신(申)·자(子)·진(辰)월: 임(壬)
해(亥)·묘(卯)·미(未)월: 갑(甲)
사(巳)·유(酉)·축(丑)월: 경(庚)

천덕
인(寅)월 정(丁) · 묘(卯)월 신(申) · 진(辰)월 임(壬)
사(巳)월 신(辛) · 오(午)월 해(亥) · 미(未)월 갑(甲)
신(申)월 계(癸) · 유(酉)월 인(寅) · 술(戌)월 병(丙)
해(亥)월 을(乙) · 자(子)월 사(巳) · 축(丑)월 경(庚)
천덕 글자 가운데 신(申)·해(亥)·인(寅)·사(巳)는 지지 글자예요.

천덕·월덕이 없는 사주도 흔하고, 사주는 원국 전체로 봐요.
학파마다 기준은 다를 수 있어요.

배경 음악: 『Morning Tendril』(을목 편) · 『Lamplit Keys』(정화 편)

#고요 #사주 #천덕귀인 #월덕귀인 #귀인 #오행음악""")

# ---------------- 9 괴강 (연결형) ----------------
R[9] = dict(date='2026-12-05', name='살05 괴강', theme='stars', kind='연결형',
 audio=[A('토', 14.5, 0.3), A('경금', 10.0), A('임수', 10.0)],
 scenes=[
  dict(sec=4.5, instant=True, big=['괴강'], big_size=150, after=['있으면 성격이 강하다고요?'], en='Kuigang: a name from the Big Dipper.'),
  dict(sec=5.0, small='괴강(魁罡)은 북두칠성에서 온 이름', big=['진(辰)과 술(戌)'], big_size=92, after=['옛 책은 진을 천강, 술을 하괴라 불렀어요']),
  dict(sec=5.0, small='흔히 꼽는 괴강 일주', big=['경진 · 경술 · 임진'], big_size=84, after=['임술 · 무술 · 무진을 넣는 기준은', '학파마다 달라요']),
  dict(sec=5.0, small='예전엔 여자에게 드세다고 했지만', big=['결단하고', '밀고 나가는 기운'], big_size=84, after=['요즘은 성별과 상관없이 이렇게 읽어요']),
  dict(sec=5.0, tint='금', small='경(庚)으로 시작하는 괴강이라면', big=['경금 편'], big_size=100, after=['매듭을 짓는 저녁에', '『Stone Bridge』(경금 편)']),
  dict(sec=5.0, tint='수', small='임(壬)으로 시작하는 괴강이라면', big=['임수 편'], big_size=100, after=['멀리 내다보는 밤에', '『Wide Water』(임수 편)']),
  dict(sec=5.0, tint='수', small='태어난 날의 기둥을 확인해 보세요', big=['내 일주는', '괴강일까요?'], big_size=92, after=['내 일주의 곡은 프로필 링크에서'], en=FIX),
 ],
 caption="""괴강(魁罡)이 있으면 성격이 강하다는 말, 들어 보셨어요?

괴강은 북두칠성에서 온 이름이에요. 옛 책은 진(辰)을 천강(天罡), 술(戌)을 하괴(河魁)라고 불렀고, 그래서 괴강 일주는 모두 진이나 술로 끝나요.

보는 법은 태어난 날의 기둥(일주)을 확인하는 거예요. 흔히 경진(庚辰), 경술(庚戌), 임진(壬辰)을 꼽고, 임술(壬戌)과 무술(戊戌), 무진(戊辰)을 넣는 기준은 학파마다 달라요.

예전에는 여자 사주에 괴강이 있으면 드세다고들 했어요. 요즘은 성별과 상관없이 결단하고 밀고 나가는 힘으로 읽어요.

괴강 하나로 성격이 정해지지는 않아요. 사주는 원국 전체로 봐요.
학파마다 기준은 다를 수 있어요.

장면마다 그 일간의 곡을 골랐어요.
『Stone Bridge』(경금 편) · 『Wide Water』(임수 편)

내 일주의 곡은 프로필 링크에서 들을 수 있어요.

#고요 #사주 #괴강 #괴강살 #신살 #오행음악""")


# ---------------- 10 태극귀인 (정보형) ----------------
R[10] = dict(date='2026-12-08', name='귀인05 태극귀인', theme='moon', kind='정보형',
 audio=[A('계수', 18.0), A('신금', 18.0)],
 scenes=[
  dict(sec=4.5, instant=True, big=['태극귀인'], big_size=150, after=['근원을 파고드는 사람에게 붙는 귀인?'], en='Taiji star: the root of things.'),
  dict(sec=5.5, small='태극(太極)은 만물의 근원', big=['일간으로 찾는 귀인'], big_size=88, after=['옛 책은 깊이 파고드는 힘으로 풀이했어요']),
  dict(sec=4.0, tint='목', small='갑(甲)·을(乙) 일간이라면', big=['자(子) · 오(午)'], big_size=96),
  dict(sec=4.0, tint='화', small='병(丙)·정(丁) 일간이라면', big=['묘(卯) · 유(酉)'], big_size=96),
  dict(sec=4.5, tint='토', small='무(戊)·기(己) 일간이라면', big=['진 · 술 · 축 · 미'], big_size=96, after=['진(辰) · 술(戌) · 축(丑) · 미(未)']),
  dict(sec=4.0, tint='금', small='경(庚)·신(辛) 일간이라면', big=['인(寅) · 해(亥)'], big_size=96),
  dict(sec=5.0, tint='수', small='임(壬)·계(癸) 일간이라면', big=['사(巳) · 신(申)'], big_size=96, after=['이 글자가 사주 지지에 있으면 태극귀인']),
  dict(sec=5.0, tint='수', small='표는 학파마다 조금씩 달라요', big=['내 사주에는', '태극귀인이 있을까요?'], big_size=84, after=['태극귀인이 없는 사주도 흔해요'], en=FIX),
 ],
 caption="""근원을 깊이 파고드는 사람에게 붙는 귀인이 있을까요?

태극(太極)은 만물의 근원을 뜻해요. 태극귀인은 태어난 날의 천간(일간)으로 찾는 귀인이고, 옛 책에서는 근원을 깊이 파고드는 힘으로 풀이했어요.

보는 법은 일간을 기준으로, 사주 네 기둥의 지지에 그 글자가 있는지 살피는 거예요.
갑(甲)·을(乙): 자(子) · 오(午)
병(丙)·정(丁): 묘(卯) · 유(酉)
무(戊)·기(己): 진(辰) · 술(戌) · 축(丑) · 미(未)
경(庚)·신(辛): 인(寅) · 해(亥)
임(壬)·계(癸): 사(巳) · 신(申)
일부 일간은 글자를 다르게 잡는 표도 있어요.

태극귀인이 없는 사주도 흔하고, 사주는 원국 전체로 봐요.
학파마다 기준은 다를 수 있어요.

배경 음악: 『Drizzle』(계수 편) · 『Clear Facet』(신금 편)

#고요 #사주 #태극귀인 #귀인 #오행음악""")

# ---------------- 11 백호 (정보형) ----------------
R[11] = dict(date='2026-12-10', name='살06 백호', theme='road', kind='정보형',
 audio=[A('갑목', 15.0), A('계수', 15.0)],
 scenes=[
  dict(sec=4.5, instant=True, big=['백호'], big_size=150, after=['무섭게만 들리는 이름, 정말 그럴까?'], en='Baekho: the White Tiger.'),
  dict(sec=6.0, small='백호(白虎)는 서쪽을 지키는 흰 호랑이', big=['태어난 날의 기둥이', '이 일곱 가운데 하나'], big_size=78, after=['갑진 · 을미 · 병술 · 정축', '무진 · 임술 · 계축']),
  dict(sec=5.0, small='예전엔 겁을 주던 이름이지만', big=['밀어붙이는 힘,', '한 분야를 파는 힘'], big_size=84, after=['요즘은 이렇게 읽기도 해요']),
  dict(sec=5.0, small='일주 말고 다른 기둥까지 보는 학파도 있어요', big=['백호 하나로', '정해지는 건 없어요'], big_size=84),
  dict(sec=5.0, small='태어난 날의 기둥을 확인해 보세요', big=['내 일주는', '백호일까요?'], big_size=92, after=['일주로 보면 백호가 없는 사주가 훨씬 많아요'], en=FIX),
 ],
 caption="""백호(白虎)라는 이름, 무섭게만 들리시나요?

백호는 서쪽을 지키는 흰 호랑이예요. 사주에서는 태어난 날의 기둥(일주)이 갑진(甲辰), 을미(乙未), 병술(丙戌), 정축(丁丑), 무진(戊辰), 임술(壬戌), 계축(癸丑) 가운데 하나면 백호로 봐요. 일주 말고 다른 기둥까지 보는 학파도 있어요.

예전에는 거센 일을 겪는 글자라며 겁을 주는 이름이었어요. 요즘은 밀어붙이는 힘, 한 분야를 깊이 파는 힘으로 읽기도 해요.

일주로 보면 예순 가운데 일곱이라, 백호가 없는 사주가 훨씬 많아요. 백호 하나로 정해지는 건 없고, 사주는 원국 전체로 봐요.
학파마다 기준은 다를 수 있어요.

배경 음악: 『Morning Oak』(갑목 편) · 『Drizzle』(계수 편)

#고요 #사주 #백호 #백호살 #신살 #오행음악""")

# ---------------- 12 국인·관귀학관·삼기 (정보형) ----------------
R[12] = dict(date='2026-12-12', name='귀인06 국인관귀삼기', theme='lamp', kind='정보형',
 audio=[A('정화', 15.0), A('을목', 15.0)],
 scenes=[
  dict(sec=4.5, instant=True, big=['국인 · 관귀 · 삼기'], big_size=100, after=['이름도 낯선 귀인 셋'], en='Three lesser-known noble stars.'),
  dict(sec=5.5, small='국인(國印)', big=['나라의 도장'], big_size=96, after=['맡은 일을 책임 있게 지키는 자리로 읽어요', '일간으로 찾아요']),
  dict(sec=5.5, small='관귀학관(官貴學館)', big=['배움이 자리로', '이어지는 귀인'], big_size=84, after=['갑·을은 사(巳), 병·정은 신(申)', '일간으로 찾아요']),
  dict(sec=5.5, small='삼기(三奇)', big=['세 천간이', '한 사주에 모이면'], big_size=84, after=['갑무경 · 을병정 · 임계신']),
  dict(sec=5.0, small='세 가지 표는 아래 글에 적어 둘게요', big=['내 사주에는', '어떤 귀인이 있을까요?'], big_size=84, after=['셋 다 없는 사주가 더 흔해요'], en=FIX),
 ],
 caption="""이름도 낯선 귀인 셋, 국인·관귀학관·삼기를 모아 봤어요.

국인(國印)은 나라의 도장이라는 뜻이에요. 맡은 일을 책임 있게 지키는 자리로 읽어요. 일간을 기준으로 사주 지지에 이 글자가 있는지 봐요.
갑(甲) 술(戌) · 을(乙) 해(亥) · 병(丙) 축(丑) · 정(丁) 인(寅) · 무(戊) 축(丑)
기(己) 인(寅) · 경(庚) 진(辰) · 신(辛) 사(巳) · 임(壬) 미(未) · 계(癸) 신(申)

관귀학관(官貴學館)은 배움이 자리로 이어지는 귀인으로 읽어요. 일간을 기준으로 지지에서 찾아요.
갑(甲)·을(乙) 사(巳) · 병(丙)·정(丁) 신(申) · 무(戊)·기(己) 해(亥) · 경(庚)·신(辛) 인(寅) · 임(壬)·계(癸) 신(申)
임·계는 인(寅)으로 보는 학파도 있어요.

삼기(三奇)는 세 천간이 한 사주의 천간에 모두 있을 때를 말해요. 갑(甲)·무(戊)·경(庚), 을(乙)·병(丙)·정(丁), 임(壬)·계(癸)·신(辛) 세 묶음이 있고, 순서대로 놓여야 본다는 쪽과 모이기만 하면 본다는 쪽이 갈려요.

셋 다 없는 사주가 더 흔하고, 사주는 원국 전체로 봐요.
학파마다 기준은 다를 수 있어요.

배경 음악: 『Lamplit Keys』(정화 편) · 『Morning Tendril』(을목 편)

#고요 #사주 #국인귀인 #관귀학관 #삼기귀인 #귀인 #오행음악""")


def yt_after(lines):
    out = []
    for l in lines:
        l = l.replace('내 일간의 곡은 프로필 링크에서', '내 일간 편은 고정 댓글에서')
        l = l.replace('내 일주의 곡은 프로필 링크에서', '내 일주 편은 고정 댓글에서')
        l = l.replace('그 글자의 곡은 프로필 링크에서', '그 글자의 편은 고정 댓글에서')
        l = l.replace('프로필 링크에서', '고요 채널에서')
        out.append(l)
    return out


def build(n, render=True):
    r = R[n]
    cfg = {'theme': r['theme'], 'audio_parts': r['audio'], 'tints': T, 'scenes': r['scenes']}
    jp = os.path.join(SD, r['name'] + '.json'); mp = jp[:-5] + '.mp4'
    json.dump(cfg, open(jp, 'w'), ensure_ascii=False, indent=1)
    cap = '/tmp/cap_%d.txt' % n; open(cap, 'w').write(r['caption'])
    k = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'ko_check.py'), cap], capture_output=True, text=True)
    print(n, 'ko_check', k.returncode, k.stdout.strip()[-400:])
    pdir = os.path.join(ROOT, 'posts', r['date'] + '-2100'); os.makedirs(pdir, exist_ok=True)
    json.dump({'type': 'reel', 'video_file': os.path.relpath(mp, ROOT), 'via': 'api', 'approved': False, 'thumb_offset': 3000,
               'note': f'신살·귀인 연재 {n}회. {r["kind"]}. 2026-11-18 밤 제작, 명리 검토 반영. 미오 님 승인 대기',
               'caption': r['caption']}, open(os.path.join(pdir, 'post.json'), 'w'), ensure_ascii=False, indent=1)
    yt = json.loads(json.dumps(cfg)); yt['scenes'][-1]['after'] = yt_after(yt['scenes'][-1].get('after', []))
    yj = os.path.join(SD, '유튜브', r['name'] + '.json'); json.dump(yt, open(yj, 'w'), ensure_ascii=False, indent=1)
    if not render: return
    for c, o in ((jp, mp), (yj, yj[:-5] + '.mp4')):
        subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'saju_reel.py'), c, o], capture_output=True)
        w = o + '.wav'
        if os.path.exists(w): os.remove(w)
        d = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', o], capture_output=True, text=True).stdout.strip()
        print(n, os.path.basename(o), 'dur', d)
    # 미리보기: 장면 가운데 프레임
    t = 0; shots = []
    for s in r['scenes'][:-1]:
        shots.append(t + s['sec'] * 0.75); t += s['sec']
    shots.append(t + 2.5)
    from PIL import Image
    ims = []
    for i, ts in enumerate(shots):
        f = f'/tmp/pv_{n}_{i}.jpg'
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-ss', str(ts), '-i', mp, '-frames:v', '1', '-vf', 'scale=270:-1', '-y', f])
        ims.append(Image.open(f).crop((0, 180, 270, 300 + 120)))
    W = 270 * 4; H = ims[0].height * ((len(ims) + 3) // 4)
    sh = Image.new('RGB', (W, H))
    for i, im in enumerate(ims): sh.paste(im, ((i % 4) * 270, (i // 4) * im.height))
    sh.save(f'/tmp/pv_{n}.jpg')


if __name__ == '__main__':
    for a in sys.argv[1:]:
        build(int(a), render=os.environ.get('NORENDER') != '1')
