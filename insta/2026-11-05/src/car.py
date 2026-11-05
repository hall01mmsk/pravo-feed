import os
from playwright.sync_api import sync_playwright
S=[('hook',"купила —<br>и <em>пожалела?</em>","правило, которое отделяет желание от покупки. Листай →"),
('01',"правило<br>24 часов","захотела что-то не из плана — <b>не покупай сразу.</b> Подожди сутки."),
('02',"почему<br>это работает","импульс быстро гаснет. Через сутки решаешь <b>ты</b>, а не эмоция."),
('03',"запиши<br>в список","всё, что хочется купить, — <b>в заметку с датой.</b> Через день перечитай."),
('04',"крупное —<br>30 дней","для дорогих покупок пауза длиннее: <b>месяц.</b> Нужное останется нужным."),
('05',"посчитай<br>в часах","цена ÷ стоимость твоего часа = <b>сколько часов жизни</b> это стоит."),
('end',"начни с <em>одной</em><br>паузы сегодня","сохрани, чтобы вспомнить перед следующей покупкой.<br><br>@halima.blaze — деньги, мышление, система"),]
css=open('common.css').read()
base=lambda inner:f"""<!doctype html><html><head><meta charset=utf-8><style>{css}
html,body{{width:1080px;height:1350px}}
#bg{{position:absolute;inset:0;background:radial-gradient(ellipse at 80% 10%,#2a1216 0%,#110b0b 55%,#090707 100%)}}
#beam{{position:absolute;width:1300px;height:420px;left:-150px;top:520px;background:linear-gradient(90deg,transparent,rgba(226,71,93,.22),transparent);filter:blur(70px);transform:rotate(-18deg)}}
.n{{position:absolute;left:96px;top:110px;font-family:'Inter Tight';font-weight:600;font-size:34px;letter-spacing:.24em;color:#e2475d}}
.p{{position:absolute;right:96px;top:110px;font-family:'Inter Tight';font-weight:600;font-size:34px;letter-spacing:.1em;color:#6f6762}}
.big{{position:absolute;right:70px;top:150px;font-family:'Unbounded';font-weight:800;font-size:330px;line-height:1;letter-spacing:-.06em;color:rgba(226,71,93,.16)}}
h1{{position:absolute;left:96px;right:96px;top:330px;font-family:'Onest';font-weight:800;font-size:110px;line-height:1.04;letter-spacing:-.035em}}
h1.hk{{font-size:104px;top:300px}}
h1 em{{font-family:'Playfair Display';font-style:italic;font-weight:700;color:#e2475d;letter-spacing:-.01em}}
.x{{display:block;font-family:'Inter Tight';font-weight:600;font-size:30px;letter-spacing:.2em;color:#6f6762;margin-bottom:30px;text-transform:uppercase}}
.t{{position:absolute;left:96px;right:120px;bottom:160px;font-family:'Manrope';font-weight:500;font-size:46px;line-height:1.32;color:#b9aea4}}
.t b{{color:#f3ede4;font-weight:800}}
.ln{{position:absolute;left:96px;width:120px;height:5px;background:#e2475d;bottom:470px}}
</style></head><body><div id=bg></div><div id=beam></div>{inner}<div id=vig></div><div id=grain></div></body></html>"""
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,(k,h,t) in enumerate(S):
        pn=f"0{i+1}/0{N}"
        if k=='hook': inner=f"<div class=n>ПСИХОЛОГИЯ ДЕНЕГ</div><div class=p>{pn}</div><h1 class=hk>{h}</h1><div class=t>{t}</div>"
        elif k=='end': inner=f"<div class=p>{pn}</div><h1>{h}</h1><div class=t>{t}</div>"
        else: inner=f"<div class=n>ШАГ {k}</div><div class=p>{pn}</div><div class=big>{k}</div><h1><span class=x>правило паузы</span>{h}</h1><div class=ln></div><div class=t>{t}</div>"
        open('c.html','w').write(base(inner)); pg.goto('file://'+os.path.abspath('c.html')); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        pg.screenshot(path=f'carousel_{i+1:02d}.jpg',type='jpeg',quality=93)
    b.close()
from PIL import Image
ims=[Image.open(f'carousel_{i:02d}.jpg').resize((270,338)) for i in range(1,N+1)]
g=Image.new('RGB',(280*4,348*2),'#444')
for i,im in enumerate(ims): g.paste(im,((i%4)*280,(i//4)*348))
g.save('still_car.jpg')
