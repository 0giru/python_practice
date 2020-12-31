from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.key_up, "Up")
screen.onkey(snake.key_down, "Down")
screen.onkey(snake.key_left, "Left")
screen.onkey(snake.key_right, "Right")

Game_On = True

snake.create_snake()
screen.update()

while Game_On:
    time.sleep(0.05)
    snake.move_snake()
    snake.collision_wall()

    if snake.segment[0].distance(food) < 15:
        food.refresh()
        scoreboard.write((0, 280), True, "center")


    # snake.create_food()
    # snake.collision_food()
    # print(snake.segment[0].heading())
    screen.update()