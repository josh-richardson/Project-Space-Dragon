from math import ceil
from math import cos
from math import sin
from math import tan
from math import *
from random import *
from geometry import *
import noise
from vector2f import *


def interpolateGradients(gradientA,gradientB,gradientC,gradientD,distanceA,distanceD,interpolationMethod):
    valueA = gradientA.dot(distanceA)
    valueB = gradientB.dot(Vector2f(distanceD.x,distanceA.y))
    valueC = gradientC.dot(Vector2f(distanceA.x,distanceD.y))
    valueD = gradientD.dot(distanceD)

    interpolant = noise.interpolationCurveX2(distanceA,interpolationMethod)

    valueAB = noise.lerp(valueA,valueB,interpolant.x)
    valueCD = noise.lerp(valueC,valueD,interpolant.x)

    valueABCD = noise.lerp(valueAB,valueCD,interpolant.y)
    return valueABCD

def getNoise(x,y,seed,interpolationMethod):
    coordinate = Vector2f(x+seed,y+seed)
    #Interpolate between pseudorandom values at grid hypercubes, in the case of  this implementation (2-dimensional noise), squares

    #Grid square ABCD in clockwise order, A at top-left (0,0) (Default Grid-Size 1, pass co-ordinate / grid-size as argument)
    # __
    #|AB|
    #|CD|
    
    #Flooring the co-ordinate to give top-left Grid co-ordinate
    gridA = coordinate.floor()

    #Ceiling the co-ordinate to give bottom-right Grid co-ordinate
    gridD = gridA.add(Vector2f(1,1))
    
    #Generate Gradients of each grid-corner
    gradientA = noise.randomGradient(gridA.x,gridA.y)
    gradientB = noise.randomGradient(gridD.x,gridA.y)
    gradientC = noise.randomGradient(gridA.x,gridD.y)
    gradientD = noise.randomGradient(gridD.x,gridD.y)

    #Fractional displacements from point A (top-left) and D (bottom-right)
    distanceA = coordinate.diff(gridA)
    distanceD = distanceA.diff(Vector2f(1,1))

    return interpolateGradients(gradientA,gradientB,gradientC,gradientD,distanceA,distanceD,interpolationMethod)


 
