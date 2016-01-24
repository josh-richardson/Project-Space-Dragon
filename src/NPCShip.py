

import random
import math
from GameEntity import *
from Projectile import *

class States():
    STOPPED, ATTACKING, RUNNING, EXPLORING = 0,1,2,3

class NPCShip(GameEntity):

    currentState = States.EXPLORING
    allegience = random.choice(("FEDERATION", "PIRATES", "REBELS"))

    if(allegience == "FEDERATION"):
        colour = "#0000FF"
    elif(allegience == "PIRATE"):
        colour = "#FF0000"
    else:
        colour = "#00FF00"

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
        fear=Settings.difficulty
        dodgeAcc=(Settings.difficulty/17.0)
        if xVelocity == 0 :
            if yVelocity > 0:
                self.setRotation(270)
            else:
                self.setRotation(90)
        else:
            self.setRotation(math.degrees(math.atan2(yVelocity, xVelocity)))

        self.fearThreshold = fear
        """self.changeDirection()"""
        self.boundRadius = 480
        self.dodgeAccuracy = dodgeAcc
        self.bulletOffset =0
        self.bulletCooldown=2
        self.spin = random.choice((-1,1))
        GameEntity.__init__(self, world, xpos, ypos, xVelocity, yVelocity, maxVelocity, shouldWrap)

    def evaluateThreat(self):
          for bullet in self.world.playerProjectileEntities:

            if self.willCollide(bullet,self.fearThreshold):
                self.evadeBullet(bullet)
                if self.bulletCooldown:
                    self.bulletCooldown-=1
                    return
                self.bulletSpread(5,1)
                break

    def bulletSpread(self,n,bulletSpeed):
        if self.bulletCooldown:
            self.bulletCooldown-=1
            return

        for i in xrange(n):
            angle = ((360 * i/n)+self.bulletOffset)%360
            """
            xVelocity = bulletSpeed*math.cos(math.radians(angle))
            yVelocity = -bulletSpeed*math.sin(math.radians(angle))"""
            self.world.npcProjectileEntities.append(Projectile(self.world,self.xPosition,self.yPosition,angle,self.xVelocity,self.yVelocity))
        self.bulletOffset += 15
        self.bulletOffset = self.bulletOffset%360



    def update(self):
        self.setRotation(-math.degrees(math.atan2(self.yVelocity, self.xVelocity)))
        #self.setRotation(self.rotation +8*self.spin)
        self.evaluateThreat()

        for bullet in self.world.playerProjectileEntities:
            if self.checkCollides(bullet):
                self.world.hitSound.play(0)

                return True




        self.shouldAttack(self.world.player)


        GameEntity.update(self)
    """
    def explore(self):
        self.currentState = States.EXPLORING

    def attack(self):
        self.currentState = States.ATTACKING
    def run(self):
        self.currentState = States.RUNNING

    def allStop(self):
        self.currentState = States.STOPPED
    """
    def evadeBullet(self,other):
        if other.xVelocity == 0 :
            if other.yVelocity > 0:
                bulletDir = math.radians(90)
            else:
                bulletDir = math.radians(270)
        else:
            bulletDir = math.atan(other.yVelocity / other.xVelocity)
        error = random.random()
        if error > self.dodgeAccuracy:
            error = error
        else:
            error = self.dodgeAccuracy

        evadeDir = random.choice((-1,1))
        angle = bulletDir+(evadeDir*error)
        self.xVelocity = self.maxVelocity*math.cos(angle)
        self.yVelocity = -self.maxVelocity*math.sin(angle)
        self.setRotation(math.degrees(angle))




    def changeDirection(self):
        self.setRotation(random.random()*359)
        self.speed = 5
        self.xVelocity = self.speed * math.cos(math.radians(self.rotation))
        self.yVelocity = -self.speed * math.sin(math.radians(self.rotation))

    def shouldAttack(self,other):
         #TODO: Check if within a certain distance from the playe r, if hostile towards the player attack.
         #Also attack if the player has attacked us.
        if GameEntity.getSquareDistance(self,other)<10000:
            print("attack")
            if self.bulletCooldown:
                self.bulletCooldown-=1
                return
            self.bulletSpread(Settings.difficulty,1)
            #self.bulletCooldown =25

        return False