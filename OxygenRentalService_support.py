#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Nov 25, 2021 09:07:02 AM IST  platform: Windows NT
#    Dec 01, 2021 10:57:30 AM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global login_method
    login_method = tk.IntVar()
    global selectedBasis
    selectedBasis = tk.IntVar()
    global spinbox
    spinbox = tk.StringVar()
    global spinbox2
    spinbox2 = tk.StringVar()
    global spinbox3
    spinbox3 = tk.StringVar()
    global selectedShop
    selectedShop = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import OxygenRentalService
    OxygenRentalService.vp_start_gui()





