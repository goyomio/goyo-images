"""무음편 쇼츠 16편 인스타 예약 폴더 만들기 (승인은 꺼 둔 채로). python3 tools/week_src/mute_posts.py"""
import json, os
S = [  # date, slot, key, kind, hook, hz, image, genre, en_hook, en_image, en_genre, en_name
 ('2026-11-21','1500','수','el','마음이 늘 바쁘세요?','水','','조용히 흐르는 그랜드 피아노 앰비언트예요','Is your mind always racing?','','quiet, flowing grand piano ambient','Water'),
 ('2026-11-22','1500','갑목','st','리더감이라는 말, 자주 들으세요?','甲木','하늘로 곧게 서는 큰 나무 같은 기운이에요.','곧게 자라는 실내악이에요',"Told you're a natural leader?",'Like a tall tree standing straight toward the sky.','chamber music that grows straight up','Yang Wood · Gapmok'),
 ('2026-11-23','2100','을목','st','친화력 좋다는 말, 자주 들으세요?','乙木','기대어 감아 오르는 덩굴 같은 기운이에요.','명랑하게 감아 오르는 실내악이에요','People say you get along with anyone?','Like a vine that leans in and climbs.','bright chamber music that winds upward','Yin Wood · Eulmok'),
 ('2026-11-24','1500','병화','st','밝다는 말, 자주 들으세요?','丙火','사방을 고루 비추는 태양 같은 기운이에요.','환하게 번지는 재즈펑크예요','Do rooms light up when you walk in?','Like the sun shining evenly on everything.','bright, spreading jazz-funk','Yang Fire · Byeonghwa'),
 ('2026-11-25','1500','정화','st','감수성이 풍부하다는 말, 들으세요?','丁火','한 자리를 오래 밝히는 촛불 같은 기운이에요.','따뜻한 재즈예요','Told you feel things more deeply than most?','Like a candle that lights one spot for a long time.','warm jazz','Yin Fire · Jeonghwa'),
 ('2026-11-26','1500','무토','st','듬직하다는 말, 자주 들으세요?','戊土','두텁고 단단한 흙의 산 같은 기운이에요.','담백하고 듬직한 로파이예요','Known as the rock of the group?','Like a mountain of thick, solid earth.','plain, steady lo-fi','Yang Earth · Muto'),
 ('2026-11-27','1500','기토','st','돌다리도 두드려 보고 건넌다는 말, 들으세요?','己土','씨앗을 품고 길러 내는 밭의 흙 같은 기운이에요.','재즈 색이 짙은 로파이예요','Always look before you leap?','Like field soil that holds seeds and helps them grow.','jazzy lo-fi','Yin Earth · Gito'),
 ('2026-11-28','1500','경금','st','의리 있다는 말, 자주 들으세요?','庚金','산에서 막 캐낸 원석 같은 기운이에요.','그랜드 피아노 한 대의 단단한 연주예요','Known as the loyal one?','Like raw ore fresh from the mountain.','one grand piano, clear and solid','Yang Metal · Gyeonggeum'),
 ('2026-11-29','1500','신금','st','안목이 좋다는 말, 들으세요?','辛金','갈고 다듬어 빛나는 돌 같은 기운이에요.','맑은 높은 음의 피아노예요','Told you have a good eye?','Like a stone that shines once it is cut and polished.','clear, high piano','Yin Metal · Singeum'),
 ('2026-11-30','2100','임수','st','스케일이 크다는 말, 들으세요?','壬水','바다로 흘러가는 큰물 같은 기운이에요.','긴 호흡으로 흐르는 앰비언트 피아노예요','Told you think big?','Like a great river flowing to the sea.','ambient piano that flows in long breaths','Yang Water · Imsu'),
 ('2026-12-01','1500','계수','st','눈치가 빠르다는 말, 자주 들으세요?','癸水','땅에 스며드는 비와 이슬 같은 기운이에요.','맑게 떨어지는 앰비언트 피아노예요','Always the first to read the room?','Like rain and dew soaking into the ground.','clear ambient piano, falling drop by drop','Yin Water · Gyesu'),
 ('2026-12-02','1500','비교편','q','소리만 듣고 맞혀 보세요, 어느 게 금(金)일까요?','金','','','Just listen. Which one is Metal?','','',''),
 ('2026-12-03','1500','목','el','시작이 늘 어려우세요?','木','','위로 자라는 현대 실내악이에요','Always struggle to get started?','','modern chamber music that grows upward','Wood'),
 ('2026-12-04','1500','화','el','열정이 금방 식으세요?','火','','따뜻하게 번지는 재즈펑크예요','Does your passion burn out fast?','','warm, spreading jazz-funk','Fire'),
 ('2026-12-05','1500','토','el','작심삼일, 자주 하세요?','土','','한 덩어리로 받쳐 주는 로파이예요','Always start strong, then fizzle out?','','lo-fi that holds everything together','Earth'),
 ('2026-12-06','1500','금','el','맺고 끊기가 어려우세요?','金','','한 음의 윤곽과 끝이 들리는 절제된 연주예요','Hard to set limits and let go?','','restrained playing where each note has a clear edge and end','Metal'),
]


def caption(kind, k, hook, hz, img, gen, eh, eimg, egen, en):
    if kind == 'st':
        ko = (f"{hook}\n\n{k}({hz}) 일간이 자주 듣는 말이에요. {img}\n\n"
              f"{k}의 소리는 {gen}. 영상 속 곡의 전곡은 다섯 가지 고요 {k}({hz}) 편, 프로필 링크에서 들을 수 있어요.\n"
              f"내 일간은 프로필 링크의 무료 사주앱에서 확인해 보세요.")
        e = (f"{eh}\n\nPeople with a {en.split(' · ')[0]} ({hz}) day master often hear this. {eimg}\n\n"
             f"The sound of {en.split(' · ')[1]}: {egen}. The full set from this video is on Five Kinds of Quiet · {en}, link in bio.\n"
             f"Find your day master in the free Saju app: link in bio.")
        tags = f"#고요 #{k} #{k}일간 #오행음악 #다섯가지고요 #saju"
    elif kind == 'el':
        ko = (f"{hook}\n\n{k}({hz})의 소리는 {gen}. 영상 속 곡의 전곡은 다섯 가지 고요 {k}({hz}) 편, 프로필 링크에서 들을 수 있어요.\n"
              f"내 사주 오행은 프로필 링크의 무료 사주앱에서 확인해 보세요.")
        e = (f"{eh}\n\nThe sound of {en} ({hz}): {egen}. The full set from this video is on Five Kinds of Quiet · {en}, link in bio.\n"
             f"See the elements in your own chart in the free Saju app: link in bio.")
        tags = f"#고요 #{k}오행 #오행음악 #다섯가지고요 #fiveelements"
    else:
        ko = (f"{hook}\n\n다섯 소리 중 하나가 금(金)이에요. 하나씩 듣고 골라 보세요. 정답은 영상 끝에 있어요.\n\n"
              f"목(木)·화(火)·토(土)·금(金)·수(水), 다섯 가지 고요는 프로필 링크에서 골라 들을 수 있어요.\n"
              f"내 사주 오행은 프로필 링크의 무료 사주앱에서 확인해 보세요.")
        e = (f"{eh}\n\nOne of these five sounds is Metal (金). Listen to each and pick one. The answer is at the end.\n\n"
             f"Wood, Fire, Earth, Metal, Water: find the full set for your element on Five Kinds of Quiet, link in bio.\n"
             f"See the elements in your own chart in the free Saju app: link in bio.")
        tags = "#고요 #오행음악 #오행퀴즈 #다섯가지고요 #fiveelements"
    return ko + "\n\n· English ·\n" + e + "\n\n" + tags


if __name__ == '__main__':
    for d, slot, k, kind, hook, hz, img, gen, eh, eimg, egen, en in S:
        vid = f'shorts/무음편/인스타/{d} {k} 무음편 인스타.mp4'
        assert os.path.exists(vid), vid
        p = f'posts/{d}-{slot}'
        if os.path.exists(p + '/post.json') and '무음편' not in open(p + '/post.json', encoding='utf-8').read():
            raise SystemExit(f'이미 다른 게시물이 있어요: {p}')
        os.makedirs(p, exist_ok=True)
        json.dump({"type": "reel", "via": "api", "approved": False, "video_file": vid,
                   "caption": caption(kind, k, hook, hz, img, gen, eh, eimg, egen, en), "thumb_offset": 800,
                   "note": f"무음편 쇼츠 {k}. 11/21 끝 장면을 「전곡은 프로필 링크에서」로 바꿔 다시 렌더(원본 고요음악/쇼츠/무음편 그대로). 유튜브와 같은 날짜·시각. 미오 님 캡션 확인 전이라 승인 꺼 둠"},
                  open(p + '/post.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('ok', len(S))
