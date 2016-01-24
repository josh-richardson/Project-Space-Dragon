from math import floor
from math import ceil
from math import sqrt
""" Basic 2D vector class (rectancular only)"""
class Vector2f:
    def __init__(self,x,y):
        self.x = (x)
        self.y = (y)

    def __repr__(self):
        return ("Vector2f(%f,%f)"%(self.x,self.y))
    """ Returns the rectangular coordinates. """
    def getRect(self):
        return self.x,self.y
    def __eq__(self,other):
        return (self.x == other.x and self.y == other.y)

    def dot(self,other):
        return self.x*other.x + self.y*other.y
    def mag(self):
        mag = sqrt(self.x**2 + self.y**2)
        return mag
    def unitVector(self):
        mag = sqrt(self.x**2 + self.y**2)
        return Vector2f(self.x/mag,self.y/mag)
    def diff(self,other):
        return Vector2f(self.x-other.x,self.y-other.y)
    def add(self,other):
        return Vector2f(self.x+other.x,self.y+other.y)

    def floor(self):
        return Vector2f(int(floor(self.x)),int(floor(self.y)))
    def ceil(self):
        print self
        return Vector2f(int(ceil(self.x)),int(ceil(self.y)))
