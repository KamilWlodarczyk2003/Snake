from turtle import Screen
import time
from Snake import Snake
from food import Food
from score import Score

Screen = Screen()
food = Food()
score=Score()

speed=0.1
SPEED_CHANGE=0.95

Screen.setup(width=600, height= 600)
Screen.bgcolor("black")
Screen.title("Snake")
Screen.tracer(0)

snake=Snake()
Screen.listen()

Screen.onkey(snake.down,"Down")
Screen.onkey(snake.up,"Up")
Screen.onkey(snake.right,"Right")
Screen.onkey(snake.left,"Left")

game_is_on=True
n=0

while game_is_on == True:
    time.sleep(speed)
    
    
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300 or snake.Colision_Check()==True:
        score.Game_Over()
        game_is_on=False
    
    snake.Multi_Move_Blocker=False
    
    snake.move()
    
    if snake.head.distance(food.xcor(),food.ycor()) < 15:
        n+=1
        food.Food_Movement()
        score.Increase_Score()
        snake.Increase()
        
    
    
    Screen.update()
    if n==10:
        speed=speed*SPEED_CHANGE
        n=0
    
    
Screen.exitonclick()