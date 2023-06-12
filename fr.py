from tkinter import *
window = Tk()
def add():
    print(var.get())
    a = var.get()
    l.config(text= a)
var = StringVar()
r1 = Radiobutton(window,text='Male',variable=var,value = 'you have selected male',command=add)
r1.pack(anchor=W)
r2 = Radiobutton(window,text='Female', variable=var,value='you have selected female',command=add)
r2.pack(anchor=W)
l = Label(window,text='')
l.pack()
window.mainloop()