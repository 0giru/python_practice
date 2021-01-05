from turtle import Turtle

class Scoreboard:

    def __init__(self):
        self.score0 = 0
        self.score0_tut = Turtle()
        self.score0_tut.color("white")
        self.score0_tut.penup()
        self.score0_tut.goto(150, 0)
        self.score0_tut.hideturtle()
        self.score0_tut.write(f"score : {self.score0}", align="center")

        self.score1 = 0
        self.score1_tut = Turtle()
        self.score1_tut.color("white")
        self.score1_tut.penup()
        self.score1_tut.goto(-150, 0)
        self.score1_tut.hideturtle()
        self.score1_tut.write(f"score : {self.score1}", align="center")
    
    def paddle0_increase(self):
        self.score0_tut.clear()
        self.score1_tut.clear()
        self.score1+=1
        self.score0_tut.write(f"score : {self.score0}", align="center")
        self.score1_tut.write(f"score : {self.score1}", align="center")
        
    def paddle1_increase(self):
        self.score0_tut.clear()
        self.score1_tut.clear()
        self.score0+=1
        self.score0_tut.write(f"score : {self.score0}", align="center")
        self.score1_tut.write(f"score : {self.score1}", align="center")      

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("white")
    #     self.penup()
    #     self.hideturtle()
    #     self.write("GAME OVER")