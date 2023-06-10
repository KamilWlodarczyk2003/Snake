from turtle import Turtle
from random import randint
from Snake import Snake


class Food(Turtle):
    
    snake=Snake()
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(x=randint(-14,14)*20,y=randint(-14,14)*20)
        
    def Food_Movement(self):
        new_x=randint(-14,14)*20
        new_y=randint(-14,14)*20
        
        while self.snake.Food_Check(new_x,new_y) == True:
            new_x=randint(-14,14)*20
            new_y=randint(-14,14)*20
        self.goto(new_x,new_y)
