import turtle
import pandas

data = pandas.read_csv("50_states.csv", index_col=False)
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

checked_states = []
def find_state():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state = data[answer_state == data["state"]]
    t.goto(state['x'].to_list()[0], state['y'].to_list()[0])
    t.write(f"{state['state'].to_string(index=False)}")
    checked_states.append(state.state.to_string(index=False))


game_on = True

while game_on:
    answer_state = screen.textinput(title=f"{len(checked_states)}/{len(data)} Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in data.state.to_list():

            if state not in checked_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if len(data[answer_state == data["state"]]) > 0:
        find_state()
        if len(checked_states) >= len(data):
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(-50, 0)
            t.write("Finished", font=("Courier", 24, "normal"))
            game_on = False
    else:
        answer_state = screen.textinput(title=f"{len(checked_states)}/{len(data)} Guess the State", prompt="What's another state's name?").title()



