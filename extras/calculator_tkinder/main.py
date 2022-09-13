# Import module
import tkinter
# TODO: round
# TODO: clear
# Create object
window = tkinter.Tk()
# Adjust size
window.geometry("300x500")
bg = tkinter.PhotoImage(file="image.png")
# Show image using label
label = tkinter.Label(window, image=bg)
label.place(x=0, y=0)

equation = tkinter.StringVar()

expression_field = tkinter.Label(window, width=10, textvariable=equation)

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
            r = round(l_n1 - l_n2, 3)
            expression = str(r)
            return equation.set(r)
        if expression.find("+") > 0:
            r = expression.find("+")
            l_n1 = float(expression[0:r])
            l_n2 = float(expression[r+1:])
            s = round(l_n1 + l_n2)
            expression = str(s)
            return equation.set(s)
        if expression.find("/") > 0:
            r = expression.find("/")
            l_n1 = float(expression[0:r])
            l_n2 = float(expression[r+1:])
            d = round(l_n1 / l_n2, 3)
            expression = str(d)
            return equation.set(d)
        if expression.find("*") > 0:
            r = expression.find("*")
            l_n1 = float(expression[0:r])
            l_n2 = float(expression[r+1:])
            m = round(l_n1 * l_n2, 3)
            expression = str(m)
            return equation.set(m)
    if num == "cl":
        expression = ""
        return equation.set(0)


    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


n0 = tkinter.Button(text="0", command=lambda: press(0))
n0.place(x=35, y=210)

n1 = tkinter.Button(text="1", command=lambda: press(1))
n1.place(x=100, y=210)

n2 = tkinter.Button(text="2", command=lambda: press(2))
n2.place(x=165, y=210)


divide = tkinter.Button(text="/", command=lambda: press("/"))
divide.place(x=230, y=210)

n3 = tkinter.Button(text="3", command=lambda: press(3))
n3.place(x=35, y=275)

n4 = tkinter.Button(text="4", command=lambda: press(4))
n4.place(x=100, y=275)

n5 = tkinter.Button(text="5", command=lambda: press(5))
n5.place(x=165, y=275)

n6 = tkinter.Button(text="6", command=lambda: press(6))
n6.place(x=165, y=275)

multiply = tkinter.Button(text="*", command=lambda: press("*"))
multiply.place(x=225, y=275)

n7 = tkinter.Button(text="7", command=lambda: press(7))
n7.place(x=35, y=335)

n8 = tkinter.Button(text="8", command=lambda: press(8))
n8.place(x=100, y=335)

n9 = tkinter.Button(text="9", command=lambda: press(9))
n9.place(x=165, y=335)

sum = tkinter.Button(text="+", command=lambda: press("+"))
sum.place(x=225, y=335)

clear = tkinter.Button(text="cl", command=lambda: press("cl"))
clear.place(x=35, y=400)

n5 = tkinter.Button(text="5", command=lambda: press("5"))
n5.place(x=100, y=400)

substra = tkinter.Button(text="-", command=lambda: press("-"))
substra.place(x=165, y=400)

result = tkinter.Button(text="=", command=lambda: press("="))
result.place(x=225, y=400)

window.mainloop()
