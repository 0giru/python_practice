from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=snake.size_width, height=snake.size_width)
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

while Game_On:
    screen.update()
    time.sleep(0.075)
    snake.move_snake()

    if snake.segment[0].distance(food) < 15:
        food.refresh()
        snake.add_segment()
        print(len(snake.segment))
        scoreboard.Increase()

    if snake.collision_wall():
        Game_On = False
        scoreboard.game_over()

    if snake.collision_tail():
        Game_On = False
        scoreboard.game_over()

screen.exitonclick()