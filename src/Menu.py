import pygame
import sys
import Settings

class Menu:
    global menuItems
    global menuSelected
    global isAtMenu
    global isAtCredits
    global isAtOptions

    def __init__(self):
        self.menuItems = ["New Game", "", "Credits", "Options", "Exit"]
        self.menuSelected = 0
        self.isAtMenu = True
        self.isAtCredits = False
        self.isAtOptions = False
        self.triangle=pygame.image.load("../assets/Background/triangle.png")
        self.triangle=pygame.transform.scale(self.triangle,(20,20))
        self.s_x=0
        self.s_y=0
        self.menuSound=pygame.mixer.Sound("../assets/Audio/menublip")
        self.music = pygame.mixer.Sound("../assets/Audio/chip.ogg")

    def render(self, screen):
        menuFont = pygame.font.SysFont("Tahoma", 25)
        menuTextPositionY = int(Settings.screen_height*0.3)
        menuTextPositionX = int(Settings.screen_width*0.25)
        if self.s_x!=Settings.screen_width or self.s_y!=Settings.screen_height:
            self.background=pygame.image.load("../assets/Background/splash.png")
            self.background=pygame.transform.scale(self.background,(Settings.screen_width,Settings.screen_height))
            self.s_x=Settings.screen_width
            self.s_y=Settings.screen_height
        screen.blit(self.background, (0, 0))
        for counter in xrange(0, len(self.menuItems)):
            label = menuFont.render(self.menuItems[counter], 1, (255, 255, 0))
            screen.blit(label, (menuTextPositionX, menuTextPositionY))
            if counter == self.menuSelected:
                 screen.blit(self.triangle, (menuTextPositionX-30, menuTextPositionY+7))
            menuTextPositionY += 30

    def setSound(self,volume):
        self.menuSound.set_volume(volume/100.0)

    def setMusic(self,volume):
        self.music.set_volume(volume/100.0)


    def incrementMenu(self):
         if self.menuSelected < len(self.menuItems) - 1:
            self.menuSelected += 1
            if self.menuSelected == 1: self.menuSelected += 1
         else:
            self.menuSelected = 0


    def decrementMenu(self):
        if self.menuSelected > 0:
            self.menuSelected -= 1
            if self.menuSelected == 1: self.menuSelected -= 1
        else:
            self.menuSelected = len(self.menuItems) - 1



    def onKeyDown(self, pressed):
        if pressed == pygame.K_DOWN:
            self.incrementMenu()
        if pressed == pygame.K_UP:
            self.decrementMenu()
        if pressed == pygame.K_RETURN:
            if (self.menuSelected == 0):
                self.isAtMenu = False
            if (self.menuSelected == 2):
                self.isAtMenu = False
                self.isAtCredits = True
            if (self.menuSelected == 3):
                self.isAtMenu = False
                self.isAtOptions = True
            if (self.menuSelected == 4):
                sys.exit()


