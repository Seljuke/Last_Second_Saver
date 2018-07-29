import pywinauto, json, PIL, ctypes
from desktopmagic.screengrab_win32 import (
	getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
	getRectAsImage, getDisplaysAsImages)

hndls = pywinauto.findwindows.find_windows()
for hndl in hndls:
    if (pywinauto.handleprops.exstyle(hndl) == 256 or 
        pywinauto.handleprops.exstyle(hndl) == 786688 or 
        pywinauto.handleprops.exstyle(hndl) == 0):
        print(str(pywinauto.handleprops.text(hndl)) + " - " + str(pywinauto.handleprops.processid(hndl)))
        rect = None
        rect = pywinauto.handleprops.rectangle(hndl)
        box = None
        box = (rect.left, rect.top, rect.right, rect.bottom)
        # app.maximize()
        if(str(pywinauto.handleprops.text(hndl)).strip()== ""):
            continue
        else:
            try:
                app = None
                app = pywinauto.controls.hwndwrapper.HwndWrapper(hndl)
                app.set_focus()
                app.maximize()
                img = None
                img = getRectAsImage(box)
                name = None
                name = str(pywinauto.handleprops.text(hndl)).strip()
                name = name.replace("/","_")
                name = name.replace(":","-")
                name = name.replace(".","-")
                img.save("./Saves/"+name+".jpg")
                app.minimize()
            except:
                print("ERROR --- "+print(str(pywinauto.handleprops.text(hndl)) + " - " + str(pywinauto.handleprops.processid(hndl))))
                continue
        
    
