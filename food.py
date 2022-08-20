from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("pink")
        self.speed("fastest")
        randomX = random.randint(-200,200)
        randomY = random.randint(-200,200)
        self.goto(randomX, randomY)
    def refresh(self):
        randomX = random.randint(-200,200)
        randomY = random.randint(-200,200)
        self.goto(randomX, randomY)