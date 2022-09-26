from ctypes import alignment
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",14,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0    
        self.update_scoreboard ()   

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()