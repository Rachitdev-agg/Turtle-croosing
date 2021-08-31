from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.n = 0
        self.STARTING_MOVE_DISTANCE = 5
        self.cars = []
        self.hideturtle()
    def create(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        color = random.choice(COLORS)
        new_car.color(color)
        new_car.penup()
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.cars.append(new_car)
    def move_car(self):
        for n in self.cars:
            n.forward(self.STARTING_MOVE_DISTANCE)
    def new_level(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT