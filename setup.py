from cx_Freeze import setup, Executable
import sys, os

# base = None
# if sys.platform == 'win32':
#     base = 'Win32GUI'

# os.environ['TCL_LIBRARY'] = r'C:\Users\TCSARIBALI\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
# os.environ['TK_LIBRARY'] = r'C:\Users\TCSARIBALI\AppData\Local\Programs\Python\Python36\tcl\tk8.6'
# distutils_path = r'C:\Users\TCSARIBALI\AppData\Local\Programs\Python\Python36\Lib\distutils'

MY_TARGET_EXE = [Executable(
    # what to build
    script = "LastSecondSaver.py",
    icon = "lastsecondsaver_icon.ico"
    # , base = base
    )]

options = {
    'build_exe': {
        'packages' : ['os', 'WindowSaver','sys', 'inspect', 'pyHook', 'ctypes', 
            'win32api', 'win32con', 'win32gui_struct', 'win32gui',
            'itertools', 'glob', 'multiprocessing', 'datetime',
            'PIL', 'pywinauto', 'desktopmagic'],
        'excludes': ['tkinter', 'distutils'],
        "include_files": ["lastsecondsaver_icon.ico"]
    }
}




setup(name='LastSecondSaver',
      version='1.0',
      description='Last Second Screenshot Taker',
      options = options,
      executables=MY_TARGET_EXE
      )
