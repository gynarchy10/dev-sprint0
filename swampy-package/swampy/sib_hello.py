# Hello exercise from Week 0

# Name: Jenna Gopilan


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()	
bob.delay = 0.03			


# This is where you put code to move bob

"""
d = down
l = left
r = right
u = up
Rules:
1. For each letter there will be 6 points of intersection as shown below:
*  *
*  *
*  *
2. The cursor will use these as reference points
3. The cursor will always start facing towards the right and end facing towards the right
4. Moving the cursor from one point to the next is considered as one movement (u, d, l, r)
"""
step = 30

def start():
	"""
	Places the cursor at the starting point.
	"""
	pu (bob)
	bk (bob, step * 5)
	pd (bob)

def down():
	"""
	Moves the cursor two points down and draws a line.
	"""
	rt (bob)
	fd (bob, 2 * step)
	lt (bob)

	
def across():
	"""
	Moves the cursor across or one point towards the right and draws a line.
	"""
	fd (bob, step)

def space():
	"""
	Moves the cursor to the starting point of the next letter.
	"""
	pu (bob)
	fd (bob, step / 3)
	lt (bob)
	fd (bob, step * 2)
	rt (bob)
	pd (bob)
	
def d():
	"""
	Moves the cursor one point down.
	"""
	pu (bob)
	rt (bob)
	fd (bob, step)
	lt (bob)
	pd (bob)
	
def dd():
	"""
	Moves the cursor two points down.
	"""
	pu (bob)
	rt (bob)
	fd (bob, step * 2)
	lt (bob)
	pd (bob)
	
def u():
	"""
	Moves the cursor one point up.
	"""
	pu (bob)
	rt (bob)
	bk (bob, step)
	lt (bob)
	pd (bob)		
	
def uu():
	"""
	Moves the cursor two points up.
	"""
	pu (bob)
	rt (bob)
	bk (bob, step * 2)
	lt (bob)
	pd (bob)
	
def ruu():
	"""
	Moves the cursor two points up and one point to the right.
	"""
	pu (bob)
	fd (bob, step)
	lt (bob)
	fd (bob, step * 2)
	rt (bob)
	pd (bob)
	
def dl():
	"""
	Moves the cursor one point down and to the left.
	"""
	pu (bob)
	bk (bob, step)
	rt (bob)
	fd (bob, step)
	lt (bob)
	pd (bob)

def l():
	"""
	Moves the cursor one point to the left.
	"""
	pu (bob)
	bk (bob, step)
	pd (bob)

def H():
	down()
	u()
	across()
	u()
	down()
	space()

def E():
	down()
	uu()
	across()
	dl()
	across()
	dl()
	across()
	space()
	
def L():
	down()
	across()
	space()

def O():
	down()
	uu()
	across()
	l()
	dd()
	across()
	uu()
	down()
	space()
		
start()
H()
E()
L()
L()
O()


wait_for_user()					
