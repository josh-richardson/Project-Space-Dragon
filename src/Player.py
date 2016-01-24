
import pygame
import math
import Settings
from GameEntity import *
from GameWorld import *
from Projectile import *

'''
My Grandfather smoked his whole life. I was about 10 years old when my mother said to him, 'If you ever want to see your grandchildren
graduate, you have to stop immediately.'. Tears welled up in his eyes when he realized what exactly was at stake. He gave it up immediately.
Three years later he died of lung cancer. It was really sad and destroyed me. My mother said to me- 'Don't ever smoke. Please don't put your family
through what your Grandfather put us through." I agreed. At 28, I have never touched a cigarette. I must say, I feel a very slight sense of regret for
never having done it, because this code gave me cancer anyway.
'''

class Player(GameEntity):

    def __init__(self, world,xpos=0, ypos=0, xVelocity=0, yVelocity=0, maxVelocity=10):
        self.engineFwOn = False
        self.engineBwOn = False
        self.engineLfOn = False
        self.engineRtOn = False
        self.engineSound = None
        self.bulletSound = None
        self.boundRadius = 512
        self.experience = 0
        self.health = 100
        self.invuln = 0

        GameEntity.__init__(self, world, xpos, ypos, xVelocity, yVelocity, maxVelocity, True)
        self.setSprite(world.playerSprite)
        self.setSprite(world.playerEngine)

    def checkCollisions(self):
        if self.invuln:
            self.invuln -= 1;
            return
        for bullet in self.world.npcProjectileEntities:
            if self.checkCollides(bullet):
                self.world.hitSound.play()
                self.health -= 5
                self.invuln = 30



    def update(self):
        self.checkCollisions()
        if self.engineFwOn and not self.engineBwOn:
            self.engineFw()

        elif self.engineBwOn and not self.engineFwOn:
            self.engineBw()

        elif(self.xVelocity != 0 or self.yVelocity != 0):
            self.activateSpacebrake()

        if self.engineLfOn and not self.engineRtOn:
            self.engineLf()

        if self.engineRtOn and not self.engineLfOn:
            self.engineRt()

        GameEntity.update(self)

    def activateSpacebrake(self):

        self.spacebrake = 0.02

        if self.xVelocity <= 0.1 and self.xVelocity >= -0.1:
            self.xVelocity = 0

        if self.yVelocity <= 0.1 and self.yVelocity >= -0.1:
            self.yVelocity = 0

        if self.xVelocity > 0.1:
            self.xVelocity -= self.xVelocity*self.spacebrake

        if self.xVelocity < -0.1:
            self.xVelocity -= self.xVelocity*self.spacebrake

        if self.yVelocity > 0.1:
            self.yVelocity -= self.yVelocity*self.spacebrake

        if self.yVelocity < -0.1:
            self.yVelocity -= self.yVelocity*self.spacebrake

    def engineFw(self):
        maxLateralVelocity=7.5
        tx=self.xVelocity+math.cos(math.radians(self.rotation))*self.enginePower
        ty=self.yVelocity-math.sin(math.radians(self.rotation))*self.enginePower

        if tx>-maxLateralVelocity and tx<maxLateralVelocity and ty>-maxLateralVelocity and ty<maxLateralVelocity:
            self.xVelocity = tx
            self.yVelocity = ty

    def engineBw(self):
        maxLateralVelocity=7.5
        tx=self.xVelocity-math.cos(math.radians(self.rotation))*self.enginePower
        ty=self.yVelocity+math.sin(math.radians(self.rotation))*self.enginePower
        if tx>-maxLateralVelocity and tx<maxLateralVelocity and ty>-maxLateralVelocity and ty<maxLateralVelocity:
            self.xVelocity = tx
            self.yVelocity = ty

    def engineLf(self):
        self.setRotation(self.rotation+3.14)

    def engineRt(self):
        self.setRotation(self.rotation-3.14)

    def onKeyDown(self, pressed):
        if pressed == Settings.key_forwards:
            self.activeSprite=1
            self.engineSound.play(1)
            self.engineFwOn = True

        if pressed == Settings.key_backwards:
            self.engineBwOn= True

        if pressed == Settings.key_left :
            self.engineLfOn = True

        if pressed == Settings.key_right:
            self.engineRtOn = True

        if pressed == pygame.K_SPACE:
            direction = self.rotation
            projectile = Projectile(self.world, self.xPosition, self.yPosition, direction,self.xVelocity,self.yVelocity,20)

            self.world.playerProjectileEntities.append(projectile)


            self.bulletSound.play(0)

    def onKeyUp(self, pressed):

        if pressed == Settings.key_forwards:
            self.activeSprite=0
            self.engineSound.stop()
            self.engineFwOn = False

        if pressed == Settings.key_backwards:
            self.engineBwOn= False;

        if pressed == Settings.key_left:
            self.engineLfOn = False;

        if pressed ==  Settings.key_right:
            self.engineRtOn = False