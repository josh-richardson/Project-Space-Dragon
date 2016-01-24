
import pygame
import sys
import time
from Background import *

from Player import *
from ProfileDisplay import *
from NPCShip import *
from Explosion import *
import Settings


class GameWorld:
    global activeEntities
    running = True
    exitTimer = -1

    def render(self, screen):
        self.background.render(screen)
        for entity in self.npcEntities:
            entity.render(screen)
        for entity in self.playerProjectileEntities:
            entity.render(screen)
        for entity in self.npcProjectileEntities:
            entity.render(screen)

        self.player.render(screen)

        self.profileDisplay.render(screen)

    def update(self):
        self.running=True
        self.player.update()
        if self.player.health<=0:
            for entity in self.npcEntities:
                self.npcEntities.remove(entity)
        self.background.paraX = self.player.xVelocity * Settings.starParallaxX
        self.background.paraY = self.player.yVelocity * Settings.starParallaxY
        self.background.update()

        for entity in self.npcEntities:
            if entity.update():
                explosion = Explosion(self, entity.xPosition, entity.yPosition)
                explosion.sprite = pygame.image.load("../assets/explosion.png")
                explosion.setSprite(explosion.sprite)
                self.npcEntities.append(explosion)
                self.npcEntities.remove(entity)

        for entity in self.playerProjectileEntities:
            if entity.update():
                self.playerProjectileEntities.remove(entity)
        for entity in self.npcProjectileEntities:
            if entity.update():
                self.npcProjectileEntities.remove(entity)


        if(self.exitTimer < 0 and len(self.npcEntities) == 0):
            self.exitTimer = 10

        if(self.exitTimer > 0):
            self.exitTimer -= 1
        elif(self.exitTimer == 0):
            self.running = False
            self.exitTimer=-1

        return self.running

    def reinitialize_background(self):
        rngseed = int(time.time()*1000)
        self.background = Background(256,3,rngseed)


    def __init__(self,screen):
        self.npcProjectileEntities = []
        self.playerProjectileEntities = []
        self.npcEntities = []
        screenMiddle = (Settings.screen_width/2,Settings.screen_height/2)
        self.profileDisplay = ProfileDisplay(self)
        rngseed = int(time.time()*1000)
        self.background = Background(256,3,rngseed)

        self.playerSprite = pygame.image.load("../assets/spehssmobile.png")
        self.playerEngine = pygame.image.load("../assets/spehssmobileengine.png")
        self.enemySprite = pygame.image.load("../assets/heresy.png")
        self.enemyEngine = pygame.image.load("../assets/heresyengine.png")
        self.bulletSprite = pygame.image.load("../assets/bullet.png")

        self.player = Player(self, screenMiddle[0],screenMiddle[1])

        self.player.engineSound = pygame.mixer.Sound("../assets/Audio/enginehum.wav")
        self.player.bulletSound = pygame.mixer.Sound("../assets/Audio/pewpew.wav")
        self.hitSound = pygame.mixer.Sound("../assets/Audio/grenade.wav")

        self.exitTimer = -1
        self.running = True


    def addEnemies(self, enemyNumber):
        for n in xrange(0, enemyNumber):
            # Add one NPC for testing
            npcShip = NPCShip(self, randint(50, Settings.screen_width - 50), randint(50, Settings.screen_height - 50), randint(-5, 5), randint(-5, 5),5,True, 2+randint(0, math.ceil(enemyNumber/4.0)),random.random())
            npcShip.setSprite(self.enemySprite)
            npcShip.setSprite(self.enemyEngine)
            self.npcEntities.append(npcShip)


    def setSound(self,volume):
        self.player.engineSound.set_volume(volume/100.0)
        self.player.bulletSound.set_volume(volume/100.0)
        self.hitSound.set_volume(volume/100.0)


    def onKeyDown(self, pressed):
        Player.onKeyDown(self.player, pressed)
    def onKeyUp(self, pressed):
        Player.onKeyUp(self.player, pressed)
