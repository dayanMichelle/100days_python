# pylint: disable=unused-variable
from os import system,name
from art import logo
def clear():
    '''
    Fuction to clear the console
    '''
    if name == "nt":
        _=system("cls")
    else:
        _=system("clear")
# Calculator
#Add
def add(n_1,n_2):
    '''
    Add two numbers
    '''
    return n_1 + n_2
#Subtract
def subtract(n_1,n_2):
    '''
    Substract two numbers
    '''
    return n_1 - n_2
#Multiply
def multiply(n_1,n_2):
    '''
    Multiply two numbers
    '''
    return n_1 * n_2
#Divide
def divide(n_1,n_2):
    '''
    Divide two numbers
    '''
    return n_1 / n_2

# directorio
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    '''
    Return the total
    '''
    print(logo)
    num1 = float(input("What is the first number?: "))

    for symbol,value in operations.items():
        print(symbol)
    should_continue= True

    while should_continue:
        operation_symbols = input("Choose an operation: ")
        num2 = float(input("What is the second number?: "))
        calculation_function = operations[operation_symbols]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbols} {num2} = {answer}")

        if input("Type 'y' to continue calculating with {answer} on' to start a new calculator: ") == "y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()

calculator()
