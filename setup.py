from cx_Freeze import setup, Executable
import os
os.environ['TCL_LIBRARY'] = r'C:\Users\DY\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\DY\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

setup(  name = "D:\Programmes\space_invaders",
        version = "0.1",
        description = "Space Invaders",
        executables = [Executable("space_invaders.py",base="Win32Gui")]
)
