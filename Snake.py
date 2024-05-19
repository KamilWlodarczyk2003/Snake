from turtle import Turtle

class Snake:
    
    Multi_Move_Blocker=False
    
    
    head=Turtle("square")      #first segmant of snake
    segment_2=Turtle("square")      #2nd segmant of snake
    segment_3=Turtle("square")      #3rd segmant of snake
    segments=[head,segment_2,segment_3]
    
    def __init__(self):     #set positions of segments and set a number of them
        self.head.penup()
        self.head.color("white")
         
        self.segment_2.penup()
        self.segment_2.color("white")
        self.segment_2.goto(-20,0)

        self.segment_3.penup()
        self.segment_3.goto(-40,0)
        self.segment_3.color("white")
        
        self.number_of_segments=2
        
    
    
    def move(self):     #move first segment one block forward and every other segments go to position of previous one
        for n in range(len(self.segments)-1,0,-1):
            self.segments[n].goto( self.segments[n-1].xcor(),  self.segments[n-1].ycor())
        self.head.forward(20)
        
    def up(self):       #set direction up
        if self.head.heading()!=270 and self.Multi_Move_Blocker == False:
            self.head.setheading(90)
            self.Multi_Move_Blocker = True
    
    def down(self):     #set direction down
        if self.head.heading()!=90 and self.Multi_Move_Blocker == False:
            self.head.setheading(270)
            self.Multi_Move_Blocker = True
            
    def right(self):        #set direction right
        if self.head.heading()!=180 and self.Multi_Move_Blocker == False:
            self.head.setheading(0)
            self.Multi_Move_Blocker = True
            
    def left(self):         #set direction left
        if self.head.heading()!=0 and self.Multi_Move_Blocker == False:
            self.head.setheading(180)
            self.Multi_Move_Blocker = True
    
    def Increase(self):     #add new segment to the and of a snake
        New_Turtle = Turtle("square")
        New_Turtle.penup()
        New_Turtle.color("white")
        New_Turtle.goto(self.segments[self.number_of_segments].xcor(),self.segments[self.number_of_segments].ycor())
        self.number_of_segments+=1
        self.segments.append(New_Turtle)
        
    def Colision_Check(self):       #check if snake hit itself
        for n in range(1,len(self.segments)):
            if round(self.head.xcor())==round(self.segments[n].xcor()) and round(self.head.ycor())==round(self.segments[n].ycor()):
                return True
            
    def Food_Check(self,x,y):       #check if snake ate food
        for n in range(0,len(self.segments)):
            if self.segments[n].distance(x,y)<15:
                return True
            
    def reset(self):        #set snake for a new round
        self.head.goto(0,0)
        self.head.setheading(0)
         
        self.segment_2.goto(-20,0)

        self.segment_3.goto(-40,0)
        
        self.number_of_segments=2
        
        for n in range(2,len(self.segments)):
            self.segments[n].goto(1000,1000)
        
        self.segments.clear()
        self.segments=[self.head,self.segment_2,self.segment_3]