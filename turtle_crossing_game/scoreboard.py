from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.penup()


    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over 🐢", align="center", font=(FONT))

    def update_level(self):
        self.goto(-230, 270)
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=(FONT))

    def next_level(self):
        self.level += 1


