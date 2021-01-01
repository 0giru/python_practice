from turtle import Turtle
from scoreboard import Scoreboard
import sys
import random
MOVE_DISTANCE = 20
SIZE_WIDTH = 900
SIZE_HEIGHT = 900

# color = ["red", "green", "yellow", "orange", "blue"]

class Snake:
    
    def __init__(self):
        self.segment = []
        self.food_x = 0
        self.food_y = 0
        self.food_on = False
        self.size_width = SIZE_WIDTH
        self.size_height = SIZE_HEIGHT

    def create_snake(self):
        for i in range(0, 3, 1):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")       
            new_segment.penup()
            new_segment.goto((-20)*i, 0)
            self.segment.append(new_segment)

    #Add Segment
    def add_segment(self):
        newnew_segment = Turtle()
        newnew_segment.shape("square")
        # choice = random.choice(color)
        newnew_segment.color("white")       
        newnew_segment.penup()
        newnew_segment.goto(self.segment[-1].position())
        self.segment.append(newnew_segment)

    def move_snake(self):
        for seq in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seq-1].xcor()
            new_y = self.segment[seq-1].ycor()
            self.segment[seq].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def key_left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)

    def key_right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)

    def key_up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)

    def key_down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)

    #Coliision Detect
    def collision_wall(self):
        if self.segment[0].xcor() > (SIZE_WIDTH/2 - 10):
            return True
        elif self.segment[0].xcor() < -(SIZE_WIDTH/2 - 10):
            return True
        elif self.segment[0].ycor() > (SIZE_WIDTH/2 - 10):
            return True
        elif self.segment[0].ycor() < -(SIZE_WIDTH/2 - 10):
            return True
        else:
            return False

    def collision_tail(self):
        for i in self.segment[1:]:
            if self.segment[0].distance(i) < 10:
                return True
                
    
