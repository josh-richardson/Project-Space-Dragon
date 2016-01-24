


import Settings
from GameEntity import *

class Projectile(GameEntity):

    speed = 8

    def __init__(self, world ,xpos=0, ypos=0, angle = 0,xInherit=0,yInherit=0,speed=8):

        unitX = math.cos(math.radians(angle))
        unitY = -math.sin(math.radians(angle))
        self.speed = speed
        magnitude =math.sqrt(xInherit**2 + yInherit**2)+self.speed
        self.boundRadius = 32



        xVelocity = magnitude * unitX
        yVelocity = magnitude * unitY

        GameEntity.__init__(self, world, xpos, ypos, xVelocity, yVelocity)
        self.setSprite(world.bulletSprite)

