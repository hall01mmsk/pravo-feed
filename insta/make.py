import sys, json
from playwright.sync_api import sync_playwright
slides = json.load(open(sys.argv[1])); out = sys.argv[2]
CSS = """
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#050505;font-family:'Montserrat','DejaVu Sans',sans-serif;color:#f4ece4;overflow:hidden;position:relative}
.bg{position:absolute;inset:0;background:radial-gradient(900px 700px at 85% 0%,rgba(140,10,40,.55),transparent 60%),radial-gradient(700px 600px at 0% 100%,rgba(110,0,30,.45),transparent 60%),#050505}
.glass{position:absolute;left:70px;right:70px;top:170px;bottom:170px;border-radius:56px;background:linear-gradient(160deg,rgba(150,20,50,.55),rgba(60,0,15,.35));border:2px solid rgba(255,190,200,.25);box-shadow:inset 0 2px 0 rgba(255,255,255,.25),0 40px 120px rgba(120,0,30,.5);padding:90px 80px;display:flex;flex-direction:column;justify-content:center}
.glass:before{content:'';position:absolute;left:30px;right:30px;top:14px;height:120px;border-radius:40px;background:linear-gradient(180deg,rgba(255,255,255,.18),transparent)}
.num{font-size:150px;font-weight:800;color:#d4af6a;line-height:1;margin-bottom:30px}
h1{font-size:84px;line-height:1.08;font-weight:800;margin-bottom:40px}
h2{font-size:66px;line-height:1.1;font-weight:800;margin-bottom:40px}
p{font-size:44px;line-height:1.35;color:#eadbd2}
.gold{color:#d4af6a}
.top{position:absolute;top:70px;left:80px;font-size:32px;letter-spacing:4px;color:#d4af6a;font-weight:700}
.bot{position:absolute;bottom:70px;right:80px;font-size:34px;color:#d4af6a;font-weight:700}
.pg{position:absolute;bottom:70px;left:80px;font-size:32px;color:#9b8a85}
"""
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1080,'height':1350})
    n=len(slides)
    for i,s in enumerate(slides,1):
        html=f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=bg></div><div class=top>@MICKEY_WOUSE · АВИТОЛОГ</div><div class=glass>{s}</div><div class=pg>{i}/{n}</div><div class=bot>{'листай →' if i<n else ''}</div></body></html>"
        pg.set_content(html); pg.wait_for_timeout(200)
        pg.screenshot(path=f"{out}_{i:02d}.jpg", type='jpeg', quality=92)
    b.close()
