from turtle import Screen
import time
from Snake import Snake

Screen = Screen()

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
    
    
    
    
    
Screen.exitonclick()