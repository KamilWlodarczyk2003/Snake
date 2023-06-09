from turtle import Turtle

class Snake:
    
    head=Turtle("square")
    segment_2=Turtle("square")
    segment_3=Turtle("square")
    
    def __init__(self):
        self.head.penup()
        self.head.color("white")
         
        self.segment_2.penup()
        self.segment_2.color("white")
        self.segment_2.goto(-20,0)

        self.segment_3.penup()
        self.segment_3.goto(-40,0)
        self.segment_3.color("white")
        
        self.number_of_segments=2
        self.segments=[self.head,self.segment_2,self.segment_3]
    
    
    def move(self):
        for n in range(len(self.segments)-1,0,-1):
            self.segments[n].goto( self.segments[n-1].xcor(),  self.segments[n-1].ycor())
        self.head.forward(20)
        
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
            
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
            
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    
    def Increase(self):
        New_Turtle = Turtle("square")
        New_Turtle.penup()
        New_Turtle.color("white")
        New_Turtle.goto(self.segments[self.number_of_segments].xcor(),self.segments[self.number_of_segments].ycor())
        self.number_of_segments+=1
        self.segments.append(New_Turtle)
        
    def Colision_Check(self):
        for segment in self.segments:
            if segment == self.head:
                pass
            elif self.head.xcor()==segment.xcor() and self.head.ycor()==segment.ycor():
                return True