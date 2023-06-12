from tkinter import *
window = Tk()
def add():
    print(var.get())
    a = var.get()
    l.config(text= a)
var = IntVar()
c1 = Checkbutton( window,text='Music',variable=var,onvalue=1,offvalue=0,height=5, width=20)
c1.pack()
btn = Button(window,text='Click',command=add)
btn.pack()
l = Label(window,text='')
l.pack()
window.mainloop()