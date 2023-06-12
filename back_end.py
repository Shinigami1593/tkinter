from tkinter import *
import sqlite3 #for database

root = Tk()
root.title('Database 01')
root.geometry('300x500')

#database

#creation of data base
# d = sqlite3.connect('Ayush.sql')
# c = d.cursor()
# c.execute(""" CREATE TABLE addresses(
#           fitst_name,
#           last_name,
#           address,
#           city,
#           state,
#           zipcode
# )""")
# d.commit()
# d.close()
def inser():
    d = sqlite3.connect('Ayush.sql')
    b = d.cursor()
    b.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :state, :city, :zip)",{
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'state': state.get(),
        'city': city.get(),
        'zip': zip.get()
    })
    d.commit()
    d.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    state.delete(0,END)
    city.delete(0,END)
    zip.delete(0,END)

def query():
    conn = sqlite3.connect('Ayush.sql')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM addresses")

    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += (record[0]) + ' ' + (record[1]) + ' ' + '\t' + str(record[6]) + '\n'

    query_label = Label(root,text=print_records)
    query_label.place(x=75,y=320)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('Ayush.sql')
    c = conn.cursor()
    c.execute("DELETE from addresses WHERE oid = " + delete_b.get())
    print('Deleted Successfully')

    delete_b.delete(0,END)
    conn.commit()
    conn.close()




l = Label(root,text='First Name')
l.place(x=10,y=10)

l1 = Label(root,text='Last Name')
l1.place(x=10,y=35)

l2 = Label(root,text='Address')
l2.place(x=10,y=60)

l3 = Label(root,text='State')
l3.place(x=10,y=85)

l4 = Label(root,text='City')
l4.place(x=10,y=110)

l5 = Label(root,text='Zipcode')
l5.place(x=10,y=135)

l6 = Label(root,text='Delete ID')
l6.place(x=10,y=240)

f_name = Entry(root,width=30)
f_name.place(x=80,y=10)

l_name = Entry(root,width=30)
l_name.place(x=80,y=35)

address = Entry(root,width=30)
address.place(x=80,y=60)

state = Entry(root,width=30)
state.place(x=80,y=85)

city = Entry(root,width=30)
city.place(x=80,y=110)

zip = Entry(root,width=30)
zip.place(x=80,y=135)

delete_b = Entry(root,width=30)
delete_b.place(x=80,y=240)


add_record = Button(root,text='Add Records',cursor='hand2',width=25,command=inser)
show_record = Button(root,text='Show Records',cursor='hand2',width=25,command=query)
delete_record = Button(root,text='Delete',cursor='hand2',width=25,command=delete)

add_record.place(x=75,y=160)
show_record.place(x=75,y=195)
delete_record.place(x=75,y=270)

root.mainloop()