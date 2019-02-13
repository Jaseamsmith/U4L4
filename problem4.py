from turtle import *

charlie = Turtle()
nana = Turtle()

charlie.color("blue")
charlie.pensize(5)
charlie.speed(5)
charlie.shape("turtle")

nana.color("green")
nana.pensize(5)
nana.speed(5)
nana.shape("turtle")

for x in range(1):
	charlie.circle(100)

for y in range(3):
	nana.forward(100)
	nana.left(120)

mainloop()
