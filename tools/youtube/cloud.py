#!/usr/bin/env python3
"""GOYO 유튜브 API를 클라우드(맥 없이)에서 돌리는 도우미 (2026-11-21 미오 님 결정: 유튜브 열쇠를 goyo-keys로 옮김)

사용 (goyo-images 저장소 맨 위에서):
  python3 tools/youtube/cloud.py goyo list
  python3 tools/youtube/cloud.py goyo loc-apply check|test|all 파일.json
  python3 tools/youtube/cloud.py goyo shorts-upload check|test|all 계획.json
  python3 tools/youtube/cloud.py goyo thumb-set all 썸네일계획.json   ([{"id": 영상ID, "thumb": 파일}])

지키는 것
 - 열쇠는 goyo-keys/youtube/ 에서 읽기만 한다(화면 출력·복사·저장소에 넣기 금지). 위치는 환경변수 GOYO_KEYS 로 바꿀 수 있음.
 - goyo_yt.py 는 맥 _api/goyo_yt.py 와 같은 파일. 여기서 고치지 않는다(공용 부분은 mio 창도 씀).
 - 클라우드에서는 브라우저 로그인이 불가능하므로, 열쇠가 죽으면 멈추고 알린다(맥에서 로그인 → goyo-keys 다시 올리기).
 - 한도 기록은 log/youtube/한도_YYYYMMDD.txt(태평양 날짜)에 남긴다. 맥의 mio 사용량은 맥 _api/한도_*.txt 에 따로 있으므로 하루 합계는 둘을 더해서 본다.
 - 채널은 goyo만 허용.
"""
import glob, os, shutil, subprocess, sys, json, time

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
KEYS = os.environ.get('GOYO_KEYS', '/home/claude/goyo-keys/youtube')
RUN = '/tmp/ytcloud'
LOGDIR = os.path.join(REPO, 'log', 'youtube')
VENV = '/tmp/ytvenv'


def _venv():
    py = f'{VENV}/bin/python'
    if not os.path.exists(py):
        subprocess.run([sys.executable, '-m', 'venv', VENV], check=True)
        subprocess.run([f'{VENV}/bin/pip', 'install', '-q', 'google-api-python-client', 'google-auth-oauthlib'], check=True)
    return py


def prepare():
    for f in ('client_secret.json', 'token_goyo.json'):
        if not os.path.exists(os.path.join(KEYS, f)):
            sys.exit(f'멈춤: 열쇠 파일이 없어요 ({KEYS}). goyo-keys 저장소를 먼저 받아 주세요.')
    os.makedirs(RUN, exist_ok=True)
    os.makedirs(LOGDIR, exist_ok=True)
    shutil.copy(os.path.join(os.path.dirname(__file__), 'goyo_yt.py'), RUN)
    for f in ('client_secret.json', 'token_goyo.json'):
        dst = os.path.join(RUN, f)
        if os.path.lexists(dst):
            os.remove(dst)
        os.symlink(os.path.join(KEYS, f), dst)
    for q in glob.glob(os.path.join(LOGDIR, '한도_*.txt')) + glob.glob(os.path.join(LOGDIR, '작업기록.txt')):
        shutil.copy(q, RUN)


def finish():
    for q in glob.glob(os.path.join(RUN, '한도_*.txt')) + glob.glob(os.path.join(RUN, '작업기록.txt')):
        shutil.copy(q, LOGDIR)


def load():
    """/tmp/ytcloud 의 goyo_yt 모듈을 불러오고, 브라우저 로그인을 막고, 썸네일 작업을 더한다."""
    sys.path.insert(0, RUN)
    import goyo_yt as g

    class NoBrowser:
        @staticmethod
        def from_client_secrets_file(*a, **k):
            g.log('멈춤: 유튜브 열쇠가 만료됐거나 끊겼어요. 맥 터미널에서 bash ~/Desktop/고요음악/_api/run.sh goyo login 뒤 '
                  'token_goyo.json 을 goyo-keys/youtube/ 에 다시 올려 주세요.')
            finish(); sys.exit(2)
    g.InstalledAppFlow = NoBrowser

    def job_thumb_set(yt, ch, channel, mode):
        from googleapiclient.http import MediaFileUpload
        path = sys.argv[4] if len(sys.argv) > 4 else None
        plan = json.load(open(path, encoding='utf-8'))
        if mode == 'check':
            for it in plan:
                print(it['id'], it['thumb'], os.path.exists(it['thumb']))
            return
        for it in (plan[:1] if mode == 'test' else plan):
            g.guard(52)
            r = yt.thumbnails().set(videoId=it['id'], media_body=MediaFileUpload(it['thumb'], mimetype='image/jpeg')).execute(); g.spend(50)
            ok = bool(r.get('items'))
            g.log(f"{'성공' if ok else '확인 필요'} 썸네일 {it['id']} | {os.path.basename(it['thumb'])}")
    g.JOBS['thumb-set'] = job_thumb_set
    return g


def run(argv):
    """argv 예: ['goyo', 'list'] — goyo_yt.main() 을 그대로 부른다."""
    if not argv or argv[0] != 'goyo':
        sys.exit('멈춤: 클라우드에서는 goyo 채널만 써요.')
    prepare()
    g = load()
    sys.argv = ['goyo_yt.py'] + list(argv)
    try:
        g.main()
    finally:
        finish()
    return g


if __name__ == '__main__':
    if os.environ.get('YT_IN_VENV') != '1':
        os.environ['YT_IN_VENV'] = '1'
        os.environ.setdefault('TZ', 'Asia/Seoul')
        sys.exit(subprocess.call([_venv(), os.path.abspath(__file__)] + sys.argv[1:]))
    run(sys.argv[1:])
