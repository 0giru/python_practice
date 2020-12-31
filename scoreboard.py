from turtle import Turtle

class Scoreboard:

    def __init__(self):
        super().__init__()
        self.score = 0
    
    def Increase(self):
        self.score+=1