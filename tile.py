from turtle import *

class Tile(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=0.5)
        self.goto(0, -250)
        self.Move_Left()
        self.Move_Right()
    
    def Move_Left(self):
        self.x = self.xcor() - 30
        self.goto(self.x, self.ycor())


    def Move_Right(self):
        self.x = self.xcor() + 30
        self.goto(self.x, self.ycor())
        
    