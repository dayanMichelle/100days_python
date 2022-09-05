import turtle
import random

timmy = turtle.Turtle()
timmy.color("#EC7272", "#F7A76C")
turtle.colormode(255)

# Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 6)
# rgb_colors = []
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
colors = [(222, 236, 254), (254, 254, 215), (223, 253, 253), (253, 187, 199)]

timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(colors))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle.Screen()

screen.exitonclick()
