from turtle import Turtle, Screen

def move_fd():
    tim.forward(10)

def move_bw():
    tim.backward(10)

def move_left():
    tim.lt(10)

def move_right():
    tim.rt(10)

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
screen.exitonclick()

