from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('300x300')
def pop():
    # messagebox.showinfo('This is my popup', 'Hello World')
    response = messagebox.askyesno('This is my popup', 'Hello World')
    Label(root,text=response).pack()
btn = Button(root,text='Popup', command=pop)
btn.pack()
root.mainloop()