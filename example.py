from tkinter import *
root = Tk()
root.configure(bg = '#6BDDFF')
redbutton = Button(root,text='LEFT', fg = 'green').pack(side = LEFT)
greenbutton = Button(root, text='RIGHT',fg='black').pack(side=RIGHT)
bluebutton = Button(root, text='TOP',fg = 'blue').pack(side=TOP)
blackbutton = Button(root,text='BOTTOM',fg='red').pack(side=BOTTOM)
root.mainloop()