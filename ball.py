from turtle import *
import time


SPEED = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed(SPEED)
        self.x_move = 10
        self.y_move = 10
    
    
    def move(self):
        self.new_x = self.xcor() + self.x_move
        self.new_y = self.ycor() + self.y_move
        self.goto(self.new_x,self.new_y)
        
    
    def bounce_x(self):
        self.x_move *= -1
        
    
    def bounce_y(self):
        self.y_move *= -1
        
    
    def outgo(self):
        time.sleep(2)
        self.hideturtle()
        self.goto(0,0)
        self.y_move *= -1
        self.showturtle()
    