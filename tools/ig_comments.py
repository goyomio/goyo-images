#!/usr/bin/env python3
"""goyo_mio 댓글 읽기·답글 (Instagram Graph API, 직접 API).
  python3 ig_comments.py list --since "2026-11-17T06:00:00+09:00"   # 그 시각 이후 새 댓글 (JSON)
  python3 ig_comments.py reply <comment_id> "답글 내용"              # 미오 님이 승인한 답글만!
토큰: goyo-keys/ig_token.txt — 출력·복사 금지."""
import json, sys, datetime as dt, urllib.request, urllib.parse, os
IG = '17841458898232975'; V = 'v23.0'; ME = 'goyo_mio'
KEY = os.environ.get('GOYO_TOKEN_FILE') or next(p for p in ['/home/claude/goyo-keys/ig_token.txt', '../goyo-keys/ig_token.txt', os.path.expanduser('~/goyo-keys/ig_token.txt')] if os.path.exists(p))
T = open(KEY).read().strip()


def call(path, data=None):
    url = f'https://graph.facebook.com/{V}/{path}'
    if data is None:
        url += ('&' if '?' in url else '?') + 'access_token=' + T
        req = urllib.request.Request(url)
    else:
        req = urllib.request.Request(url, urllib.parse.urlencode(dict(data, access_token=T)).encode())
    try:
        return json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        print('ERR', e.read().decode()); sys.exit(1)


def ts(s):
    return dt.datetime.fromisoformat(s.replace('+0000', '+00:00'))


def pages(path):
    r = call(path)
    while True:
        yield from r.get('data', [])
        nxt = r.get('paging', {}).get('next')
        if not nxt:
            return
        r = json.load(urllib.request.urlopen(nxt, timeout=60))


def list_new(since):
    since = dt.datetime.fromisoformat(since)
    out = []
    for m in pages(f'{IG}/media?fields=id,caption,permalink,timestamp,comments_count&limit=50'):
        if not m.get('comments_count'):
            continue
        cap = (m.get('caption') or '').split('\n')[0]
        for c in pages(f"{m['id']}/comments?fields=id,text,username,timestamp,replies{{username}}&limit=50"):
            if c.get('username') == ME or ts(c['timestamp']) < since:
                continue
            if any(r.get('username') == ME for r in c.get('replies', {}).get('data', [])):
                continue
            out.append({'comment_id': c['id'], 'username': c.get('username'), 'text': c.get('text'),
                        'timestamp': c['timestamp'], 'post': cap, 'permalink': m.get('permalink')})
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'list':
        list_new(a[a.index('--since') + 1])
    elif a and a[0] == 'reply' and len(a) == 3:
        print(json.dumps(call(f'{a[1]}/replies', {'message': a[2]})))
    else:
        print(__doc__); sys.exit(2)
