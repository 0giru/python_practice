from turtle import Turtle, Screen
from snake import Snake
import time

# Snake = []

# first_length : int = screen.textinput("start", "make first snake length")

# def CreateBody():
#     body = Turtle()
#     body.shape("square")
#     body.color("white")
#     return body

# def MakeSnake(templist : list):
#     length = len(templist)
#     for i in range(length):
#         templist[i].penup()
#         templist[i].setpos(-20*(i-1), 0)

# def Move_FWD(templist : list):
#     templist[0].forward(20)

# def SnakeBirth():
#     for temp in range(3):
#         temp = CreateBody()
#         Snake.append(temp)

# def SnakeTrace(parlist : list):
#     for list_num in range(len(Snake)-1, 0, -1):
#         new_x = parlist[list_num - 1].xcor()
#         new_y = parlist[list_num - 1].ycor()
#         parlist[list_num].goto(new_x, new_y)

snake = Snake()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

Game_On = True

snake.create_snake()
screen.update()

while Game_On:
    time.sleep(0.5)
    snake.move_snake()
    screen.update()
    
    screen.exitonclick()
