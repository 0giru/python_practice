from turtle import Turtle, Screen
import random

T = []
is_race_on = False

screen = Screen()
screen.setup(width = 500, height = 400)

colors = ["red", "RosyBrown", "RoyalBlue", "SaddleBrown", "SeaGreen", "SlateBlue"]

user_bet = screen.textinput("make your bet", "which turtle win the race?")

for i in range(len(colors)):
    turtle = Turtle()
    T.append(turtle)
    T[i].penup()
    T[i].shape("turtle")
    T[i].color(colors[i])
    T[i].goto(-150, -60 + 20*i)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in T:
        print(i.color())
        random_number = random.randint(0, 20)
        i.forward(random_number)
        if i.xcor() >= 230:
            is_race_on = False
            temp = i.pencolor()
            break

if temp == user_bet:
    print("you win")
else:
    print("you lose")


screen.exitonclick()


