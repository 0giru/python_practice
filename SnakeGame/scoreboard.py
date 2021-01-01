from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write(f"score : {self.score}", align="center")
    
    def Increase(self):
        self.clear()
        self.score+=1
        self.write(f"score : {self.score}", align="center")

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write("GAME OVER")