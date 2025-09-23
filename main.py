import turtle

from turtle import right, left, forward, backward, speed


side_length = 5  
circumference = side_length * 100
radius = circumference/(3.14*2)
def draw_circle():
    for i in range(1,101):
        speed(i)
        forward(side_length)
        right(360/100)

def draw_interior(): 
    forward(radius)
    left(45)
    forward(radius)
    left(180)
    forward(radius)
    for i in range(2):
        left(135)
        forward(radius)
        left(180)
        forward(radius)
    left(45)
    forward(radius)

draw_circle()
right(90)
draw_interior()
forward(100)
left(90)
draw_circle()
right(90)
draw_interior()

forward(50)
right(90)
forward(100)

for i in range(1,40):
    speed(1)
    turtle.forward(5*i)
    turtle.right(90)
forward(100)
left(90)
forward(100)
for i in range(1,40):
    speed(1)
    forward(5*i)
    left(90)
turtle.exitonclick()