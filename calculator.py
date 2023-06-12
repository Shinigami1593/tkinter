from tkinter import *

root = Tk()

#defining title project
root.title('Simple Calculator')
e = Entry(root,width=45,borderwidth=5)
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
#for clear
def button_clear():
    e.delete(0,END)

#for addition
def button_add():
    f_number = e.get()
    global a
    a = 'add'
    global f_num
    f_num = int(f_number)
    e.delete(0,END)

#for substraction
def button_minus():
    f_number = e.get()
    global a
    a = 'sub'
    global f_no
    f_no = int(f_number)
    e.delete(0,END)

#for multiplication
def button_mul():
    f_number = e.get()
    global a
    a = 'mul'
    global f_no
    f_no = int(f_number)
    e.delete(0,END)

#for division
def button_div():
    f_number = e.get()
    global a
    a = 'div'
    global f_no
    f_no = int(f_number)
    e.delete(0,END)

#for squaring
def button_sq():
    f_number = e.get()
    global a
    a = 'sq'
    global f_no
    f_no = int(f_number)
    e.delete(0,END)

#for power of a number
def button_squ():
    f_number = e.get()
    global a
    a = 'squ'
    global f_no
    f_no = int(f_number)
    e.delete(0,END)

#equal to button and all the arithmetic operation to function
def button_equal():
    s_number = e.get()
    e.delete(0,END)
    if a == 'add':
        e.insert(0, f_num + int(s_number))
    elif a == 'sub':
        e.insert(0, f_no - int(s_number))
    elif a == 'mul':
        e.insert(0, f_no * int(s_number))
    elif a == 'div':
        e.insert(0, f_no / int(s_number))
    elif a == 'sq':
        e.insert(0, f_no ** 2)
    elif a == 'squ':
        e.insert(0, f_no ** int(s_number))


#button of numbers and operations
b_1 =  Button(root,text='1',padx=40,pady=20,command=lambda : button_click(1))
b_2 =  Button(root,text='2',padx=40,pady=20,command=lambda : button_click(2))
b_3 =  Button(root,text='3',padx=40,pady=20,command=lambda : button_click(3))
b_4 =  Button(root,text='4',padx=40,pady=20,command=lambda : button_click(4))
b_5 =  Button(root,text='5',padx=40,pady=20,command=lambda : button_click(5))
b_6 =  Button(root,text='6',padx=40,pady=20,command=lambda : button_click(6))
b_7 =  Button(root,text='7',padx=40,pady=20,command=lambda : button_click(7))
b_8 =  Button(root,text='8',padx=40,pady=20,command=lambda : button_click(8))
b_9 =  Button(root,text='9',padx=40,pady=20,command=lambda : button_click(9))
b_0 =  Button(root,text='0',padx=40,pady=20,command=lambda : button_click(0))
b_add =  Button(root,text='+',padx=40,pady=20,command=button_add)
b_minus =  Button(root,text='-',padx=40,pady=20,command=button_minus)
b_mul =  Button(root,text='x',padx=40,pady=20,command=button_mul)
b_div =  Button(root,text='%',padx=40,pady=20,command=button_div)
b_sq =  Button(root,text='^2',padx=40,pady=20,command=button_sq)
b_squ =  Button(root,text='^',padx=40,pady=20,command=button_squ)
b_equal =  Button(root,text='=',padx=91,pady=20,command=button_equal)
b_clear =  Button(root,text='CE',padx=35,pady=20,command=button_clear)


#placing buttons in the screen
b_1.grid(row=4,column=0)
b_2.grid(row=4,column=1)
b_3.grid(row=4,column=2)

b_4.grid(row=3,column=0)
b_5.grid(row=3,column=1)
b_6.grid(row=3,column=2)

b_7.grid(row=2,column=0)
b_8.grid(row=2,column=1)
b_9.grid(row=2,column=2)

b_0.grid(row=5,column=0)
b_clear.grid(row=1,column=0)
b_add.grid(row=1,column=1)
b_minus.grid(row=1,column=2)
b_mul.grid(row=2,column=3)
b_div.grid(row=3,column=3)
b_sq.grid(row=4,column=3)
b_squ.grid(row=5,column=3)
b_equal.grid(row=5,column=1,columnspan=2)


root.mainloop()

