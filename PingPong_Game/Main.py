from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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

    # paddle collision
    if ball.segment[0].distance(paddle.segment[0]) <= 50 and ball.segment[0].xcor() < -330:
        ball.paddle_reflect()
    elif ball.segment[0].distance(paddle.segment[0]) <= 50 and ball.segment[0].xcor() < -370:
        pass
    elif ball.segment[0].distance(paddle.segment[1]) <= 50 and ball.segment[0].xcor() > 330:
        ball.paddle_reflect()
    elif ball.segment[0].distance(paddle.segment[1]) <= 50 and ball.segment[0].xcor() > 370:
        pass

    # top_bottom wall collision
    if ball.segment[0].ycor() > 290 or ball.segment[0].ycor() < -290:
        ball.wall_reflect()

screen.exitonclick()