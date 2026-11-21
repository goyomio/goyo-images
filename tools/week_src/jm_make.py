"""정미년 시리즈 릴스/쇼츠 한 편 만들기 (유튜브 2027-01 창, 11/22).
python3 tools/week_src/jm_make.py spec.json
spec: {key:"0110-2100", date:"2027-01-10", slot:"2100"|"1800"|"1300", name:"숭례문",
       audio:{pyeon:"화1", title:"Warm Room", file:"/path/to/60s.m4a", start_hms:"..."},
       music_ko:"화(火)", music_en:"Fire", end_tag:"오늘 밤의 소리",
       scenes:[...example_reel scene...], caption:"...", note:"..."}
끝 장면은 자동(인스타: 프로필 링크 / 유튜브: 채널 상단 링크·아래 관련 영상)."""
import json, os, shutil, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FG = [236, 233, 226]; EN = [214, 210, 202]; GD = [200, 180, 140]


def end_items(sp, yt):
    a = sp['audio']; mk, me = sp['music_ko'], sp['music_en']
    links = ("내 일간은 채널 상단 링크의 무료 앱에서\n음악은 아래 관련 영상" if yt else "내 일간 찾기와 음악은\n프로필 링크에서")
    en = (f"Five Kinds of Quiet · {me}\n“{a['title']}”\nFind your Day Master: free app,\nlink at the top of our channel\nMusic: related video below" if yt
          else f"Five Kinds of Quiet · {me}\n“{a['title']}”\nFind your Day Master:\nfree app & music, link in bio")
    t = a['title']; tk = "『" + (t if len(t) <= 16 else t.replace(' ', '\n', 1)) + "』"
    return [["다섯 가지 고요 · " + mk, 54, FG, True, 10], [tk, 74, FG, True, 34], [links, 42, GD, False, 26], [en, 30, EN, False, 0]]


def main(path):
    sp = json.load(open(path, encoding='utf-8'))
    os.chdir(ROOT)
    a = sp['audio']; safe = a['title'].replace(' ', '')
    rel_audio = f"shorts/정미년/audio/{a['pyeon']}_{safe}_60s.m4a"
    if not os.path.exists(rel_audio): shutil.copy(a['file'], rel_audio)
    mp = json.load(open('shorts/곡대응표.json', encoding='utf-8'))
    mp[rel_audio] = {"편": a['pyeon'], "곡": a['title'], "근거": a.get('근거', f"원곡: {a['pyeon']} {a.get('start_hms','')} {a['title']} (곡 시작부터 60초)")}
    json.dump(mp, open('shorts/곡대응표.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    name = f"{sp['key'][:4]} {sp['name']}"
    for which, d in (('ig', '인스타'), ('yt', '유튜브')):
        scenes = [dict(s) for s in sp['scenes']]
        endsc = {'sec': sp.get('end_sec', 5.5), 'tag': sp.get('end_tag', '이 영상의 소리'), 'step': 0.6, 'items': end_items(sp, which == 'yt')}
        if sp.get('end_art'): endsc['art'] = sp['end_art']
        scenes.append(endsc)
        cfg = {'audio': rel_audio, 'fx': sp.get('fx', {'stars': 60, 'wipe': True, 'rise': True}), 'scenes': scenes}
        cp = f"shorts/정미년/{d}/{name}.json"; json.dump(cfg, open(cp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        subprocess.run([sys.executable, 'tools/week_src/example_reel.py', cp, which, f"shorts/정미년/{d}/{name}.mp4"], check=True)
    pdir = f"posts/{sp['date']}" + ('' if sp['slot'] == '1800' else '-' + sp['slot'])
    os.makedirs(pdir, exist_ok=True)
    json.dump({"type": "reel", "via": "api", "approved": False, "video_file": f"shorts/정미년/인스타/{name}.mp4",
               "caption": sp['caption'], "thumb_offset": 1000, "note": sp.get('note', '') + ' · 유튜브 2027-01 창 자동 제작(미오 님 수면 중 11/22) · 미오 님 「승인」 뒤 true'},
              open(f"{pdir}/post.json", 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for chk in (['tools/ko_check.py', f'{pdir}/post.json'], ['tools/reel_check.py', f'{pdir}/post.json']):
        r = subprocess.run([sys.executable] + chk, capture_output=True, text=True)
        print('점검', chk[0], r.returncode, r.stdout.strip()[:400])
    # 유튜브 폴더용
    out = f"/mnt/user-data/outputs/jm/{sp['key']}"; os.makedirs(out, exist_ok=True)
    shutil.copy(f"shorts/정미년/유튜브/{name}.mp4", f"{out}/쇼츠_{sp['name']}.mp4")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '1', '-i', f"{out}/쇼츠_{sp['name']}.mp4", '-frames:v', '1', '-q:v', '2', f"{out}/쇼츠_썸네일.jpg"], check=True)
    # 장면 사진
    from PIL import Image
    tot = 0; mids = []
    for s in cfg['scenes']: mids.append(tot + s['sec'] * 0.8); tot += s['sec']
    ims = []
    for i, t in enumerate(mids):
        f = f"/tmp/jm_{sp['key']}_{i}.png"
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', f"shorts/정미년/유튜브/{name}.mp4", '-frames:v', '1', '-vf', 'scale=240:-1', f], check=True)
        ims.append(Image.open(f))
    m = Image.new('RGB', (240 * len(ims), ims[0].height)); [m.paste(x, (i * 240, 0)) for i, x in enumerate(ims)]
    m.save(f"/tmp/장면_{sp['key']}.png"); print('ok', name, tot)


if __name__ == '__main__':
    main(sys.argv[1])
