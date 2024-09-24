from turtle import *
import random

screen = Screen()


class Blocks:
    def __init__(self):
        self.blocks_arr = []
        self.level = 1
        self.no_blocks = 11
        self.y = 250
        self.CreateBlocks(-225, 250, 11)
        self.CreateBlocks(-200, 225, 10)
        self.CreateBlocks(-175, 200, 9)
        self.CreateBlocks(-150, 175, 8)

        
    def CreateBlocks(self, start_x, start_y, blocks):
        color_arr = ["red", "blue", "yellow", "green", "violet", "indigo", "orange" ]
        screen.tracer(0)
        for i in range(0,blocks * 44, 44):
            turtle = Turtle()
            turtle.speed(0)
            turtle.shape('square')
            turtle.shapesize(stretch_len=2)
            turtle.penup()
            turtle.color(random.choice(color_arr))
            turtle.goto(start_x + i, start_y)
            self.blocks_arr.append(turtle)
        screen.update()
        screen.tracer(1)
        
    def Increment_Level(self):
        self.level += 1
        for i in range(0, self.level+4):
            self.y -= 25
            self.CreateBlocks(-225, self.y, 11)

