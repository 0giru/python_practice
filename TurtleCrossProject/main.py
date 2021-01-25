import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()

screen.listen()
screen.onkey(timmy.move, "Up")

car = CarManager()

count = 0

game_is_on = True
while game_is_on:
    count += 1
    time.sleep(0.05)
    screen.update()
    if count % 6 == 0:
        car.create_car()
        car.move()
