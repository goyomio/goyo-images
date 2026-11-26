import json,sys
sys.path.insert(0,'../번역_1126b_정미년쇼츠9편')
PL='https://www.youtube.com/playlist?list=PLRm375HI5ZcA';MV='https://youtu.be/oIt-DzA96Bw'
exec(open('../번역_1126b_정미년쇼츠9편/build.py').read().split("HT = ")[0].split("LB = ",1)[0])
LB=eval(open('../번역_1126b_정미년쇼츠9편/build.py').read().split("LB = ",1)[1].split("\nHT")[0])
T={
'en':("Manghaesa, Gimje: the Temple That Looks Out to Sea","""Manghaesa in Gimje, the temple that looks out to sea.

Where the Gimje–Mangyeong plains, one of the few places in Korea where you can see the horizon over land, come to an end, the sea begins. The sun is 丙火 Yang Fire (Byeonghwa), the great fire in the sky. To us, the sun sinking low at the edge of the fields looks like 2027: a big fire settling into a small light (our own reading). What time the January sun sets, the temple's old stories, and what to check before you go are in our channel post.

Playing now: Amber Window from 「다섯 가지 고요」 (Five Kinds of Quiet) · Yang Fire.""","#FiveElementsMusic #Korea #Sunset"),
'de':("Manghaesa in Gimje: der Tempel, der aufs Meer blickt","""Manghaesa in Gimje, der Tempel, der aufs Meer blickt.

Wo die Ebene von Gimje und Mangyeong endet – einer der wenigen Orte in Korea, an denen man einen Horizont über Land sieht –, beginnt das Meer. Die Sonne ist 丙火 Yang-Feuer (Byeonghwa), das große Feuer am Himmel. Wie sie am Rand der Felder tief sinkt, lesen wir als Bild für 2027: Ein großes Feuer geht in ein kleines Licht über (unsere eigene Deutung). Wann die Januarsonne untergeht, die alten Geschichten des Tempels und was Sie vor dem Besuch prüfen sollten, steht in unserem Kanal-Beitrag.

Jetzt läuft: Amber Window aus 「다섯 가지 고요」 („Fünf Arten von Stille“) · Yang-Feuer.""","#FiveElementsMusic #Korea #Sunset"),
'es':("Manghaesa, Gimje: el templo que mira al mar","""Manghaesa en Gimje, el templo que mira al mar.

Donde terminan las llanuras de Gimje y Mangyeong, uno de los pocos lugares de Corea donde se ve el horizonte sobre la tierra, empieza el mar. El sol es 丙火 Fuego Yang (Byeonghwa), el gran fuego del cielo. Vemos el sol que baja al borde de los campos como la forma de 2027: un gran fuego que pasa a ser una luz pequeña (es nuestra propia lectura). A qué hora se pone el sol en enero, las historias antiguas del templo y qué revisar antes de ir: está en la publicación del canal.

Ahora suena: Amber Window, de 「다섯 가지 고요」 («Cinco formas de quietud») · Fuego Yang.""","#FiveElementsMusic #Korea #Sunset"),
'fr':("Manghaesa, Gimje : le temple qui regarde la mer","""Manghaesa à Gimje, le temple qui regarde la mer.

Là où s'achèvent les plaines de Gimje et Mangyeong, l'un des rares endroits de Corée où l'on voit l'horizon au-dessus des terres, commence la mer. Le soleil est 丙火 Feu Yang (Byeonghwa), le grand feu du ciel. Nous voyons ce soleil qui descend au bord des champs comme la forme de 2027 : un grand feu qui devient une petite lumière (c'est notre propre lecture). L'heure du coucher du soleil en janvier, les vieilles histoires du temple et ce qu'il faut vérifier avant d'y aller sont dans l'onglet Posts de la chaîne.

À l'écoute : Amber Window, de 「다섯 가지 고요」 (« Cinq formes de calme ») · Feu Yang.""","#FiveElementsMusic #Korea #Sunset"),
'it':("Manghaesa, Gimje: il tempio che guarda il mare","""Manghaesa a Gimje, il tempio che guarda il mare.

Dove finiscono le pianure di Gimje e Mangyeong, uno dei pochi luoghi in Corea da cui si vede l'orizzonte sulla terra, comincia il mare. Il sole è 丙火 Fuoco Yang (Byeonghwa), il grande fuoco del cielo. Vediamo il sole che scende basso al bordo dei campi come la forma del 2027: un grande fuoco che diventa una piccola luce (è la nostra lettura). A che ora tramonta il sole a gennaio, le antiche storie del tempio e cosa controllare prima di andare: è nella scheda Post del canale.

In ascolto: Amber Window, da 「다섯 가지 고요」 («Cinque forme di quiete») · Fuoco Yang.""","#FiveElementsMusic #Korea #Sunset"),
'pt':("Manghaesa, Gimje: o templo que olha para o mar","""Manghaesa em Gimje, o templo que olha para o mar.

Onde terminam as planícies de Gimje e Mangyeong, um dos poucos lugares da Coreia onde se vê o horizonte sobre a terra, começa o mar. O sol é 丙火 Fogo Yang (Byeonghwa), o grande fogo do céu. Vemos o sol descendo baixo na beira dos campos como a forma de 2027: um grande fogo que vira uma pequena luz (é a nossa leitura). A que horas o sol se põe em janeiro, as histórias antigas do templo e o que conferir antes de ir: está na aba Postagens do canal.

Tocando agora: Amber Window, de 「다섯 가지 고요」 («Cinco formas de quietude») · Fogo Yang.""","#FiveElementsMusic #Korea #Sunset"),
'ja':("海を望む寺、金堤・望海寺の夕日","""海を望む寺、金堤の望海寺（マンヘサ）。

地平線が見られる数少ない場所、金堤・万頃の平野が終わるところで海が始まります。太陽は丙火（ひのえ）、空の大きな火。その太陽が野の果てで低く沈んでいく姿を、大きな火が小さな灯りへ移っていく2027年の形として見ています（私たちの解釈です）。1月の日の入りの時刻、寺に伝わる古い話、行く前に確かめることは、チャンネルの「投稿」タブにあります。

いま流れているのは「다섯 가지 고요」（五つの静けさ）丙火編の『Amber Window』です。""","#FiveElementsMusic #Korea #Sunset"),
'zh-Hans':("望海寺：金堤看海的寺院与日落","""金堤望海寺，一座望着大海的寺院。

金堤·万顷平原是韩国少数能看到地平线的地方，平原的尽头就是大海。太阳是丙火，天上的大火。我们把太阳在田野尽头低低落下的样子，看作大火转成小小灯光的2027年（这是我们的解读）。一月几点日落、寺院的古老故事、出发前要确认的事，都在频道的帖子里。

正在播放：「다섯 가지 고요」（五种静谧）丙火篇的《Amber Window》。""","#FiveElementsMusic #Korea #Sunset"),
'zh-Hant':("望海寺：金堤看海的寺院與日落","""金堤望海寺，一座望著大海的寺院。

金堤·萬頃平原是韓國少數能看到地平線的地方，平原的盡頭就是大海。太陽是丙火，天上的大火。我們把太陽在田野盡頭低低落下的樣子，看作大火轉成小小燈光的2027年（這是我們的解讀）。一月幾點日落、寺院的古老故事、出發前要確認的事，都在頻道的貼文裡。

正在播放：「다섯 가지 고요」（五種靜謐）丙火篇的〈Amber Window〉。""","#FiveElementsMusic #Korea #Sunset"),
'vi':("Manghaesa, Gimje: ngôi chùa ngắm biển","""Manghaesa ở Gimje, ngôi chùa ngắm biển.

Đồng bằng Gimje – Mangyeong là một trong số ít nơi ở Hàn Quốc có thể thấy đường chân trời trên đất liền, và nơi cánh đồng kết thúc chính là nơi biển bắt đầu. Mặt trời là Bính Hỏa (丙火), ngọn lửa lớn trên trời. Chúng tôi xem cảnh mặt trời hạ thấp ở cuối cánh đồng như hình dáng của năm 2027: ngọn lửa lớn chuyển thành ánh sáng nhỏ (đây là cách đọc của chúng tôi). Mặt trời tháng Giêng lặn lúc mấy giờ, những câu chuyện xưa của chùa và những điều cần kiểm tra trước khi đi đều có trong bài đăng của kênh.

Đang phát: Amber Window trong 「다섯 가지 고요」 (Năm kiểu tĩnh lặng) · Bính Hỏa.""","#FiveElementsMusic #Korea #Sunset"),
'th':("มังแฮซา คิมเจ: วัดที่มองทะเล","""มังแฮซาที่คิมเจ วัดที่มองออกไปยังทะเล

ที่ราบคิมเจ–มังกย็องเป็นหนึ่งในไม่กี่แห่งในเกาหลีที่มองเห็นเส้นขอบฟ้าบนแผ่นดิน และตรงที่ทุ่งสิ้นสุดลงคือที่ที่ทะเลเริ่มต้น ดวงอาทิตย์คือไฟหยาง (丙火) ไฟใหญ่บนฟ้า เรามองภาพดวงอาทิตย์ที่ลดต่ำลงที่ปลายทุ่งว่าเป็นรูปของปี 2027 ไฟใหญ่ที่ค่อย ๆ กลายเป็นแสงเล็ก ๆ (เป็นการอ่านของเราเอง) ดวงอาทิตย์เดือนมกราคมตกกี่โมง เรื่องเก่าของวัด และสิ่งที่ควรเช็กก่อนไป อยู่ในโพสต์ของช่อง

กำลังเล่น: Amber Window จาก 「다섯 가지 고요」 (ความสงบห้าแบบ) · ไฟหยาง""","#FiveElementsMusic #Korea #Sunset"),
'ar':("مانغهيسا في كيمجي: المعبد المطل على البحر","""مانغهيسا في كيمجي، المعبد الذي يطل على البحر.

سهول كيمجي ومانغيونغ من الأماكن القليلة في كوريا التي يُرى فيها الأفق فوق اليابسة، وحيث تنتهي الحقول يبدأ البحر. الشمس هي 丙火 نار اليانغ (بيونغ هوا)، النار الكبيرة في السماء. نرى الشمس وهي تنخفض عند طرف الحقول صورةً لعام 2027: نار كبيرة تتحول إلى ضوء صغير (وهذه قراءتنا الخاصة). موعد غروب شمس يناير، وحكايات المعبد القديمة، وما ينبغي التحقق منه قبل الزيارة: كلها في منشورات القناة.

تُعزف الآن: Amber Window من «خمسة وجوهٍ للسكون» · نار اليانغ.""","#FiveElementsMusic"),
}
out={'TxgQp6pk37M':{}}
for l,(t,b,h) in T.items():
    lab=LB[l]; lines=[f'{lab[0]} ▶ {MV}',f'{lab[1]} ▶ {PL}']
    if lab[2]: lines+=[f'{lab[2]} ▶ https://goyomio.com',f'{lab[3]} ▶ https://www.instagram.com/goyo_mio']
    assert len(t)<=95
    out['TxgQp6pk37M'][l]={'title':t,'description':b+'\n\n'+'\n'.join(lines)+'\n\n'+h}
json.dump(out,open('loc.json','w'),ensure_ascii=False,indent=1);print(len(out['TxgQp6pk37M']))
