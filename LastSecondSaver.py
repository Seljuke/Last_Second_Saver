from pywinauto import handleprops, findwindows, win32functions
from pywinauto.controls import hwndwrapper
from desktopmagic.screengrab_win32 import getRectAsImage
from PIL import Image
import os
from ctypes import wintypes
from datetime import datetime
# import time, sys

def Last_Second_Save():
    # start = time.time()
    hndls = findwindows.find_windows()
    imgs = []
    for hndl in hndls:
        if (handleprops.exstyle(hndl) == 256 or 
            handleprops.exstyle(hndl) == 786688 or
            handleprops.exstyle(hndl) == 262400 or
            handleprops.exstyle(hndl) == 65792 or
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
                    # app.set_focus()
                    app.maximize()
                    win32functions.WaitGuiThreadIdle(hndl)
                    app.set_focus()
                    img = None
                    img = getRectAsImage(box)
                    imgs.append(img)
                except:
                    # print("ERROR --- "+(str(handleprops.text(hndl)) + " - " + str(handleprops.processid(hndl))))
                    # print("Unexpected error:", sys.exc_info()[0])
                    continue
    #START IF#
    if len(imgs) > 0:
        if bool(len(imgs) % 2):
            if len(imgs) == 1:
                matrix_col, matrix_row = (1, 1)
            else:
                matrix_col, matrix_row = (int(len(imgs) // 2), int(len(imgs) // 2) + 1)
        else:
            matrix_col, matrix_row = (int(len(imgs) // 2), int(len(imgs) // 2))

        # print("MATRIX: " + str(matrix_row) + "x" + str(matrix_col))
        finalRes_width = 960 * matrix_col
        finalRes_height = 540 * matrix_row
        result = Image.new("RGB", (finalRes_width, finalRes_height))
        # print("RESULT IMAGE SIZE: " + str(result.size))
        perImg_width = 960
        perImg_height = 540
        lst_counter = 0
        # print("NUMBER OF IMGS: " + str(len(imgs)))
        for col in range(matrix_col):
            for row in range(matrix_row):
                if len(imgs) > lst_counter:
                    imgs[lst_counter].thumbnail((perImg_width, perImg_height), Image.LANCZOS)
                    x = col * perImg_width
                    y = row * perImg_height
                    w, h = imgs[lst_counter].size
                    result.paste(imgs[lst_counter], (x, y, x + w, y + h))
                    lst_counter +=1

        now = datetime.now()
        name = ("LastSecondSave-" + str(now.year) + "-" + str(now.month) + "-" + str(now.day)
            + "-" + str(now.hour) + "-" + str(now.minute) )
        homeDir = os.path.expanduser("~")
        if os.path.isdir(homeDir+"\\LastSeconSave"):
            result.save(homeDir+"\\LastSeconSave\\"+name+".jpg")
        else:
            os.mkdir(homeDir+"\\LastSeconSave")
            result.save(homeDir+"\\LastSeconSave\\"+name+".jpg")
    #END IF#
    # stop = time.time()
    # print("TIME: " + str(stop-start))
        
# Last_Second_Save()
