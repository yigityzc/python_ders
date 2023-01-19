# Assume that the object is a turtle
import turtle
import random

# Set the screen size
turtle.setup(800, 600)

# Set the turtle's starting position
turtle.setpos(random.randint(-400, 400), random.randint(-300, 300))

# Move the turtle in a random direction
turtle.forward(random.randint(1, 100))
turtle.left(random.randint(1, 360))

# Repeat the process until the turtle hits the edge of the screen
while True:
  x, y = turtle.pos()
  if abs(x) > 400 or abs(y) > 300:
    break
  turtle.forward(random.randint(1, 100))
  turtle.left(random.randint(1, 360))

turtle.done()
