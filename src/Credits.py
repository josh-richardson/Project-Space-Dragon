# -*- coding: utf-8 -*-

import pygame
import sys
import Settings

class Credits:
    global font
    def __init__(self):
        font=pygame.font.SysFont("Comic Sans MS",35)
        self.y=Settings.screen_height
        self.labels=[""]*20
        self.labels[0]=font.render("Project Space Dragon",1,(255,255,0))
        self.labels[1]=font.render("",1,(255,255,0))
        self.labels[2]=font.render(u"\u00a92015 CompSci Squad A",1,(255,255,0))
        self.labels[3]=font.render("Joshua Richardson - Starmap/Initial development",1,(255,255,0))
        self.labels[4]=font.render("Tom Whitehouse - The Idea/Initial development",1,(255,255,0))
        self.labels[5]=font.render("Youssef the muncher - Nothing",1,(255,255,0))
        self.labels[6]=font.render("Petar Petrov - Settings/Credits/Fixing bugs",1,(255,255,0))
        self.labels[7]=font.render("Adam Carr - The AI Prodigy (Also graphics and sfx)",1,(255,255,0))
        self.labels[8]=font.render("Background track - Expedition by Azureflux",1,(255,255,0))
    def render(self,screen):
        screen.fill((0,0,0))
        for i in xrange(0,8):
            screen.blit(self.labels[i],(Settings.screen_width/2-self.labels[i].get_width()/2,self.y+50*(i+1)))
        self.y=self.y-2
        if self.y<-450:
            self.y=Settings.screen_height