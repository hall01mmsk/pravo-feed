import sys,os
from playwright.sync_api import sync_playwright
html=sys.argv[1]; ts=[float(x) for x in sys.argv[2].split(',')]
from PIL import Image
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+os.path.abspath(html)); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(800)
    ims=[]
    for i,t in enumerate(ts):
        pg.evaluate(f'render({t})'); pg.screenshot(path=f'/tmp/s{i}.png'); ims.append(Image.open(f'/tmp/s{i}.png').resize((360,640)))
    b.close()
g=Image.new('RGB',(370*len(ims),640),'#444')
for i,im in enumerate(ims): g.paste(im,(i*370,0))
g.save(sys.argv[3])
