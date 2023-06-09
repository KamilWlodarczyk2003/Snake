from turtle import Screen
import time
from Snake import Snake
from food import Food

Screen = Screen()
Food = Food()

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
    Screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.segment_1.distance(Food.xcor(),Food.ycor()) < 15:
        Food.Food_Movement()
    
    
    
    
    
Screen.exitonclick()