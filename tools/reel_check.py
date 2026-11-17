#!/usr/bin/env python3
"""릴스 곡 이름 점검. 화면·캡션에 적힌 『곡』(○○ 편)이 실제 음원과 맞는지 확인한다.
사용:
  python3 tools/reel_check.py --build                 # shorts/곡대응표.json 다시 만들기(업로드 문구에서 추출)
  python3 tools/reel_check.py <릴스설정.json>          # 영상 만들기 전 점검(saju_reel.py 가 자동 호출)
  python3 tools/reel_check.py posts/<폴더>/post.json   # 게시 전 점검(run_post.py 가 자동 호출)
문제가 있으면 [곡오류] 줄을 출력하고 종료코드 1. 근거가 없는 곡 이름은 통과시키지 않는다."""
import glob, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
MAP = os.path.join(ROOT, 'shorts', '곡대응표.json')
TITLE = re.compile(r'『([^』]+)』\s*\(([^)]+?)\s*편\)')


def build():
    out = {}
    for txt in sorted(glob.glob(os.path.join(ROOT, 'shorts', '**', '*.txt'), recursive=True)):
        rel_dir = os.path.relpath(os.path.dirname(txt), ROOT)
        lines = open(txt, encoding='utf-8').read().splitlines()
        cur = None; cur_pyeon = None
        for i, ln in enumerate(lines, 1):
            m = re.search(r'—\s*(\S+)\s+파일:\s*(.+?\.mp4)', ln)
            if m:
                cur = os.path.join(rel_dir, m.group(2).strip()); cur_pyeon = m.group(1)
                out[cur] = {'편': cur_pyeon, '곡': None, '근거': None}
                continue
            m = re.search(r'쇼츠 속 곡은 (.+)', ln)
            if m and cur:
                s = m.group(1)
                t = re.search(r'곡\s+([A-Z][A-Za-z\' ]+?)\s*\(\d', s) or re.search(r'의\s+([A-Z][A-Za-z\' ]+?)(예요|이에요)', s)
                if t:
                    pyeon = cur_pyeon
                    pm = re.search(r'(\S+)\(.\)\s*본편', s)
                    if pm and pm.group(1) == '금': pyeon = '금1'
                    out[cur] = {'편': pyeon, '곡': t.group(1).strip(), '근거': f'{os.path.relpath(txt, ROOT)}:{i}'}
    json.dump(out, open(MAP, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    known = sum(1 for v in out.values() if v['곡'])
    print(f'곡대응표: {len(out)}개 쇼츠, 곡 확인 {known}개 → {os.path.relpath(MAP, ROOT)}')


def catalog():
    p = os.path.join(ROOT, 'catalog', 'goyo_tracks.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}


def check_titles(where, text, allowed, cat, errs):
    for t, pyeon in TITLE.findall(text):
        if (t, pyeon) in allowed:
            continue
        in_cat = pyeon in cat and any(x[1] == t for x in cat[pyeon])
        if allowed is not None and allowed and where.startswith('화면'):
            errs.append(f'[곡오류] {where}: 『{t}』({pyeon} 편)이 이 영상에 깔린 음원에 없어요. 깔린 곡: '
                        + ', '.join(f'{a}({b} 편)' for a, b in sorted(allowed)))
        elif not in_cat and (t, pyeon) not in allowed:
            errs.append(f'[곡오류] {where}: 『{t}』({pyeon} 편)의 근거가 없어요(음원·전곡목록 어디에도 없음)')


def check_config(cfg_path, errs, mp, cat):
    cfg = json.load(open(cfg_path, encoding='utf-8'))
    parts = cfg.get('audio_parts') or ([{'file': cfg['audio']}] if cfg.get('audio') else [])
    allowed = set()
    for p in parts:
        m = mp.get(p['file'])
        if m is None:
            errs.append(f'[곡오류] 음원 {p["file"]} 이 곡대응표에 없어요'); continue
        if m['곡']:
            allowed.add((m['곡'], m['편']))
    for i, sc in enumerate(cfg.get('scenes', []), 1):
        text = ' '.join([sc.get('small') or ''] + sc.get('big', []) + sc.get('after', []) + [sc.get('en') or ''])
        if TITLE.search(text):
            # 장면에 이름을 적었다면, 그 장면에 깔린 음원의 곡이어야 한다
            check_titles(f'화면 {i}번 장면', text, allowed, cat, errs)
            names = re.findall(r'『([^』]+)』', text)
            unknown = [p for p in parts if mp.get(p['file'], {}).get('곡') is None]
            if unknown and any(n not in {a for a, _ in allowed} for n in names):
                errs.append(f'[곡오류] 화면 {i}번 장면: 곡 이름을 모르는 음원({", ".join(p["file"] for p in unknown)})이 섞여 있어요')
        elif re.search(r'『', text):
            errs.append(f'[곡오류] 화면 {i}번 장면: 곡 이름은 『곡』(○○ 편) 형식으로 적어야 해요')
    # 장면 시간과 음원 구간이 맞물리는지: 이름을 적은 장면의 시작 시각이 해당 곡 구간 안인지
    if cfg.get('audio_parts'):
        t = 0; bounds = []
        for p in parts:
            m = mp.get(p['file'], {}); bounds.append((t, t + p['dur'], (m.get('곡'), m.get('편')))); t += p['dur']
        s0 = 0
        for i, sc in enumerate(cfg['scenes'], 1):
            mid = s0 + sc.get('sec', 0) / 2; s0 += sc.get('sec', 0)
            text = ' '.join([sc.get('small') or ''] + sc.get('big', []) + sc.get('after', []))
            for title, pyeon in TITLE.findall(text):
                playing = [b[2] for b in bounds if b[0] <= mid < b[1]]
                if playing and playing[0] != (title, pyeon):
                    errs.append(f'[곡오류] 화면 {i}번 장면: 『{title}』({pyeon} 편)이라고 적었지만 그때 흐르는 곡은 '
                                f'{playing[0][0] or "이름 미상"}({playing[0][1]} 편)이에요')
    return allowed


def main():
    if '--build' in sys.argv:
        build(); return
    mp = json.load(open(MAP, encoding='utf-8')) if os.path.exists(MAP) else {}
    cat = catalog(); errs = []
    for path in sys.argv[1:]:
        d = json.load(open(path, encoding='utf-8'))
        if 'scenes' in d:
            check_config(path, errs, mp, cat)
        elif d.get('type') == 'reel':
            vid = d.get('video_file', '')
            cfg = os.path.join(ROOT, os.path.splitext(vid)[0] + '.json')
            allowed = set()
            if os.path.exists(cfg):
                allowed = check_config(cfg, errs, mp, cat)
            elif vid in mp and mp[vid]['곡']:
                allowed = {(mp[vid]['곡'], mp[vid]['편'])}
            check_titles('캡션', d.get('caption', ''), allowed, cat, errs)
    for e in errs:
        print(e)
    sys.exit(1 if errs else 0)


if __name__ == '__main__':
    main()
