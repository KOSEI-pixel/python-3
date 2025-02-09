import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
num_sides=10
len_sides=200
angle=360/num_sides
for i in range(num_sides):
    polygon.forward(len_sides)
    polygon.right(angle)
turtle.done()