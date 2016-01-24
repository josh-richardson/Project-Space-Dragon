from vector2f import *
from math import sqrt
#returns sqrt of square sum
def getHype(*n):
    sqsum = 0
    for e in n:
        sqsum += e**2
    return  sqrt(sqsum)

def sqSum(*values):
    total = 0
    for x in values:
        total +=  x**2
    return total

""" Calculates and returns the euclidian distance between two input vectors. """
def getEuclidianDist(vectora=Vector2f(0,0),vectorb=Vector2f(0,0)):
    return getHype(vectora.x-vectorb.x, vectora.y-vectorb.y)

""" Calculates and returns the manhatten distance between two input vectors. """
def getManhattenDist(x1=0,y1=0,x2=0,y2=0):
    return (abs(x1-x2)) + (abs(y1-y2))
def getSquaredDistance(vectora,vectorb):
    xdist = vectora.x - vectorb.x
    ydist = vectora.y - vectorb.y
    return xdist**2 + ydist**2
