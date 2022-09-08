import pandas
import turtle
import random

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)


# random position
turtle.shape(image)
list_x = data.x.to_list()
random_x = random.choice(list_x)
index = list_x.index(random_x)
list_y = data.y.to_list()
random_y = list_y[index]


# find the state info
data = data.to_numpy().tolist()
state = ''
for da in data:
    if da[1] == random_x and da[2] == random_y:
        state = da
print(state)


# play game
game_on = True
while game_on:
    timmy = turtle.Turtle("turtle")
    timmy.color("#645CAA")
    timmy.penup()
    timmy.goto(random_x, random_y)
    answer_state = screen.textinput(title=f"Guess the State", prompt="What's the state's name?").title()
    while not answer_state == state[0]:
        answer_state = screen.textinput(title=f"Guess the State", prompt="What's the state's name?").title()

    win = turtle.Turtle()
    win.hideturtle()
    win.penup()
    win.goto(-30, 0)
    win.write("Correct", font=("Arial", 24))
    game_on = False


screen.mainloop()
