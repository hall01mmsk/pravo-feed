import os
from playwright.sync_api import sync_playwright
S=[('hook',"ты работаешь<br><em>в</em> бизнесе,<br>а не <em>на</em> бизнес","5 признаков. Посчитай, сколько совпало →"),
('01',"без тебя<br>всё встаёт","уехала на 3 дня — и работа стоит. Это не бизнес, это <b>место работы</b>, которое ты себе купила."),
('02',"весь день —<br>срочное","ни одного часа на <b>важное</b>: цены, продукт, стратегию. Тушишь пожары вместо того, чтобы строить."),
('03',"нет цифр —<br>только ощущения","не знаешь, что приносит <b>больше всего денег</b>, а что только забирает время."),
('04',"цены стоят<br>на месте","расходы растут, опыт растёт, а прайс&nbsp;— <b>как год назад</b>. Пересматривай хотя бы раз в квартал."),
('05',"отдых —<br>с чувством вины","если выходной ощущается как потеря денег — у тебя <b>нет системы</b>, которая работает без тебя."),
('end',"начни<br>с <em>одного</em>","выбери признак, который болит сильнее всего, и начни с него на этой неделе.<br><br>Сколько совпало? Напиши цифру. Сохрани и подпишись — <b>@halima.blaze</b>"),]
css=open('common.css').read()
base=lambda inner:f"""<!doctype html><html><head><meta charset=utf-8><style>{css}
html,body{{width:1080px;height:1350px;background:#efe7dc;color:#16110f}}
#grain{{opacity:.07}}
.n{{position:absolute;left:96px;top:100px;font-family:'JetBrains Mono';font-weight:700;font-size:32px;letter-spacing:.18em;color:#e2475d}}
.p{{position:absolute;right:96px;top:100px;font-family:'JetBrains Mono';font-weight:700;font-size:32px;letter-spacing:.08em;color:#9b8f86}}
.big{{position:absolute;right:60px;top:120px;font-family:'Unbounded';font-weight:800;font-size:360px;line-height:1;letter-spacing:-.06em;color:rgba(226,71,93,.13)}}
h1{{position:absolute;left:96px;right:96px;top:330px;font-family:'Onest';font-weight:800;font-size:116px;line-height:1.02;letter-spacing:-.045em}}
h1.hk{{font-size:120px;top:270px}}
h1 em{{font-family:'Cormorant Garamond';font-style:italic;font-weight:600;color:#e2475d;letter-spacing:-.01em;font-size:1.08em}}
.t{{position:absolute;left:96px;right:110px;bottom:150px;font-family:'Manrope';font-weight:500;font-size:46px;line-height:1.32;color:#5d534d}}
.t b{{color:#16110f;font-weight:800}}
.ln{{position:absolute;left:96px;width:140px;height:8px;background:#e2475d;bottom:500px}}
.hl{{position:absolute;left:96px;bottom:150px;font-family:'Unbounded';font-weight:800;font-size:44px;color:#e2475d}}
</style></head><body>{inner}<div id=grain></div></body></html>"""
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,(k,h,t) in enumerate(S):
        pn=f"0{i+1}/0{N}"
        if k=='hook': inner=f"<div class=n>БИЗНЕС-ЧЕК</div><div class=p>{pn}</div><h1 class=hk>{h}</h1><div class=t>{t}</div>"
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
