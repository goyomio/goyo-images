# Native review instructions

You are a native-speaker editor for the target language. You did NOT write the drafts; review them critically.
Files: RULES.md (rules), job_<lang>.json (Korean sources, items with mode), draft_<lang>.json (drafts keyed by video id).

For every item, compare with the Korean source and RULES.md:
1. Meaning matches the Korean; nothing added or lost (numbers, durations, links, @goyo_mio, track names, timestamps, ▶ lines).
2. Sounds natively natural for that culture, not literal; terminology is what that language's Four Pillars / BaZi community actually uses.
3. No forbidden content: effect promises, country-of-origin claims, five-colour talk, artist or Korean instrument names, "no ads". Sentences that are not in the Korean must go (except a brief gloss of a Korean playlist name).
4. Metal shorts use the "Metal (Stone & Ore)" equivalent.
5. Title ≤95 characters (Python len), key words first. description_only items keep existing_title exactly.
6. English hashtags only; no hangul left in prose except quoted playlist names.
7. Korean descriptions that repeat each line in English: a single target-language version is correct (no English duplicate needed).

Fix problems directly. Save the full corrected set as final_<lang>.json (same format, ensure_ascii=False) and a log review_<lang>.md (each change: id, before → after, reason, one line). Re-run a Python check on final_<lang>.json (all ids, title lengths, description_only titles unchanged).
If the Korean title and description contradict each other, stay faithful and list it under "Korean source issues".
Reply with only: number of items changed, the "Korean source issues" list, and anything that should not be published (id + reason).
