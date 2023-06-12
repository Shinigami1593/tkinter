from tkinter import *
window = Tk()
window.geometry('300x300')
def myClick():
    mylabel = Label(window,text='Look! I clicked the button',fg='red',bg='#000099',font = 50)
    mylabel.pack()
mybutton = Button(window,text="Click Me!",padx=10,pady=10,command=myClick,fg='red',bg='blue')
mybutton.pack()
mybutton = Button(window,text='Button',padx=20,pady=20,command=myClick,fg='red',bg='blue', state=DISABLED)
mybutton.pack()
window.mainloop()