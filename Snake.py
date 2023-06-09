from turtle import Turtle

class Snake:
    
    segment_1=Turtle("square")
    segment_2=Turtle("square")
    segment_3=Turtle("square")
    
    def __init__(self):
        self.segment_1.penup()
        self.segment_1.color("white")
         
        self.segment_2.penup()
        self.segment_2.color("white")
        self.segment_2.goto(-20,0)

        self.segment_3.penup()
        self.segment_3.goto(-40,0)
        self.segment_3.color("white")

    segments=[segment_1,segment_2,segment_3]
    
    def move(self):
        for n in range(len(self.segments)-1,0,-1):
            self.segments[n].goto( self.segments[n-1].xcor(),  self.segments[n-1].ycor())
        self.segment_1.forward(20)
        
    def up(self):
        if self.segment_1.heading()!=270:
            self.segment_1.setheading(90)
    
    def down(self):
        if self.segment_1.heading()!=90:
            self.segment_1.setheading(270)
            
    def right(self):
        if self.segment_1.heading()!=180:
            self.segment_1.setheading(0)
            
    def left(self):
        if self.segment_1.heading()!=0:
            self.segment_1.setheading(180)