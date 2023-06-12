from tkinter import *
import sqlite3

root = Tk()
root.title("Classwork")
root.geometry('400x500')

# d = sqlite3.connect('class.sql')
# c = d.cursor()
# c.execute(""" CREATE TABLE classwork(
#           first_name,
#           last_name,
#           email,
#           age,
#           phone_number,
#           father_name,
#           mother_name
# )""")
# d.commit()
# d.close()

def inser():
    d = sqlite3.connect('class.sql')
    b = d.cursor()
    b.execute("INSERT INTO classwork VALUES(:f_name, :l_name, :email, :age, :phone_num, :father, :mother)",{
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'email': email.get(),
        'age': age.get(),
        'phone_num': phone.get(),
        'father': father.get(),
        'mother': mother.get()
    })
    d.commit()
    d.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    email.delete(0,END)
    age.delete(0,END)
    phone.delete(0,END)
    father.delete(0,END)
    mother.delete(0,END)

def query():
    conn = sqlite3.connect('class.sql')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM classwork")

    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += (record[0]) + ' ' + (record[1]) + ' ' + (record[5]) + ' ' + (record[6]) + ' ' + '\t' + str(record[7]) + '\n'

    query_label = Label(root,text=print_records)
    query_label.place(x=75,y=380)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('class.sql')
    c = conn.cursor()
    c.execute("DELETE from classwork WHERE oid = " + delete_b.get())
    print('Deleted Successfully')

    delete_b.delete(0,END)
    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect('class.sql')
    c = conn.cursor()

    record_id = delete_b.get()

    c.execute(""" UPDATE classwork SET
           first_name = :first,
           last_name = :last,
           email = :email,
           age = :age,
           phone_number = :phone,
           father_name = :father,
           mother_name = :mother
           WHERE oid = :oid""",
           {'first' : F_name.get(),
            'last' : L_name.get(),
            'email' : Email.get(),
            'age' : Age.get(),
            'phone' : Phone.get(),
            'father' : Father.get(),
            'mother' : Mother.get(),
            'oid' : record_id
               
           }

        )
    conn.commit()
    conn.close()

    editor.destroy()

def win():
    global editor

    editor = Tk()
    editor.title('Update Data')
    editor.geometry('300x300')

    record_id = delete_b.get()

    conn = sqlite3.connect('class.sql')
    c = conn.cursor()
    c.execute("SELECT * FROM classwork WHERE oid = " + record_id)
    
    records = c.fetchall()

    global F_name
    global L_name
    global Email
    global Age
    global Phone
    global Father
    global Mother 

    L = Label(editor,text='First_Name')
    L.place(x=10,y=10)

    L_1 = Label(editor,text='Last_Name')
    L_1.place(x=10,y=35)

    L_2 = Label(editor,text='Email_add')
    L_2.place(x=10,y=60)

    L_3 = Label(editor,text='age')
    L_3.place(x=10,y=85)

    L_4 = Label(editor,text='Phone_Number')
    L_4.place(x=10,y=110)

    L_5 = Label(editor,text='Father_Name')
    L_5.place(x=10,y=135)
  
    L_6 = Label(editor,text='Mother_Name')
    L_6.place(x=10,y=160)


    F_name = Entry(editor,width=30)
    F_name.place(x=100,y=10)

    L_name = Entry(editor,width=30)
    L_name.place(x=100,y=35)

    Email = Entry(editor,width=30)
    Email.place(x=100,y=60)

    Age = Entry(editor,width=30)
    Age.place(x=100,y=85)

    Phone = Entry(editor,width=30)
    Phone.place(x=100,y=110)

    Father = Entry(editor,width=30)
    Father.place(x=100,y=135)

    Mother = Entry(editor,width=30)
    Mother.place(x=100,y=160)
    
    for record in records:
        F_name.insert(0,record[0])
        L_name.insert(0,record[1])
        Email.insert(0,record[2])
        Age.insert(0,record[3])
        Phone.insert(0,record[4])
        Father.insert(0,record[5])
        Mother.insert(0,record[6])


    b = Button(editor,text='Save',cursor='hand2',width=25,command=update)
    b.place(x=100,y=195)
    

    editor.mainloop()


l = Label(root,text='First Name')
l.place(x=10,y=10)

l1 = Label(root,text='Last Name')
l1.place(x=10,y=35)

l2 = Label(root,text='Email')
l2.place(x=10,y=60)

l3 = Label(root,text='Age')
l3.place(x=10,y=85)

l4 = Label(root,text='Phone Number')
l4.place(x=10,y=110)

l5 = Label(root,text='Father Name')
l5.place(x=10,y=135)

l6 = Label(root,text='Mother Name')
l6.place(x=10,y=160)

l7 = Label(root,text='Delete ID')
l7.place(x=10,y=280)

f_name = Entry(root,width=30)
f_name.place(x=100,y=10)

l_name = Entry(root,width=30)
l_name.place(x=100,y=35)

email = Entry(root,width=30)
email.place(x=100,y=60)

age = Entry(root,width=30)
age.place(x=100,y=85)

phone = Entry(root,width=30)
phone.place(x=100,y=110)

father = Entry(root,width=30)
father.place(x=100,y=135)

mother = Entry(root,width=30)
mother.place(x=100,y=160)

delete_b = Entry(root,width=30)
delete_b.place(x=100,y=280)


b1 = Button(root,text='Add Records',width=25,cursor='hand2',command=inser)
b2 = Button(root,text='Show Records',width=25,cursor='hand2',command=query)
b3 = Button(root,text='Delete',width=25,cursor='hand2',command=delete)
b4 = Button(root,text='Update',width=25,cursor='hand2',command=win)


b1.place(x=100,y=195)
b2.place(x=100,y=230)
b3.place(x=100,y=310)
b4.place(x=100,y=340)

root.mainloop()