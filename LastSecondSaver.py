import ctypes
from pywinauto.application import Application, AppNotConnected, ProcessNotFoundError
import time
from PIL import Image
import os
 
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId
IsWindowVisible = ctypes.windll.user32.IsWindowVisible
 
titles = []
def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        proc_id = ctypes.c_int()
        GetWindowThreadProcessId(hwnd, ctypes.byref(proc_id))
        titles.append((proc_id.value, buff.value))
        length = None
        buff = None
        proc_id = None
    return True
EnumWindows(EnumWindowsProc(foreach_window), 0)
 

print(titles)
connections = []
for title in titles:
    if(title[1] != ''):
        print(title[1])
        connections.append(Application().Connect(process=title[0]))
        dlgs = connections[-1].windows()
        print(dlgs)
        

