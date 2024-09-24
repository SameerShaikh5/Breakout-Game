from turtle import *
from blocks import Blocks
from tile import Tile
from ball import Ball
from score_life import Score, Life
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")


blocks = Blocks()
tile = Tile()
ball = Ball()

#Score and lifeline
score = Score()
life = Life()


screen.listen()
screen.onkey(tile.Move_Left, "Left")
screen.onkey(tile.Move_Right, "Right")


is_game_on = True
while is_game_on:
    ball.move()
    
    #Increase Level
    if len(blocks.blocks_arr) == 0:
        blocks.Increment_Level()
        ball.goto(0,0)
        life.Increment_Life()
        screen.tracer(1)
        screen.update()
        time.sleep(2)
        
        
    
    # sidewalls collision
    if ball.xcor() >= 290 or ball.xcor() <= -290:
        ball.bounce_x()
    
    #upperwall collision
    if ball.ycor() >= 290:
        ball.bounce_y()
    
    #tile collision
    if tile.distance(ball) <=25:
        ball.bounce_y()
    
    # ball hitting blocks
    for i in blocks.blocks_arr:
        if ball.distance(i) <= 25:
            ball.bounce_y()
            i.speed(0)
            i.goto(1000, 1000)
            blocks.blocks_arr.remove(i)
            score.Increment_Score()
            

    #outgo bottom
    if ball.ycor() <= -270:
        ball.outgo()
        life.Decrement_Life()
        if life.life == 0:
            is_game_on = False
            life.GameOver()
        
            
    
    screen.update()

     
    
    
    
    
    



screen.exitonclick()


