import turtle

loadWindow = turtle.Screen()
loadWindow.bgcolor("light green") # Set the window background color

skk = turtle.Turtle()
skk.color("blue") # Set the turtle color
skk.speed(0) # Set speed to fastest for quick drawing

for i in range(100):
    skk.circle(5 * i) # Draw circles with increasing radius
    skk.circle(-5 * i) # Draw circles in the opposite direction
    skk.left(i) # Rotate the turtle slightly each time

turtle.exitonclick() # Keep the window open until a mouse click
