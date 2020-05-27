from tkinter import *

root = Tk()

mylabel1 = Label(root, text='my name is ade')
mylabel2 = Label(root, text='python programming is great')
mylabel3 = Label(root, text='hello world')
mylabel4 = Label(root, text='tkinter is nice library')
mylabel5 = Label(root, text='nice')

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)
mylabel3.grid(row=2, column=2)
mylabel4.grid(row=3, column=3)
mylabel5.grid(row=4, column=4)

root.mainloop()