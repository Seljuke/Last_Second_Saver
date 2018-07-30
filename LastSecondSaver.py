from pywinauto import handleprops, findwindows
from pywinauto.controls import hwndwrapper
from desktopmagic.screengrab_win32 import getRectAsImage
import time

start = time.time()
hndls = findwindows.find_windows()
for hndl in hndls:
    if (handleprops.exstyle(hndl) == 256 or 
        handleprops.exstyle(hndl) == 786688 or 
        handleprops.exstyle(hndl) == 0):
        print(str(handleprops.text(hndl)) + " - " + str(handleprops.processid(hndl)))
        rect = None
        rect = handleprops.rectangle(hndl)
        box = None
        box = (rect.left, rect.top, rect.right, rect.bottom)
        # app.maximize()
        if(str(handleprops.text(hndl)).strip()== ""):
            continue
        else:
            try:
                app = None
                app = hwndwrapper.HwndWrapper(hndl)
                app.set_focus()
                app.maximize()
                img = None
                img = getRectAsImage(box)
                name = None
                name = str(handleprops.text(hndl)).strip()
                name = name.replace("/","_")
                name = name.replace(":","-")
                name = name.replace(".","-")
                img.save("./Saves/"+name+".jpg")
                app.minimize()
            except:
                print("ERROR --- "+(str(handleprops.text(hndl)) + " - " + str(handleprops.processid(hndl))))
                continue
time.sleep(1)
stop = time.time()
print("TIME: " + str(stop-start))
        
    
