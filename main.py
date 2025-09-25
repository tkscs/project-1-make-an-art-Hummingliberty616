import turtle

from turtle import right, left, forward, backward, speed


side_length = 5  
def draw_circle(number_of_sides):
    for i in range(1,number_of_sides+1):
        circumference = side_length * number_of_sides
        radius = circumference/(3.14*2)
        speed(i)
        forward(side_length)
        right(360/number_of_sides)

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

draw_circle(100)
right(90)
draw_interior()
forward(100)
left(90)
draw_circle(101)
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