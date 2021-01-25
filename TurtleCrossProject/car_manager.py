import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

MAX_CAR_POS_Y = 200
MIN_CAR_POS_Y = -200

MAX_CAR_POS_X = 300
MIN_CAR_POS_X = 250

class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(1, 2)
        new_car.setheading(180)
        clr = random.choice(COLORS)
        new_car.color(clr)
        new_car.goto(random.randrange(MIN_CAR_POS_X, MAX_CAR_POS_X), random.randrange(MIN_CAR_POS_Y, MAX_CAR_POS_Y))
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE+5)   
