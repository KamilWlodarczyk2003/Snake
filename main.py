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

path = os.getenv('APPDATA')
print(path)

print(f"{path}/Orzel")

try:
    os.mkdir(f"{path}/Orzel")   #try to make a dir to save highscore
except:
    pass
    
try:
    with open(f"{path}/Orzel/data.txt","x+") as high_score_file:        #if file doesn't exist it creates new and place 0 in it
        high_score_file.write("0") 
except:
    pass

with open(f"{path}/Orzel/data.txt",'r+') as high_score_file:        #import a highscore from a file to the program
    
    read=int(high_score_file.read())
    
    if read > 0:
        score.high_score=read
    else:
        score.high_score=0

speed=0.1

SPEED_CHANGE=0.95

Screen.setup(width=600, height= 600)
Screen.bgcolor("black")
Screen.title("Snake")
Screen.tracer(0)


Screen.listen()

#arrow keys interaction
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
    
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300 or snake.Colision_Check()==True:      #check if snake hit a wall or itself
        score.reset()
        snake.reset()
        speed=0.1
    
    
    
    if snake.head.distance(food.xcor(),food.ycor()) < 15:       #eat a food if snake is close enough
        n+=1
        food.Food_Movement()
        snake.Increase()
        score.Increase_Score()
        
    
    
    Screen.update()
    if n==10:       #every 10 score it increase a speed by SPEED_CHANGE value
        speed=speed*SPEED_CHANGE
        n=0
        
    with open(f"{path}/Orzel/data.txt","w") as high_score:      #update high score in the file
        high_score.write(str(score.high_score))
        
    score.high_score_check()
