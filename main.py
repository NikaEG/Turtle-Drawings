import turtle
s = turtle.Screen()
s.bgcolor("black")
t = turtle.Turtle()
t.color("red") 
t.speed(0) 
t.pensize(2)

def square(size):
	for i in range(4):
		t.fd(size)
		t.rt(90)
square(50)

def triangle(size):
	for i in range(3):
		t.fd(size)
		t.lt(120)
triangle(50)

def house(size):
    square(size)
    triangle(size)
house(50)

for i in range(5):
  t.penup()
  t.forward(100)
  t.pendown()
  house(50)

def square(size)
  while size > 0
  square(size)
  t.penup
  t.rt(45)
  t.fd(10/math.sqrt(2))
  t.lt(45)
  t.rt(5)
  t.pendown
  size -= 20