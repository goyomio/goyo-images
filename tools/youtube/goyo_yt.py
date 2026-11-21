# -*- coding: utf-8 -*-
"""유튜브 도우미 (YouTube Data API v3, 무료) — GOYO·mio 두 채널 공용

  bash run.sh <채널> <작업> [모드]
    채널: goyo | mio
    작업:
      login            로그인만 하고 어느 채널인지 확인 (처음 한 번)
      list             쇼츠·본편 목록과 개수만 보여줌 (아무것도 안 바꿈)
      saju-line        (goyo 전용) 쇼츠 설명란 둘째 줄에 사주앱 안내 넣기
      loc-apply        번역 파일 넣기: bash run.sh goyo loc-apply check|test|all 파일.json
    모드: check(목록만, 기본) | test(1편만) | all(전부)
  예) bash run.sh goyo saju-line all
      bash run.sh mio login
"""
import os, sys, re, time, json, datetime, warnings
warnings.filterwarnings("ignore")
from datetime import timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
SECRET = os.path.join(HERE, "client_secret.json")
LOG = os.path.join(HERE, "작업기록.txt")
CHANNELS_FILE = os.path.join(HERE, "channels.json")
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
DAILY_LIMIT = 8000          # 하루 10,000점 중 8,000점까지만 (두 채널 합산)
SHORT_MAX_SEC = 240

CHANNELS = {   # 채널 번호는 처음 로그인 때 channels.json에 저장되고, 그 뒤로는 그 번호만 허용
    "goyo": {"id": "UCmXTroWxrDKnjIshIu--qMQ", "token": "token_goyo.json", "pick": "미오플리"},
    "mio":  {"id": None,                       "token": "token_mio.json",  "pick": "mio"},
}
NEVER = {"UCmXTroWxrDKnjIshIu--qMQ": "goyo"}   # 다른 채널 이름으로 GOYO에 들어가는 것 방지

SAJU_LINE = "▶ 내 일간과 오행 찾기: @goyo_mio 채널 맨 위 링크"
SAJU_MARK = "내 일간과 오행 찾기"

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


# ---------- 기록·한도 ----------
def log(msg):
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}  {msg}"
    print(line)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def _quota_file():
    day = (datetime.datetime.now(timezone.utc) - timedelta(hours=8)).strftime("%Y%m%d")  # 태평양 날짜 기준
    return os.path.join(HERE, f"한도_{day}.txt")

def used():
    f = _quota_file()
    return int((open(f).read().strip() or 0)) if os.path.exists(f) else 0

def spend(n):
    u = used() + n
    open(_quota_file(), "w").write(str(u))
    return u

def guard(cost):
    if used() + cost > DAILY_LIMIT:
        log(f"한도 멈춤: 오늘 {used()}점 사용. 내일(한국 시간 오후 4~5시 이후) 같은 명령으로 이어서 하면 돼요.")
        sys.exit(0)


# ---------- 로그인·채널 확인 ----------
def saved_ids():
    return json.load(open(CHANNELS_FILE)) if os.path.exists(CHANNELS_FILE) else {}

def login(ch):
    cfg = CHANNELS[ch]
    token = os.path.join(HERE, cfg["token"])
    creds = None
    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                creds = None
        if not creds or not creds.valid:
            print(f"\n브라우저에 구글 창이 열립니다. 계정 고르는 화면에서 「{cfg['pick']}」를 고르세요.\n")
            flow = InstalledAppFlow.from_client_secrets_file(SECRET, SCOPES)
            creds = flow.run_local_server(port=0, prompt="select_account consent")
        with open(token, "w") as f:
            f.write(creds.to_json())
        os.chmod(token, 0o600)
    yt = build("youtube", "v3", credentials=creds)
    r = yt.channels().list(part="snippet,contentDetails", mine=True).execute(); spend(1)
    items = r.get("items", [])
    if not items:
        log("멈춤: 이 계정에는 유튜브 채널이 없어요.")
        os.remove(token); sys.exit(1)
    got_id, got_name = items[0]["id"], items[0]["snippet"]["title"]
    want = cfg["id"] or saved_ids().get(ch)
    wrong = (want and got_id != want) or (not want and got_id in NEVER and NEVER[got_id] != ch)
    if wrong:
        log(f"멈춤: {ch} 채널이 아니에요 → {got_name}. 같은 줄을 다시 실행해 「{cfg['pick']}」를 고르세요.")
        os.remove(token); sys.exit(1)
    if not want:
        ids = saved_ids(); ids[ch] = got_id
        json.dump(ids, open(CHANNELS_FILE, "w"), ensure_ascii=False, indent=1)
        log(f"{ch} 채널 번호를 처음 저장했어요: {got_name} ({got_id}). 앞으로는 이 채널만 허용해요.")
    log(f"채널 확인: {got_name} ({got_id})")
    return yt, items[0]


# ---------- 영상 목록 ----------
def seconds(iso):
    m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    d, h, mi, s = (int(x) if x else 0 for x in m.groups()) if m else (0, 0, 0, 0)
    return d * 86400 + h * 3600 + mi * 60 + s

def all_videos(yt, channel):
    uploads = channel["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, token = [], None
    while True:
        r = yt.playlistItems().list(part="contentDetails", playlistId=uploads, maxResults=50, pageToken=token).execute(); spend(1)
        ids += [i["contentDetails"]["videoId"] for i in r["items"]]
        token = r.get("nextPageToken")
        if not token:
            break
    vids = []
    for k in range(0, len(ids), 50):
        r = yt.videos().list(part="snippet,status,contentDetails", id=",".join(ids[k:k + 50])).execute(); spend(1)
        vids += r["items"]
    return vids

def split(vids):
    shorts = [v for v in vids if seconds(v["contentDetails"]["duration"]) <= SHORT_MAX_SEC]
    longs = [v for v in vids if v not in shorts]
    sched = sorted([v for v in shorts if v["status"].get("publishAt") and v["status"]["privacyStatus"] == "private"],
                   key=lambda v: v["status"]["publishAt"])
    pub = sorted([v for v in shorts if v["status"]["privacyStatus"] == "public"],
                 key=lambda v: v["snippet"]["publishedAt"], reverse=True)
    return shorts, longs, sched, pub


# ---------- 설명란 고치기 (공통) ----------
def update_description(yt, v, new_desc, mark):
    guard(52)
    sn = v["snippet"]
    body = {"id": v["id"], "snippet": {"title": sn["title"], "description": new_desc, "categoryId": sn["categoryId"]}}
    for key in ("tags", "defaultLanguage", "defaultAudioLanguage"):
        if key in sn:
            body["snippet"][key] = sn[key]
    resp = yt.videos().update(part="snippet", body=body).execute(); spend(50)
    ok = mark in resp["snippet"].get("description", "")
    time.sleep(3)
    after = yt.videos().list(part="snippet,status", id=v["id"]).execute()["items"][0]; spend(1)
    same_status = (after["status"].get("publishAt") == v["status"].get("publishAt")
                   and after["status"]["privacyStatus"] == v["status"]["privacyStatus"])
    same_title = after["snippet"]["title"] == sn["title"]
    same_tags = sorted(after["snippet"].get("tags") or []) == sorted(sn.get("tags") or [])
    log(f"{'성공' if ok else '실패'} {v['id']} | 예약·공개상태 {'그대로' if same_status else '바뀜!'}"
        f" | 제목 {'그대로' if same_title else '바뀜!'} | 태그 {'그대로' if same_tags else '바뀜!'}"
        f" | {after['status']['privacyStatus']} {after['status'].get('publishAt','')} | {sn['title'][:40]}")
    return ok and same_status and same_title and same_tags


# ---------- 작업들 ----------
def job_list(yt, ch, channel, mode):
    shorts, longs, sched, pub = split(all_videos(yt, channel))
    log(f"[{ch}] 본편 {len(longs)}편 · 쇼츠 {len(shorts)}편 (예약 {len(sched)} · 공개 {len(pub)})")
    for v in longs + sched + pub:
        st = v["status"]
        print(f"  {'본편' if v in longs else '쇼츠'} {st['privacyStatus']:8s} {(st.get('publishAt') or v['snippet'].get('publishedAt',''))[:16]}  {v['id']}  {v['snippet']['title'][:45]}")

def job_saju_line(yt, ch, channel, mode):
    if ch != "goyo":
        log("멈춤: saju-line은 GOYO 전용이에요."); sys.exit(1)
    shorts, longs, sched, pub = split(all_videos(yt, channel))
    todo = [v for v in sched + pub if SAJU_MARK not in v["snippet"].get("description", "")]
    log(f"[goyo] 쇼츠 예약 {len(sched)} · 공개 {len(pub)} | 이미 들어감 {len(sched)+len(pub)-len(todo)} | 고칠 것 {len(todo)}")
    if mode == "check":
        for n, v in enumerate(todo, 1):
            print(f"{n:2d}. {v['id']}  {v['snippet']['title'][:45]}")
        print("\n(아무것도 바꾸지 않았어요)"); return
    if mode == "test":
        todo = todo[:1]
    for v in todo:
        d = v["snippet"].get("description", "")
        lines = d.split("\n")
        new = SAJU_LINE if not d.strip() else "\n".join([lines[0], SAJU_LINE] + lines[1:])
        if not update_description(yt, v, new, SAJU_MARK):
            log("멈춤: 확인이 맞지 않아 여기서 멈췄어요. Claude에게 알려 주세요."); sys.exit(1)
        time.sleep(1)
    log(f"끝: {len(todo)}편 고침 | 오늘 한도 사용 {used()}점 / 10,000")


# ---------- 번역(localizations) 넣기 ----------
def job_loc_apply(yt, ch, channel, mode):
    """번역 파일(JSON) {영상ID: {언어: {title, description}}} 을 기존 번역에 더한다.
    기존 언어는 그대로 두고(파일에 같은 언어가 있으면 그 언어만 바꿈), 제목 95자 초과는 멈춤."""
    path = sys.argv[4] if len(sys.argv) > 4 else None
    if not path or not os.path.exists(path):
        log("멈춤: 번역 파일을 찾지 못했어요."); sys.exit(1)
    data = json.load(open(path, encoding="utf-8"))
    order = list(data.keys())
    log(f"[{ch}] 번역 넣기: 파일 {os.path.basename(path)} · 영상 {len(order)}편")
    bad = [(vid, l, len(t["title"])) for vid in order for l, t in data[vid].items() if len(t.get("title", "")) > 95 or not t.get("title")]
    bad += [(vid, l, len(t["description"])) for vid in order for l, t in data[vid].items() if len(t.get("description", "")) > 4900]
    if bad:
        log(f"멈춤: 길이 초과 또는 빈 제목 {bad[:5]}"); sys.exit(1)
    if mode == "check":
        for vid in order:
            print(vid, ",".join(sorted(data[vid])))
        print("\n(아무것도 바꾸지 않았어요)"); return
    if mode == "test":
        order = order[:1]
    done = 0
    for vid in order:
        guard(53)
        cur = yt.videos().list(part="snippet,status,localizations", id=vid).execute()["items"][0]; spend(1)
        old = cur.get("localizations", {})
        if not cur["snippet"].get("defaultLanguage"):
            log(f"멈춤: {vid} 기본 언어가 비어 있어요."); sys.exit(1)
        if all(old.get(l, {}).get("title") == t["title"] and old.get(l, {}).get("description", "") == t.get("description", "") for l, t in data[vid].items()):
            log(f"건너뜀 {vid} | 이미 들어가 있음"); continue
        new = dict(old)
        for l, t in data[vid].items():
            new[l] = {"title": t["title"], "description": t.get("description", "")}
        yt.videos().update(part="localizations", body={"id": vid, "localizations": new}).execute(); spend(50)
        time.sleep(2)
        aft = yt.videos().list(part="snippet,status,localizations", id=vid).execute()["items"][0]; spend(1)
        al = aft.get("localizations", {})
        kept = all(al.get(k) == v for k, v in old.items() if k not in data[vid])
        added = all(al.get(l, {}).get("title") == t["title"] and al.get(l, {}).get("description", "") == t.get("description", "") for l, t in data[vid].items())
        same = (aft["snippet"]["title"] == cur["snippet"]["title"] and aft["snippet"]["description"] == cur["snippet"]["description"]
                and aft["status"].get("publishAt") == cur["status"].get("publishAt") and aft["status"]["privacyStatus"] == cur["status"]["privacyStatus"])
        log(f"{'성공' if kept and added and same else '실패'} {vid} | 기존 번역 {'그대로' if kept else '바뀜!'} | 새 번역 {'들어감' if added else '안 맞음!'}"
            f" | 한국어·예약 {'그대로' if same else '바뀜!'} | 언어 {len(al)}개 | {cur['snippet']['title'][:30]}")
        if not (kept and added and same):
            log("멈춤: 확인이 맞지 않아 여기서 멈췄어요."); sys.exit(1)
        done += 1
        time.sleep(1)
    log(f"끝: {done}편 번역 넣음 | 오늘 한도 사용 {used()}점 / 10,000")

# ---------- 쇼츠 새로 올리기 (11/19 추가) ----------
def job_shorts_upload(yt, ch, channel, mode):
    """계획 파일(JSON 목록: file, thumb, title, description, tags, publishAt, playlist)로 쇼츠를 예약 업로드.
    check=목록·재생목록·중복만 확인 / test=1편 / all=전부. 같은 제목이 이미 있으면 건너뜀."""
    from googleapiclient.http import MediaFileUpload
    path = sys.argv[4] if len(sys.argv) > 4 else None
    if ch != "goyo" or not path or not os.path.exists(path):
        log("멈춤: goyo 채널과 계획 파일이 필요해요."); sys.exit(1)
    plan = json.load(open(path, encoding="utf-8"))
    titles = {v["snippet"]["title"] for v in all_videos(yt, channel)}
    pls = yt.playlists().list(part="snippet", mine=True, maxResults=50).execute(); spend(1)
    pmap = {p["snippet"]["title"]: p["id"] for p in pls.get("items", [])}
    log(f"[goyo] 쇼츠 올리기 계획 {len(plan)}편 | 재생목록 {list(pmap)}")
    for it in plan:
        dup = it["title"] in titles
        miss = [k for k in ("file", "thumb") if it.get(k) and not os.path.exists(it[k])]
        print(f"  {'이미 있음' if dup else '올릴 것'} | {it['publishAt']} | 재생목록 {it['playlist']}={'있음' if it['playlist'] in pmap else '없음!'} | 파일없음 {miss} | {it['title'][:40]}")
        if miss or it["playlist"] not in pmap:
            log("멈춤: 파일이나 재생목록이 없어요."); sys.exit(1)
    if mode == "check":
        print("\n(아무것도 바꾸지 않았어요)"); return
    todo = [it for it in plan if it["title"] not in titles]
    if mode == "test":
        todo = todo[:1]
    for it in todo:
        guard(160)
        body = {"snippet": {"title": it["title"], "description": it["description"], "tags": it["tags"], "categoryId": "10",
                            "defaultLanguage": "ko", "defaultAudioLanguage": "ko"},
                "status": {"privacyStatus": "private", "publishAt": it["publishAt"], "selfDeclaredMadeForKids": False,
                           "containsSyntheticMedia": True, "embeddable": True, "license": "youtube"},
                "paidProductPlacementDetails": {"hasPaidProductPlacement": False}}
        media = MediaFileUpload(it["file"], mimetype="video/mp4", chunksize=8 * 1024 * 1024, resumable=True)
        req = yt.videos().insert(part="snippet,status,paidProductPlacementDetails", body=body, media_body=media)
        resp = None
        while resp is None:
            _, resp = req.next_chunk()
        vid = resp["id"]
        log(f"올림 {vid} | {it['title'][:40]}")
        time.sleep(3)
        st0 = {"privacyStatus": "private", "publishAt": it["publishAt"], "license": "youtube", "embeddable": True,
               "publicStatsViewable": True, "selfDeclaredMadeForKids": False, "containsSyntheticMedia": True}
        r0 = yt.videos().update(part="status", body={"id": vid, "status": st0}).execute(); spend(50)
        log(f"AI 표시 다시 넣음 {vid} | 응답 containsSyntheticMedia={r0['status'].get('containsSyntheticMedia')}")
        if it.get("thumb"):
            yt.thumbnails().set(videoId=vid, media_body=MediaFileUpload(it["thumb"], mimetype="image/jpeg")).execute(); spend(50)
        yt.playlistItems().insert(part="snippet", body={"snippet": {"playlistId": pmap[it["playlist"]],
                                  "resourceId": {"kind": "youtube#video", "videoId": vid}}}).execute(); spend(50)
        time.sleep(3)
        a = yt.videos().list(part="snippet,status,paidProductPlacementDetails", id=vid).execute()["items"][0]; spend(1)
        sn, st = a["snippet"], a["status"]
        chk = {"제목": sn["title"] == it["title"], "설명": sn.get("description") == it["description"],
               "태그": sorted(sn.get("tags") or []) == sorted(it["tags"]), "카테고리 음악": sn.get("categoryId") == "10",
               "언어 한국어": sn.get("defaultLanguage") == "ko" and sn.get("defaultAudioLanguage") == "ko",
               "비공개+예약": st.get("privacyStatus") == "private" and (st.get("publishAt") or "").startswith(it["publishAt"][:16]),
               "아동용 아님": st.get("selfDeclaredMadeForKids") is False,
               "유료 프로모션 없음": a.get("paidProductPlacementDetails", {}).get("hasPaidProductPlacement") is False}
        log(f"{'성공' if all(chk.values()) else '확인 필요'} {vid} | " + " · ".join(f"{k} {'O' if v else 'X'}" for k, v in chk.items())
            + f" | AI 표시 「예」 넣음(API로는 다시 읽히지 않음 — 스튜디오에서 확인) | 예약 {st.get('publishAt')} | 썸네일·재생목록 「{it['playlist']}」 넣음")
        if not all(chk.values()):
            log("멈춤: 확인이 맞지 않아 여기서 멈췄어요."); sys.exit(1)
    log(f"끝: {len(todo)}편 올림 | 오늘 한도 사용 {used()}점 / 10,000 (업로드 자체는 별도 한도)")

JOBS = {"login": None, "list": job_list, "saju-line": job_saju_line, "loc-apply": job_loc_apply}
JOBS["shorts-upload"] = job_shorts_upload


def main():
    a = sys.argv[1:]
    if len(a) < 2 or a[0] not in CHANNELS or a[1] not in JOBS:
        print(__doc__); sys.exit(1)
    ch, job = a[0], a[1]
    mode = a[2] if len(a) > 2 else "check"
    yt, channel = login(ch)
    if JOBS[job]:
        JOBS[job](yt, ch, channel, mode)
    log(f"오늘 한도 사용 {used()}점 / 10,000 (두 채널 합산)")

if __name__ == "__main__":
    main()
