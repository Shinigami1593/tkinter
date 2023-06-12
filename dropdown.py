from tkinter import *
root = Tk()
root.geometry('200x200')
def show():
    label.config(text = clicked.get())
#Dropdown menu option
options = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thrusday',
    'Friday',
    'Saturday',
    'Sunday'
]
clicked = StringVar()
clicked.set('Monday')

drop = OptionMenu(root,clicked,*options)
drop.pack()

button = Button(root,text='Click Me',command=show).pack()

label = Label(root,text=" ")
label.pack()
root.mainloop()