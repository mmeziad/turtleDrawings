import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
count = 3
colors = ["red", "yellow", "green", "purple", "brown", "black", "cyan", "blue"]
# tim.pensize(10)
directions = [0, 90, 180, 270]
tim.speed("fastest")
turtle.colormode(255)


# TODO: our random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup


# TODO: Spirograph
for i in range(120):
    tim.color(random_color())
    tim.circle(70)
    tim.right(3)


# # TODO: random walk
def rand_walk():
    for i in range(300):
        tim.color(random_color())
        tim.setheading(random.choice(directions))
        tim.forward(20)


rand_walk()


# TODO: draw different shapes
def shaping(count):
    for i in range(count):
        tim.forward(100)
        tim.right(360 / count)


for i in range(8):
    color_picked = random.choice(colors)
    tim.color(color_picked)
    shaping(i)

# TODO: Dashed Lines
for i in range(4):
    for j in range(20):
        if j % 2 == 0:
            tim.penup()
            tim.forward(5)
        else:
            tim.pendown()
            tim.forward(5)
    # tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
