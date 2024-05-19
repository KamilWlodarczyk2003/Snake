from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score=0
        self.high_score=0
        self.ht()
        self.color("yellow")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score} High Score: {self.high_score}",False,"center",("Courier",20,"normal"))     #text displayed as scoreboard
        
        
        
    def Increase_Score(self):       #increase score
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",False,"center",("Courier",20,"normal"))
        
    def high_score_check(self):     #if actual score is bigger than high score it sets new high score
        if self.score>self.high_score:
            self.high_score=self.score
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",False,"center",("Courier",20,"normal"))
        
    def reset(self):        #reset scoreboard for a new round
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",False,"center",("Courier",20,"normal"))
        
        
    #def Game_Over(self):
        #New=Turtle()
        #New.ht()
        #New.color("white")
        #New.write("GAME OVER", False,"center",("Courier",15,"normal"))
        #print(f"score: {self.score}")