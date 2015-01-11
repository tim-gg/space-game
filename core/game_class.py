from space_classes import *
import pygame
import random
import os

pygame.init()

click_sound = pygame.mixer.Sound("8bit_bomb_explosion.wav")
laser_sound = pygame.mixer.Sound("laser.wav")
hit_sound = pygame.mixer.Sound("hit.wav")



black = (0,0,0)
white =(255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,200)

r = random.randrange(0, 255)
g = random.randrange(0, 255)
b = random.randrange(0, 255)

star_list = []
for i in range(100):
    x = random.randrange(0,700)
    y = random.randrange(0,500)
    star_list.append([x,y])




class Game():
    p = 0
    a = 5
    bomb = 0


    enemy_list = None
    missiles_list = None
    all_sprites =None
    damaged_list = None
    
    def __init__(self):
        self.enemy_list = pygame.sprite.Group() 
        self.missiles_list = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.damaged_list = pygame.sprite.Group()
        self.bonus_list = pygame.sprite.Group()


        coords = []
        for k in range(8):
            
            enemy = Enemy((30,30))
            enemy.rect.x = random.randrange(1,700)
            enemy.rect.y = random.randrange(-500,0)

            for i in coords:
                if (enemy.rect.x < i[0]+15 or enemy.rect.x > i[0]-15) and (enemy.rect.y < i[1]+15 or enemy.rect.y > i[1]-15):
                    enemy.rect.x = random.randrange(1,700)
                    enemy.rect.y = random.randrange(-500,0)

            coords.append((enemy.rect.x, enemy.rect.y))
            
            self.enemy_list.add(enemy)
            self.all_sprites.add(enemy)

        bomb = Bomb((30, 30))
        bomb.rect.x = random.randrange(1,700)
        bomb.rect.y = -50
        self.all_sprites.add(bomb)
        self.bonus_list.add(bomb)

        self.shipC = ShipC()
        self.all_sprites.add(self.shipC)
        self.shipC.rect.x = 350
        self.shipC.rect.y = 200


    def controller(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.shipC.x_speed=-15
                elif event.key == pygame.K_d:
                    self.shipC.x_speed=15
                elif event.key == pygame.K_w:
                    self.shipC.y_speed=-15
                elif event.key == pygame.K_s:
                    self.shipC.y_speed=15
                
                elif event.key == pygame.K_SPACE:
                    missile = Missile()

                    missile.rect.x = self.shipC.rect.x+35
                    missile.rect.y = self.shipC.rect.y

                
                    self.all_sprites.add(missile)
                    self.missiles_list.add(missile)
                    laser_sound.play()



                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.shipC.x_speed=0
                elif event.key == pygame.K_d:
                    self.shipC.x_speed=0
                elif event.key == pygame.K_w:
                    self.shipC.y_speed=0
                elif event.key == pygame.K_s:
                    self.shipC.y_speed=0
                
        return False

    def run_logic(self):

        self.enemy_list.update()
        self.missiles_list.update()
        self.damaged_list.update()

        n = 8 - (len(self.enemy_list) + len(self.damaged_list))

        coords = []
        for k in range(n):
            enemy = Enemy((30,30))
            enemy.rect.x = random.randrange(1,700)
            enemy.rect.y = random.randrange(-500,0)

            for i in coords:
                if (enemy.rect.x < i[0]+15 or enemy.rect.x > i[0]-15) and (enemy.rect.y < i[1]+15 or enemy.rect.y > i[1]-15):
                    enemy.rect.x = random.randrange(1,700)
                    enemy.rect.y = random.randrange(-500,0)

            coords.append((enemy.rect.x, enemy.rect.y))
            self.enemy_list.add(enemy)
            self.all_sprites.add(enemy)
            


        for enemy in self.enemy_list:
            if self.shipC.rect.x+45 in range(enemy.rect.x, enemy.rect.x + 30) and self.shipC.rect.y in range(enemy.rect.y, enemy.rect.y + 30):
                click_sound.play()                
                self.a -= 1
                self.shipC.rect.y += 40

            if self.shipC.rect.x+25 in range(enemy.rect.x, enemy.rect.x + 30) and self.shipC.rect.y+14 in range(enemy.rect.y, enemy.rect.y + 30):
                click_sound.play()                
                self.a -= 1
                self.shipC.rect.y += 40

            if self.shipC.rect.x+65 in range(enemy.rect.x, enemy.rect.x + 30) and self.shipC.rect.y + 14 in range(enemy.rect.y, enemy.rect.y + 30):
                click_sound.play()                
                self.shipC.rect.y += 40
                self.a -= 1

            if self.shipC.rect.x in range(enemy.rect.x, enemy.rect.x + 30) and self.shipC.rect.y+50 in range(enemy.rect.y, enemy.rect.y + 30):
                click_sound.play()
                self.a -= 1
                self.shipC.rect.y += 40

            if self.shipC.rect.x+90 in range(enemy.rect.x, enemy.rect.x + 30) and self.shipC.rect.y+50 in range(enemy.rect.y, enemy.rect.y + 30):
                click_sound.play()                
                self.a -= 1
                self.shipC.rect.y += 40
               





                
        for dam in self.damaged_list:
            if self.shipC.rect.x+40 in range(dam.rect.x-30, dam.rect.x+60) and self.shipC.rect.y+25 in range(dam.rect.y-20, dam.rect.y+35):
                click_sound.play()
                self.a -= 1
        

        for enemy in self.enemy_list:

            enemy_block_hit = pygame.sprite.spritecollide(enemy, self.missiles_list, True)

            for hit in enemy_block_hit:
                self.enemy_list.remove(enemy)
                self.all_sprites.remove(enemy)
                
            for i in range(len(enemy_block_hit)):   
                d = Damaged((30,30))
                d.rect.x = enemy.rect.x
                d.rect.y = enemy.rect.y
                self.all_sprites.add(d)
                self.damaged_list.add(d)

                hit_sound.play()
            


        for mis in self.missiles_list:
            enemy_hit = pygame.sprite.spritecollide(mis, self.enemy_list, True)
            damaged_block_hit = pygame.sprite.spritecollide(mis, self.damaged_list, True)

            for h in enemy_hit:
                self.missiles.remove(mis)
                self.all_sprites.remove(mis)
                
            for hit in damaged_block_hit:
                self.missiles_list.remove(mis)
                self.all_sprites.remove(mis)
                self.missiles_list.remove(mis)
                hit_sound.play()

                self.p += 1
             
            if mis.rect.y < -10:
                self.missiles_list.remove(mis)
                self.all_sprites.remove(mis)


        if self.p > 10:
            self.bonus_list.update()
            
            self.shipC.pick_bonus(self.bonus_list, self.all_sprites, click_sound, self.bomb)
                




    def display_frame(self, screen):

        screen.fill(black)
        
        for i in range(len(star_list)):
            pygame.draw.circle(screen, white, star_list[i], 2)
            star_list[i][1] += 1

            if star_list[i][1] > 500:
                y = random.randrange(-50,-10)
                star_list[i][1] = y
        
                x = random.randrange(0,700)
                star_list[i][0] = x

        self.shipC.move((r,g,b))
        self.all_sprites.draw(screen)


        font = pygame.font.Font(os.path.join('vera.ttf'), 25)

        hp = font.render("HP:  " + str(self.a),True,white)
        points = font.render("POINTS:  " + str(self.p),True,white)
        bombs = font.render("BOMBS:  " + str(self.bomb),True, white)

    
 
        screen.blit(hp, [5,450])
        screen.blit(points, [5,470])

        screen.blit(bombs, [550, 450])

 

        pygame.display.flip()

