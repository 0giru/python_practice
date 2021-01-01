from turtle import Turtle, Screen

timmy = Turtle()

def move(user):
    user.forward(100)
    user.right(90)

for i in range(4):
    move(timmy)

screen = Screen()
screen.exitonclick()