# Polygon exercise from Week 0

# Name: Jenna Gopilan

from math import pi
from TurtleWorld import * 		

world = TurtleWorld()			
bob = Turtle()


# This is where you put code to move bob
def fdrt (length, angle):
	"""
	The turtle cursor will draw a straight line, turn right, and draw another line based on the defined length and angle.
	"""
	fd (bob, length)
	rt (bob, angle)
	
def repeatDraw (sides, length, angle):
	"""
	The turtle cursor will draw a straight line, turn right, and draw another line based on the defined number of lines, length, and angle.
	"""
	for s in range (sides):
		fdrt (length, angle)

def square (length):
	"""
	The turtle cursor will draw a square.
	"""
	repeatDraw(4, length, 90)

def polygon (sides, length):
	"""
	The turtle cursor will draw a regular polygon based on the sides and length identified.
	"""
	extAngle = 360.0/sides
	repeatDraw(sides, length, extAngle)

		
def circle (radius):
	"""
	The turtle cursor will draw a circle based on a regular polygon based on the radius identified.
	"""
	circumference = 2 * pi * radius
	sides = int(circumference / 3) + 1
	length = circumference/sides
	polygon (sides, length)	

def arc (radius, theta):
	"""
	The turtle cursor will draw an arc of a circle based on the radius and theta identified.
	"""
	arcLength = (2 * pi * radius * theta)/360
	sides = int(arcLength / 3) + 1
	turtleLength = arcLength / sides
	turtleAngle = float(theta) / sides
	repeatDraw (sides, turtleLength, turtleAngle)
	


if __name__ == '__main__':
	bob.delay = 0.0001
	arc (60, 60)
	rt(bob)
#	rt(bob)
	arc (60, 60)
	rt(bob)
#	rt(bob)
	arc (60, 60)
	
	wait_for_user()				
	