# from pywinauto.application import Application, AppNotConnected, ProcessNotFoundError
import pywinauto 

# app = Application().Connect(process=11432)
# dlgs = app.windows()
# # print(dlgs)

# for dlg in dlgs:
#     if dlg.is_in_taskbar():
#         print(dlg)
#         print("YEEEEEEEESSSSSSS")

hndls = pywinauto.findwindows.find_windows(enabled_only =True)

for hndl in hndls:
    # if pywinauto.handleprops.text(hndl) == "":
    #     print("//boş//")
    # else:
    #     print(pywinauto.handleprops.text(hndl))
    # print(pywinauto.handleprops.exstyle(hndl))
    if (pywinauto.handleprops.exstyle(hndl) == 256 or 
        pywinauto.handleprops.exstyle(hndl) == 786688 or 
        pywinauto.handleprops.exstyle(hndl) == 0):
        print(pywinauto.handleprops.text(hndl) + " -- " + str(hndl))
        print("AND THESE ARE HER CHILDREN:")
        print("-"*10)
        print(pywinauto.handleprops.children(hndl))
        print("-"*10)
    # if pywinauto.handleprops.iswindow(hndl):
    #     print("--WINDOW--")
    # if pywinauto.handleprops.isvisible(hndl):
    #     print("--VISIBLE--")
    # if pywinauto.handleprops.isenabled(hndl):
    #     print("--ENABLED--")
    # if pywinauto.handleprops.is_toplevel_window(hndl):
    #     print("--TOPLEVEL--")
    # print(pywinauto.handleprops.classname(hndl))
    # print(pywinauto.handleprops.exstyle(hndl))
    # print(pywinauto.handleprops.style(hndl))
    # print(pywinauto.handleprops.userdata(hndl))