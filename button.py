from tkinter import *

root = Tk()

def click():
    mylabel = Label(root, text='its working')
    mylabel.pack()

mybutton = Button(root, text='click')

mybutton2 = Button(root, text='click', state=DISABLED)

mybutton3 = Button(root, text='click', padx=100, pady=50)

mybutton4 = Button(root, text='check', command=click)

mybutton5 = Button(root, text='click', fg='green', bg='black')

mybutton.pack()
mybutton2.pack()
mybutton3.pack()
mybutton4.pack()
mybutton5.pack()

root.mainloop()