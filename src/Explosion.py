


import random
import math
from GameEntity import *
from Projectile import *


class Explosion(GameEntity):


    def __init__(self, world, xpos=0, ypos=0, xVelocity=0, yVelocity=0, maxVelocity=10, shouldWrap=True,fear=5,dodgeAcc=0.6):
        """self.xPosition = xpos
        self.yPosition = ypos
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.stoppedScore = 0
        self.attackScore = 0
        self.runScore = 0
        self.exploreScore = 0
        """

        self.life = 30
        GameEntity.__init__(self, world, xpos, ypos, xVelocity, yVelocity, maxVelocity, shouldWrap)



    def update(self):
        self.life -= 2
        if self.life < 1:
            self.world.npcEntities.remove(self)
        elif self.life < 10:
            if len(self.sprites) == 2:
                self.sprite3 = pygame.image.load("../assets/explosion3.png")
                self.setSprite(self.sprite3)
            self.activeSprite = 2
        elif self.life < 20:
            if len(self.sprites) == 1:
                self.sprite2 = pygame.image.load("../assets/explosion2.png")
                self.setSprite(self.sprite2)
            self.activeSprite = 1

        GameEntity.update(self)
