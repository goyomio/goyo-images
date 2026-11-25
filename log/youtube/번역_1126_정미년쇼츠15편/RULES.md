# GOYO 번역 규칙 (agents) — YouTube localized title + description

Channel: GOYO (고요), handle @goyo_mio. Quiet instrumental playlists, each one carrying one of the Five Elements (오행: 木 Wood, 火 Fire, 土 Earth, 金 Metal, 水 Water) and the ten Heavenly Stems (천간: 甲 갑목 … 癸 계수). The creator is Korean.

## Input
`job_<lang>.json` — a list of items. Each item:
- `id`, `kind` (`short` = YouTube Short, `main` = 1h+ playlist video), `ko_title`, `ko_description` (the CURRENT Korean text on YouTube — this is the source of truth)
- `reference_en`: existing English translation, if any (may be older than the Korean; use only for term consistency, never copy facts the Korean no longer has)
- `mode`: `full` → write title + description. `description_only` → the title in this language already exists (`existing_title`) and MUST stay unchanged; write only the description.

## Absolute rules
1. **Title ≤ 95 characters** (Python `len()`). Never exceed. Shorter is better: the first ~40 chars are what phones show, so put the element / use (study, sleep, focus…) / hook first.
2. Facts and structure stay the same as the Korean (numbers, durations, instruments, track names, timestamps, links, @goyo_mio, the playlist URL). **Never add claims that are not in the Korean.**
3. **Not literal translation.** Rewrite each sentence so it sounds natural to a native reader of that culture (말맛·글맛). Keep the meaning; change the wording.
4. Forbidden:
   - Promising effects (better focus, luck improves, fixes your chart). The Korean already avoids this — keep it that way.
   - Naming a country as the origin ("Chinese tradition", "Korean tradition"). At most "an old East Asian way of seeing the world".
   - Five-colour (오방색) explanations.
   - Element name alone in Western languages where it could read as a plain noun: write "Fire element" / "Feuer-Element" etc. where natural (titles may use "Fire (火)").
   - Names of real artists; names of Korean traditional instruments.
   - "No ads" or anything not factual.
5. Metal (金) is not just metal — it includes stone and ore. When a Short is about Metal, use: EN `Metal (Stone & Ore)`, JA `金（石・鉱石）`, ES `Metal (piedra y mineral)`, PT `Metal (pedra e minério)`, other languages the equivalent ("metal, stone and ore").
6. Hashtags: replace Korean hashtags with English ones, 1–3 total, e.g. `#FiveElementsMusic #BirthChart` (saju-themed) or `#FiveElementsMusic #StudyMusic` / `#SleepMusic` (use-themed). Keep `#Shorts` if the Korean has it.
7. Lines starting with `▶` stay as separate lines in the same order.
   - The line `▶ 내 일간과 오행 찾기: @goyo_mio 채널 맨 위 링크` = "▶ Find your Day Master and element: first link on the @goyo_mio channel page". Translate naturally; keep `@goyo_mio`.
   - Playlist names in quotes like 「GOYO 오행음악」 stay in Korean inside quotes.
8. The ※ sentence: translate the meaning of the Korean ※ line exactly (it says it is an interpretive series by a creator who studied the Five Elements, carrying each element's character into tempo, melody and harmony). In gendered languages (de, es, it, pt, fr, ar) avoid gendering "the creator": use passive voice or "a personal interpretation".
9. Address: DE `Sie`, FR `vous`, ES `tú` (Latin American), PT `você` (Brazilian Portuguese), IT `tu`.
10. Language specifics:
    - Saju/사주 = Four Pillars of Destiny / birth chart. JA 命式・四柱推命, ZH 八字, VI lá số bát tự, TH ดวงสี่เสา / ดวงชะตา.
    - 일간 = Day Master. JA 日干, ZH 日主/日元, VI nhật chủ, TH ธาตุประจำวันเกิด (ดิถีวัน) — pick the term natives in that astrology community actually use.
    - Heavenly Stems: JA readings 甲（きのえ）乙（きのと）丙（ひのえ）丁（ひのと）戊（つちのえ）己（つちのと）庚（かのえ）辛（かのと）壬（みずのえ）癸（みずのと）. ZH/VI keep Hanja-style names (甲木 / Giáp Mộc). Western languages: romanised Korean + Hanja, e.g. `Gapmok (甲木)`, `Gyeonggeum (庚金)`, `Imsu (壬水)`. TH: สิบก้านฟ้า (never ราศี).
    - JA/ZH/VI titles for Shorts: no 【】 prefix needed; natural hook phrasing.
    - **Arabic (ar): remove every mention of saju / fortune / luck / astrology / birth chart / Day Master / luck practices (개운법)** — possibly sensitive in Islamic cultures. Reframe as nature and yin–yang philosophy and the sound itself. Drop the `▶ 내 일간과 오행 찾기` line entirely. If a Short's whole hook is about saju, rewrite the title/description around the element's nature and the music (e.g. "Too much Water in your chart?" → "The sound of Water: piano that flows like a great river"). Keep all links and @goyo_mio lines that are not about saju.
    - Chinese: zh-Hans for mainland (学习·自习 vocabulary), zh-Hant for Taiwan (唸書·讀書, 影片, 播放清單).
11. Track titles in English and timestamps stay exactly as in Korean. Translate only headings.
12. A main video (`kind: main`) keeps the Korean section structure, separators (━ ─ lines) and order.

## Output
JSON object `{ "<id>": {"title": "...", "description": "..."} }` covering every item (for `description_only`, set `title` to `existing_title` unchanged). Use exactly the item order. Write real newlines (\n) as in the Korean.

## 2026-11-18 unified terms (override older lines above)
- Day Master: EN Day Master / DE Tagesmeister (saju → BaZi) / FR Maître du Jour / ES Maestro del Día / PT Mestre do Dia / IT Maestro del Giorno / JA 日干 / ZH 日主 / VI nhật chủ / TH ธาตุเจ้าเรือน.
- Thai Heavenly Stems: ไม้หยาง/ไม้หยิน… + Hanja (not Korean transliteration).
- Series name: Arabic «خمسة وجوهٍ للسكون»; elsewhere 「다섯 가지 고요」 in quotes + short gloss.
- Track names in 『』 (e.g. 『Morning Tendril』) stay exactly; 을목 편 etc. = the Eulmok (乙木) episode.
- The ▶ line (2nd line of each Korean description, e.g. `▶ 무료 사주앱에서 내 ○○과 오행음악 찾기: @goyo_mio 채널 맨 위 링크`) = "▶ Find your ○○ and its Five Elements music in the free saju app: top link on the @goyo_mio channel page". Translate naturally. Arabic: drop this line.
- Add per-episode term lines here (shinsal names in each language), e.g. 문창 文昌 / 학당 學堂: ZH 文昌贵人·学堂贵人, JA 文昌貴人・学堂貴人, VI Văn Xương · Học Đường, Western "Scholar Star (文昌, Munchang)".
- Arabic false positive: «قدرة» (ability) contains «قدر» — not a fate word.

## 2026-11-21 batch notes (example saju shorts, tarot short, two older shorts)
- 예시 사주 풀이 #N = "Example Saju Reading #N" (an example chart, not a real client). Keep the birth date/time/sex exactly. Answers stay soft ("the flow allows…", "it's okay to…"); never stronger than the Korean.
- 「@goyo_mio 채널 게시물」 = the Posts (community) tab of the GOYO (@goyo_mio) YouTube channel.
- The line 「매일 아침 오늘의 타로 보기 (인스타그램) ▶ https://www.instagram.com/goyo_mio」 = "Daily tarot every morning on Instagram". Keep the URL. Arabic: drop this line (tarot = fortune-telling).
- Korean descriptions contain a «· English ·» block. Write ONE version in the target language only (merge, no English duplicate). For `en`, produce one clean English version.
- Series name inside the text: 「다섯 가지 고요」 in quotes + short gloss (e.g. EN "Five Kinds of Quiet"); Arabic «خمسة وجوهٍ للسكون».
- (11/21 17:45 미오 님 새 규칙) Western languages name the ten stems ONLY by yin-yang + element: EN "Yang Water (Imsu)", ES "Agua Yang (Imsu)", FR "Eau Yang (Imsu)", PT "Água Yang (Imsu)", DE "Yang-Wasser (Imsu)", IT "Acqua Yang (Imsu)". Asian languages keep Hanja-style names.
- Arabic for example-saju shorts: the whole hook is saju. Rewrite title/description around the question as a life moment + the music (e.g. "Money: can it be saved? A quiet piece of music for a careful season"), no chart, no birth data, no fortune words, no Posts-tab reading line, no saju app line, no tarot line. Keep the music link and the playlist link.
- Tarot short (eowoy8xi04Q) is English only.

## 2026-11-26 batch notes (정미년 series shorts, 2027-01-01 ~ 01-12) — OVERRIDE older notation lines
- These Shorts are a New Year (2027, 丁未 year) series. Korean source descriptions contain a «· English ·» block already written by the channel; use it as a reference for terms, but write ONE version in the target language only.
- ★ Stem/branch notation (11/21 final, all channels): inside ONE title+description, the FIRST mention is Hanja + yin-yang element in that language + (romanised Korean), afterwards the yin-yang element only.
  EN: first `丁火 Yin Fire (Jeonghwa)` → later `Yin Fire`. ES `丁火 Fuego Yin (Jeonghwa)` → `Fuego Yin`. FR `丁火 Feu Yin (Jeonghwa)`. PT `丁火 Fogo Yin (Jeonghwa)`. DE `丁火 Yin-Feuer (Jeonghwa)`. IT `丁火 Fuoco Yin (Jeonghwa)`.
  Stems: 甲木 Yang Wood (Gapmok) · 乙木 Yin Wood (Eulmok) · 丙火 Yang Fire (Byeonghwa) · 丁火 Yin Fire (Jeonghwa) · 戊土 Yang Earth (Muto) · 己土 Yin Earth (Gito) · 庚金 Yang Metal (Gyeonggeum) · 辛金 Yin Metal (Singeum) · 壬水 Yang Water (Imsu) · 癸水 Yin Water (Gyesu).
  Branches (time of day + element): 子 Midnight Water (Jasu) · 丑 Deep Night Earth (Chukto) · 寅 Predawn Wood (Inmok) · 卯 Daybreak Wood (Myomok) · 辰 Morning Earth (Jinto) · 巳 Midmorning Fire (Sahwa) · 午 Noon Fire (Ohwa) · 未 Afternoon Earth (Mito) · 申 Late Day Metal (Singeum) · 酉 Dusk Metal (Yugeum) · 戌 Nightfall Earth (Sulto) · 亥 Late Night Water (Haesu).
  Year: first `the 丁未 year (Jeongmi) · Yin Fire · Afternoon Earth`, later `this year` / `Yin Fire · Afternoon Earth`. 丙午 year (Byeong-o) · Yang Fire · Noon Fire. Translate the words "Yin Fire / Afternoon Earth / Noon Fire" etc. into the target Western language the same way.
  Asian languages (ja, zh-Hans, zh-Hant, vi, th) keep the unified terms above (JA 丁（ひのと）, ZH 丁火, VI Đinh Hỏa, TH ไฟหยิน (丁)…); branches JA 未（ひつじ）is an ANIMAL reading — avoid animal words: write 未 plus 「午後の土」-type gloss.
  NEVER animal names (Horse, Goat, Sheep…) and NEVER clock-number hours for branches. 「Saju」 stays Saju in Western languages (DE may use BaZi per older note → for this batch use "Saju").
  입춘 = start of spring (立春) — translate naturally, keep 立春.
- Series music name: 『다섯 가지 고요｜갑목(甲木)』 = 「다섯 가지 고요」 (Five Kinds of Quiet) · 甲木 Yang Wood (Gapmok) etc. Track names in 『』 stay exactly in English as written.
- 「채널 게시물」/「피드 게시물」 = the Posts tab of the @goyo_mio channel.
- Classical quotes (적천수 滴天髓 Di Tian Sui, 궁통보감 窮通寶鑑, 지봉유설 芝峰類說 etc.): keep the Hanja quote exactly, translate the gloss.
- Links block: the lines `… ▶ URL` stay one per line in the same order with URLs unchanged; translate the labels. Arabic: drop the saju-app line and the tarot line (see above) and remove every saju/fortune/Day Master mention; reframe around nature, season, culture and the music.
- Hashtags: 1–3, English (e.g. #FiveElementsMusic #Saju #NewYear) — Arabic: #FiveElementsMusic only.
- Do not add any claim not in the Korean. Soft wording stays soft ("can", "may", "how it lands depends on the whole chart").
