import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """
    Generate random cars
    """
    def __init__(self):
        self.all_cars = []
        self.MOVE_INCREMENT = 0.1

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)

    def collision(self, player):
        for car in self.all_cars:
            if car.distance(player) < 20:
                return True