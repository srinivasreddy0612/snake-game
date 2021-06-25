from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.f = open("hs.txt", "r")
        self.high_score = int(self.f.read())
        self.f.close()
        self.score = 0
        self.color("orange")
        self.penup()
        self.goto(0, 267)
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(f"score: {self.score}  high score {self.high_score}", align="center", font=("Arial", 24, "normal"))
        self.score += 1

    def reset(self):
        if self.score - 1 > self.high_score:
            self.high_score = self.score-1
            self.f = open("hs.txt", "w")
            self.f.write(f"{self.high_score}")
            self.f.close()
        self.score = 0
        self.updatescore()
        
    def gameover(self):
        #self.clear()
        #self.goto(0, 0)
        #self.write(f" GAME OVER 😩  ", align="center", font=("Arial", 24, "normal"))
        #self.goto(0, -50)
        #self.write(f"score: {self.score -1}  ", align="center", font=("Arial", 24, "normal"))
        time.sleep(1)
