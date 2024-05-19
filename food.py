from turtle import Turtle
from random import randint
from Snake import Snake


class Food(Turtle):
    
    snake=Snake()
    
    def __init__(self):
        super().__init__()
        self.shape("circle")    #set a shape of food
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)     #scale down size of food
        self.color("blue")      #food color
        self.speed("fastest")
        self.goto(x=randint(-14,14)*20,y=randint(-14,14)*20)    #place first food in a random place
        
    def Food_Movement(self):
        new_x=randint(-14,14)*20
        new_y=randint(-14,14)*20
        
        while self.snake.Food_Check(new_x,new_y) == True:   #check if food doesn't collide with a snake, if yes it generates new random numbers
            new_x=randint(-14,14)*20
            new_y=randint(-14,14)*20
        self.goto(new_x,new_y)      #place food in generated location
        
    def Test(self):
        self.goto(0,0)