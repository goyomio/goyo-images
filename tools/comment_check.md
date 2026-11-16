# 게시 뒤 댓글 확인 (예약 작업용 지시)

[게시 뒤 댓글 확인 — 게시가 끝난 다음에 하고, 알림은 게시 결과와 한 번에 보냅니다]
C1) Windsor 도구로 댓글을 읽습니다. mcp__Windsor_ai_for_Social_Media__get_data, connector "instagram", accounts ["17841458898232975"], fields ["comment_id","comment_text","comment_username","comment_timestamp","comment_parent_id","media_id","media_caption"], date_preset "last_3m". force_refresh는 쓰지 않습니다. Windsor가 없거나 오류면 한 번만 다시 시도하고, 그래도 안 되면 알림에 "댓글 확인 실패: 원인"만 덧붙입니다(게시는 그대로 진행).
C2) 다룰 댓글: 예약 작업 프롬프트에 적힌 확인 구간(한국 시간). goyo_mio 본인 댓글, 이미 goyo_mio가 답글을 단 댓글은 제외. 새 댓글이 없으면 알림에 댓글 이야기는 넣지 않습니다.
C3) 새 댓글마다 답글 초안: 해요체, 두세 문장, 댓글 유도 금지. 효과 주장 금지("채워 준다, 운이 바뀐다, 필요한 사주" 대신 "곁에 두기 좋은 소리"). 단정적 예언·의료·법률·투자 판단 금지. 링크·URL 대신 "프로필 링크 → GOYO". 곡은 이 목록만(각 영상 첫 곡, 지어내지 않기): 목: 갑목 Morning Oak(대표), 을목 Morning Tendril / 화: 병화 Noon Avenue(대표), 정화 Lamplit Keys / 토: 무토 Mountain Desk(대표), 기토 Tilled Morning / 금: 경금 Granite Light(대표), 신금 Prism / 수: 임수 Wide Water(대표), 계수 Drizzle. 영상 이름은 「다섯 가지 고요｜갑목(甲木)」처럼. 오행 두 개 이상 말한 댓글은 기운마다 대표곡 하나씩, 최대 두 기운. "다 있어요/다 없어요"류는 "사주마다 필요한 기운이 달라서, 고요에는 다섯 오행이 다 있어요"로. 악성·광고·스팸은 초안 없이 "숨기기 추천" 표시만.
C4) 알림에 댓글별로 [작성자, 원문, 게시물(캡션 첫 줄), 답글 초안]을 붙이고 끝에 "올릴 답글 번호를 말씀해 주시면 게시할게요".
C5) 절대 스스로 답글 게시·숨기기·삭제를 하지 않습니다. 미오 님이 이 대화에서 번호를 지정해 승인한 답글만 mcp__Windsor_ai_for_Social_Media__execute_action (connector "instagram", action "reply_to_comment", account "17841458898232975", params {"comment_id":..., "message":...})로 게시합니다.
