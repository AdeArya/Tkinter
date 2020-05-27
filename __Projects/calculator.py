from tkinter import *

root = Tk()
operator = ""
text_input = StringVar()
root.title('Stark Calculator')


# functions for buttons

def button_click(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)

def button_c():
    global operator
    operator = ""
    text_input.set("")

def button_e():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)


# header

space = Label(root, text="")
space.grid(row=0)

inputs = Entry(root, textvariable = text_input, border=9, justify='right', width=30)
inputs.grid(row=1, column=0, columnspan=4)

logo = Label(root, font=('arial',12,'bold'), text='ade calculator'.upper())
logo.grid(row=2, columnspan=4)


# define button 

button_1        = Button(root, bd = 4, bg='gray', font = ('arial', 12, 'bold'), text='1', padx=12, pady=15, command=lambda: button_click(1))
button_2        = Button(root, bd = 4, bg='gray', font = ('arial', 12, 'bold'), text='2', padx=12, pady=15, command=lambda: button_click(2))
button_3        = Button(root, bd = 4, bg='gray', font = ('arial', 12, 'bold'), text='3', padx=12, pady=15, command=lambda: button_click(3))
button_4        = Button(root, bd = 4, bg='gray', font = ('arial', 12, 'bold'), text='4', padx=12, pady=15, command=lambda: button_click(4))
button_5        = Button(root, bd = 4, bg='gray', font = ('arial', 12, 'bold'), text='5', padx=12, pady=15, command=lambda: button_click(5))
button_6        = Button(root, bd = 4, bg='gray', font = ('arial', 12, 'bold'), text='6', padx=12, pady=15, command=lambda: button_click(6))
button_7        = Button(root, bd = 4, bg='gray', font = ('arial', 12, 'bold'), text='7', padx=12, pady=15, command=lambda: button_click(7))
button_8        = Button(root, bd = 4, bg='gray', font = ('arial', 12, 'bold'), text='8', padx=12, pady=15, command=lambda: button_click(8))
button_9        = Button(root, bd = 4, bg='gray', font = ('arial', 12, 'bold'), text='9', padx=12, pady=15, command=lambda: button_click(9))
button_0        = Button(root, bd = 4, bg='gray', font = ('arial', 12, 'bold'), text='0', padx=12, pady=15, command=lambda: button_click(0))

button_clear    = Button(root, bd = 4, bg='gray', font = ('arial', 15, 'bold'), text='c', padx=12, pady=15, command=lambda: button_c())
button_plus     = Button(root, bd = 4, bg='gray', font = ('arial', 15, 'bold'), text='+', padx=30, pady=15, command=lambda: button_click("+"))
button_minus    = Button(root, bd = 4, bg='gray', font = ('arial', 15, 'bold'), text='-', padx=30, pady=15, command=lambda: button_click('-'))
button_times    = Button(root, bd = 4, bg='gray', font = ('arial', 15, 'bold'), text='x', padx=30, pady=15, command=lambda: button_click('*'))
button_divide   = Button(root, bd = 4, bg='gray', font = ('arial', 15, 'bold'), text=':', padx=30, pady=15, command=lambda: button_click('/'))
button_equals   = Button(root, bd = 4, bg='gray', font = ('arial', 15, 'bold'), text='=', padx=12, pady=15, command=lambda: button_e())


# buttons grid

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)

button_0.grid(row=6, column=0)
button_plus.grid(row=3, column=3)
button_minus.grid(row=4, column=3)
button_times.grid(row=5, column=3)
button_divide.grid(row=6, column=3)
button_equals.grid(row=6, column=2)
button_clear.grid(row=6, column=1)

root.mainloop()