import pygame
import os
import random
import time
from pygame import mixer


pygame.font.init()
pygame.font.init()
pygame.mixer.init()

#import colors
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
TRANSPARENT = (0, 0, 0, 0)
HP = 100
lvl = 1
mob1_hp = 100
mob2_hp = 100
mob3_hp = 100

gameover = False


right_dmg = 1
mob1_dmg = 0.1
mob2_dmg = 0
mob3_dmg = 0

max_mob1_health = 100
max_mob2_health = 100
max_mob3_health = 100
max_boss_health = 200

hp_bar_width = 100
hp_bar_height = 20


#random beallitasok
WIDTH, HEIGHT = 900, 500
CHARACTER_WIDTH, CHARACTER_HEIGHT = 110, 90
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Borsodi szitu)")
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
FPS = 60
VEL_RIGHT = 4
VEL_MOB1 = 1
VEL_MOB2 = 1
VEL_MOB3 = 1

clock = pygame.time.Clock()
COUNTER = 2
SHIELD_ON = "off"
SPEED_ON = "off"
look = "down"
mob1_x = random.randrange(50, 850)
mob1_y = random.randrange(50, 450)

mob2_x = random.randrange(50, 850)
mob2_y = random.randrange(50, 450)

mob3_x = random.randrange(50, 850)
mob3_y = random.randrange(50, 450)

boss_hp = 200

HP_font = pygame.font.SysFont("comicsant", 40)
dmg_up_txt = False
hp_up_txt = False
speed_up_txt = False

#x = int(input("Cheatcode:"))
#if x == 5:
#    lvl = 5

#Import/scale images
UPMOVE1_IMAGE = pygame.image.load(os.path.join("images", "forwardmove1.png"))
UPMOVE1 = pygame.transform.scale(UPMOVE1_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
LEFTMOVE1_IMAGE = pygame.image.load(os.path.join("images", "leftmove1.png"))
LEFTMOVE1 = pygame.transform.scale(LEFTMOVE1_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
DOWNMOVE1_IMAGE = pygame.image.load(os.path.join("images", "backmove1.png"))
DOWNMOVE1 = pygame.transform.scale(DOWNMOVE1_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
RIGHTMOVE1_IMAGE = pygame.image.load(os.path.join("images", "rightmove1.png"))
RIGHTMOVE1 = pygame.transform.scale(RIGHTMOVE1_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
C_X_IMAGE = pygame.image.load(os.path.join("images", "c_x.png"))
C_X = pygame.transform.scale(C_X_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
frm_IMAGE = pygame.image.load(os.path.join("images", "frm.png"))
FRM = pygame.transform.scale(frm_IMAGE, (WIDTH, HEIGHT))

CURRENTRIGHT = DOWNMOVE1

#ability images

SPEED_IMAGE = pygame.image.load(os.path.join("images", "speedboost.png"))
SPEED = pygame.transform.scale(SPEED_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

HEAL_IMAGE = pygame.image.load(os.path.join("images", "heal.png"))
HEAL = pygame.transform.scale(HEAL_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

FREEZE_IMAGE = pygame.image.load(os.path.join("images", "freeze.png"))
FREEZE = pygame.transform.scale(FREEZE_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))


MOB_IMAGE = pygame.image.load(os.path.join("images", "mob.png"))
MOB = pygame.transform.scale(MOB_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

BOSS_IMAGE = pygame.image.load(os.path.join("images", "mob.png"))
BOSS = pygame.transform.scale(MOB_IMAGE, (CHARACTER_WIDTH * 2, CHARACTER_HEIGHT * 2))

MOB_DEAD_IMAGE = pygame.image.load(os.path.join("images", "mob_dead.png"))
MOB_DEAD = pygame.transform.scale(MOB_DEAD_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

BACKGROUND_IMAGE = pygame.image.load(os.path.join("images", "background.jpg"))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

CHEST_IMAGE = pygame.image.load(os.path.join("images", "chest.png"))
CHEST = pygame.transform.scale(CHEST_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

CHEST_OPENED_IMAGE = pygame.image.load(os.path.join("images", "chest_opened.png"))
CHEST_OPENED = pygame.transform.scale(CHEST_OPENED_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

CROWN_IMAGE = pygame.image.load(os.path.join("images", "crown.png"))
CROWN = pygame.transform.scale(CROWN_IMAGE, (85, 65))


opened = False

CURRENTBOSS = BOSS
CURRENTMOB1 = MOB
CURRENTMOB2 = MOB
CURRENTMOB3 = MOB

MOB_WIDTH = 60
MOB_HEIGHT = 50

#ability
ABILITY_TYPE = random.randrange(1, 3)

DROP_X = 400
DROP_Y = 300

DROP_HEIGHT = 30
DROP_WIDTH = 30
ABILITY1 = pygame.Rect(DROP_X, DROP_Y, DROP_HEIGHT, DROP_WIDTH)

chest_x = 400
chest_y = 200

boss_x = 400
boss_y = 200
boss_dmg = 0
VEL_BOSS = 0.5

#Rajzok
def rajzok(right):
    

    WIN.blit(BACKGROUND, (0, 0))

    if lvl == 1:
        if mob1_hp < 0:
            if opened == False:
                WIN.blit(CHEST, (chest_x, chest_y))
            elif opened == True:
                WIN.blit(CHEST_OPENED, (400, 200))
    if lvl == 2:
        if  mob1_hp < 0 and mob2_hp < 0:
            if opened == False:
                WIN.blit(CHEST, (400, 200))
            elif opened == True:
                WIN.blit(CHEST_OPENED, (400, 200))
            
    if 5 > lvl > 2 or lvl > 5:
        if mob1_hp < 0 and mob2_hp < 0 and mob3_hp < 0:
            if opened == False:
                WIN.blit(CHEST, (400, 200))
            elif opened == True:
                WIN.blit(CHEST_OPENED, (400, 200))

    if lvl == 5:
        if boss_hp < 0:
            if opened == False:
                WIN.blit(CHEST, (400, 200))
            elif opened == True:
                WIN.blit(CHEST_OPENED, (400, 200))

    if lvl == 1:
        WIN.blit(CURRENTMOB1, (mob1_x, mob1_y))
        pygame.draw.rect(WIN, WHITE, (mob1_x , mob1_y - 30, hp_bar_width, hp_bar_height))
        pygame.draw.rect(WIN, RED, (mob1_x, mob1_y - 30, mob1_hp, hp_bar_height))
    elif lvl == 2:
        WIN.blit(CURRENTMOB1, (mob1_x, mob1_y))
        pygame.draw.rect(WIN, WHITE, (mob1_x , mob1_y - 30, hp_bar_width, hp_bar_height))
        pygame.draw.rect(WIN, RED, (mob1_x, mob1_y - 30, mob1_hp, hp_bar_height))
        WIN.blit(CURRENTMOB2, (mob2_x, mob2_y))
        pygame.draw.rect(WIN, WHITE, (mob2_x , mob2_y - 30, hp_bar_width, hp_bar_height))
        pygame.draw.rect(WIN, RED, (mob2_x, mob2_y - 30, mob2_hp, hp_bar_height))
    elif 2 < lvl < 5:
        WIN.blit(CURRENTMOB1, (mob1_x, mob1_y))
        pygame.draw.rect(WIN, WHITE, (mob1_x , mob1_y - 30, hp_bar_width, hp_bar_height))
        pygame.draw.rect(WIN, RED, (mob1_x, mob1_y - 30, mob1_hp, hp_bar_height))
        WIN.blit(CURRENTMOB2, (mob2_x, mob2_y))
        pygame.draw.rect(WIN, WHITE, (mob2_x , mob2_y - 30, hp_bar_width, hp_bar_height))
        pygame.draw.rect(WIN, RED, (mob2_x, mob2_y - 30, mob2_hp, hp_bar_height))
        WIN.blit(CURRENTMOB3, (mob3_x, mob3_y))
        pygame.draw.rect(WIN, WHITE, (mob3_x , mob3_y - 30, hp_bar_width, hp_bar_height))
        pygame.draw.rect(WIN, RED, (mob3_x, mob3_y - 30, mob3_hp, hp_bar_height))
    elif lvl == 5:
        WIN.blit(CURRENTBOSS, (boss_x, boss_y))
        pygame.draw.rect(WIN, WHITE, (boss_x , boss_y - 30, max_boss_health, hp_bar_height))
        pygame.draw.rect(WIN, RED, (boss_x, boss_y - 30, boss_hp, hp_bar_height))
        if boss_hp < 0:
            WIN.blit(CROWN, (right.x + 20, right.y - 10))
    elif lvl > 5:
        WIN.blit(CROWN, (right.x, right.y))
        WIN.blit(CURRENTMOB1, (mob1_x, mob1_y))
        pygame.draw.rect(WIN, WHITE, (mob1_x , mob1_y - 30, hp_bar_width, hp_bar_height))
        pygame.draw.rect(WIN, RED, (mob1_x, mob1_y - 30, mob1_hp, hp_bar_height))
        WIN.blit(CURRENTMOB2, (mob2_x, mob2_y))
        pygame.draw.rect(WIN, WHITE, (mob2_x , mob2_y - 30, hp_bar_width, hp_bar_height))
        pygame.draw.rect(WIN, RED, (mob2_x, mob2_y - 30, mob2_hp, hp_bar_height))
        WIN.blit(CURRENTMOB3, (mob3_x, mob3_y))
        pygame.draw.rect(WIN, WHITE, (mob3_x , mob3_y - 30, hp_bar_width, hp_bar_height))
        pygame.draw.rect(WIN, RED, (mob3_x, mob3_y - 30, mob3_hp, hp_bar_height))
    pygame.draw.rect(WIN, WHITE, (right.x , right.y - 30, 100, hp_bar_height))
    pygame.draw.rect(WIN, RED, (right.x, right.y - 30, HP, hp_bar_height))


    right_hp_txt = HP_font.render("Hp: " + str(HP), 1, WHITE)
    WIN.blit(CURRENTRIGHT, (right.x, right.y))
    WIN.blit(FRM, (0, 0))
    lvlup_txt = HP_font.render("Level: " + str(round(lvl)), 1, WHITE)
    dmg_txt = HP_font.render("Damage: " + str(round(right_dmg, 2)), 1, WHITE)
    speed_txt = HP_font.render("Speed: " + str(round(VEL_RIGHT, 2)), 1, WHITE)
    WIN.blit(dmg_txt, (40, 10))
    WIN.blit(speed_txt, (250, 10))
    WIN.blit(lvlup_txt, (750, 10))
    
    if gameover == True:
        game_over_txt = HP_font.render("meghaltál", 1, WHITE)
        press_enter_txt = HP_font.render("nyomj spacet, hogy újraéledj", 1, WHITE)
        WIN.fill(BLACK)
        WIN.blit(game_over_txt, (350, 200))
        WIN.blit(press_enter_txt, (250, 250))

    pygame.display.update()

    
if lvl < 5:
    mixer.music.load(os.path.join("images", "chill.wav"))
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)
    

mob_death_sound = mixer.Sound(os.path.join("images", "mobdeathsound.wav"))
mob_death_sound.set_volume(1)
chest_open_sound = mixer.Sound(os.path.join("images", "chestopen.wav"))
chest_open_sound.set_volume(1)


#main gam
chest = pygame.Rect(400, 200, CHARACTER_WIDTH // 2, CHARACTER_HEIGHT// 2)
chest_opened = pygame.Rect(400, 200, CHARACTER_WIDTH, CHARACTER_HEIGHT)
right = pygame.Rect(700, 100, CHARACTER_WIDTH, CHARACTER_HEIGHT)
mob1 = pygame.Rect(mob1_x, mob1_y, MOB_WIDTH, MOB_HEIGHT)
mob2 = pygame.Rect(mob2_x, mob2_y, MOB_WIDTH, MOB_HEIGHT)
mob3 = pygame.Rect(mob3_x, mob3_y, MOB_WIDTH, MOB_HEIGHT)
boss = pygame.Rect(boss_x, boss_y, CHARACTER_HEIGHT * 2, CHARACTER_HEIGHT * 2)
run = True
opened_sound = False

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

    if lvl == 1:
        if mob1_hp < 0:
            if right.colliderect(chest):
                if opened_sound == False:
                    for i in range(100):
                        i += 1
                    chest_open_sound.play()
                    opened_sound = True
                else:
                    pass
    if lvl == 2:
        if mob1_hp < 0 and mob2_hp < 0:
            if right.colliderect(chest):
                if opened_sound == False:
                    for i in range(100):
                        i += 1
                    chest_open_sound.play()
                    opened_sound = True
                else:
                    pass
    
    if lvl > 2:
        if mob1_hp < 0 and mob2_hp < 0 and mob3_hp < 0:
            if right.colliderect(chest):
                if opened_sound == False:
                    for i in range(100):
                        i += 1
                    chest_open_sound.play()
                    opened_sound = True
                else:
                    pass



    #right w
    if lvl < 4:
        if mob1_hp and mob2_hp and mob1_hp < 0:
            if right.x > 780:
                if 245 > right.y > 170:
                    right.x = 20
                    right.y = 200
                    lvl = lvl + 1
                    time.sleep(0.5)
                    mob1_x = random.randrange(900)
                    mob1_y = random.randrange(400)
                    mob2_x = random.randrange(900)
                    mob2_y = random.randrange(400)
                    mob3_x = random.randrange(900)
                    mob3_y = random.randrange(400)
                    mob1_hp = 100
                    mob2_hp = 100
                    mob3_hp = 100
                    CURRENTMOB1 = MOB
                    CURRENTMOB2 = MOB
                    CURRENTMOB3 = MOB
                    HP = HP + 25
                    VEL_MOB1 = 1
                    VEL_MOB2 = 1
                    VEL_MOB3 = 1
                    hp_up_txt = False
                    speed_up_txt = False
                    dmg_up_txt = False
                    opened = False
                    opened_sound = False
                    random_drop = random.randrange(1,4)
                    print(random_drop)
    elif lvl == 4:
        if mob1_hp and mob2_hp and mob1_hp < 0:
            if right.x > 780:
                if 245 > right.y > 170:
                    right.x = 20
                    right.y = 200
                    lvl = lvl + 1
                    time.sleep(0.5)
                    mob1_hp = 0
                    mob2_hp = 0
                    mob3_hp = 0
                    mob1_dmg = 0
                    mob2_dmg = 0
                    mob3_dmg = 0
                    VEL_MOB1 = 0
                    VEL_MOB2 = 0
                    VEL_MOB3 = 0
                    boss_hp = 200
                    pygame.mixer.music.stop()
                    mixer.music.load(os.path.join("images", "lvl4music.wav"))
                    mixer.music.set_volume(0.5)
                    mixer.music.play(-1)
                    opened_sound = False
                    CURRENTMOB1.fill(TRANSPARENT)
                    CURRENTMOB2.fill(TRANSPARENT)
                    CURRENTMOB3.fill(TRANSPARENT)
    elif lvl == 5:
        if boss_hp < 0:
            if right.x > 780:
                if 245 > right.y > 170:
                    right.x = 20
                    right.y = 200
                    lvl = lvl + 1
                    time.sleep(0.5)
                    mob1_x = random.randrange(900)
                    mob1_y = random.randrange(400)
                    mob2_x = random.randrange(900)
                    mob2_y = random.randrange(400)
                    mob3_x = random.randrange(900)
                    mob3_y = random.randrange(400)
                    hp_bar_width = 150
                    mob1_hp = 150
                    mob2_hp = 150
                    mob3_hp = 150
                    CURRENTMOB1 = MOB
                    CURRENTMOB2 = MOB
                    CURRENTMOB3 = MOB
                    opened_sound = False
                    HP = HP + 25
                    VEL_MOB1 = 1.3
                    VEL_MOB2 = 1.3
                    VEL_MOB3 = 1.3
                    hp_up_txt = False
                    speed_up_txt = False
                    dmg_up_txt = False
                    opened = False
                    random_drop = random.randrange(1,4)
                    print(random_drop)
    elif lvl > 5:
        if mob1_hp and mob2_hp and mob1_hp < 0:
            if right.x > 780:
                if 245 > right.y > 170:
                    right.x = 20
                    right.y = 200
                    lvl = lvl + 1
                    time.sleep(0.5)
                    mob1_x = random.randrange(900)
                    mob1_y = random.randrange(400)
                    mob2_x = random.randrange(900)
                    mob2_y = random.randrange(400)
                    mob3_x = random.randrange(900)
                    mob3_y = random.randrange(400)
                    mob1_hp = 150
                    mob2_hp = 150
                    mob3_hp = 150
                    CURRENTMOB1 = MOB
                    CURRENTMOB2 = MOB
                    CURRENTMOB3 = MOB
                    HP = HP + 25
                    VEL_MOB1 = 1.3
                    VEL_MOB2 = 1.3
                    VEL_MOB3 = 1.3
                    hp_up_txt = False
                    speed_up_txt = False
                    dmg_up_txt = False
                    opened = False
                    opened_sound = False
                    random_drop = random.randrange(1,4)
                    print(random_drop)

                    

    
    if right.x - 50 < mob1_x < right.x + 50 and right.y - 90 < mob1_y < right.y + 50 or right.x == mob1_x and right.y == mob1_y:
        if mob1_hp < 0:
            HP = HP
            mob1_dmg == 0    
        else:
            HP = HP - mob1_dmg

    if right.x -50 < mob2_x < right.x + 50 and right.y - 90 < mob2_y < right.y + 50 or right.x == mob1_x and right.y == mob1_y:
        if mob2_hp < 0:
            HP = HP
            mob2_dmg == 0    
        else:
            HP = HP - mob2_dmg
    
    if right.x - 50 < mob3_x < right.x + 50 and right.y - 90< mob3_y < right.y + 50 or right.x == mob1_x and right.y == mob1_y:
        if mob3_hp < 0:
            HP = HP 
            mob3_dmg == 0    
        else:
            HP = HP - mob3_dmg

    if right.x - 100 < boss_x < right.x + 100 and right.y - 180 < boss_y < right.y + 100 or right.x == boss_x and right.y == boss_y:
        if boss_hp < 0:
            HP = HP
            boss_dmg == 0    
        else:
            HP = HP - boss_dmg

    if lvl == 1:
        if mob1_hp < 0:
            if right.colliderect(chest):
                opened = True
                while VEL_RIGHT < 5:
                    VEL_RIGHT = VEL_RIGHT + 1
                    
    if lvl == 2:
        if mob1_hp < 0 and mob2_hp < 0:
            if right.colliderect(chest):
                if random_drop == 1:
                    if opened != True:
                        VEL_RIGHT += 0.3
                        speed_up_txt = True
                        print(VEL_RIGHT)
                        opened = True
                    else:
                        pass
                elif random_drop == 2:
                    if opened != True:
                        if HP + 50 > 100:
                            HP = 100
                        else:
                            HP += 50
                        hp_up_txt = True
                        opened = True
                    else:
                        pass
                elif random_drop == 3:
                    if opened != True:
                        right_dmg += 0.2
                        print(right_dmg)
                        dmg_up_txt = True
                        opened = True
                    else:
                        pass
                    
    if 5 > lvl > 2 or lvl > 5:
        if mob1_hp < 0 and mob2_hp < 0 and mob3_hp < 0:
            if right.colliderect(chest):
                if random_drop == 1:
                    if opened != True:
                        VEL_RIGHT += 0.3
                        print(VEL_RIGHT)
                        opened = True
                    else:
                        pass
                elif random_drop == 2:
                    if opened != True:
                        if HP + 50 > 100:
                            HP = 100
                        else:
                            HP += 50
                        opened = True
                    else:
                        pass
                elif random_drop == 3:
                    if opened != True:
                        right_dmg += 0.2
                        print(right_dmg)
                        opened = True
                    else:
                        pass

    if lvl == 5:
        if boss_hp < 0:
            if right.colliderect(chest):
                if random_drop == 1:
                    if opened != True:
                        VEL_RIGHT += 0.5
                        print(VEL_RIGHT)
                        opened = True
                    else:
                        pass
                elif random_drop == 2:
                    if opened != True:
                        HP = 150
                        opened = True
                    else:
                        pass
                elif random_drop == 3:
                    if opened != True:
                        right_dmg += 0.4
                        print(right_dmg)
                        opened = True
                    else:
                        pass


    if HP < 0:
        CURRENTRIGHT = C_X
        VEL_RIGHT = VEL_RIGHT - VEL_RIGHT 
        time.sleep(1)
        gameover = True

    keys_pressed = pygame.key.get_pressed()
    if gameover == True:
        time.sleep(0.2)
        if keys_pressed[pygame.K_SPACE]:
            lvl = 1
            HP = 100
            mob1_hp = 100
            mob2_hp = 100
            mob3_hp = 100
            gameover = False
            VEL_RIGHT = 4
            right.x = 700
            right.y = 100
            CURRENTRIGHT = DOWNMOVE1
            boss_dmg = 0
            boss_hp = 200

    #mob spawn
    if lvl == 1:
        mob2_dmg = 0
        mob3_dmg = 0
    elif lvl == 2:
        mob2_dmg = 0.1
        mob3_dmg = 0
    elif 5 > lvl > 2 or lvl > 5:
        mob2_dmg = 0.1
        mob3_dmg = 0.1

    elif lvl == 5:
        boss_dmg = 0.1
        mob1_dmg = 0
        mob2_dmg = 0
        mob3_dmg = 0

    #mob control
    if mob1_y > right.y:
        mob1_y -= VEL_MOB1
    elif mob1_y < right.y:
        mob1_y += VEL_MOB1

    if mob1_x > right.x:
        mob1_x -= VEL_MOB1
    elif mob1_x < right.x:
        mob1_x += VEL_MOB1

    if lvl == 2:
        if mob2_y > right.y:
            mob2_y -= VEL_MOB2
        elif mob2_y < right.y:
            mob2_y += VEL_MOB2

        if mob2_x > right.x:
            mob2_x -= VEL_MOB2
        elif mob2_x < right.x:
            mob2_x += VEL_MOB2

    if 5 > lvl > 2 or lvl > 5:
        if mob2_y > right.y:
            mob2_y -= VEL_MOB2
        elif mob2_y < right.y:
            mob2_y += VEL_MOB2

        if mob2_x > right.x:
            mob2_x -= VEL_MOB2
        elif mob2_x < right.x:
            mob2_x += VEL_MOB2
            
        if mob3_y > right.y:
            mob3_y -= VEL_MOB3
        elif mob3_y < right.y:
            mob3_y += VEL_MOB3

        if mob3_x > right.x:
            mob3_x -= VEL_MOB3
        elif mob3_x < right.x:
            mob3_x += VEL_MOB3
    
    if lvl == 5:
        if boss_y > right.y + 2:
            boss_y -= VEL_BOSS
        elif boss_y < right.y + 2:
            boss_y += VEL_BOSS

        if boss_x > right.x + 2:
            boss_x -= VEL_BOSS
        elif boss_x < right.x + 2:
            boss_x += VEL_BOSS
            

    #jobb ability control
    


    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and right.x - VEL_RIGHT > 0:
        right.x -= VEL_RIGHT
        look = "left"
        if HP < 0:
            pass
        else:
            CURRENTRIGHT = LEFTMOVE1
    
    if keys_pressed[pygame.K_d] and right.x + VEL_RIGHT < WIDTH-CHARACTER_WIDTH :
        right.x += VEL_RIGHT
        look = "right"
        if HP < 0:
            pass
        else:
            CURRENTRIGHT = RIGHTMOVE1
        
     
    if keys_pressed[pygame.K_w] and right.y - VEL_RIGHT > 0-30:
        right.y -= VEL_RIGHT
        look = "up"
        if HP < 0:
            pass
        else:
            CURRENTRIGHT = UPMOVE1
        
        
    if keys_pressed[pygame.K_s] and right.y - VEL_RIGHT < HEIGHT-CHARACTER_HEIGHT:
        right.y += VEL_RIGHT
        look = "down"
        if HP < 0:
            pass
        else:
            CURRENTRIGHT = DOWNMOVE1
        
    
    if keys_pressed[pygame.K_SPACE]:
        if look == "down":
            if mob1_x + 30 > right.x > mob1_x - 30:
                if mob1_y + 0 > right.y > mob1_y - 70:
                    mob1_hp = mob1_hp - right_dmg
                    if mob1_hp < 0:
                        mob_death_sound.play()
                        CURRENTMOB1 = MOB_DEAD
                        mob1_dmg = 0
                        VEL_MOB1 = 0

        elif look == "right":
            if mob1_x - 70 < right.x < mob1_x: 
                if right.y - 30< mob1_y < right.y + 30:
                    mob1_hp = mob1_hp - right_dmg
                    if mob1_hp < 0:
                        mob_death_sound.play()
                        CURRENTMOB1 = MOB_DEAD
                        mob1_dmg = 0
                        VEL_MOB1 = 0

        elif look == "left":
            if mob1_x + 70 > right.x > mob1_x:
                if right.y - 30< mob1_y < right.y + 30:
                    mob1_hp = mob1_hp - right_dmg
                    if mob1_hp < 0:
                        mob_death_sound.play()
                        CURRENTMOB1 = MOB_DEAD
                        mob1_dmg = 0
                        VEL_MOB1 = 0

        elif look == "up":
            if mob1_x + 30 > right.x > mob1_x - 30:
                if mob1_y + 70 > right.y > mob1_y:
                    mob1_hp = mob1_hp - right_dmg
                    if mob1_hp < 0:
                        mob_death_sound.play()
                        CURRENTMOB1 = MOB_DEAD
                        mob1_dmg = 0
                        VEL_MOB1 = 0

    #
    if keys_pressed[pygame.K_SPACE]:
        if look == "down":
            if mob2_x + 30 > right.x > mob2_x - 30:
                if mob2_y + 0 > right.y > mob2_y - 70:
                    mob2_hp = mob2_hp - right_dmg
                    if mob2_hp < 0:
                        mob_death_sound.play()
                        CURRENTMOB2 = MOB_DEAD
                        mob2_dmg = 0
                        VEL_MOB2 = 0

        elif look == "right":
            if mob2_x - 70 < right.x < mob2_x: 
                if right.y - 30< mob2_y < right.y + 30:
                    mob2_hp = mob2_hp - right_dmg
                    if mob2_hp < 0:
                        mob_death_sound.play()
                        CURRENTMOB2 = MOB_DEAD
                        mob2_dmg = 0
                        VEL_MOB2 = 0

        elif look == "left":
            if mob2_x + 70 > right.x > mob2_x:
                if right.y - 30< mob2_y < right.y + 30:
                    mob2_hp = mob2_hp - right_dmg
                    if mob2_hp < 0:
                        mob_death_sound.play()
                        CURRENTMOB2 = MOB_DEAD
                        mob2_dmg = 0
                        VEL_MOB2 = 0

        elif look == "up":
            if mob2_x + 30 > right.x > mob2_x - 30:
                if mob2_y + 70 > right.y > mob2_y:
                    mob2_hp = mob2_hp - right_dmg
                    if mob2_hp < 0:
                        mob_death_sound.play()
                        CURRENTMOB2 = MOB_DEAD
                        mob2_dmg = 0
                        VEL_MOB2 = 0
    
    if keys_pressed[pygame.K_SPACE]:
        if look == "down":
            if mob3_x + 30 > right.x > mob3_x - 30:
                if mob3_y + 0 > right.y > mob3_y - 70:
                    mob3_hp = mob3_hp - right_dmg
                    if mob3_hp < 0:
                        mob_death_sound.play()
                        CURRENTMOB3 = MOB_DEAD
                        mob3_dmg = 0
                        VEL_MOB3 = 0

        elif look == "right":
            if mob3_x - 70 < right.x < mob3_x: 
                if right.y - 30< mob3_y < right.y + 30:
                    mob3_hp = mob3_hp - right_dmg
                    if mob3_hp < 0:
                        mob_death_sound.play()
                        CURRENTMOB3 = MOB_DEAD
                        mob3_dmg = 0
                        VEL_MOB3 = 0

        elif look == "left":
            if mob3_x + 70 > right.x > mob3_x:
                if right.y - 30< mob3_y < right.y + 30:
                    mob3_hp = mob3_hp - right_dmg
                    if mob3_hp < 0:
                        mob_death_sound.play()
                        CURRENTMOB3 = MOB_DEAD
                        mob3_dmg = 0
                        VEL_MOB3 = 0

        elif look == "up":
            if mob3_x + 30 > right.x > mob3_x - 30:
                if mob3_y + 70 > right.y > mob3_y:
                    mob3_hp = mob3_hp - right_dmg
                    if mob3_hp < 0:
                        mob_death_sound.play()
                        CURRENTMOB3 = MOB_DEAD
                        mob3_dmg = 0
                        VEL_MOB3 = 0
    

    if keys_pressed[pygame.K_SPACE]:
        if look == "down":
            if boss_x + 70 > right.x > boss_x - 20:
                if boss_y + 0 > right.y > boss_y - 50:
                    boss_hp = boss_hp - right_dmg
                    if boss_hp < 0:
                        #CURRENTBOSS = MOB_DEAD
                        boss_dmg = 0
                        VEL_BOSS = 0

        elif look == "right":
            if boss_x - 30< right.x < boss_x: 
                if boss_y - 30< right.y < boss_y + 100:
                    boss_hp = boss_hp - right_dmg
                    if boss_hp < 0:
                        #CURRENTBOSS = MOB_DEAD
                        boss_dmg = 0
                        VEL_BOSS = 0

        elif look == "left":
            if boss_x + 100 > right.x > boss_x + 60:
                if boss_y - 30 < right.y < boss_y + 100:
                    boss_hp = boss_hp - right_dmg
                    if boss_hp < 0:
                        #CURRENTBOSS = MOB_DEAD
                        boss_dmg = 0
                        VEL_BOSS = 0

        if look == "up":
            if boss_x + 70 > right.x > boss_x - 20:
                if boss_y + 90 > right.y > boss_y + 50:
                    boss_hp = boss_hp - right_dmg
                    if boss_hp < 0:
                        #CURRENTBOSS = MOB_DEAD
                        boss_dmg = 0
                        VEL_BOSS = 0

    rajzok(right)
pygame.quit()