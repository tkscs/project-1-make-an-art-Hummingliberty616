import turtle

from turtle import right, left, forward, backward, speed


side_length = 5 #
circumference = side_length * 100
radius = circumference/(2*3.14)   
def draw_circle(number_of_sides): 
    for i in range(1,number_of_sides+1):        
        speed(100*i)
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
draw_circle(105)
right(90)
draw_interior()

forward(50)
right(90)
forward(100)


corner_angle = 90 #
for j in range(1,40):
    speed(10)
    turtle.forward(5*j)
    turtle.right(corner_angle)
forward(100)
left(corner_angle)
forward(100)
for k in range(1,40):
    speed(10)
    forward(5*k)
    left(corner_angle)
turtle.exitonclick()