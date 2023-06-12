from tkinter import *
import sqlite3

root = Tk()
root.geometry('400x500')
root.title('Instagram')

conn = sqlite3.connect('Instagram')
d = conn.cursor()
d.execute("""CREATE TABLE registration(
        first_name,
        last_name,
        city,
        state,
        gender
)""")
conn.commit()
conn.close()

l = Label(root,text='First Name')
l.place(x=10,y=10)

l1 = Label(root,text='Last Name')
l1.place(x=10,y=35)

l2 = Label(root,text='City')
l2.place(x=10,y=60)

l3 = Label(root,text='State')
l3.place(x=10,y=85)

l4 = Label(root,text='Gender')
l4.place(x=10,y=110)

e = Entry(root,width=30)
e.place(x=108,y=10)

e1 = Entry(root,width=30)
e1.place(x=108,y=35)

e2 = Entry(root,width=30)
e2.place(x=108,y=60)

e3 = Entry(root,width=30)
e3.place(x=108,y=85)

e4 = Entry(root,width=30)
e4.place(x=108,y=110)




root.mainloop()