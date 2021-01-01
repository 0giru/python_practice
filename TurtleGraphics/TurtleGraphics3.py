from turtle import Turtle, Screen
import time

On = True

def move_fd():
    tim.forward(10)
    print(tim.xcor())
    print(tim.ycor())

def move_bw():
    tim.backward(0)

def move_left():
    tim.lt(90)

def move_right():
    tim.rt(90)

def clear():
    tim.reset()

tim = Turtle()
screen = Screen()
screen.listen()
screen.onkey(move_fd, "w")
screen.onkey(move_bw, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "x")


