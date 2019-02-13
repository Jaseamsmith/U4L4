from turtle import *

screen = Screen()
screen.bgcolor("red")

charlie = Turtle()

charlie.color("yellow")
charlie.pensize(2)
charlie.speed(0)
charlie.shape("turtle")

for x in range(10):
	charlie.forward(15)
	charlie.left(10)
	charlie.backward(15)
	charlie.left(10)

mainloop()
