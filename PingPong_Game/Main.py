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
paddle.create_paddle(350)
# index 1 paddle on the left
paddle.create_paddle(-350)
ball.create_ball()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My PingPong Game")
screen.listen()

screen.onkey(paddle.go_up1, "Up")
screen.onkey(paddle.go_down1, "Down")
screen.onkey(paddle.go_up2, "w")
screen.onkey(paddle.go_down2, "s")

screen.tracer(0)

Game_On = True

while Game_On:
    time.sleep(0.01)
    screen.update()
    ball.ball_move()

    # paddle collision
    if ball.segment[0].distance(paddle.segment[0]) < 10:
        ball.ball_reflect()

    if ball.segment[0].distance(paddle.segment[1]) < 10:
        ball.ball_reflect()

    # # wall collision
    # if(ball.ball_segment.ycor() > 290 or ball.ball_segment.ycor() < -290):
    #     ball.wall_collision()

    # if(ball.ball_reflex()):
    #     scoreboard.paddle1_increase()
    #     Game_On = False

    # if(ball.ball_segment.xcor() > 295):
    #     scoreboard.paddle1_increase()
    #     Game_On = False
    #     scoreboard.game_over()
    # elif(ball.ball_segment.xcor() < -295):
    #     scoreboard.paddle2_increase()
    #     Game_On = False
    #     scoreboard.game_over()

screen.exitonclick()