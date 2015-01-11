# -*- coding: utf-8 -*-
import pygame
import random


black = (0,0,0)
white =(255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,200)

r = random.randrange(0, 255)
g = random.randrange(0, 255)
b = random.randrange(0, 255)



class Enemy(pygame.sprite.Sprite):
    def __init__(self, (width, height)):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(white)
        self.image.set_colorkey(white)

        pygame.draw.ellipse(self.image, red,[2,2,width, height])

        self.rect = self.image.get_rect()
        
    def reset_pos(self):
        self.rect.y = random.randrange(-100,-10)
        self.rect.x = random.randrange(0, 700)

    def update(self):
        self.rect.y += 2
        if self.rect.y > 450:
            self.reset_pos()


class Damaged(pygame.sprite.Sprite):
    def __init__(self, (width, height)):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(white)
        self.image.set_colorkey(white)

        pygame.draw.ellipse(self.image, blue,[2,2,width, height])

        self.rect = self.image.get_rect()
        
    def reset_pos(self):
        self.rect.y = random.randrange(-100,-10)
        self.rect.x = random.randrange(0, 700)

    def update(self):
        self.rect.y += 2
        if self.rect.y > 450:
            self.reset_pos()






    

class ShipC(pygame.sprite.Sprite):
    x = 350
    y = 200

    x_speed = 0
    y_speed = 0

    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    color = white
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((90, 50))
        self.image.fill(black)
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()

        pygame.draw.rect(self.image, self.color,[self.rect.x + 25,self.rect.y + 14, 40 ,28])
        pygame.draw.polygon(self.image,self.color,[[self.rect.x,self.rect.y + 50], [self.rect.x+25, self.rect.y + 50],[self.rect.x + 25, self.rect.y + 17]])
        pygame.draw.polygon(self.image,self.color,[[self.rect.x + 90,self.rect.y + 50], [self.rect.x + 65, self.rect.y + 50],[self.rect.x + 65, self.rect.y + 17]])
        pygame.draw.polygon(self.image,self.color,[[self.rect.x + 25,self.rect.y + 14], [self.rect.x+65, self.rect.y + 14],[self.rect.x + 45, self.rect.y]])

        pygame.draw.polygon(self.image,blue,[[self.rect.x + 32,self.rect.y + 11], [self.rect.x+58, self.rect.y + 11],[self.rect.x + 45, self.rect.y + 5]])
        pygame.draw.rect(self.image,red,[self.rect.x + 28,self.rect.y + 14, 36 , 24])

        pygame.draw.polygon(self.image,blue,[[self.rect.x + 6,self.rect.y + 46], [self.rect.x+21, self.rect.y + 46],[self.rect.x + 21, self.rect.y + 25]])
        pygame.draw.polygon(self.image,blue,[[self.rect.x + 84,self.rect.y + 46], [self.rect.x + 69, self.rect.y + 46],[self.rect.x + 69, self.rect.y + 25]])
        pygame.draw.rect(self.image, blue,[self.rect.x + 31,self.rect.y + 18, 30 ,15])

    def move(self,c):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        ref = (c)
        

    def pick_bonus(self, bonus_list, sprites, sound, meter):
        for bonus in bonus_list:
            if self.rect.x+45 in range(bonus.rect.x, bonus.rect.x + 30) and self.rect.y in range(bonus.rect.y, bonus.rect.y + 30):
                sound.play()                
                meter += 1
                bonus_list.remove(bonus)
                sprites.remove(bonus)
                print meter
                
                
            elif self.rect.x+25 in range(bonus.rect.x, bonus.rect.x + 30) and self.rect.y+14 in range(bonus.rect.y, bonus.rect.y + 30):
                sound.play()                
                meter += 1
                bonus_list.remove(bonus)
                sprites.remove(bonus)
                print meter
                
            elif self.rect.x+65 in range(bonus.rect.x, bonus.rect.x + 30) and self.rect.y + 14 in range(bonus.rect.y, bonus.rect.y + 30):
                sound.play()                
                meter += 1
                bonus_list.remove(bonus)
                sprites.remove(bonus)
                print meter

            elif self.rect.x in range(bonus.rect.x, bonus.rect.x + 30) and self.rect.y+50 in range(bonus.rect.y, bonus.rect.y + 30):
                sound.play()
                meter += 1
                bonus_list.remove(bonus)
                sprites.remove(bonus)
                print meter
                
            elif self.rect.x+90 in range(bonus.rect.x, bonus.rect.x + 30) and self.rect.y+50 in range(bonus.rect.y, bonus.rect.y + 30):
                sound.play()                
                meter += 1
                bonus_list.remove(bonus)
                sprites.remove(bonus)
                print meter
            



        

class Missile(pygame.sprite.Sprite):

    color = (220,220,220)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        pygame.draw.ellipse(self.image, self.color,[self.rect.x,self.rect.y, 10, 10])


        
    def update(self):
        self.rect.y -= 10
        self.color = (random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255))


class Bomb(pygame.sprite.Sprite):

    color = (250,250,250)
    def __init__(self, (width, height)):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(black)
        self.image.set_colorkey(black)

        pygame.draw.ellipse(self.image, self.color,[2,2,width, height])

        self.rect = self.image.get_rect()


        
    def update(self):
        self.rect.y += 4
        self.color = (random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255))
    
