# from tkinter import *
# root = Tk()
# root.title("GUI")
# root.maxsize(width=600,height=300)
# root.minsize(width=200,height=100)

# def add():
#     x = var.get()
#     print(x)
#     mylabell.config(text=x,bg='green')

# mylabel = Label(root,text='User Name', fg='red',bg='yellow')
# mylabel.place(x=10,y=10)
# mylabell = Label(root,text='Nothing',fg='red',bg='yellow')
# mylabell.place(x=40,y=120)
# var = StringVar()
# ent = Entry(root,bg='black',fg='white',textvariable=var)
# ent.place(x = 80,y=10)
# btn = Button(root,text='Submit',bg='green',fg='white',command=add)
# btn.place(x=20,y=80)
# root.mainloop()

a = 'b001'
b = [a.find('0')]
c = len(b) ^ 2
print(c)
