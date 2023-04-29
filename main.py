from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
user_guess = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")
screen.setup(width=500, height=400)
all_turtles = []


def create_turtle(num_turtles, y):
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "brown", "pink", "grey", "chartreuse"]
    for i in range(num_turtles):
        x = -230
        y = y + 30
        turtles = Turtle(shape="turtle")
        turtles.penup()
        turtles.color(colors[i])
        turtles.goto(x, y)
        all_turtles.append(turtles)


create_turtle(6, -100)


if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            if user_guess == turtle.pencolor():
                print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner!")
            is_race_on = False

screen.exitonclick()

