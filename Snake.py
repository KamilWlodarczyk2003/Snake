from turtle import Turtle

class Snake:
    
    Multi_Move_Blocker=False
    
    head=Turtle("square")
    segment_2=Turtle("square")
    segment_3=Turtle("square")
    
    def __init__(self):
        self.lost=False
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
        if self.Colision_Check()==True:
            self.lost=True
        elif self.head.heading()!=270 and self.Multi_Move_Blocker == False:
            self.head.setheading(90)
            self.Multi_Move_Blocker = True
    
    def down(self):
        if self.Colision_Check()==True:
            self.lost=True
        if self.head.heading()!=90 and self.Multi_Move_Blocker == False:
            self.head.setheading(270)
            self.Multi_Move_Blocker = True
            
    def right(self):
        if self.Colision_Check()==True:
            self.lost=True
        if self.head.heading()!=180 and self.Multi_Move_Blocker == False:
            self.head.setheading(0)
            self.Multi_Move_Blocker = True
            
    def left(self):
        if self.Colision_Check()==True:
            self.lost=True
        if self.head.heading()!=0 and self.Multi_Move_Blocker == False:
            self.head.setheading(180)
            self.Multi_Move_Blocker = True
    
    def Increase(self):
        New_Turtle = Turtle("square")
        New_Turtle.penup()
        New_Turtle.color("white")
        New_Turtle.goto(self.segments[self.number_of_segments].xcor(),self.segments[self.number_of_segments].ycor())
        self.number_of_segments+=1
        self.segments.append(New_Turtle)
        
    def Colision_Check(self):
        for n in range(1,len(self.segments)):
            if self.head.xcor()==self.segments[n].xcor() and self.head.ycor()==self.segments[n].ycor():
                return True