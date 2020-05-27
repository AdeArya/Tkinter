from tkinter import *

root = Tk()

a = Entry(root)
b = Entry(root, width=50)
c = Entry(root, borderwidth=5)


def click():
    # get is output from entry
    mylabel = Label(root, text=a.get())
    mylabel.pack()

text = Label(root, text='hello guys')
button = Button(root, text='done', command=click)

text.pack()
a.pack()

# insert is inside label
a.insert(0,'enter your name')
button.pack()

b.pack()
c.pack()

root.mainloop()