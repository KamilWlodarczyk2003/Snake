from turtle import Screen
import time
from score import Score
from Snake import Snake
from food import Food
import os


Screen = Screen()
snake=Snake()
food = Food()
score=Score()

try:
    os.mkdir("C:/Users/venox/AppData/Roaming/Orzel")
except:
    pass
    
try:
    with open("C:/Users/venox/AppData/Roaming/Orzel/data.txt","x+") as high_score_file:
        high_score_file.write("0") 
except:
    pass

with open("C:/Users/venox/AppData/Roaming/Orzel/data.txt",'r+') as high_score_file:
    
    read=int(high_score_file.read())
    
    if read > 0:
        score.high_score=read
        print("Gowna")
    else:
        score.high_score=0

speed=0.1

SPEED_CHANGE=0.95

Screen.setup(width=600, height= 600)
Screen.bgcolor("black")
Screen.title("Snake")
Screen.tracer(0)


Screen.listen()

Screen.onkey(snake.down,"Down")
Screen.onkey(snake.up,"Up")
Screen.onkey(snake.right,"Right")
Screen.onkey(snake.left,"Left")
n=0

score.high_score_check()

while True:
    time.sleep(speed)
    
    snake.Multi_Move_Blocker=False
    
    snake.move()
    
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300 or snake.Colision_Check()==True:
        score.reset()
        snake.reset()
        speed=0.1
    
    
    
    if snake.head.distance(food.xcor(),food.ycor()) < 15:
        n+=1
        food.Food_Movement()
        snake.Increase()
        score.Increase_Score()
        
    
    
    Screen.update()
    if n==10:
        speed=speed*SPEED_CHANGE
        n=0
        
    with open("C:/Users/venox/AppData/Roaming/Orzel/data.txt","w") as high_score:
        high_score.write(str(score.high_score))
        
    score.high_score_check()


    
Screen.exitonclick()