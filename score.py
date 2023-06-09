from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score=0
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",False,"center",("Courier",20,"normal"))
        
        
        
    def Increase_Score(self):
        self.score+=1
        self.clear()
        self.write(f"score: {self.score}",False,"center",("Courier",20,"normal"))
        
    def Game_Over(self):
        New=Turtle()
        New.color("white")
        New.write("Game Over", False,"center",("Courier",15,"normal"))