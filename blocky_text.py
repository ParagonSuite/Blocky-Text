from turtle import *
cat_shape = [(0, 30),(10, 40),(15, 30),(30, 25),(30, -10),(15, -30),(0, -25),(-15, -30),(-30, -10),(-30, 25),(-15, 30),(-10, 40),(0, 30)]
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("white")
register_shape("cat", cat_shape)
cat = Turtle()
cat.shape("cat")
cat.color("orange", "white")
cat.speed(8)
def moveforward(amount, object):
  try:
    object.fd(amount*2)
  except:
    print(f"Uh oh! Your code can't be read. Make sure you wrote it right.")

def glideto(coordinates, object):
  try:
    object.goto(coordinates)
  except ValueError as e:
    print(f"Uh oh! Your code can't be read. Make sure you wrote it right.\nHere are some solutions:\n- Check your object name\n- Check the coordinates. (They should look like this: (a, b) )")
