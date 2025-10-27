import turtle

turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(600, 600)

polygon = turtle.Turtle()
num_sides = 6
side_length = 100
angle = 360 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
