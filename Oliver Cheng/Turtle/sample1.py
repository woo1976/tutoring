import turtle

# Create a screen and a turtle object
wn = turtle.Screen()
wn.bgcolor("red") # Set the background color
wn.title("My Turtle Oliver") # Set the window title

my_turtle = turtle.Turtle()
my_turtle.pensize(10) # Make the line thicker
my_turtle.color("black") # Set the drawing color
my_turtle.speed(2) # Set the drawing speed (1 slowest, 10 fastest)

# Draw a square using a loop
for i in range(4):
    my_turtle.forward(100) # Move forward by 100 steps
    my_turtle.left(90) # Turn left by 90 degrees

# Keep the window open until the user clicks or closes it
turtle.done()
