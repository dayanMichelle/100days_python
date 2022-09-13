# Import module
import tkinter
import math
# TODO: round
# TODO: clear
# Create object

BLUE = "#1A374D"
window = tkinter.Tk()
window.config(bg=BLUE)
# Adjust size
window.geometry("300x500")

canvas = tkinter.Canvas(width=300, height=500, bg=BLUE, highlightthickness=0)
image = tkinter.PhotoImage(file="image.png")
canvas.create_image(150, 250, image=image)
canvas.place(x=0, y=0)
equation = tkinter.StringVar()

expression_field = tkinter.Label(window, width=10, textvariable=equation, bg=BLUE)

expression_field.place(x=160, y=140)

expression = ""



def press(num):
    # point out the global expression variable
    global expression

    if num == "=":
        print(expression)
        if expression.find("-") > 0:
            r = expression.find("-")
            l_n1 = float(expression[0:r])
            l_n2 = float(expression[r+1:])
            r = round((l_n1 - l_n2), 3)
            expression = str(r)
            return equation.set(r)
        if expression.find("+") > 0:
            r = expression.find("+")
            l_n1 = float(expression[0:r])
            l_n2 = float(expression[r+1:])
            s = round((l_n1 + l_n2), 3)
            expression = str(s)
            return equation.set(s)
        if expression.find("/") > 0:
            r = expression.find("/")
            l_n1 = float(expression[0:r])
            l_n2 = float(expression[r+1:])
            d =  round((l_n1 / l_n2), 3)
            expression = str(d)
            return equation.set(d)
        if expression.find("*") > 0:
            r = expression.find("*")
            l_n1 = float(expression[0:r])
            l_n2 = float(expression[r+1:])
            m = round((l_n1 * l_n2), 3)
            expression = str(m)
            return equation.set(m)
    if num == "cl":
        expression = ""
        return equation.set(0)


    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)

2
n0 = tkinter.Button(text="0", width=2, height=2, highlightbackground=BLUE, command=lambda: press(0))
n0.place(x=25, y=200)

n1 = tkinter.Button(text="1", width=2, height=2, highlightbackground=BLUE, command=lambda: press(1))
n1.place(x=90, y=200)

n2 = tkinter.Button(text="2", width=2, height=2,  highlightbackground=BLUE, command=lambda: press(2))
n2.place(x=155, y=200)


divide = tkinter.Button(text="/", width=2, height=2, highlightbackground=BLUE, command=lambda: press("/"))
divide.place(x=220, y=200)

n3 = tkinter.Button(text="3", width=2, height=2, highlightbackground=BLUE, command=lambda: press(3))
n3.place(x=30, y=265)

n4 = tkinter.Button(text="4", width=2, height=2, highlightbackground=BLUE, command=lambda: press(4))
n4.place(x=90, y=265)

n5 = tkinter.Button(text="5", width=2, height=2, highlightbackground=BLUE, command=lambda: press(5))
n5.place(x=155, y=265)

n6 = tkinter.Button(text="6", width=2, height=2, highlightbackground=BLUE, command=lambda: press(6))
n6.place(x=155, y=265)

multiply = tkinter.Button(text="*", width=2, height=2, highlightbackground=BLUE, command=lambda: press("*"))
multiply.place(x=220, y=265)

n7 = tkinter.Button(text="7", width=2, height=2, highlightbackground=BLUE, command=lambda: press(7))
n7.place(x=30, y=330)

n8 = tkinter.Button(text="8", width=2, height=2, highlightbackground=BLUE, command=lambda: press(8))
n8.place(x=95, y=330)

n9 = tkinter.Button(text="9", width=2, height=2, highlightbackground=BLUE, command=lambda: press(9))
n9.place(x=160, y=330)

sum = tkinter.Button(text="+", width=2, height=2, highlightbackground=BLUE, command=lambda: press("+"))
sum.place(x=220, y=330)

clear = tkinter.Button(text="cl", width=2, height=2, highlightbackground=BLUE, command=lambda: press("cl"))
clear.place(x=30, y=395)

n5 = tkinter.Button(text="5", width=2, height=2, highlightbackground=BLUE, command=lambda: press("5"))
n5.place(x=95, y=395)

substra = tkinter.Button(text="-", width=2, height=2, highlightbackground=BLUE, command=lambda: press("-"))
substra.place(x=160, y=395)

result = tkinter.Button(text="=", width=2, height=2, highlightbackground=BLUE, command=lambda: press("="))
result.place(x=220, y=395)

window.mainloop()
