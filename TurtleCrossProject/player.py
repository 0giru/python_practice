from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player:
    def __init__(self):
        self.player = Turtle()
        self.player.color("black")
        self.player.shape("turtle")
        self.player._rotate(90)
        self.player.penup()
        self.player.goto(STARTING_POSITION)

    def move(self):
        self.player.forward(MOVE_DISTANCE)
