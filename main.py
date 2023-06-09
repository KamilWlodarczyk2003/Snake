from turtle import Screen
import time
from Snake import Snake
from food import Food
from score import Score

Screen = Screen()
Food = Food()
score=Score()

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

while game_is_on == True:
    
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300 or snake.Colision_Check()==True:
        score.Game_Over()
        game_is_on=False
    
    snake.Multi_Move_Blocker=False
    time.sleep(0.1)

    if snake.head.distance(Food.xcor(),Food.ycor()) < 15:
        Food.Food_Movement()
        score.Increase_Score()
        snake.Increase()
    
    snake.move()
    Screen.update()
    
    
Screen.exitonclick()