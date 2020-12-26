from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.move_snake()

    def create_snake(self):
        for i in range(0, 2, 1):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")       
            new_segment.penup()
            new_segment.setpos(i*(-20), 0)
            self.segment.append(new_segment)

    def move_snake(self):
        self.segment[0].forward(MOVE_DISTANCE)
        for list_num in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[list_num - 1].xcor()
            new_y = self.segment[list_num - 1].ycor()
            self.segment[list_num].goto(new_x, new_y)