from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 200)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score} {self.r_score}", align="center", font=("Courier", 70, "normal"))

    def increase_score1(self):
        self.r_score+=1
        self.update_scoreboard()

    def increase_score2(self):
        self.l_score+=1
        self.update_scoreboard()
