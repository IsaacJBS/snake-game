import random
from turtle import Turtle

class Maca(Turtle):
    def __init__(self):
        super(Maca, self).__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.nova_maca()

    def nova_maca(self):
        x, y = random.randint(-280, 280), random.randint(-280, 280)
        self.goto(x, y)
