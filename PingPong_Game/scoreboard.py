from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.goto(-150, 0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write(f"score : {self.score1}", align="center")

        self.score2 = 0
        self.goto(150, 0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write(f"score : {self.score2}", align="center")
    
    def paddle1_increase(self):
        self.clear()
        self.score1+=1
        self.write(f"score : {self.score1}", align="center")
        
    def paddle2_increase(self):
        self.clear()
        self.score2+=1
        self.write(f"score : {self.score2}", align="center")        

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write("GAME OVER")