from turtle import *
screen = Screen()

class Score:
    def __init__(self):
        self.score = 0
        screen.tracer(1)
        self.Current_Score()
        screen.update()
        
    def Current_Score(self):
        self.Score_text = Turtle()
        self.Score_text.penup()
        self.Score_text.goto(-50,269)
        self.Score_text.hideturtle()
        self.Score_text.color("white")
        self.Score_text.write("Score: ", font=("Arial", 16, "normal"))
        self.Score_count = Turtle()
        self.Score_count.penup()
        self.Score_count.goto(15,268)
        self.Score_count.hideturtle()
        self.Score_count.color("white")
        self.Score_count.write(f"{self.score}", font=("Arial", 16, "normal"))
        
    def Increment_Score(self):
        self.Score_count.clear()
        self.score += 1
        self.Score_count.write(f"{self.score}", font=("Arial", 16, "normal"))
        
        
class Life:
    def __init__(self):
        screen.tracer(1)
        self.life = 3
        self.Life = Turtle()
        self.Life.hideturtle()
        self.Life.penup()
        self.Life.goto(-279,-280)
        self.Life.color("white")
        self.Life.write(f"Life: {self.life}", font=("Arial", 16, "normal"))
        screen.update()
        
    def Decrement_Life(self):
        self.life -= 1
        self.Life.clear()
        self.Life.write(f"Life: {self.life}", font=("Arial", 16, "normal"))
        
    def Increment_Life(self):
        if self.life <= 5:
            self.life += 2
            self.Life.clear()
            self.Life.write(f"Life: {self.life}", font=("Arial", 16, "normal"))
        
    def GameOver(self):
        screen.tracer(0)
        gameover_text = Turtle()
        gameover_text.hideturtle()
        gameover_text.color("red")
        gameover_text.penup()
        gameover_text.goto(-110, 20)
        gameover_text.write("Game Over", font=("Jaini Purva", 30, "bold"))
        screen.update()
        