from tkinter import *

# creatin a window
root = Tk()
root.title('Simple Calculator')

# creating a display
e = Entry(root, width=45, borderwidth=5, relief=SUNKEN)
e.grid(row=0, column=0, columnspan=3)

# defing a command to enter a number when the button is pressed
def button_com(number):
    e.insert(END, number)

# clear commanf
def button_clear():
    e.delete(0, END)

# addition command
def button_add():
    first_number = e.get()
    global f_num
    global math
    f_num = int(first_number)
    math = "Addition"
    e.delete(0, END)

# subtraction command
def button_sub():
    first_number = e.get()
    global f_num
    global math
    f_num = int(first_number)
    math = "Subtraction"
    e.delete(0, END)

# multiplication command
def button_mul():
    first_number = e.get()
    global f_num
    global math
    f_num = int(first_number)
    math = "Multiplication"
    e.delete(0, END)

# division command
def button_div():
    first_number = e.get()
    global f_num
    global math
    f_num = int(first_number)
    math = "Division"
    e.delete(0, END)

# creating a command to calculate based on the type of math
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "Addition":
        e.insert(0, f_num + int(second_number))

    if math == "Subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "Multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "Division":
        e.insert(0, f_num / int(second_number))

# creating button layout
button_1 = Button(root, text='1', pady=40, padx=40, command=lambda: button_com(1))
button_2 = Button(root, text='2', pady=40, padx=40, command=lambda: button_com(2))
button_3 = Button(root, text='3', pady=40, padx=40, command=lambda: button_com(3))
button_4 = Button(root, text='4', pady=40, padx=40, command=lambda: button_com(4))
button_5 = Button(root, text='5', pady=40, padx=40, command=lambda: button_com(5))
button_6 = Button(root, text='6', pady=40, padx=40, command=lambda: button_com(6))
button_7 = Button(root, text='7', pady=40, padx=40, command=lambda: button_com(7))
button_8 = Button(root, text='8', pady=40, padx=40, command=lambda: button_com(8))
button_9 = Button(root, text='9', pady=40, padx=40, command=lambda: button_com(9))
button_0 = Button(root, text='0', pady=40, padx=40, command=lambda: button_com(0))
button_clear = Button(root, text='C', pady=40, padx=40, command=button_clear)
button_add = Button(root, text='+', pady=40, padx=40, command=button_add)
button_equal = Button(root, text='=', pady=40, padx=40, command=button_equal)
button_sub = Button(root, text='-', pady=40, padx=40, command=button_sub)
button_div = Button(root, text='/', pady=40, padx=40, command=button_div)
button_mul = Button(root, text='*', pady=40, padx=40, command=button_mul)

# creating a grid layout
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

root.mainloop()