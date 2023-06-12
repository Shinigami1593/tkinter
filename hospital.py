from tkinter import *
import sqlite3

root = Tk()
root.title('Hospital')
root.geometry('400x500')

# d = sqlite3.connect('Hospital.sql')
# conn = d.cursor()
# conn.execute(""" CREATE TABLE Patient_registration(
#               name,
#               age,
#               wieght,
#               marital_stat,
#               guardians_name,
#               city,
#               state,
#               mobile_num
# )""")
# d.commit()
# d.close()

def insert():
    d = sqlite3.connect('Hospital.sql')
    b = d.cursor()
    b.execute("INSERT INTO Patient_registration VALUES(:name, :age, :wieght, :marital_stat, :guardians_name, :city, :state, :mobile_num)",{
        'name': e.get(),
        'age': e1.get(),
        'wieght': e2.get(),
        'marital_stat': e3.get(),
        'guardians_name': e4.get(),
        'city': e5.get(),
        'state': e6.get(),
        'mobile_num' : e7.get()
    })
    d.commit()
    d.close()
    e.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)

def query():
    conn = sqlite3.connect('Hospital.sql')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM Patient_registration")

    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += (record[0]) + ' ' + (record[1]) + ' ' + (record[2]) + ' ' + (record[4]) + ' ' + '\t' + str(record[8]) + '\n'

    query_label = Label(root,text=print_records)
    query_label.place(x=75,y=380)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('Hospital.sql')
    c = conn.cursor()
    c.execute("DELETE from Patient_registration WHERE oid = " + e8.get())
    print('Deleted Successfully')

    e8.delete(0,END)
    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect('Hospital.sql')
    c = conn.cursor()

    record_id = e8.get()

    c.execute(""" UPDATE Patient_registration SET
           name = :name,
           age = :age,
           wieght = :weight,
           marital_stat = :marriage,
           guardians_name = :g_name,
           city = :city,
           state = :state,
           mobile_num = :mobile
           WHERE oid = :oid""",
           {'name' : E0.get(),
            'age' : E1.get(),
            'weight' : E2.get(),
            'marriage' : E3.get(),
            'g_name' : E4.get(),
            'city' : E5.get(),
            'state' : E6.get(),
            'mobile' : E7.get(),
            'oid' : record_id
               
           }

        )
    conn.commit()
    conn.close()

    win.destroy()


def new():
    global win

    win = Tk()
    win.title('Update Window')
    win.geometry('400x500')

    b = sqlite3.connect('Hospital.sql')
    conn = b.cursor()
    record = e8.get()
    conn.execute(" SELECT * FROM Patient_registration WHERE oid = " + record)

    records = conn.fetchall()

    global E0
    global E1
    global E2
    global E3
    global E4
    global E5
    global E6
    global E7


    l = Label(win,text='Name')
    l.place(x=10,y=10)

    l1 = Label(win,text='Age')
    l1.place(x=10,y=35)

    l2 = Label(win,text='Weight')
    l2.place(x=10,y=60)

    l3 = Label(win,text='Marital_Status')
    l3.place(x=10,y=85)

    l4 = Label(win,text='Guardians_Name')
    l4.place(x=10,y=110)

    l5 = Label(win,text='City')
    l5.place(x=10,y=135)

    l6 = Label(win,text='State')
    l6.place(x=10,y=160)

    l7 = Label(win,text='Mobile_Number')
    l7.place(x=10,y=185)

    E0 = Entry(win,width=30)
    E0.place(x=108,y=10)

    E1 = Entry(win,width=30)
    E1.place(x=108,y=35)

    E2 = Entry(win,width=30)
    E2.place(x=108,y=60)

    E3 = Entry(win,width=30)
    E3.place(x=108,y=85)

    E4 = Entry(win,width=30)  
    E4.place(x=108,y=110)

    E5 = Entry(win,width=30)
    E5.place(x=108,y=135)

    E6 = Entry(win,width=30)
    E6.place(x=108,y=160)

    E7 = Entry(win,width=30)
    E7.place(x=108,y=185)
    
    for i in records:
        E0.insert(0,i[0])
        E1.insert(0,i[1])
        E2.insert(0,i[2])
        E3.insert(0,i[3])
        E4.insert(0,i[4])
        E5.insert(0,i[5])
        E6.insert(0,i[6])
        E7.insert(0,i[7])

    b = Button(win,text='Save',cursor='hand2',width=26,command=update)
    b.place(x=108,y=215)

l = Label(root,text='Name')
l.place(x=10,y=10)

l1 = Label(root,text='Age')
l1.place(x=10,y=35)

l2 = Label(root,text='Weight')
l2.place(x=10,y=60)

l3 = Label(root,text='Marital_Status')
l3.place(x=10,y=85)

l4 = Label(root,text='Guardians_Name')
l4.place(x=10,y=110)

l5 = Label(root,text='City')
l5.place(x=10,y=135)

l6 = Label(root,text='State')
l6.place(x=10,y=160)

l7 = Label(root,text='Mobile_Number')
l7.place(x=10,y=185)

l8 = Label(root,text='Enter ID')
l8.place(x=10,y=290)

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

e5 = Entry(root,width=30)
e5.place(x=108,y=135)

e6 = Entry(root,width=30)
e6.place(x=108,y=160)

e7 = Entry(root,width=30)
e7.place(x=108,y=185)

e8 = Entry(root,width=30)
e8.place(x=108,y=290)

b = Button(root,text='Submit',cursor='hand2',width=26,command=insert)
b.place(x=108,y=215)

b1 = Button(root,text='Show Details',width=26,cursor='hand2',command=query)
b1.place(x=108,y=245)

b2 = Button(root,text='Delete',width=26,cursor='hand2',command=delete)
b2.place(x=105,y=315)

b3 = Button(root,text='Update Record',width=26,cursor='hand2',command=new)
b3.place(x=105,y=345)

root.mainloop()