from turtle import Screen, Turtle
import time

Screen = Screen()

Screen.setup(width=600, height= 600)
Screen.bgcolor("black")
Screen.title("Snake")
Screen.tracer(0)

segment_1=Turtle("square")
segment_1.penup()
segment_1.color("white")

segment_2=Turtle("square")
segment_2.penup()
segment_2.color("white")
segment_2.goto(-20,0)

segment_3=Turtle("square")
segment_3.penup()
segment_3.goto(-40,0)
segment_3.color("white")

segments=[segment_1,segment_2,segment_3]

game_is_on=True

while game_is_on == True:
    Screen.update()
    time.sleep(0.2)
    
    for n in range(len(segments)-1,0,-1):
        segments[n].goto( segments[n-1].xcor(),  segments[n-1].ycor())
    segment_1.forward(20)
    
    






Screen.exitonclick()