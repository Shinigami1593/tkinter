from tkinter import *
window = Tk()

e = Entry(window,width=50,bg='blue',fg='white',borderwidth=5,font=20)
e.pack()

def click():
    a = e.get()
    
    l.config(text='hello ' + a)

    
btn = Button(window,text='Click Me',padx=10,pady=10,command=click)
btn.pack()
l = Label(window,text='hello ' + e.get())
l.pack()   

window.mainloop()