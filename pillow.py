from tkinter import *
from PIL import Image,ImageTk
window = Tk()
window.title("LOGIN")
my_image = ImageTk.PhotoImage(Image.open('aj.png'))
label = Label(image=my_image)
label.pack()

button = Button(window,text='Exit',command=window.quit)
button.pack

window.mainloop()