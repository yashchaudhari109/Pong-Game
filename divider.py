from turtle import Turtle

class Divider(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.right(90)
        self.pendown()
        self.width(4)
        self.forward(550)
        self.hideturtle()
