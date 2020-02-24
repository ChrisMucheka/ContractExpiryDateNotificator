import sys

from cx_Freeze import setup, Executable
import os
os.environ['TCL_LIBRARY'] = r'C:/Users/Fifofa/AppData/Local/Programs/Python/Python36-32/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = r'C:/Users/Fifofa/AppData/Local/Programs/Python/Python36-32/tcl/tk8.6'

exe = Executable(
    script=r"example.py",
    base="Win32GUI",
    )
includefiles = ["tcl86t.dll", "tk86t.dll"]
buildOptions = dict(excludes = ["tkinter"], includes =["idna.idnadata"], optimize=1)
setup(
    name="Contract End Notifier",
    description="Notify the client that their contract is ending in the coming days",
    version="1.0.1",
    executables = [exe],
    options = dict(build_exe = buildOptions)
    )
