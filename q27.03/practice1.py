import turtle

turtle.color("red")
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.penup()
turtle.forward(150)
turtle.pendown()

turtle.color("green")
for _ in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.penup()
turtle.forward(150)
turtle.pendown()

turtle.pencolor("blue")
for _ in range(5):
    turtle.forward(100)
    turtle.right(72)

turtle.done()