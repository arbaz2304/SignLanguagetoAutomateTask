from tkinter import *
from tkinter.tix import *
from functools import partial
import tkinter.messagebox as tmsg
from unicodedata import name
from PIL import ImageTk
from click import command
import os
import mouse_controll as mc
import hand_gesture_detection as hgd
import drawing_control as dc
import volume_controll as vc
from tkhtmlview import HTMLLabel
import webbrowser

def helper(win,fun):
    win.destroy()
    fun()
    begin()

def begin():
    window = Tk()
    window.geometry('500x500+270+100')
    window.state('zoomed')
    window.configure(bg = "white")
    canvas = Canvas(
        window,
        bg = "cyan",
        height = 400,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "flat")
    canvas.place(x = 250, y = 150)
    
            
    canvas.create_line(10,250,0+200,250,fil='black')
    canvas.create_line(30,150,30,250+50,fil='black')

    canvas.create_rectangle(
        400, 34, 400+356, 34+336,
        fill = "cyan",
        outline = "")


    imgx = PhotoImage(file = f"cap1.png")

    bx = Button(
        image = imgx,
        borderwidth = 0,
        highlightthickness = 0,
        command=window.destroy,
        relief = "flat")

    bx.place(
        x = 690, y = 475,
        width = 272,
        height = 54)


    img0 = PhotoImage(file = f"cap2.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command=partial(helper,window,vc.cntrl_vol),
        relief = "flat")

    b0.place(
        x = 690, y = 400,
        width = 272,
        height = 54)

    img1 = PhotoImage(file = f"cap5.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command=partial(helper,window,dc.draw),
        relief = "flat")

    b1.place(
        x = 690, y = 327,
        width = 272,
        height = 54)

    img2 = PhotoImage(file = f"cap3.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command= partial(helper,window,mc.mouse_control),
        relief = "flat")

    b2.place(
        x = 690, y = 250,
        width = 272,
        height = 54)

    img3 = PhotoImage(file = f"cap4.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command=partial(helper,window,hgd.gesture_Recognition),
        relief = "flat")

    b3.place(
        x = 690, y = 175,
        width = 272,
        height = 54)

    canvas.create_text(
        200.5, 200.0,
        text = "HAND GESTURE \nRECOGNIZER",
        fill = "black",
        font = ("PurplePurse-Regular", int(30.0)))
        

    def callback(url):
        webbrowser.open_new_tab(url)

    #Create a Label to display the link
    link = Label(window, text="MANUAL",font=('Helveticabold', 15), fg="blue", cursor="hand2")
    link.place(x = 690, y = 475,
        width = 272,
        height = 54)
    link.bind("<Button-1>", lambda e:
    callback("readme.html"))

    window.mainloop()

    window.resizable(False, False)
    window.mainloop()

begin()
