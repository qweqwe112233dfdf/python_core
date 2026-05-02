import turtle
import random

for _ in range(36):
    turtle.color(random.random(), random.random(), random.random())

    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

    turtle.right(10)

turtle.done()