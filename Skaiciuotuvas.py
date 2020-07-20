from math import sqrt
from tkinter import *


root = Tk()
root.title("Skaičiuotuvas")
root.geometry("390x350")
root.config(bg='bisque2')
root.iconbitmap("calculator.ico")



e = Entry(root,font=("arial", 15, "bold"), width=25, borderwidth=10, bg="bisque", bd=5, justify="right")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=30)


def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clrbut():
    e.delete(0, END)


def add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def minus():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def square_root():
    first_number = e.get()
    global f_num
    global math
    math = "square_root"
    f_num = int(first_number)
    e.delete(0, END)

def square_raise():
    first_number = e.get()
    global f_num
    global math
    math = "squaring"
    f_num = int(first_number)
    e.delete(0, END)

def cube_raise():
    first_number = e.get()
    global f_num
    global math
    math = "cubing"
    f_num = int(first_number)
    e.delete(0, END)


def equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        try:
            e.insert(0, f_num / int(second_number))
        except ZeroDivisionError:
            e.insert(0, 'ErrorDivision from zero impossible')
    if math == "square_root":
        e.insert(0, sqrt(f_num))
    if math == "squaring":
        e.insert(0, f_num **2)
    if math == "cubing":
        e.insert(0, f_num **3)






# Skaičių mygtukai
button_1 = Button(root, text="1", padx=45, pady=10,fg="brown", command=lambda:click(1))
button_2 = Button(root, text="2", padx=45, pady=10, command=lambda:click(2))
button_3 = Button(root, text="3", padx=45, pady=10, command=lambda:click(3))
button_4 = Button(root, text="4", padx=45, pady=10, command=lambda:click(4))
button_5 = Button(root, text="5", padx=45, pady=10, command=lambda:click(5))
button_6 = Button(root, text="6", padx=45, pady=10, command=lambda:click(6))
button_7 = Button(root, text="7", padx=45, pady=10, command=lambda:click(7))
button_8 = Button(root, text="8", padx=45, pady=10, command=lambda:click(8))
button_9 = Button(root, text="9", padx=45, pady=10, command=lambda:click(9))
button_0 = Button(root, text="0", padx=98, pady=10, command=lambda:click(0))

button_1.grid(row=4, column=0,)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)



button_0.grid(row=5, column=0, columnspan=2)

# Funkcionaliniai mygtukai
button_add = Button(root, text="+", padx=29, pady=10, command=add)
button_add.grid(row=4, column=3)
button_minus = Button(root, text="-", padx=30, pady=10, command=minus)
button_minus.grid(row=3, column=3)
button_multiply = Button(root, text="*", padx=30, pady=10, command=multiply)
button_multiply.grid(row=2, column=3)
button_divide = Button(root, text="/", padx=30, pady=10, command=divide)
button_divide.grid(row=1, column=3)

button_square_root = Button(root, text="√", padx=45, pady=10, command=square_root)
button_square_root.grid(row=1, column=2)
button_square = Button(root, text="x²", padx=43, pady=10, command=square_raise)
button_square.grid(row=1, column=1)
button_cube = Button(root, text="x³", padx=43, pady=10, command=cube_raise)
button_cube.grid(row=1, column=0)

button_equal = Button(root, text="=", padx=29, pady=10, command=equal)
button_equal.grid(row=5, column=3)
button_C = Button(root, text="C", padx=45, pady=10, command=clrbut)
button_C.grid(row=5, column=2)



root.mainloop()