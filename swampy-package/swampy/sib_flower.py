# Flower exercise (4.2) from Week 0

# Name: Jenna Gopilan

from sib_polygon import *
bob.delay = 0.001


# This is where you put code to move bob

def start ():
    """
    Moving the turtle cursor to the starting point. 
    """
    pu (bob)
    bk (bob, 120)
    pd (bob)

def stop (radius):
    """
    Moving the turtle cursor after each flower to the next starting point based on the radius of the flower.
    """    
    pu (bob)
    fd (bob, radius + 70)
    pd (bob)   
        
def flower (petals, radius, angle):
    """
    Drawing the flower with the number of petals based on the radius and angle of the arc. The thickness of the petal is dependent on the angle.
    """
    for i in range(petals):
        arc (radius, angle)
        rt (bob, 180.0 - angle)
        arc (radius, angle)
        rt (bob, 180.0 - angle)
        lt (bob, 360.0 / petals)
    stop (radius)

# Drawing the flowers

start ()    
flower (7, 70.0, 360.0/7)

flower (10, 40.0, 80.0)

flower (20, 150.0, 360.0/20)

die (bob)

wait_for_user()

