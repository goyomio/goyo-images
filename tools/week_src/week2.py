import asyncio, base64, os
src=open('/home/claude/goyo/make_slides.py').read().split('post1 = [')[0]
exec(src)
OUT='/home/claude/week/out2'; os.makedirs(OUT,exist_ok=True)
b64=lambda p:'data:image/jpeg;base64,'+base64.b64encode(open(p,'rb').read()).decode()
E=lambda e,t=None: f'<span style="{tc(e)}">{t or e}</span>'
S=lambda t: E("수",t)
P='style="font-size:42px;line-height:1.65"'
arrow='<span style="color:#666"> → </span>'
def bg(img,text,h=560):
    return (f'<div style="position:absolute;inset:0;background:url({img}) center/cover"></div>'
      f'<div style="position:absolute;left:0;right:0;bottom:0;height:{h}px;background:linear-gradient(transparent,rgba(0,0,0,.93))"></div>'
      f'<div style="position:absolute;left:96px;right:96px;bottom:150px">{text}</div>')
# 수 — 제작
make=[
 ('<h1 style="font-size:100px">500곡이<br>넘는데,<br>같은 곡은<br>하나도 없어요</h1><div class="rule"></div><p class="sub">고요는 이렇게 만들어요</p>', SWIPE),
 ('<div class="step">하나 · 음악은 배경이에요</div><div class="rule"></div>'
  '<h2>곡이 바뀐 걸 알아채면<br>실패예요.</h2><br>'
  f'<p {P}>쉬고, 공부하고, 잠들 때 틀어 두는 음악이라<br>갑자기 바뀌는 전환,<br>세게 치는 연주는 쓰지 않아요.<br>고요한 건 괜찮지만, 우울한 곡은 넣지 않아요.</p>',""),
 ('<div class="step">둘 · 오행은 제 해석이에요</div><div class="rule"></div>'
  f'<p style="font-size:46px;line-height:1.9">{E("목")}은 자람 · {E("화")}는 번짐<br>{E("토")}는 받쳐 줌 · {E("금")}은 한 음의 윤곽<br>{S("수")}는 흐름과 내맡김</p><br>'
  f'<p {P}>명리 문헌에 있는 방법은 아니에요.<br>오행을 공부하며 각 기운의 성질을<br>템포·선율·화음으로 옮겨 봤어요.</p>',""),
 ('<div class="step">셋 · 형용사가 아니라 구조로</div><div class="rule"></div>'
  '<h2 style="font-size:60px;line-height:1.6">"차갑게"라고 쓰는 대신<br>화음을 비워서 차갑게,<br><br>"넓게"라고 쓰는 대신<br>악기 수를 줄여서 넓게.</h2>',""),
 ('<div class="step">넷 · 한 번에 두 곡이 나오면</div><div class="rule"></div>'
  '<h2>하나만 써요.</h2><br>'
  f'<p {P}>비슷한 곡이 겹치지 않게<br>한 곡씩 직접 듣고 고르고,<br>버린 곡과 실패도 모두 기록해요.<br>기준은 "좋은 곡인가"보다<br>"다른 곡들과 어울리는가"예요.</p>',""),
 ('<div class="step">다섯 · 억지로 늘이지 않아요</div><div class="rule"></div>'
  f'<p {P}>곡을 억지로 늘이는 기능은 쓰지 않고<br>한 곡씩 이어서 길이를 채워요.</p><br>'
  '<h2>그래서 한 편 안에서는<br>같은 곡이<br>되풀이되지 않아요.</h2><br>'
  '<p>프로필 링크에서 들을 수 있어요.</p>',""),
]
# 목 — 고요의 그림 읽기 #1
HP=b64('ham_paint.jpg'); HD=b64('ham_det.jpg')
CR='<p style="font-size:30px;color:#9a9a9a;margin-top:34px;line-height:1.6">빌헬름 함메르쇠이, 〈스트란가데의 실내, 바닥의 햇빛〉<br>1901 · 덴마크 국립미술관(SMK)</p>'
art=[
 ('<div class="step">고요의 그림 읽기 #1</div><div class="rule" style="margin-bottom:40px"></div>'
  f'<img src="{HP}" style="width:100%;display:block">'+CR, SWIPE),
 (bg(HD,'<h2 style="font-size:66px;line-height:1.5">이 방에는<br>흰색이 마흔 가지 넘게<br>들어 있어요.</h2>'),""),
 ('<div class="step">흰색 마흔 가지</div><div class="rule"></div>'
  f'<p {P}>2012년 전시를 앞두고<br>이 그림을 세척하던 복원가가<br>서로 다른 흰색을<br>마흔 가지 넘게 찾아냈어요.</p><br>'
  '<h2>같은 흰 벽, 같은 흰 문인데<br>하나도 같은 흰색이<br>아니에요.</h2>',""),
 ('<div class="step">같은 방을 66번</div><div class="rule"></div>'
  f'<p {P}>덴마크 화가 함메르쇠이는<br>1898년 아내 이다와<br>코펜하겐 스트란가데 30번지로 이사했어요.</p><br>'
  '<h2>이 집을 그린 실내화가<br>약 66점,<br>그 시기 작품의<br>거의 절반이에요.</h2>',""),
 ('<div class="step">등을 돌린 사람</div><div class="rule"></div>'
  f'<p {P}>그림 속 여인은 아내 이다예요.<br>얼굴은 끝내 보여 주지 않아요.<br>닫힌 문, 창, 바닥에 떨어진 빛만 남겨서<br>이야기는 보는 사람이 채우게 돼요.</p>',""),
 ('<div class="step">"그냥 그렇게 됐어요"</div><div class="rule"></div>'
  f'<p {P}>1907년, 왜 실내만 그리느냐는 질문에<br>그는 "그냥 그렇게 됐다"고 답했어요.<br>실내화가 부유층 사이에 유행이었고,<br>풍경화는 그려도 잘 팔리지 않았다는 것도<br>인정했어요.</p><br>'
  '<p>죽고 나서 한동안 잊혔지만,<br>지금은 국제적으로 가장 잘 알려진<br>덴마크 화가로 꼽혀요.</p>',""),
 (f'<div class="step">고요의 그림 읽기 · {E("금","금(金)")}</div><div class="rule"></div>'
  f'<p style="font-size:40px;line-height:1.75"><b>보이는 것</b><br>흰 벽, 곧은 문틀, 창살이 남긴 빛의 윤곽<br><br>'
  f'<b>그리는 방식</b><br>흰색을 마흔 가지로 좁혀 가며 다듬는 정련<br><br>'
  f'<b>화가의 사주</b><br>1864년 5월 15일생, 갑자년 기사월 경진일<br>일간 {E("금","경금(庚金)")}</p>'
  '<p style="font-size:30px;color:#9a9a9a;margin-top:26px">태어난 시는 기록이 없어 일주까지만 봤어요.<br>공교롭게도 세 겹이 모두 금이에요. 제 해석이에요.</p>',""),
 ('<div class="step">이 그림 옆에 틀어 두고 싶은 소리</div><div class="rule"></div>'
  f'<h1 style="font-size:104px">고요<br>{E("금","경금(庚金)")} 편</h1><br>'
  '<p>곧게 정리된 방에서,<br>한 가지 일에 집중할 때<br>틀어 두기 좋아요.</p><br>'
  '<p>프로필 링크에서 들을 수 있어요.</p>',""),
]
# 금 — 오행 이야기
gen=[
 (f'<h1 style="font-size:100px">{E("화")}·{S("수")}·{E("목")}·{E("금")}·{E("토")}<br>요일,<br>이 이름이<br>오행이에요</h1><div class="rule"></div><p class="sub">몰랐던 오행 이야기</p>', SWIPE),
 ('<div class="step">요일 이름의 비밀</div><div class="rule"></div>'
  f'<p {P}>일요일과 월요일은 해와 달,<br>나머지 다섯 요일은<br>오행 이름을 딴 다섯 행성에서 왔어요.</p><br>'
  f'<h2 style="font-size:58px;line-height:1.7">{E("화")}성 · {S("수")}성 · {E("목")}성 · {E("금")}성 · {E("토")}성</h2><br>'
  '<p>우리는 매주 오행을<br>한 바퀴 돌고 있는 셈이에요.</p>',""),
 ('<div class="step">원소가 아니라 움직임</div><div class="rule"></div>'
  f'<p {P}>영어로는 흔히 "Five Elements"라고 옮겨요.<br>그리스의 4원소에 빗댄 번역이라<br>오해를 부를 수 있어서<br>"Five Phases" 같은 번역도 함께 써요.</p><br>'
  '<h2>오행의 행(行)은<br>"다니다, 움직이다"예요.<br>멈춰 있는 물질이 아니라<br>돌고 바뀌는 기운이에요.</h2>',""),
 ('<div class="step">상생 · 계절이 도는 순서</div><div class="rule"></div>'
  f'<h2 style="font-size:56px;line-height:1.6;white-space:nowrap">{E("목")}{arrow}{E("화")}{arrow}{E("토")}{arrow}{E("금")}{arrow}{S("수")}{arrow}{E("목")}</h2><br>'
  f'<p {P}>봄(목)에 자라 여름(화)에 무성하고,<br>환절기(토)에 여물어 가을(금)에 거두고,<br>겨울(수)에 갈무리했다가<br>다시 봄이 와요.</p>',""),
 ('<div class="step">상극 · 서로 누른다</div><div class="rule"></div>'
  f'<h2 style="font-size:56px;line-height:1.6;white-space:nowrap">{E("목")}{arrow}{E("토")}{arrow}{S("수")}{arrow}{E("화")}{arrow}{E("금")}{arrow}{E("목")}</h2><br>'
  f'<p {P}>나무는 흙을 뚫고, 흙은 물을 막고,<br>물은 불을 끄고, 불은 쇠를 녹이고,<br>쇠는 나무를 베어요.</p>',""),
 ('<div class="step">상극은 나쁜 걸까요?</div><div class="rule"></div>'
  '<h2>누르는 힘이 있어야<br>넘치지 않아요.</h2><br>'
  f'<p {P}>둑이 있어야 물이 제 길로 흐르듯,<br>극은 기운을 다듬는 힘이기도 해요.<br>사주에서는 돕는 힘과 누르는 힘의<br>균형을 함께 봐요.</p>',""),
 ('<div class="step">고요에는 다섯 오행이 다 있어요</div><div class="rule"></div>'
  f'<h1 style="font-size:96px">{E("목")} {E("화")} {E("토")} {E("금")} {S("수")}</h1><br>'
  '<p>사주마다 필요한 기운이 달라서,<br>다섯 결의 소리를 모두 만들었어요.</p><br>'
  '<p>프로필 링크에서 들을 수 있어요.</p>',""),
]
# 일 — 소설
sun=[
 ('<div class="step">11월 22일</div><div class="rule"></div><h1 style="font-size:130px">소설<br>小雪</h1><p class="sub">첫눈이 온다는 날</p>', SWIPE),
 ('<div class="step">옛말 하나</div><div class="rule"></div>'
  '<h2 style="font-size:66px">"소설 추위는<br>빚을 내서라도 한다"</h2><br>'
  f'<p {P}>이 무렵엔 제대로 추워야<br>보리농사가 잘된다고 믿었어요.<br>추위를 반가워한 거예요.</p>',""),
 ('<div class="step">옛말 둘 · 손돌바람</div><div class="rule"></div>'
  f'<p {P}>소설 무렵 부는 매서운 바람을<br>손돌바람이라고 불렀어요.<br>뱃사공 손돌이 억울하게 죽은 날이<br>음력 10월 20일이라는 전설에서 왔어요.</p><br>'
  '<h2>그래서 이 무렵엔<br>뱃사람들이 배를<br>잘 띄우지 않았대요.</h2>',""),
 ('<div class="step">옛말 셋 · 작은 봄</div><div class="rule"></div>'
  f'<p {P}>그러면서도 이 무렵엔<br>봄처럼 따뜻한 날이 가끔 끼어서<br>음력 10월을 이렇게도 불렀어요.</p><br>'
  '<h1 style="font-size:120px">소춘<br>小春</h1><p class="sub">작은 봄</p>',""),
 ('<div class="step">긴 겨울밤에 틀어 두기</div><div class="rule"></div>'
  f'<h1 style="font-size:100px">고요<br>{S("임수(壬水)")} 편</h1><br>'
  '<p>잠들 때 듣는 피아노,<br>두 시간 넘게 이어져요.</p><br>'
  '<h2 style="font-size:56px">프로필 링크 → GOYO 유튜브에서<br>들을 수 있어요.</h2>',""),
]
async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for tag,sl in [('make',make),('ham',art),('ohaeng',gen),('soseol',sun)]:
            for i,(body,extra) in enumerate(sl,1):
                html=BASE.replace("{body}",body).replace("{extra}",extra).replace("{page}",f"{i:02d} / {len(sl):02d}")
                await pg.set_content(html); await pg.wait_for_timeout(400)
                await pg.screenshot(path=f"{OUT}/{tag}_{i:02d}.png")
        await b.close()
asyncio.run(main())
