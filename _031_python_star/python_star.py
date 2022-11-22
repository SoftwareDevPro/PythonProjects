

import turtle

colors =  [ "green", "blue", "yellow", "red", "purple" ]
screen = turtle.Screen()

pen = turtle.Turtle()
pen.speed(0)

for idx in range(1, 225):
    pen.color(colors[idx % 5])
    pen.width(idx / 20 + 1)
    pen.fd(idx / 100 + 1)
    pen.rt(120)
    pen.fd(idx)
    pen.rt(144)
    pen.fd(idx)
    pen.rt(144)

screen.exitonclick()    

