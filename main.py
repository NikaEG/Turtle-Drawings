import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.color("#00ff22")
t.speed(0)
t.penup
t.goto(-50, 60)
def square(size):
  for i in range(4):
    t.fd(size)
   t.rt(90)
square(50)
