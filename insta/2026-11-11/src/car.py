import os
from playwright.sync_api import sync_playwright
S=[('hook',"ты растёшь,<br>даже если<br><em>пока не видно</em>","6 признаков. Посчитай, сколько про тебя →"),
('01',"в старом<br>стало тесно","то, что раньше устраивало, больше не радует. Это не кризис — ты <b>выросла из потолка</b>."),
('02',"ты считаешь,<br>а не надеешься","знаешь свои цифры, даже если они пока небольшие. <b>Учёт — первый шаг к росту.</b>"),
('03',"ты говоришь<br>«нет»","отказываешься от того, что не ведёт к цели, — <b>без долгих оправданий</b>."),
('04',"ошибка —<br>это данные","не «у меня не получается», а <b>«что поменять в следующий раз»</b>."),
('05',"окружение<br>меняется","с кем-то стало не о чем говорить, с кем-то — <b>интересно и сложно</b>. Это нормально."),
('06',"делаешь<br>без настроения","мотивация ушла, а <b>привычка держит</b>. Это и есть дисциплина."),
('end',"рост сначала<br>внутри, потом —<br>в <em>цифрах</em>","Сколько признаков про тебя? Напиши цифру.<br><br>Сохрани, чтобы перечитать в трудный день, и подпишись — <b>@halima.blaze</b>"),]
css=open('common.css').read()
base=lambda inner:f"""<!doctype html><html><head><meta charset=utf-8><style>{css}
html,body{{width:1080px;height:1350px;background:radial-gradient(ellipse at 30% 20%,#221619,#0c0a0b 60%,#070606);color:#f3ede4}}
#grain{{opacity:.08}}
.n{{position:absolute;left:96px;top:100px;font-family:'JetBrains Mono';font-weight:700;font-size:32px;letter-spacing:.18em;color:#e2475d}}
.p{{position:absolute;right:96px;top:100px;font-family:'JetBrains Mono';font-weight:700;font-size:32px;letter-spacing:.08em;color:#6f6762}}
.big{{position:absolute;right:60px;top:120px;font-family:'Unbounded';font-weight:800;font-size:360px;line-height:1;letter-spacing:-.06em;color:rgba(226,71,93,.16)}}
h1{{position:absolute;left:96px;right:96px;top:330px;font-family:'Onest';font-weight:800;font-size:116px;line-height:1.02;letter-spacing:-.045em}}
h1.hk{{font-size:118px;top:260px}}
h1 em{{font-family:'Cormorant Garamond';font-style:italic;font-weight:600;color:#e2475d;letter-spacing:-.01em;font-size:1.08em}}
.t{{position:absolute;left:96px;right:110px;bottom:150px;font-family:'Manrope';font-weight:500;font-size:46px;line-height:1.32;color:#b9aea4}}
.t b{{color:#f3ede4;font-weight:800}}
.ln{{position:absolute;left:96px;width:140px;height:8px;background:#e2475d;bottom:500px}}
.hl{{position:absolute;left:96px;bottom:150px;font-family:'Unbounded';font-weight:800;font-size:44px;color:#e2475d}}
</style></head><body>{inner}<div id=grain></div></body></html>"""
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,(k,h,t) in enumerate(S):
        pn=f"0{i+1}/0{N}"
        if k=='hook': inner=f"<div class=n>ЧЕК РОСТА</div><div class=p>{pn}</div><h1 class=hk>{h}</h1><div class=t>{t}</div>"
        elif k=='end': inner=f"<div class=n>ИТОГ</div><div class=p>{pn}</div><h1>{h}</h1><div class=t>{t}</div>"
        else: inner=f"<div class=n>ПРИЗНАК {k}</div><div class=p>{pn}</div><div class=big>{k}</div><h1>{h}</h1><div class=ln></div><div class=t>{t}</div>"
        open('c.html','w').write(base(inner)); pg.goto('file://'+os.path.abspath('c.html')); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        pg.screenshot(path=f'../carousel_{i+1:02d}.jpg',type='jpeg',quality=93)
    b.close()
from PIL import Image
ims=[Image.open(f'../carousel_{i:02d}.jpg').resize((270,338)) for i in range(1,N+1)]
g=Image.new('RGB',(280*4,348*2),'#444')
for i,im in enumerate(ims): g.paste(im,((i%4)*280,(i//4)*348))
g.save('still_car.jpg')
