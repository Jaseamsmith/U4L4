from turtle import *

charlie = Turtle()

charlie.color("orange")
charlie.pensize(5)
charlie.speed(5)
charlie.shape("turtle")

for x in range(1):
	charlie.forward(80)
	charlie.left(50)
	charlie.forward(200)
	charlie.right(150)
	charlie.forward(50)
	charlie.circle(25)
	charlie.backward(300)

mainloop()