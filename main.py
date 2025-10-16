import turtle

from turtle import right, left, forward, backward, speed



side_length = 5 #A variable, changing the variable changes the picture, variable must be between five and ten.  
circumference = side_length * 100 #Another variable, changing the variable changes the picture.

radius = circumference/(2*3.14)   
def draw_circle(number_of_sides): #A function with at least one parameter. 
    for i in range(1,number_of_sides+1): #For loop.        
        speed(100*i)
        forward(side_length)
        right(360/number_of_sides)

def draw_interior():
    forward(radius)
    left(45)
    forward(radius)
    left(180)
    forward(radius)
    for i in range(2): #Another for loop.
        left(135)
        forward(radius) 
        left(180)
        forward(radius)
    left(45)
    forward(radius)

draw_circle(100) #First call 
right(90)
draw_interior() #First call
forward(100)
left(90)
draw_circle(105)#Second call, different argument
right(90)
draw_interior()#Second call

forward(50)
right(90)
forward(100)

corner_angle = 90 #
for j in range(1,40): #Yet another for loop, changes behavior each iteration.
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