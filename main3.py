import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle named "square_turtle"
square_turtle = turtle.Turtle()
square_turtle.speed(1)

# Function to draw a square
def draw_square():
    for _ in range(4):
        square_turtle.forward(100)
        square_turtle.right(90)

# Draw squares repeatedly
while True:
    draw_square()
    square_turtle.right(10)  # Rotate slightly before drawing the next square

# Close the window when clicked
wn.mainloop()