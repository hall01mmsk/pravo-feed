import sys,os,subprocess
from playwright.sync_api import sync_playwright
html,out,T=sys.argv[1],sys.argv[2],float(sys.argv[3]); fps=30
fr=out+'_fr'; os.makedirs(fr,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+os.path.abspath(html)); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(800)
    for i in range(int(fps*T)):
        pg.evaluate(f'render({i/fps})')
        pg.screenshot(path=f'{fr}/{i:04d}.jpg',type='jpeg',quality=92)
    b.close()
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',f'{fr}/%04d.jpg','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','64k','-movflags','+faststart',out],check=True)
print('ok',out)
