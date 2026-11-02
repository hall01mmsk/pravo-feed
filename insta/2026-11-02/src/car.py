import os
from playwright.sync_api import sync_playwright
S=[('hook',"6 фраз,<br>которые держат<br>тебя <em>на одном</em><br>доходе","листай →"),
('01',"«мне это<br>не по карману»","спроси иначе: <b>как мне это себе позволить?</b> Первая фраза закрывает мозг, вторая — включает."),
('02',"«деньги<br>портят людей»","деньги <b>усиливают</b> то, что в человеке уже есть. Щедрый станет щедрее."),
('03',"«сначала накоплю,<br>потом начну»","идеального момента нет. <b>Начни с малого</b> — понимание приходит в процессе, а не до него."),
('04',"«просить больше —<br>неловко»","цена — это <b>информация</b> о ценности, а не наглость. Неловко — нормально, молчать — дорого."),
('05',"«богатым<br>просто повезло»","везение любит тех, кто <b>часто пробует</b>. Больше попыток — больше шансов."),
('06',"«я не умею<br>в деньги»","это не талант, а <b>навык</b>. Навыку учатся: учёт, план, повторение."),
('end',"поймала себя<br>на одной<br>из них? <em>сохрани</em>","и перечитай, когда фраза снова прозвучит в голове.<br><br>@halima.blaze — деньги, мышление, система"),]
css=open('common.css').read()
base=lambda inner:f"""<!doctype html><html><head><meta charset=utf-8><style>{css}
html,body{{width:1080px;height:1350px}}
#g{{position:absolute;width:1200px;height:1200px;left:-60px;top:-200px;border-radius:50%;background:radial-gradient(circle,rgba(226,71,93,.30),transparent 62%);filter:blur(40px)}}
.n{{position:absolute;left:96px;top:110px;font-family:'Inter Tight';font-weight:600;font-size:34px;letter-spacing:.24em;color:#e2475d}}
.p{{position:absolute;right:96px;top:110px;font-family:'Inter Tight';font-weight:600;font-size:34px;letter-spacing:.1em;color:#6f6762}}
h1{{position:absolute;left:96px;right:96px;top:260px;font-family:'Unbounded';font-weight:800;font-size:84px;line-height:1.08;letter-spacing:-.035em}}
h1.big{{font-size:100px;top:300px}}
h1 em{{font-family:'Cormorant Garamond';font-style:italic;font-weight:600;color:#e2475d;font-size:1.45em;letter-spacing:-.01em}}
.x{{display:block;font-family:'Inter Tight';font-weight:600;font-size:30px;letter-spacing:.2em;color:#6f6762;margin-bottom:26px;text-transform:uppercase}}
.t{{position:absolute;left:96px;right:120px;bottom:160px;font-family:'Manrope';font-weight:500;font-size:46px;line-height:1.32;color:#b9aea4}}
.t b{{color:#f3ede4;font-weight:800}}
.ln{{position:absolute;left:96px;width:120px;height:5px;background:#e2475d;bottom:500px}}
</style></head><body><div id=g></div>{inner}<div id=vig></div><div id=grain></div></body></html>"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,(k,h,t) in enumerate(S):
        if k=='hook': inner=f"<div class=n>ПСИХОЛОГИЯ ДЕНЕГ</div><div class=p>01/08</div><h1 class=big>{h}</h1><div class=t>{t}</div>"
        elif k=='end': inner=f"<div class=p>08/08</div><h1>{h}</h1><div class=t>{t}</div>"
        else: inner=f"<div class=n>ФРАЗА {k}</div><div class=p>0{i+1}/08</div><h1><span class=x>бедное мышление</span>{h}</h1><div class=ln></div><div class=t>{t}</div>"
        open('c.html','w').write(base(inner)); pg.goto('file://'+os.path.abspath('c.html')); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        pg.screenshot(path=f'car_{i+1:02d}.jpg',type='jpeg',quality=93)
    b.close()
from PIL import Image
ims=[Image.open(f'car_{i:02d}.jpg').resize((270,338)) for i in range(1,9)]
g=Image.new('RGB',(270*4+30,338*2+10),'#444')
for i,im in enumerate(ims): g.paste(im,((i%4)*280,(i//4)*348))
g.save('still_car.jpg')
