
from random import *
import pygame
import Settings
class Star():
    def __init__(self,x,y,sizeIndex):
        self.x=x
        self.y=y
        self.sizeIndex=sizeIndex


class Background:

    def __init__(self,n,sizes,rngseed):
        self.paraX, self.paraY = 0,0
        self.stars = []
        seed(rngseed)
        #Initialise Sprites
        self.sprites = []


        self.sprites.append(pygame.image.load("../assets/Background/Star.png"))


        for i in xrange(2,sizes):
            self.sprites.append(pygame.transform.scale2x(self.sprites[i-2]))
        #Generate Stars pseudorandomly
        for i in xrange(n):
            xPos = randint(0,Settings.screen_width)
            yPos = randint(0,Settings.screen_height)
            star_size = randint(0,len(self.sprites)-1)

            self.stars.append(Star(xPos,yPos,star_size))

        # for i in xrange(0, 3):
        #  self.sprites.append(pygame.transform.scale2x(pygame.image.load("../assets/Background/planetA.png")))


    def render(self,screen):
        for star in self.stars:
            screen.blit(self.sprites[star.sizeIndex-1],(int(star.x),int(star.y)))
    def update(self):
        for star in self.stars:
            star.x += self.paraX
            star.y += self.paraY
            if star.x < 0:
                star.x = Settings.screen_width
            if star.x > Settings.screen_width:
                star.x = star.x%Settings.screen_width

            if star.y < 0:
                star.y = Settings.screen_height
            if star.y > Settings.screen_height:
                star.y = star.y%Settings.screen_height





