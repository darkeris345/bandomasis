from tkinter import *


root = Tk()
root.title("Skaičiuotuvas")
root.geometry("390x439")
root.config(bg='bisque2')

e = Entry(root, width=45, borderwidth=20, bg="bisque")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=30)
# e.insert(0,'' )




def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))




def equlbut():
    global operator
    add = str(eval(operator))
    textin.set(add)
    operator = ''


def equlbut():
    global operator
    sub = str(eval(operator))
    textin.set(sub)
    operator = ''


def equlbut():
    global operator
    mul = str(eval(operator))
    textin.set(mul)
    operator = ''


def equlbut():
    global operator
    div = str(eval(operator))
    textin.set(div)
    operator = ''


def clrbut():
    e.delete(0, END)



# Skaičių mygtukai
button_1 = Button(root, text="1", padx=45, pady=20,fg="brown", command=lambda:click(1))
button_2 = Button(root, text="2", padx=45, pady=20,fg="brown", command=lambda:click(2))
button_3 = Button(root, text="3", padx=45, pady=20,fg="brown", command=lambda:click(3))
button_4 = Button(root, text="4", padx=45, pady=20,fg="brown", command=lambda:click(4))
button_5 = Button(root, text="5", padx=45, pady=20,fg="brown", command=lambda:click(5))
button_6 = Button(root, text="6", padx=45, pady=20,fg="brown", command=lambda:click(6))
button_7 = Button(root, text="7", padx=45, pady=20,fg="brown", command=lambda:click(7))
button_8 = Button(root, text="8", padx=45, pady=20,fg="brown", command=lambda:click(8))
button_9 = Button(root, text="9", padx=45, pady=20,fg="brown", command=lambda:click(9))
button_0 = Button(root, text="0", padx=98, pady=20,fg="brown", command=lambda:click(0))

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
button_add = Button(root, text="+", padx=29, pady=20, command=lambda:click("+"))
button_minus = Button(root, text="-", padx=30, pady=20, command=lambda:click("-"))
button_multiplication = Button(root, text="*", padx=30, pady=20, command=lambda:click("*"))
button_divide = Button(root, text="/", padx=30, pady=20, command=lambda:click("/"))

button_add.grid(row=4, column=3)
button_minus.grid(row=3, column=3)
button_multiplication.grid(row=2, column=3)
button_divide.grid(row=1, column=3)

button_square_root = Button(root, text="√", padx=45, pady=20, command=lambda:click())
button_square = Button(root, text="x²", padx=43, pady=20, command=lambda:click())
button_cube = Button(root, text="x³", padx=43, pady=20, command=lambda:click())

button_square_root.grid(row=1, column=2)
button_square.grid(row=1, column=1)
button_cube.grid(row=1, column=0)

button_equal = Button(root, text="=", padx=29, pady=20, command=equlbut)
button_C = Button(root, text="C", padx=45, pady=20, command=clrbut)

button_equal.grid(row=5, column=3)
button_C.grid(row=5, column=2)



root.mainloop()