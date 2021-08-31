import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.n += 1
    if car.n % 4 == 0:
        car.create()
    car.move_car()
    if player.ycor() > 280:
        player.next_level()
        car.new_level()
        scoreboard.update_score()
    for m in car.cars:
        if player.distance(m) < 25:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()