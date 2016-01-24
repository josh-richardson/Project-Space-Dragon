
import math
import pygame
import Settings

PI = math.pi
TWO_PI = math.pi * 2


class GameEntity:

    xPosition = yPosition = rotation = 0
    xVelocity , yVelocity , maxVelocity = 0,0,1
    spacebrake = 0.01
    enginePower = 1
    width = height = 0
    spriteOffset = (0,0)
    visible=True
    health = 100

    def __init__(self, world, xpos = 0, ypos = 0, xVelocity = 0, yVelocity = 0, maxVelocity = 10, shouldWrap = False):
        self.sprites = []
        self.xPosition = xpos
        self.yPosition = ypos
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.maxVelocity = maxVelocity
        self.activeSprite = 0
        self.shouldWrap = shouldWrap
        self.world = world

    def update(self):
        # Velocity
        self.xPosition += self.xVelocity
        self.yPosition += self.yVelocity

        if self.xPosition > Settings.screen_width + self.width/2:
            if (self.shouldWrap):
                self.xPosition = 0
            else:
                return True



        elif self.xPosition < 0:
            if (self.shouldWrap):
                 self.xPosition = Settings.screen_width
            else:
                return True

        elif self.yPosition > Settings.screen_height + self.height/2:
            if (self.shouldWrap):
                  self.yPosition = 0
            else:
                return True

        elif self.yPosition < 0:
            if (self.shouldWrap):
                self.yPosition = Settings.screen_height
            else:
                return True

    def render(self, screen):
        if self.visible:
            scaledActiveSprite = self.sprites[self.activeSprite]
            scaledActiveSprite = pygame.transform.scale2x(scaledActiveSprite)
            scaledActiveSprite = pygame.transform.rotate(scaledActiveSprite, self.rotation)

            screen.blit(scaledActiveSprite,(self.xPosition - (scaledActiveSprite.get_width()/2), self.yPosition - (scaledActiveSprite.get_height()/2)))
        else:
            return

    def setSprite(self, sprite):
        self.sprites.append(sprite)
        self.width = self.sprites[-1].get_width()

        self.height = self.sprites[-1].get_height()
        print("Sprite Loaded")

    def getDisplacement(self,other):
        xDist = (other.xPosition - self.xPosition)
        yDist = (other.yPosition - self.yPosition)
        return xDist,yDist

    def getSquareDistance(self,other):
        xDist = (other.xPosition - self.xPosition)**2
        yDist = (other.yPosition - self.yPosition)**2
        return xDist + yDist

    def checkCollides(self, other):
        squareDist = self.getSquareDistance(other)
        return self.boundRadius+other.boundRadius>=squareDist

    def __eq__(self, other):
        return (self.xPosition == other.xPosition) and (self.yPosition == other.yPosition)

    def isNear(self,other,maxSquareDist):
        squareDist = self.getSquareDistance(other)
        return squareDist <= maxSquareDist
    def willCollide(self,other,n):
        '''if self.xVelocity==0:
            return False
        k1=self.yVelocity/self.xVelocity
        m1=(self.xPosition*self.yVelocity-self.xVelocity*self.yPosition)/self.xVelocity
        k2=other.yVelocity/other.xVelocity
        m2=(other.xPosition*other.yVelocity-other.xVelocity*other.yPosition)/other.xVelocity
        if k1==k2:
            return True
        collideX=(m2-m1)/(k1-k2)
        collideY=k1*self.xPosition+m1
        print collideX,"_",collideY
        if ((collideX-other.xPosition)**2+(collideY-other.yPosition)**2)<512:
            return True
        return False'''


        selfX = self.xPosition
        selfY = self.yPosition

        otherX = other.xPosition
        otherY = other.yPosition
        for i in xrange(n):
            selfX += (self.xVelocity)
            selfY += (self.yVelocity)

            otherX += (other.xVelocity)
            otherY += (other.yVelocity)
            if ((selfX-otherX)**2 + (selfY-otherY)**2) - other.boundRadius <= self.boundRadius :
                return True
        return False


    def setRotation(self, rotation):
        self.rotation = (rotation % 360)
