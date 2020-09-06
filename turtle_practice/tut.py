import turtle
screen= turtle.Screen()
screen.bgcolor('red')
pen = turtle.Pen()
pen.color('white')

for i in range(35):
    pen.heading()
    pen.forward(50)


# pen.circle(50)

turtle.exitonclick() 