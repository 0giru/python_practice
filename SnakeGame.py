from turtle import Turtle, Screen
from snake import Snake
import time

snake = Snake()

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
    time.sleep(0.1)
    snake.move_snake()
    snake.collision_wall()
    # snake.create_food()
    # snake.collision_food()
    # print(snake.segment[0].heading())
    screen.update()