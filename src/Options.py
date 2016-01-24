import pygame
import sys
import Settings
import ConfigParser
from GameWorld import *

def init():
    config=ConfigParser.RawConfigParser()
    config.read('settings.cfg')
    if not config.has_section('settings'):
        config.add_section('settings')
        config.set('settings','width',800)
        config.set('settings','height',600)
        config.set('settings','volume',100)
        config.set('settings','music',50)
        config.set('settings','difficulty',1)
    if not config.has_option('settings','width'):
        config.set('settings','width',800)
    if not config.has_option('settings','height'):
        config.set('settings','height',600)
    if not config.has_option('settings','volume'):
        config.set('settings','volume',100)
    if not config.has_option('settings','music'):
        config.set('settings','music',50)
    if not config.has_option('settings','difficulty'):
        config.set('settings','difficulty',1)
    pygame.mixer.pre_init()
    pygame.init()
    pygame.RESIZABLE = False
    pygame.NOFRAME = False
    screen = pygame.display.set_mode([config.getint('settings','width'), config.getint('settings','height')],pygame.FULLSCREEN|pygame.HWSURFACE)
    Settings.screen_width=config.getint('settings','width')
    Settings.screen_height=config.getint('settings','height')
    Settings.game_difficulty=config.getint('settings','difficulty')
    world=GameWorld(screen)
    world.setSound(config.getint('settings','volume')/100.0)
    f=open('settings.cfg','w')
    config.write(f)
    f.close()
    return (screen,world)

class Options:
    def __init__(self):
        self.font=pygame.font.SysFont("Tahoma",20)
        self.string_res=self.font.render("Screen resolution",1,(255,255,0))
        self.string_audio=self.font.render("Volume",1,(255,255,0))
        self.string_music=self.font.render("Music Volume",1,(255,255,0))
        self.string_diff=self.font.render("Difficulty",1,(255,255,0))
        self.string_apply=self.font.render("To apply settings, please press ENTER",1,(255,0,0))
        self.triangle=pygame.image.load("../assets/Background/triangle.png")
        self.triangle=pygame.transform.scale(self.triangle,(16,16))
        self.menu_sel=0
        self.modes=[]
        self.modes_sel=0
        config=ConfigParser.RawConfigParser()
        config.read('settings.cfg')
        self.temp_volume=config.getint('settings','volume')
        self.temp_music=config.getint('settings','music')
        t=pygame.display.list_modes(32,pygame.FULLSCREEN)
        count=0
        for el in t:
            self.modes.append([el[0],el[1]])
            if el[0]==Settings.screen_width and el[1]==Settings.screen_height:
                self.modes_sel=count
            count=count+1
        self.temp_res_x=self.modes[self.modes_sel][0]
        self.temp_res_y=self.modes[self.modes_sel][1]
        self.temp_diff=Settings.game_difficulty
    def render(self,screen):
        diffs=["","Easy","Medium","Hard"]
        screen.fill((0,0,0))
        screen.blit(self.string_res,(Settings.screen_width/2-100-self.string_res.get_width()/2,100))
        option_res=self.font.render(str(self.temp_res_x)+"x"+str(self.temp_res_y),1,(255,255,0))
        screen.blit(option_res,(Settings.screen_width/2+100-option_res.get_width()/2,100))

        if self.menu_sel==0:
            screen.blit(self.triangle,(Settings.screen_width/2-100-self.string_res.get_width(),102))
        screen.blit(self.string_audio,(Settings.screen_width/2-100-self.string_audio.get_width()/2,200))
        option_audio=self.font.render(str(self.temp_volume)+"%",1,(255,255,0))
        screen.blit(option_audio,(Settings.screen_width/2+100-option_audio.get_width()/2,200))
        if self.menu_sel==1:
            screen.blit(self.triangle,(Settings.screen_width/2-100-self.string_audio.get_width(),202))

        screen.blit(self.string_music,(Settings.screen_width/2-100-self.string_music.get_width()/2,300))
        option_music=self.font.render(str(self.temp_music)+"%",1,(255,255,0))
        screen.blit(option_music,(Settings.screen_width/2+100-option_music.get_width()/2,300))
        if self.menu_sel==2:
            screen.blit(self.triangle,(Settings.screen_width/2-100-self.string_music.get_width(),302))

        screen.blit(self.string_diff,(Settings.screen_width/2-100-self.string_diff.get_width()/2,400))
        option_diff=self.font.render(diffs[self.temp_diff],1,(255,255,0))
        screen.blit(option_diff,(Settings.screen_width/2+100-option_diff.get_width()/2,400))
        if self.menu_sel==3:
            screen.blit(self.triangle,(Settings.screen_width/2-100-self.string_diff.get_width(),402))
        screen.blit(self.string_apply,(Settings.screen_width/2-self.string_apply.get_width()/2,Settings.screen_height-100))

    def onKeyDown(self,pressed):
        global screen
        global world
        if pressed==pygame.K_LEFT:
            if self.menu_sel==0:
                if self.modes_sel<len(self.modes)-1:
                    self.modes_sel=self.modes_sel+1
            elif self.menu_sel==1:
                if self.temp_volume>0:
                    self.temp_volume=self.temp_volume-10
                    if self.temp_volume<0:
                        self.temp_volume=0
            elif self.menu_sel==2:
                if self.temp_music>0:
                    self.temp_music=self.temp_music-10
                    if self.temp_music<0:
                        self.temp_music=0
            elif self.menu_sel==3:
                if self.temp_diff>1:
                    self.temp_diff=self.temp_diff-1
        elif pressed==pygame.K_RIGHT:
            if self.menu_sel==0:
                if self.modes_sel>0:
                    self.modes_sel=self.modes_sel-1
            elif self.menu_sel==1:
                if self.temp_volume<100:
                    self.temp_volume=self.temp_volume+10
                    if self.temp_volume>100:
                        self.temp_volume=100
            elif self.menu_sel==2:
                if self.temp_music<100:
                    self.temp_music=self.temp_music+10
                    if self.temp_music>100:
                        self.temp_music=100
            elif self.menu_sel==3:
                if self.temp_diff<3:
                    self.temp_diff=self.temp_diff+1
        elif pressed==pygame.K_DOWN:
            if self.menu_sel<3:
                self.menu_sel=self.menu_sel+1
        elif pressed==pygame.K_UP:
            if self.menu_sel>0:
                self.menu_sel=self.menu_sel-1
        self.temp_res_x=self.modes[self.modes_sel][0]
        self.temp_res_y=self.modes[self.modes_sel][1]