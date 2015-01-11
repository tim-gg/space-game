import pygame
import random
from game_class import *
from space_classes import *

def main():
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

if __name__ == '__main__':
    main()
