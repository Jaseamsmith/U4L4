
from turtle import *

charlie = Turtle()

charlie.color("green")
charlie.pensize(5)
charlie.speed(5)
charlie.shape("turtle")

for x in range(4):
	charlie.forward(100)
	charlie.left(90)

mainloop()