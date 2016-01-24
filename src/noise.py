from vector2f import *
from geometry import sqSum
from math import pi
from math import floor
from math import ceil
from math import cos
from math import sin
from math import tan
import random
from geometry import *
import perlin

def randomGradient(x,y,seed=0):
    x = (x+seed)
    y = (y+seed)
    xy = (x,y)
    hashval = hash(xy)
    random.seed(hashval)
    angle = random.random() * 2 * pi
    return Vector2f(cos(angle),sin(angle))

def lerp(a,b,t):
    return a*(1-t) + b*t

def interpolationCurve(t,interpolationMethod):
    if interpolationMethod == "HERMITE":
        return t * t * t *(t * (t * 6 - 15) + 10)
    if interpolationMethod == "COSINE":
        return (1.0 - cos(pi*t))/2.0
    if interpolationMethod == "LINEAR":
        return t
    if interpolationMethod == "NEAREST-NEIGHBOUR":
        return int(t)
    
def interpolationCurveX2(t,interpolationMethod):
    
    if interpolationMethod == "HERMITE":
        x = 6*(t.x**5) - 15*(t.x**4) + 10*(t.x**3)
        y = 6*(t.y**5) - 15*(t.y**4) + 10*(t.y**3)
        return Vector2f(x,y)
    if interpolationMethod == "COSINE":
        x = (1.0 - cos(pi*t.x))/2.0
        y = (1.0 - cos(pi*t.y))/2.0
        return Vector2f(x,y)
    if interpolationMethod == "LINEAR":
        return Vector2f(t.x,t.y)
    if interpolationMethod == "NEAREST-NEIGHBOUR":
        return Vector2f(int(t.x),int(t.y))

def intNoise2D(x,y,seed):
    x,y = int(x+seed),int(y+seed)
    s = (x*7793 + y)%65203
    #s = (s >> 17)^s
    #num = (s * (s * s * 49831 + 15490919) + 553110211) & 0x7fffffff
    #return 1-((num/1057438801.0))
    random.seed(s)
    return random.random()   
    

"""Generates a set of inpuot length random , between input height and input width
def getSectorDistributedPoints(pointResolution=512,sectors = 1,width=800,height=600,seed=0):
    ranges = []
    points = []

    for sector in xrange(sectors+1):
        ranges.append(sector/float(sectors))
    sectorres = pointResolution // (sectors**2)
    sectorposx = [int(x*width) for x in ranges]
    sectorposy = [int(y*height) for y in ranges]
    sectorrangex = []
    sectorrangey = []

    for i,x in enumerate(sectorposx):
        if i == len(sectorposx) - 1 :
            break
        sectorrangex.append((x,sectorposx[i+1]))
    for i,y in enumerate(sectorposy):
        if i==len(sectorposy) - 1:
            break
        sectorrangey.append((y,sectorposy[i+1]))
    random.seed()
    for x in sectorrangex:
        for y in sectorrangey:
            for i in xrange(sectorres):
                
                pointx = random.randrange(x[0],x[1])
                pointy = random.randrange(y[0],y[1])
                points.append(Vector2f(pointx,pointy))
    return points
"""      
        

def getRandomPoints(pointResolution,maxwidth,maxheight,seed):
    points = []
    random.seed(seed)
    for point in xrange(pointResolution):
        x = int(random.random() * maxwidth)
        y = int(random.random() * maxheight)
        points.append(Vector2f(x,y))
    return points

def getRandomPoint(x0=0.0,x1=1.0,y0=0.0,y1=1.0):
    dx = x1-x0
    dy = y1-y0
    x = x0 + random.random()*dx
    y = y0 + random.random()*dy
    return Vector2f(x,y)

def fractionalBrownianMotion(width,height,interpolationMethod,seed,startfrequency,lacunarity,persistence,octaves):
    #Initialise empty 2Darray width*height
    values = [[0 for x in xrange(height)]for y in xrange(width)]
    
    #For each value
    for i in xrange(width):
        for j in xrange(height):
            #For each value
            #Reset value total, frequency and amplitude
            value = 0.0
            amplitude = 1.0
            frequency = startfrequency
            
            for octave in xrange(octaves):
                #For each octave
                value += 1.414*amplitude*perlin.getNoise(i/frequency,j/frequency,seed,interpolationMethod)
                amplitude *= persistence
                frequency /= lacunarity
            #Assign 8bit integer height/lightness value
            value = int((0.5*value+0.5)*0xff)
            values[i][j] = value       
    return values

def perlinMap(width,height,frequency,interpolationMethod,seed):
    #Initialise empty 2Darray width*height
    values = [[0 for x in xrange(height)]for y in xrange(width)]
    
    #For each value
    for i in xrange(width):
        for j in xrange(height):
            #For each value
            value = 1.414*perlin.getNoise(i/frequency,j/frequency,seed,interpolationMethod)
            #Assign 8bit integer height/lightness value
            value = int((0.5*value+0.5)*0xff)
            values[i][j] = value       
    return values


    



        
    
    

