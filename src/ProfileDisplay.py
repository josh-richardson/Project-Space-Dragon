

import pygame
import Settings

class ProfileDisplay:

        def __init__(self, gameworld):
            self.gameworld = gameworld


        def render(self, screen):
            profileFont = pygame.font.SysFont("Tahoma", 15)
            experienceLabel = profileFont.render("Life : "+str((self.gameworld.player.health ))+"%", 1, (255, 255, 255))
            self.drawProgressBar(screen, (self.gameworld.player.health), 5, 5)
            self.drawProgressBar(screen, ((Settings.difficulty-5)/10.0)*100, 220, 5)

            screen.blit(experienceLabel, (68, 9))
            experienceLabel = profileFont.render("Level: "+str(Settings.difficulty-5), 1, (255, 255, 255))
            screen.blit(experienceLabel, (300, 9))


        def drawProgressBar(self, screen, percentage, xLocation, yLocation):
            pygame.draw.rect(screen, (255, 0, 0), (xLocation, yLocation, 200, 25), 2)
            pygame.draw.rect(screen, (255, 0, 0), (xLocation + 3, yLocation + 3, (195 * percentage) / 100, 20), 0)

