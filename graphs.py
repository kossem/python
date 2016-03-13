from tkinter import * 
from tkinter import messagebox
from math import *

windowH = Tk()
windowH.title("Graph")
c = Canvas(windowH, borderwidth=1, width=400, height=400, bg="white")
def resize(event):
    c.scale("all")
def key(event):
    if(event.char and ord(event.char) == 13):
        plotcmd(0)
windowH.bind('<Key>', key)
tb = Frame(windowH, height=25)
Label(tb, text="f(x)=").pack(side=LEFT)
func = StringVar()
func.set("x")
Entry(tb, textvariable=func).pack(side=LEFT)
Label(tb, text="xmin=").pack(side=LEFT)
xmin = DoubleVar()
xmin.set(-1)
Entry(tb, textvariable=xmin, width=5).pack(side=LEFT)
Label(tb, text="xmax=").pack(side=LEFT)
xmax = DoubleVar()
xmax.set(1)
Entry(tb, textvariable=xmax, width=5).pack(side=LEFT)
def plotcmd2(event):
    plotcmd()
def plotcmd(arg=1):
    try:
        g = eval('lambda x: ' + func.get())
        g(xmin.get())
    except:
        messagebox.showerror("Error", "Error in function")
        return
    ymax = -10 ** 6
    ymin = 10 ** 6
    w = c.winfo_width() - 22
    h = c.winfo_height() - 22
    ywmax = h
    ywmin = 11
    c.delete("all")
    dx = (xmax.get() - xmin.get()) / w
    for i in range(0, w):
        if ymax <= g(xmin.get() + dx * i):
            ymax = g(xmin.get() + dx * i)
        if ymin >= g(xmin.get() + dx * i):
            ymin = g(xmin.get() + dx * i)
    points = []
    cY = lambda y: round(ywmax - (ywmax - ywmin) * ((y - ymin) / (ymax - ymin)))
    for i in range(0, w):
        arg1 = xmin.get() + dx * i
        points.append(11 + i)
        points.append(cY(g(arg1)))
    c.create_line(points, width=2.0)
    c.create_line(0, cY(0), w + 11, cY(0), arrow=LAST)
    c.create_line(11 - xmin.get() / dx, h + 11, 11 - xmin.get() / dx, 11, arrow=LAST)
    c.create_text(w, cY(0) - 10, text="x")
    c.create_text(-xmin.get() / dx, 20, text="y")
    c.create_text(-xmin.get() / dx + 20, cY(0) - 10, text="O")
    c.update()
Button(tb, text="Plot!", command=plotcmd).pack(side=LEFT)
c.pack(side=TOP, fill=BOTH, expand=1)
tb.pack()
windowH.bind('<Configure>', plotcmd2)
windowH.mainloop()
