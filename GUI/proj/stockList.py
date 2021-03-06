#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Dec 19, 2018 09:20:53 PM PKT  platform: Windows NT

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

import stockList_support


def back():
    root.destroy()
    from p2 import vp_start_gui
    vp_start_gui()


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    stockList_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    stockList_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font10 = "-family Tahoma -size 18 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font13 = "-family {Shonar Bangla} -size 14 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font16 = "-family {Segoe UI} -size 12 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"
        font17 = "-family {Segoe UI} -size 11 -weight normal -slant " \
                 "roman -underline 1 -overstrike 0"
        font19 = "-family {Segoe UI} -size 15 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"

        top.geometry("633x469+344+129")
        top.title("Stock List")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.269, rely=0.021, height=31, width=274)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#2269c6")
        self.Label1.configure(text='''STOCKS''')
        self.Label1.configure(width=274)

        self.Button1 = tk.Button(top, command=back)
        self.Button1.place(relx=0.032, rely=0.043, height=24, width=36)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Back''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.016, rely=0.128, relheight=0.842
                , relwidth=0.972)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="1")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#d9d9d9")
        self.Frame1.configure(width=615)

        self.Canvas1 = tk.Canvas(self.Frame1)
        vbar = tk.Scrollbar(self.Frame1, orient="vertical", command=self.Canvas1.yview)
        self.Canvas1.configure(scrollregion=(0, 0, 5000, 5000))
        vbar.pack(side="right", fill="y")
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=0.995, relwidth=0.997)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief='ridge')
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=613)
        self.Canvas1.configure(yscrollcommand=vbar.set)
        self.Canvas1.pack(side="left", expand=True, fill="both")

        for num in range(4):
            b = tk.Frame(self.Canvas1)
            b.pack(fill='x', padx=7, pady=3)
            b.configure(height=45)
            b.configure(relief='groove')
            b.configure(borderwidth="1")
            b.configure(relief='groove')
            b.configure(background="#d9d9d9")
            b.configure(highlightcolor="#d9d9d9")

            l1 = tk.Label(b)
            l1.place(relx=0.071, rely=0.222, height=27, width=57)
            l1.configure(background="#d9d9d9")
            l1.configure(disabledforeground="#a3a3a3")
            l1.configure(font=font13)
            l1.configure(foreground="#000000")
            if(num==0):
                comName="GOOG"
            if (num == 1):
                comName = "FB"
            if (num == 2):
                comName = "EBAY"
            if (num == 3):
                comName = "AAPL"
            assert isinstance(comName, str)
            l1.configure(text=comName)
            l1.configure(width=57)

            l2 = tk.Label(b)
            l2.place(relx=0.496, rely=0.222, height=17, width=15)
            l2.configure(background="#d9d9d9")
            l2.configure(disabledforeground="#a3a3a3")
            l2.configure(font=font16)
            l2.configure(foreground="#000000")
            l2.configure(text='''$''')
            l2.configure(width=15)

            l3 = tk.Label(b)
            l3.place(relx=0.549, rely=0.222, height=21, width=34)
            l3.configure(background="#d9d9d9")
            l3.configure(disabledforeground="#a3a3a3")
            l3.configure(font=font17)
            l3.configure(foreground="#000000")
            if (num == 0):
                price = "1075.56"
            if (num == 1):
                price = "147.7"
            if (num == 2):
                price = "29.95"
            if (num == 3):
                price = "206.0"
            assert isinstance(price, str)
            l3.configure(text=price)
            l3.configure(width=34)

            l4 = tk.Label(b)
            l4.place(relx=0.018, rely=0.222, height=21, width=12)
            l4.configure(background="#d9d9d9")
            l4.configure(disabledforeground="#a3a3a3")
            l4.configure(font=font19)
            l4.configure(foreground="#000000")
            l4.configure(text='''-''')
            l4.configure(width=12)







