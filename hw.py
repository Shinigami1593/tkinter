from tkinter import *
root = Tk()
root.title('Login'.center(80))
root.geometry('400x400')
root.resizable(0,1)
root.iconbitmap('D:\\tkinter\\c.ico')

def pri():
    a = e1.get()
    b = e2.get()
    print(a)
    print(b)
    empty["text"]=a + ' ' + b

login = Label(root,text="FACEBOOK",font='Arial',fg='#0034B6')
login.pack(side=TOP)
name = Label(root,text='Username')
name.place(x=30,y=50)
e1 = Entry(root)
e1.place(x=90,y=50)
Password = Label(root,text="Password")
Password.place(x=30,y=90)
e2 = Entry(root,show='*')
e2.place(x=90,y=90)
empty = Label(root,text="output will be here")
empty.place(x=125,y=180)
submit = Button(root,text='Login',command=pri )
submit.place(x=135 ,y=125)

root.mainloop()