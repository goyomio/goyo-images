#!/usr/bin/env python3
"""인스타 열쇠(ig_token.txt)가 아직 되는지만 확인. 열쇠 값은 절대 출력하지 않음.
종료코드 0 = 정상, 1 = 안 됨(만료·끊김 가능)."""
import json, sys, urllib.request, urllib.parse
t = open('/home/claude/goyo-keys/ig_token.txt').read().strip()
u = 'https://graph.facebook.com/v23.0/17841458898232975?' + urllib.parse.urlencode({'fields': 'username', 'access_token': t})
try:
    d = json.load(urllib.request.urlopen(u, timeout=30))
    print('ok', d.get('username')); sys.exit(0)
except urllib.error.HTTPError as e:
    try: err = json.load(e).get('error', {})
    except Exception: err = {}
    print('fail', e.code, err.get('code'), err.get('error_subcode'), (err.get('message') or '')[:120].replace(t, '***')); sys.exit(1)
