import json, os
D = os.path.dirname(os.path.abspath(__file__))
PL = 'https://www.youtube.com/playlist?list=PLRm375HI5ZcA'
APP = 'https://goyomio.com'
IG = 'https://www.instagram.com/goyo_mio'
V = {'A': ('FGwsULeuSIQ', 'VzDuEs2i5es'), 'B': ('SedElVh2ezg', 'g3Eeu8QVaJY'), 'C': ('7rrraS-O1qM', '8hLmKk8ag08'),
     'D': ('Go56Wv--DUM', 'q8w4WV76ah4'), 'E': ('WbCckaq7tf0', '_tcQg4N6gt8'), 'F': ('uBZBnff2kSE', 'xDGOypKeG_s'),
     'G': ('ENjKdCeT-SM', '8hLmKk8ag08'), 'H': ('WMF8D0Tsr5Y', 'oIt-DzA96Bw'), 'I': ('NAujLwEjFXM', 'VzDuEs2i5es')}
# 링크 줄: (음악, 재생목록, 앱, 타로)
LB = {
 'en': ('Music', 'All GOYO five-element music', 'Free Saju app (find your Day Master)', 'Daily tarot every morning on Instagram'),
 'de': ('Musik', 'Alle Fünf-Elemente-Musik von GOYO', 'Kostenlose Saju-App (Tagesmeister finden)', 'Jeden Morgen Tarot auf Instagram'),
 'es': ('Música', 'Toda la música de los cinco elementos de GOYO', 'App gratuita de Saju (encuentra tu Maestro del Día)', 'Tarot del día cada mañana en Instagram'),
 'fr': ('Musique', 'Toute la musique des cinq éléments de GOYO', 'Appli Saju gratuite (trouvez votre Maître du Jour)', 'Le tarot du jour chaque matin sur Instagram'),
 'it': ('Musica', 'Tutta la musica dei cinque elementi di GOYO', 'App Saju gratuita (trova il tuo Maestro del Giorno)', 'I tarocchi del giorno ogni mattina su Instagram'),
 'pt': ('Música', 'Toda a música dos cinco elementos do GOYO', 'App de Saju grátis (descubra seu Mestre do Dia)', 'Tarô do dia toda manhã no Instagram'),
 'ja': ('音楽', 'GOYO 五行音楽プレイリスト', '無料の四柱推命アプリ（自分の日干を調べる）', '毎朝の今日のタロット（Instagram）'),
 'zh-Hans': ('音乐', 'GOYO 五行音乐全部播放', '免费八字App（查你的日主）', '每天早上的今日塔罗（Instagram）'),
 'zh-Hant': ('音樂', 'GOYO 五行音樂播放清單', '免費八字App（查你的日主）', '每天早上的今日塔羅（Instagram）'),
 'vi': ('Nhạc', 'Toàn bộ nhạc ngũ hành của GOYO', 'Ứng dụng bát tự miễn phí (tìm nhật chủ của bạn)', 'Tarot mỗi sáng trên Instagram'),
 'th': ('เพลง', 'เพลงห้าธาตุทั้งหมดของ GOYO', 'แอปดวงสี่เสาฟรี (หาธาตุเจ้าเรือนของคุณ)', 'ไพ่ทาโรต์ประจำวันทุกเช้าบน Instagram'),
 'ar': ('الموسيقى', 'كل موسيقى العناصر الخمسة من GOYO', None, None),
}
HT = {'ar': '#FiveElementsMusic'}
T = {}  # T[lang][key] = (title, body, hashtags)
exec(open(os.path.join(D, 'texts_west.py'), encoding='utf-8').read())
exec(open(os.path.join(D, 'texts_east.py'), encoding='utf-8').read())

out = {}
for k, (vid, mv) in V.items():
    out[vid] = {}
    for l, lab in LB.items():
        title, body, tags = T[l][k]
        lines = [f'{lab[0]} ▶ https://youtu.be/{mv}', f'{lab[1]} ▶ {PL}']
        if lab[2]:
            lines += [f'{lab[2]} ▶ {APP}', f'{lab[3]} ▶ {IG}']
        desc = body.strip() + '\n\n' + '\n'.join(lines) + '\n\n' + (HT.get(l) or tags)
        out[vid][l] = {'title': title, 'description': desc}
json.dump(out, open(os.path.join(D, 'loc_merged.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(out))
