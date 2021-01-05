from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time

screen = Screen()
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

# index 0 paddle on the right
paddle.create_paddle(-350)
paddle.create_paddle(350)
ball.create_ball()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My PingPong Game")
screen.listen()

screen.onkey(paddle.go_up1, "w")
screen.onkey(paddle.go_down1, "s")
screen.onkey(paddle.go_up2, "p")
screen.onkey(paddle.go_down2, ";")

screen.tracer(0)

Game_On = True

while Game_On:
    time.sleep(0.01)
    screen.update()
    ball.ball_move()

    #paddle collision
    if ball.segment[0].distance(paddle.segment[0]) <= 50 and ball.segment[0].xcor() < -330:
        ball.paddle_reflect()
    elif ball.segment[0].xcor() < -340:
        pass
    elif ball.segment[0].distance(paddle.segment[1]) <= 50 and ball.segment[0].xcor() > 330:
        ball.paddle_reflect()
    elif ball.segment[0].xcor() > 340:
        pass

    #top_bottom wall collision
    if ball.segment[0].ycor() > 290 or ball.segment[0].ycor() < -290:
        ball.wall_reflect()

    #score record
    if ball.segment[0].xcor() < -370:
        scoreboard.paddle1_increase()
        time.sleep(0.5)
        ball.segment[0].goto(0, 0)
        paddle.segment[0].goto(-350, 0)
        paddle.segment[1].goto(350, 0)
        ball.segment[0].setheading(ball.random_choice())

    elif ball.segment[0].xcor() > 370:
        scoreboard.paddle0_increase()
        time.sleep(0.5)
        ball.segment[0].goto(0, 0)
        paddle.segment[0].goto(-350, 0)
        paddle.segment[1].goto(350, 0)
        ball.segment[0].setheading(ball.random_choice())

screen.exitonclick()