import pygame

from Credits import *
from Menu import *
from Options import *
from Starmap import *

'''

'''
(screen,world)=init()
launch = True
menu = Menu()
starmap = StarMap()
credits = Credits()
options = Options()
#world = GameWorld(screen)
t1 = 0
t0 = 0
config=ConfigParser.RawConfigParser()
config.read('settings.cfg')
menu.setSound(config.getint('settings','volume'))
menu.setMusic(config.getint('settings','music'))

starmap_timer=time.clock()
starmap_active=False
pygame.mouse.set_visible(False)
# pygame.transform.set_smoothscale_backend("MMX")
menu.music.play(-1)


while launch:

    # Receive events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launch = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pressed = event.key
            if menu.isAtMenu:
                if pressed==pygame.K_UP or pressed==pygame.K_DOWN:
                    menu.menuSound.play()
                if pressed==pygame.K_RETURN:
                    menu.menuSound.play()

                menu.onKeyDown(pressed)
            elif menu.isAtOptions:
                if pressed==pygame.K_RETURN:
                    config=ConfigParser.RawConfigParser()
                    config.read('settings.cfg')
                    config.set('settings','width',options.temp_res_x)
                    config.set('settings','height',options.temp_res_y)
                    config.set('settings','volume',options.temp_volume)
                    config.set('settings','music',options.temp_music)
                    config.set('settings','difficulty',options.temp_diff)
                    f=open('settings.cfg','w')
                    config.write(f)
                    f.close()
                    (screen,world)=init()
                    world.setSound(options.temp_volume)
                    menu.setSound(options.temp_volume)
                    menu.setMusic(options.temp_music)
                elif pressed==pygame.K_UP or pressed==pygame.K_DOWN:
                    menu.menuSound.play()
                options.onKeyDown(pressed)
            elif starmap.isAtStarmap:
                if not starmap_active:
                    starmap.onKeyDown(pressed)
                    if pressed == pygame.K_RETURN:
                        Settings.difficulty=6
                        GameWorld.addEnemies(world, starmap.menuSelected + 1)
                    if pressed == pygame.K_UP or pressed == pygame.K_DOWN:
                        menu.menuSound.play()
            else:
                if pressed == pygame.K_m:
                    pass
                GameWorld.onKeyDown(world, pressed)
            if pressed == pygame.K_ESCAPE:
                if menu.isAtCredits:
                    menu.isAtCredits=False
                    menu.isAtMenu=True
                elif menu.isAtOptions:
                    menu.isAtOptions=False
                    menu.isAtMenu=True
                else:
                    launch = False
                    sys.exit()
        elif event.type ==pygame.KEYUP:
            pressed = event.key
            if not menu.isAtMenu:
                GameWorld.onKeyUp(world,pressed)



    t1=time.clock()
    delta = t1 - t0
    if delta>0.016:
        if menu.isAtMenu:
            Menu.render(menu, screen)
        elif menu.isAtCredits:
            Credits.render(credits,screen)
        elif menu.isAtOptions:
            Options.render(options,screen)
        elif starmap.isAtStarmap:
            screen.fill((0, 0, 0))
            StarMap.render(starmap, screen)
        else:
            screen.fill((0, 0, 0))
            GameWorld.render(world, screen)
            if not GameWorld.update(world):
                for entity in world.npcProjectileEntities:
                    world.npcProjectileEntities.remove(entity)
                for entity in world.npcEntities:
                    world.npcEntities.remove(entity)
                for entity in world.playerProjectileEntities:
                    world.playerProjectileEntities.remove(entity)
                starmap.isAtStarmap = True
                if world.player.health<=0:
                    starmap.message="Game over!"
                    starmap.messageColour=(128,0,0)
                    world.player.health=100
                elif Settings.difficulty==15:
                    starmap.message="You won!"
                    starmap.messageColour=(0,128,0)
                    world.player.health=100
                else:
                    starmap.message="Level completed!"
                    starmap.messageColour=(0,128,0)
                    if Settings.game_difficulty==1:
                        world.player.health=100
                    elif Settings.game_difficulty==2:
                        world.player.health=world.player.health*2
                        if world.player.health>100:
                            world.player.health=100
                starmap_timer=time.clock()
                starmap.incrementMenu()
                starmap_active=True

        if starmap_active==True:
            if time.clock()-starmap_timer>2:
                if starmap.message=="Level completed!":
                    starmap.isAtStarmap= False
                    Settings.difficulty = Settings.difficulty+1
                    GameWorld.addEnemies(world, starmap.menuSelected)
                starmap.message=""
                starmap_active=False


        pygame.display.flip()
        t0 = time.clock()

    pygame.display.update()
