from turtle import Turtle
import sys
import random
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.segment = []
        self.food_x = 0
        self.food_y = 0
        self.food_on = False

    def create_snake(self):
        for i in range(0, 3, 1):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")       
            new_segment.penup()
            new_segment.goto((-20)*i, 0)
            self.segment.append(new_segment)
            
    def move_snake(self):
        for seq in range(2, 0, -1):
            new_x = self.segment[seq-1].xcor()
            new_y = self.segment[seq-1].ycor()
            self.segment[seq].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def key_left(self):
        # if int(self.segment[0].heading()) == 90:
        #     self.segment[0].left(90)
        # elif int(self.segment[0].heading()) == 270:
        #     self.segment[0].right(90)
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)

    def key_right(self):
        # if int(self.segment[0].heading()) == 90:
        #     self.segment[0].right(90)
        # elif int(self.segment[0].heading()) == 270:
        #     self.segment[0].left(90)
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)

    def key_up(self):
        # if int(self.segment[0].heading()) == 0:
        #     self.segment[0].left(90)
        # elif int(self.segment[0].heading()) == 180:
        #     self.segment[0].right(90)
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)

    def key_down(self):
        # if int(self.segment[0].heading()) == 0:
        #     self.segment[0].right(90)
        # elif int(self.segment[0].heading()) == 180:
        #     self.segment[0].left(90)
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)

    def collision_wall(self):
        if self.segment[0].xcor() > 290:
            sys.exit()
        elif self.segment[0].xcor() < (-290):
            sys.exit()
        elif self.segment[0].ycor() > 290:
            sys.exit()
        elif self.segment[0].ycor() < (-290):
            sys.exit()
            
    # def collision_food(self):
    #     if (self.segment[0].xcor() <= self.food_x + 20 and
    #      self.segment[0].xcor() >= self.food_x - 20 and
    #       self.segment[0].ycor() <= self.food_y + 20 and
    #        self.segment[0].ycor() >= self.food_y - 20):

    #         self.food_on = False

    # def create_food(self):
    #     if self.food_on == False:
    #         self.food_x = int(random.randrange(-290, 290))
    #         self.food_y = int(random.randrange(-290, 290))
    #         self.food_segment.shape("square")
    #         self.food_segment.color("red")
    #         self.food_segment.penup()
    #         self.food_segment.goto(self.food_x, self.food_y)
    #         self.food_on = True
    #     else:
    #         pass

    # def plus(self):
    #     new_segment = Turtle()
    #     new_segment.shape("square")
    #     new_segment.color("white")       
    #     new_segment.penup()
    #     self.segment.append(new_segment)
