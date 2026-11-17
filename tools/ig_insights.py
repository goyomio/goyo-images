#!/usr/bin/env python3
"""주간 성과 요약. 사용: python3 tools/ig_insights.py [일수=7]
최근 N일 피드 게시물의 조회·도달·저장·공유·좋아요·댓글을 모아 순위를 낸다.
기준(중앙값) 대비 3배 이상이면 '튄 게시물'로 표시. 결과는 log/insights/YYYY-MM-DD.md 에도 저장."""
import json, sys, os, statistics, datetime as dt, urllib.request, urllib.parse, urllib.error
IG='17841458898232975'; V='v23.0'
KEY=next(p for p in ['/home/claude/goyo-keys/ig_token.txt','../goyo-keys/ig_token.txt'] if os.path.exists(p))
T=open(KEY).read().strip()
def get(path, **q):
    q['access_token']=T
    try: return json.load(urllib.request.urlopen(f'https://graph.facebook.com/{V}/{path}?'+urllib.parse.urlencode(q),timeout=60))
    except urllib.error.HTTPError as e: return {'error':e.read().decode()[:200]}
days=int(sys.argv[1]) if len(sys.argv)>1 else 7
since=dt.datetime.now(dt.timezone.utc)-dt.timedelta(days=days)
acct=get(IG, fields='followers_count,media_count')
rows=[]; url_next=None
data=get(f'{IG}/media', fields='id,timestamp,media_type,media_product_type,permalink,caption,like_count,comments_count', limit=50).get('data',[])
for m in data:
    ts=dt.datetime.strptime(m['timestamp'],'%Y-%m-%dT%H:%M:%S%z')
    if ts<since: continue
    met={}
    for k in ['views','reach','saved','shares']:
        r=get(f"{m['id']}/insights", metric=k)
        met[k]=r['data'][0]['values'][0]['value'] if r.get('data') else None
    kst=ts.astimezone(dt.timezone(dt.timedelta(hours=9)))
    title=(m.get('caption') or '').split('\n')[0][:28]
    kind='릴스' if m.get('media_product_type')=='REELS' else ('타로' if '고요의 세 장' in (m.get('caption') or '') else '피드')
    rows.append(dict(t=kst.strftime('%m/%d %H:%M'),kind=kind,title=title,link=m['permalink'],likes=m.get('like_count',0),comments=m.get('comments_count',0),**met))
def score(r): return (r['reach'] or 0)+3*(r['saved'] or 0)+3*(r['shares'] or 0)
rows.sort(key=score, reverse=True)
perm_ok=any(r['reach'] is not None for r in rows)
med=statistics.median([r['reach'] or 0 for r in rows]) if rows else 0
L=[f"# 고요 주간 성과 ({dt.date.today()} 기준 최근 {days}일)",f"팔로워 {acct.get('followers_count','?')} · 전체 게시물 {acct.get('media_count','?')} · 이번 기간 {len(rows)}개 · 도달 중앙값 {med:g}","",
   ("" if perm_ok or not rows else "※ 토큰에 instagram_manage_insights 권한이 없어 도달·조회·저장·공유는 비어 있음(좋아요·댓글만 집계)"),"",
   "| 순위 | 게시 | 종류 | 첫 줄 | 도달 | 조회 | 저장 | 공유 | 좋아요 | 댓글 | 비고 |","|---|---|---|---|---|---|---|---|---|---|---|"]
for i,r in enumerate(rows,1):
    note='튄 게시물(중앙값 3배↑)' if med and (r['reach'] or 0)>=3*med else ''
    L.append(f"| {i} | {r['t']} | {r['kind']} | {r['title']} | {r['reach']} | {r['views']} | {r['saved']} | {r['shares']} | {r['likes']} | {r['comments']} | {note} |")
out='\n'.join(L); print(out)
os.makedirs('log/insights',exist_ok=True); open(f'log/insights/{dt.date.today()}.md','w').write(out+'\n')
