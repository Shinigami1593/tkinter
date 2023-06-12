from tkinter import *
root = Tk()
root.title('Login'.center(80))
root.geometry('400x400')
root.resizable(0,1)
root.iconbitmap('D:\\tkinter\\c.ico')

def pri():
    username = 'ram'
    password = '123'
    if e1.get() == username and e2.get() == password:
        print("Login succesfully")
        root.destroy()
    else:
        print("Try Again")

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
submit = Button(root,text='Login',command=pri )
submit.place(x=135 ,y=125)
root.mainloop()