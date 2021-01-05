from turtle import Turtle
import random

MOVING_DISTANCE =2

heading = [30, 150, -30, -150]

class Ball:

    def __init__(self):
        self.segment = []

    def create_ball(self):
        ball_segment = Turtle("circle")
        ball_segment.color("white")
        ball_segment.penup()
        ball_segment.goto(0, 0)
        self.segment.append(ball_segment)
        self.segment[0].setheading(random.choice(heading))

    def ball_move(self):
        self.segment[0].forward(MOVING_DISTANCE)
    
    def paddle_reflect(self):
        new_heading = 180 - self.segment[0].heading()
        self.segment[0].setheading(new_heading)
    
    def wall_reflect(self):
        new_heading = -(self.segment[0].heading())
        self.segment[0].setheading(new_heading)


