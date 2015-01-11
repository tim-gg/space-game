#
# libengine.py
# If you want some more structure other than the benefit the exe gives you, here is some pygame
#     related stuff
# libengine.py MUST have a run() method that runs the game
# Other than that its up to you
#
#  this version will build on some other base code
#   * engine.py - handles timing, input, and display
#   * world.py - some engines call this a state, its a displayable runable part of a game,
#                    such as a menu, or the level running code. Worlds contain Agents, the
#                    equivalent of sprites
#   * controller.py - handles some basic input for toggling fullscreen, or quitting the game
#
#   Important to note, game runs on a fixed timestep (currently set to 60hz)
#   Update functions don't need to know the time passed since last frame, just assume
#   it's been 1/60, or if you change the framerate, 1/framerate
#

import pygame
import random
from game_class import *
from space_classes import *

import sys,os
import time
import engine
import controller
import world
if sys.platform=="win32":
    os.environ['SDL_VIDEODRIVER']='windib'


    

def run():
    pygame.init()

    click_sound = pygame.mixer.Sound("8bit_bomb_explosion.wav")
    laser_sound = pygame.mixer.Sound("laser.wav")
    hit_sound = pygame.mixer.Sound("hit.wav")

    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space_v2')

    done = False

    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    game = Game()


    

    while done == False:
        r = random.randrange(255)
        g = random.randrange(255)
        b = random.randrange(255)
        done = game.controller()
        game.run_logic()
        game.display_frame(screen)
        game.shipC.color = (r,g,b)



        clock.tick(20)

    pygame.quit()

if __name__=="__main__":
    run()
