from turtle import Turtle

class Paddle:

    def __init__(self):
        self.segment = []

    def create_paddle(self, position):
        new_paddle = Turtle("square")
        new_paddle.penup()
        new_paddle.color("white")
        new_paddle.shapesize(5, 1)
        new_paddle.goto(position, 0)
        self.segment.append(new_paddle)

    def go_up1(self):
        x = self.segment[0].xcor()
        new_y = self.segment[0].ycor() + 20
        self.segment[0].goto(x, new_y)
        
    def go_down1(self):
        x = self.segment[0].xcor()
        new_y = self.segment[0].ycor() - 20
        self.segment[0].goto(x, new_y)

    def go_up2(self):
        x = self.segment[1].xcor()
        new_y = self.segment[1].ycor() + 20
        self.segment[1].goto(x, new_y)
        
    def go_down2(self):
        x = self.segment[1].xcor()
        new_y = self.segment[1].ycor() - 20
        self.segment[1].goto(x, new_y)