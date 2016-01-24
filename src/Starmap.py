import pygame

import random
import Settings


class StarMap:
    menuSelected = 0
    startRender = 0
    systems = []
    isAtStarmap = True
    triangle=pygame.image.load("../assets/Background/triangle.png")
    triangle=pygame.transform.scale(triangle,(20,20))
    message=""
    messageColor=(0,0,0)


    def __init__(self):
        self.generateGalaxy()

    def render(self, screen):

        menuFont = pygame.font.SysFont("Tahoma", 25)
        menuTextPositionY = 10
        menuTextPositionX = int(Settings.screen_width*0.2)

        label = menuFont.render(str(self.menuSelected+1) + ". " + self.systems[self.menuSelected], 1, (255, 255, 0))
        screen.blit(label,(menuTextPositionX,Settings.screen_height/2-label.get_height()/2))
        screen.blit(self.triangle, (menuTextPositionX-30, Settings.screen_height/2 - label.get_height()/2 + 8))

        pos_y=Settings.screen_height/2-label.get_height()/2-30
        for counter in xrange(self.menuSelected-1, -1, -1):
            label = menuFont.render(str(counter+1) + ". " + self.systems[counter], 1, (255, 255, 0))
            screen.blit(label, (menuTextPositionX, pos_y))
            pos_y=pos_y-30
        pos_y=Settings.screen_height/2-label.get_height()/2+30
        for counter in xrange(self.menuSelected+1,len(self.systems)):
            label = menuFont.render(str(counter+1) + ". " + self.systems[counter], 1, (255, 255, 0))
            screen.blit(label, (menuTextPositionX, pos_y))
            pos_y=pos_y+30

        if self.message!="":
            messageFont = pygame.font.SysFont("Verdana",20)
            screen.fill(self.messageColour,(Settings.screen_width/2-300/2,Settings.screen_height/2-50/2,300,50))
            messageLabel = messageFont.render(self.message,1,(255,255,255))
            screen.blit(messageLabel,(Settings.screen_width/2-messageLabel.get_width()/2,Settings.screen_height/2-messageLabel.get_height()/2))

    def onKeyDown(self, pressed):
        if pressed == pygame.K_DOWN:
            self.incrementMenu()
        if pressed == pygame.K_UP:
            self.decrementMenu()
        if pressed == pygame.K_RETURN:
            self.isAtStarmap = False

    def incrementMenu(self):
         if self.menuSelected < len(self.systems) - 1:
            self.menuSelected += 1
         else:
            self.menuSelected = 0


    def decrementMenu(self):
        if self.menuSelected > 0:
            self.menuSelected -= 1
        else:
            self.menuSelected = len(self.systems) - 1

    def generateStarName(self):
        greek = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta",
                "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho",
                "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega"]

        constellation = ["Andromedae", "Antliae", "Apodis", "Aquarii", "Aquilae", "Arae",
                        "Arietis", "Aurigae", "Bootis", "Caeli", "Camelopardalis", "Cancri",
                        "Canum", "Canis", "Capricorni", "Carinae", "Cassiopeiae", "Ceti", "Chinpo",
                        "Chamaeleontis", "Circini", "Columbae", "Comae Berenices", "Coronae Australis",
                        "Coronae Borealis", "Corvi","Crateris", "Crucis", "Cygni", "Delphini", "Doradus",
                        "Draconis", "Equulei", "Eridani", "Fornacis", "Geminorum", "Gruis", "Herculis",
                        "Horologii", "Hydrae", "Hydri", "Indi", "Lacertae", "Leonis", "Leporis", "Librae",
                        "Lupi", "Lyncis", "Lyrae", "Mensae", "Microscopii", "Muscae", "Normae", "Octantis",
                        "Ophiuchi", "Orionis", "Pavonis", "Pegasi", "Phoenicis", "Pictoris", "Piscium",
                        "Piscis", "Puppis", "Pyxidis", "Reticuli", "Sagittae", "Sagittarii", "Scorpii",
                        "Sculptoris", "Scuti", "Serpentis", "Sextanis", "Tauri", "Telescopii", "Trianguli",
                        "Tucanae", "Ursae", "Velorum", "Virginis", "Volantis", "Vulpeculae"]

        greekName = random.choice(greek)
        constellationName = random.choice(constellation)
        suffix = str(unichr(random.randint(65, 90))) + str(unichr(random.randint(65, 90))) + "-" + str(random.randint(100,999))

        starName = greekName + " " + constellationName + " " + suffix

        return starName

    def generateGalaxy(self):
        for i in range(0, 100):
            self.systems.append(self.generateStarName())