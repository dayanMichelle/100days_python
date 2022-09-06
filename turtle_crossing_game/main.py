import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Create a player
player = Player()
screen.onkey(player.move, "Up")

car = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(car.MOVE_INCREMENT)
    screen.update()

    scoreboard.update_level()

    car.create_car()
    car.move()

    if car.collision(player):
        scoreboard.game_over()
        game_is_on = False

    if player.win():
        scoreboard.next_level()
        car.MOVE_INCREMENT *= 0.5





screen.exitonclick()