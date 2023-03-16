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
lvl = 0
mob1_hp = 100
mob2_hp = 100
mob3_hp = 100

gameover = False

mob1_hit = pygame.USEREVENT + 1
mob2_hit = pygame.USEREVENT + 2
mob3_hit = pygame.USEREVENT + 3

right_dmg = 1
mob1_dmg = 0
mob2_dmg = 0
mob3_dmg = 0

next_shot = 0

max_mob1_health = 100
max_mob2_health = 100
max_mob3_health = 100
max_boss_health = 200

hp_bar_width = 100
hp_bar_height = 10

count = 1000

#random beallitasok
WIDTH, HEIGHT = 900, 500
CHARACTER_WIDTH, CHARACTER_HEIGHT = 110, 90
HEAD_WIDTH, HEAD_HEIGHT = 110, 90
BODY_WIDTH, BODY_HEIGHT = 110, 90
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Borsodi szitu)")
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
FPS = 60
VEL_RIGHT = 4
VEL_MOB1 = 2
VEL_MOB2 = 2
VEL_MOB3 = 2

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

shot_delay = 0

bullets_left = []
bullets_right = []
bullets_down = []
bullets_up = []



VEL_BULLETS = 6
max_bullets = 3




HP_font = pygame.font.SysFont("comicsant", 40)
dmg_up_txt = False
hp_up_txt = False
speed_up_txt = False

x = int(input("Cheatcode:"))
lvl = x
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

BODY_LEFT_IMAGE = pygame.image.load(os.path.join("images","character", "body_left.png"))
BODY_LEFT = pygame.transform.scale(BODY_LEFT_IMAGE, (BODY_WIDTH, BODY_HEIGHT))
BODY_UP_IMAGE = pygame.image.load(os.path.join("images","character", "body_up.png"))
BODY_UP = pygame.transform.scale(BODY_UP_IMAGE, (BODY_WIDTH, BODY_HEIGHT))
BODY_RIGHT_IMAGE = pygame.image.load(os.path.join("images","character", "body_right.png"))
BODY_RIGHT = pygame.transform.scale(BODY_RIGHT_IMAGE, (BODY_WIDTH, BODY_HEIGHT))
CURRENTBODY = BODY_UP

HEAD_DOWN_IMAGE = pygame.image.load(os.path.join("images","character", "head_down.png"))
HEAD_DOWN = pygame.transform.scale(HEAD_DOWN_IMAGE, (HEAD_WIDTH, HEAD_HEIGHT))
HEAD_UP_IMAGE = pygame.image.load(os.path.join("images","character", "head_up.png"))
HEAD_UP = pygame.transform.scale(HEAD_UP_IMAGE, (HEAD_WIDTH, HEAD_HEIGHT))
HEAD_RIGHT_IMAGE = pygame.image.load(os.path.join("images","character", "head_right.png"))
HEAD_RIGHT = pygame.transform.scale(HEAD_RIGHT_IMAGE, (HEAD_WIDTH, HEAD_HEIGHT))
HEAD_LEFT_IMAGE = pygame.image.load(os.path.join("images","character", "head_left.png"))
HEAD_LEFT = pygame.transform.scale(HEAD_LEFT_IMAGE, (HEAD_WIDTH, HEAD_HEIGHT))
CURRENTHEAD = HEAD_DOWN


CURRENTRIGHT = DOWNMOVE1

SPEED_IMAGE = pygame.image.load(os.path.join("images", "speedboost.png"))
SPEED = pygame.transform.scale(SPEED_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

HEAL_IMAGE = pygame.image.load(os.path.join("images", "heal.png"))
HEAL = pygame.transform.scale(HEAL_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

FREEZE_IMAGE = pygame.image.load(os.path.join("images", "freeze.png"))
FREEZE = pygame.transform.scale(FREEZE_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))


MOB_IMAGE = pygame.image.load(os.path.join("images", "character", "lvl1mob.png"))
MOB = pygame.transform.scale(MOB_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

MOB2_IMAGE = pygame.image.load(os.path.join("images", "character", "lvl2mob.png"))
MOB2 = pygame.transform.scale(MOB2_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

MOB3_IMAGE = pygame.image.load(os.path.join("images", "character", "lvl3mob.png"))
MOB3 = pygame.transform.scale(MOB3_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

MOB4_IMAGE = pygame.image.load(os.path.join("images", "character", "lvl4mob.png"))
MOB4 = pygame.transform.scale(MOB4_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

BOSS_IMAGE = pygame.image.load(os.path.join("images", "mob.png"))
BOSS = pygame.transform.scale(MOB_IMAGE, (CHARACTER_WIDTH * 2, CHARACTER_HEIGHT * 2))

MOB_DEAD_IMAGE = pygame.image.load(os.path.join("images", "mob_dead.png"))
MOB_DEAD = pygame.transform.scale(MOB_DEAD_IMAGE, (CHARACTER_WIDTH * 1.2, CHARACTER_HEIGHT * 1.2))

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
VEL_BOSS = 0


def rajzok(right, bullets_right,bullets_down,bullets_left,bullets_up, bullet_right, bullet_left, bullet_up, bullet_down):
    WIN.blit(BACKGROUND, (0, 0))

    if lvl == 1:
        if mob1_hp <= 0:
            if opened == False:
                WIN.blit(CHEST, (chest_x, chest_y))
            elif opened == True:
                WIN.blit(CHEST_OPENED, (400, 200))
    if lvl == 2:
        if  mob1_hp <= 0 and mob2_hp <= 0:
            if opened == False:
                WIN.blit(CHEST, (400, 200))
            elif opened == True:
                WIN.blit(CHEST_OPENED, (400, 200))
            
    if 5 > lvl > 2 or lvl > 5:
        if mob1_hp <= 0 and mob2_hp <= 0 and mob3_hp <= 0:
            if opened == False:
                WIN.blit(CHEST, (400, 200))
            elif opened == True:
                WIN.blit(CHEST_OPENED, (400, 200))

    if lvl == 5:
        if boss_hp <= 0:
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
    elif 5 > lvl > 2 or 10 > lvl > 5 or 15 > lvl > 10 or 20 > lvl > 15:
        WIN.blit(CURRENTMOB1, (mob1_x, mob1_y))
        pygame.draw.rect(WIN, WHITE, (mob1_x , mob1_y - 30, hp_bar_width, hp_bar_height))
        pygame.draw.rect(WIN, RED, (mob1_x, mob1_y - 30, mob1_hp, hp_bar_height))
        WIN.blit(CURRENTMOB2, (mob2_x, mob2_y))
        pygame.draw.rect(WIN, WHITE, (mob2_x , mob2_y - 30, hp_bar_width, hp_bar_height))
        pygame.draw.rect(WIN, RED, (mob2_x, mob2_y - 30, mob2_hp, hp_bar_height))
        WIN.blit(CURRENTMOB3, (mob3_x, mob3_y))
        pygame.draw.rect(WIN, WHITE, (mob3_x , mob3_y - 30, hp_bar_width, hp_bar_height))
        pygame.draw.rect(WIN, RED, (mob3_x, mob3_y - 30, mob3_hp, hp_bar_height))
    elif lvl == 5 or lvl == 10 or lvl == 15 or lvl == 20:
        WIN.blit(CURRENTBOSS, (boss_x, boss_y))
        pygame.draw.rect(WIN, WHITE, (boss_x , boss_y - 30, max_boss_health, hp_bar_height))
        pygame.draw.rect(WIN, RED, (boss_x, boss_y - 30, boss_hp, hp_bar_height))
        if boss_hp <= 0:
            WIN.blit(CROWN, (right.x + 25, right.y - 10))
    #elif lvl > 5:
    #    WIN.blit(CROWN, (right.x + 25, right.y - 10))
    #    WIN.blit(CURRENTMOB1, (mob1_x, mob1_y))
    #    pygame.draw.rect(WIN, WHITE, (mob1_x , mob1_y - 30, hp_bar_width, hp_bar_height))
    #    pygame.draw.rect(WIN, RED, (mob1_x, mob1_y - 30, mob1_hp, hp_bar_height))
    #    WIN.blit(CURRENTMOB2, (mob2_x, mob2_y))
    #    pygame.draw.rect(WIN, WHITE, (mob2_x , mob2_y - 30, hp_bar_width, hp_bar_height))
    #    pygame.draw.rect(WIN, RED, (mob2_x, mob2_y - 30, mob2_hp, hp_bar_height))
    #    WIN.blit(CURRENTMOB3, (mob3_x, mob3_y))
    #    pygame.draw.rect(WIN, WHITE, (mob3_x , mob3_y - 30, hp_bar_width, hp_bar_height))
    #    pygame.draw.rect(WIN, RED, (mob3_x, mob3_y - 30, mob3_hp, hp_bar_height))
    pygame.draw.rect(WIN, WHITE, (right.x , right.y - 30, 100, hp_bar_height))
    pygame.draw.rect(WIN, RED, (right.x, right.y - 30, HP, hp_bar_height))


    right_hp_txt = HP_font.render("Hp: " + str(HP), 1, WHITE)
    WIN.blit(CURRENTBODY, (right.x, right.y))
    WIN.blit(CURRENTHEAD, (right.x, right.y - 20))
    WIN.blit(FRM, (0, 0))
    lvlup_txt = HP_font.render("Level: " + str(round(lvl)), 1, WHITE)
    dmg_txt = HP_font.render("Damage: " + str(round(right_dmg, 2)), 1, WHITE)
    speed_txt = HP_font.render("Speed: " + str(round(VEL_RIGHT, 2)), 1, WHITE)
    WIN.blit(dmg_txt, (40, 10))
    WIN.blit(speed_txt, (250, 10))
    WIN.blit(lvlup_txt, (750, 10))


    for bullet_right in bullets_right:
        pygame.draw.rect(WIN, RED, bullet_right)
    for bullet_down in bullets_down:
        pygame.draw.rect(WIN, RED, bullet_down)
    for bullet_up in bullets_up:
        pygame.draw.rect(WIN, RED, bullet_up)
    for bullet_left in bullets_left:
        pygame.draw.rect(WIN, RED, bullet_left)
    
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

shoot_sound = mixer.Sound(os.path.join("images", "shoot.wav"))
shoot_sound.set_volume(1)

#main gam
chest = pygame.Rect(400, 200, CHARACTER_WIDTH // 2, CHARACTER_HEIGHT// 2)
chest_opened = pygame.Rect(400, 200, CHARACTER_WIDTH, CHARACTER_HEIGHT)
right = pygame.Rect(700, 100, CHARACTER_WIDTH, CHARACTER_HEIGHT)
mob1 = pygame.Rect(mob1_x, mob1_y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
mob2 = pygame.Rect(mob2_x, mob2_y, MOB_WIDTH, MOB_HEIGHT)
mob3 = pygame.Rect(mob3_x, mob3_y, MOB_WIDTH, MOB_HEIGHT)
boss = pygame.Rect(boss_x, boss_y, CHARACTER_HEIGHT * 2, CHARACTER_HEIGHT * 2)
bullet_right = pygame.Rect(right.x + CHARACTER_WIDTH, right.y + CHARACTER_HEIGHT//2, 15, 5)
bullet_left = pygame.Rect(right.x + CHARACTER_WIDTH, right.y + CHARACTER_HEIGHT//2, 15, 5)
bullet_down = pygame.Rect(right.x + CHARACTER_WIDTH, right.y + CHARACTER_HEIGHT//2, 15, 5)
bullet_up = pygame.Rect(right.x + CHARACTER_WIDTH, right.y + CHARACTER_HEIGHT//2, 15, 5)
run = True
opened_sound = False

def handle_bullets(bullets_right,bullets_down,bullets_left,bullets_up, right, mob1, mob1_hp, bullet_right, bullet_left, bullet_up, bullet_down, mob2, mob2_hp, mob3, mob3_hp):
    for bullet_right in bullets_right:
        bullet_right.x += VEL_BULLETS
        if mob1.colliderect(bullet_right):
            bullets_right.remove(bullet_right)
    for bullet_left in bullets_left:
        bullet_left.x -= VEL_BULLETS
        if mob1.colliderect(bullet_left):
            bullets_left.remove(bullet_left)
    for bullet_up in bullets_up:
        bullet_up.y -= VEL_BULLETS
        if mob1.colliderect(bullet_up):
            bullets_up.remove(bullet_up)
    for bullet_down in bullets_down:
        bullet_down.y += VEL_BULLETS
        if mob1.colliderect(bullet_down):
            bullets_down.remove(bullet_down)

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if lvl == 1:
        if mob1_hp <= 0:
            if right.colliderect(chest):
                if opened_sound == False:
                    for i in range(100):
                        i += 1
                    chest_open_sound.play()
                    opened_sound = True
                else:
                    pass
    if lvl == 2:
        if mob1_hp <= 0 and mob2_hp <= 0:
            if right.colliderect(chest):
                if opened_sound == False:
                    for i in range(100):
                        i += 1
                    chest_open_sound.play()
                    opened_sound = True
                else:
                    pass
    
    if 5 > lvl > 2:
        if mob1_hp <= 0 and mob2_hp <= 0 and mob3_hp <= 0:
            if right.colliderect(chest):
                if opened_sound == False:
                    for i in range(100):
                        i += 1
                else:
                    pass

    if lvl == 5:
        if boss_hp <= 0:
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
        if lvl == 0:
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
                    VEL_MOB1 = 2
                    VEL_MOB2 = 2
                    VEL_MOB3 = 2
                    hp_up_txt = False
                    speed_up_txt = False
                    dmg_up_txt = False
                    opened = False
                    opened_sound = False
                    random_drop = random.randrange(1,4)
                    bullets_left = []
                    bullets_right = []
                    bullets_down = []
                    bullets_up = []
                    shot_delay = 0
                    next_shot = 0
                    mob1_dmg = 0.1

        if lvl == 1:
            if mob1_hp <= 0:
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
                        VEL_MOB1 = 2
                        VEL_MOB2 = 2
                        VEL_MOB3 = 2
                        hp_up_txt = False
                        speed_up_txt = False
                        dmg_up_txt = False
                        opened = False
                        opened_sound = False
                        random_drop = random.randrange(1,4)
                        bullets_left = []
                        bullets_right = []
                        bullets_down = []
                        bullets_up = []
                        shot_delay = 0
                        next_shot = 0
                        print(random_drop)
        elif lvl == 2:
            if mob1_hp <= 0 and mob2_hp <= 0:
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
                        VEL_MOB1 = 2
                        VEL_MOB2 = 2
                        VEL_MOB3 = 2
                        hp_up_txt = False
                        speed_up_txt = False
                        dmg_up_txt = False
                        opened = False
                        opened_sound = False
                        random_drop = random.randrange(1,4)
                        bullets_left = []
                        bullets_right = []
                        bullets_down = []
                        bullets_up = []
                        shot_delay = 0
                        next_shot = 0
                        print(random_drop)
        elif lvl == 3:
            if mob1_hp <= 0 and mob2_hp <= 0 and mob3_hp <= 0:
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
                        VEL_MOB1 = 2
                        VEL_MOB2 = 2
                        VEL_MOB3 = 2
                        hp_up_txt = False
                        speed_up_txt = False
                        dmg_up_txt = False
                        opened = False
                        opened_sound = False
                        random_drop = random.randrange(1,4)
                        bullets_left = []
                        bullets_right = []
                        bullets_down = []
                        bullets_up = []
                        shot_delay = 0
                        next_shot = 0
                        print(random_drop)
    elif lvl == 4 or lvl == 9 or lvl == 14 or lvl == 19:
        if mob1_hp <= 0 and mob2_hp <= 0 and mob3_hp <= 0:
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
                    mob1_x = 1000
                    mob2_x = 1000
                    mob3_x = 1000
                    VEL_MOB1 = 0
                    VEL_MOB2 = 0
                    VEL_MOB3 = 0
                    boss_hp = 200
                    pygame.mixer.music.stop()
                    mixer.music.load(os.path.join("images", "lvl4music.wav"))
                    mixer.music.set_volume(0.5)
                    mixer.music.play(-1)
                    opened_sound = False
                    #CURRENTMOB1.fill(TRANSPARENT)
                    #CURRENTMOB2.fill(TRANSPARENT)
                    #CURRENTMOB3.fill(TRANSPARENT)
                    bullets_left = []
                    bullets_right = []
                    bullets_down = []
                    bullets_up = []
                    shot_delay = 0
                    next_shot = 0

    elif 9 > lvl > 4:
        if mob1_hp <= 0 and mob2_hp <= 0 and mob3_hp <= 0:
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
                    CURRENTMOB1 = MOB2
                    CURRENTMOB2 = MOB2
                    CURRENTMOB3 = MOB2
                    HP = HP + 25
                    VEL_MOB1 = 2.3
                    VEL_MOB2 = 2.3
                    VEL_MOB3 = 2.3
                    hp_up_txt = False
                    speed_up_txt = False
                    dmg_up_txt = False
                    opened = False
                    opened_sound = False
                    random_drop = random.randrange(1,4)
                    bullets_left = []
                    bullets_right = []
                    bullets_down = []
                    bullets_up = []
                    shot_delay = 0
                    next_shot = 0
                    print(random_drop)
    
    elif 14 > lvl > 9:
        if mob1_hp <= 0 and mob2_hp <= 0 and mob3_hp <= 0:
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
                    CURRENTMOB1 = MOB3
                    CURRENTMOB2 = MOB3
                    CURRENTMOB3 = MOB3
                    HP = HP + 25
                    VEL_MOB1 = 2.5
                    VEL_MOB2 = 2.5
                    VEL_MOB3 = 2.5
                    hp_up_txt = False
                    speed_up_txt = False
                    dmg_up_txt = False
                    opened = False
                    opened_sound = False
                    random_drop = random.randrange(1,4)
                    bullets_left = []
                    bullets_right = []
                    bullets_down = []
                    bullets_up = []
                    shot_delay = 0
                    next_shot = 0
                    print(random_drop)

    elif 19 > lvl > 14:
        if mob1_hp <= 0 and mob2_hp <= 0 and mob3_hp <= 0:
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
                    CURRENTMOB1 = MOB2
                    CURRENTMOB2 = MOB2
                    CURRENTMOB3 = MOB2
                    HP = HP + 25
                    VEL_MOB1 = 2.5
                    VEL_MOB2 = 2.5
                    VEL_MOB3 = 2.5
                    hp_up_txt = False
                    speed_up_txt = False
                    dmg_up_txt = False
                    opened = False
                    opened_sound = False
                    random_drop = random.randrange(1,4)
                    bullets_left = []
                    bullets_right = []
                    bullets_down = []
                    bullets_up = []
                    shot_delay = 0
                    next_shot = 0
                    print(random_drop)
        
    
    if right.x - 50 < mob1_x < right.x + 50 and right.y - 90 < mob1_y < right.y + 50 or right.x == mob1_x and right.y == mob1_y:
        if mob1_hp <= 0:
            HP = HP
            mob1_dmg == 0    
        else:
            HP = HP - mob1_dmg

    if right.x -50 < mob2_x < right.x + 50 and right.y - 90 < mob2_y < right.y + 50 or right.x == mob1_x and right.y == mob1_y:
        if mob2_hp <= 0:
            HP = HP
            mob2_dmg == 0    
        else:
            HP = HP - mob2_dmg
    
    if right.x - 50 < mob3_x < right.x + 50 and right.y - 90< mob3_y < right.y + 50 or right.x == mob1_x and right.y == mob1_y:
        if mob3_hp <= 0:
            HP = HP 
            mob3_dmg == 0    
        else:
            HP = HP - mob3_dmg

    if right.x - 100 < boss_x < right.x + 100 and right.y - 180 < boss_y < right.y + 100 or right.x == boss_x and right.y == boss_y:
        if boss_hp <= 0:
            HP = HP
            boss_dmg == 0    
        else:
            HP = HP - boss_dmg


############################# CHEST DROP #############################
    if lvl == 1:
        if mob1_hp <= 0:
            if right.colliderect(chest):
                opened = True
                while VEL_RIGHT < 5:
                    VEL_RIGHT = VEL_RIGHT + 1
                    
    if lvl == 2:
        if mob1_hp <= 0 and mob2_hp <= 0:
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
                    
    if 5 > lvl > 2 or 10 > lvl > 5 or 15 > lvl > 10 or 20 > lvl > 15:
        if mob1_hp <= 0 and mob2_hp <= 0 and mob3_hp <= 0:
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

    if lvl == 5 or lvl == 10 or lvl == 15 or lvl == 20:
        if boss_hp <= 0:
            CURRENTBOSS = MOB_DEAD
            VEL_BOSS = 0
            boss_dmg = 0
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


    if mob1_hp <= 0:
        VEL_MOB1 = 0
    
    if mob2_hp <= 0:
        VEL_MOB2 = 0
    
    if mob3_hp <= 0:
        VEL_MOB3 = 0

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
    elif 5 > lvl > 2 or 10 > lvl > 5 or 15 > lvl > 10 or 20 > lvl > 15:
        mob2_dmg = 0.1
        mob3_dmg = 0.1

    elif lvl == 5 or lvl == 10 or lvl == 15 or lvl == 20:
        boss_dmg = 0.1
        mob1_dmg = 0
        mob2_dmg = 0
        mob3_dmg = 0

############################# MOB MOVEMENT #############################
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

    if 5 > lvl > 2 or 10 > lvl > 5 or 15 > lvl > 10 or 20 > lvl > 15:
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
    
    if lvl == 5 or lvl == 10 or lvl == 15 or lvl == 20:
        if boss_y > right.y + 2:
            boss_y -= VEL_BOSS
        elif boss_y < right.y + 2:
            boss_y += VEL_BOSS

        if boss_x > right.x + 2:
            boss_x -= VEL_BOSS
        elif boss_x < right.x + 2:
            boss_x += VEL_BOSS
########################################################################            

############################# MOVEMENT #############################
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and right.x - VEL_RIGHT > 0:
        right.x -= VEL_RIGHT
        if HP < 0:
            pass
        else:
            CURRENTBODY = BODY_LEFT
    
    if keys_pressed[pygame.K_d] and right.x + VEL_RIGHT < WIDTH-CHARACTER_WIDTH :
        right.x += VEL_RIGHT
        if HP < 0:
            pass
        else:
            CURRENTBODY = BODY_RIGHT
        
     
    if keys_pressed[pygame.K_w] and right.y - VEL_RIGHT > 0-30:
        right.y -= VEL_RIGHT
        if HP < 0:
            pass
        else:
            CURRENTBODY = BODY_UP
        
        
    if keys_pressed[pygame.K_s] and right.y - VEL_RIGHT < HEIGHT-CHARACTER_HEIGHT:
        right.y += VEL_RIGHT
        if HP < 0:
            pass
        else:
            CURRENTBODY = BODY_UP
        
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        look = "left"
        CURRENTHEAD = HEAD_LEFT
    if keys_pressed[pygame.K_RIGHT]:
        look = "right"
        CURRENTHEAD = HEAD_RIGHT
    if keys_pressed[pygame.K_UP]:
        look = "up"
        CURRENTHEAD = HEAD_UP
    if keys_pressed[pygame.K_DOWN]:
        look = "down"
        CURRENTHEAD = HEAD_DOWN
##################################################################################        
    shot_delay += 1

    if keys_pressed[pygame.K_SPACE]:
        if shot_delay > next_shot:
            if look == "right":
                shoot_sound.play()   
                bullet_right = pygame.Rect(right.x + CHARACTER_WIDTH//2, right.y + 20, 15, 15)
                bullets_right.append(bullet_right)
            if look == "left":
                shoot_sound.play()
                bullet_left = pygame.Rect(right.x + CHARACTER_WIDTH//2, right.y + 20, 15, 15)
                bullets_left.append(bullet_left)
            if look == "down":
                shoot_sound.play()
                bullet_down = pygame.Rect(right.x + CHARACTER_WIDTH//2, right.y + 20, 15, 15)
                bullets_down.append(bullet_down)
            if look == "up":
                shoot_sound.play()
                bullet_up = pygame.Rect(right.x + CHARACTER_WIDTH//2, right.y + 20, 15, 15)
                bullets_up.append(bullet_up)
            next_shot = shot_delay + 30


    for bullet_right in bullets_right:
        if bullet_right.x > WIDTH or bullet_right.x < 0 or bullet_right.y > HEIGHT or bullet_right.y < 0:
            bullets_right.remove(bullet_right)
    for bullet_left in bullets_left:
        if bullet_left.x > WIDTH or bullet_left.x < 0 or bullet_left.y > HEIGHT or bullet_left.y < 0:
            bullets_left.remove(bullet_left)
    for bullet_down in bullets_down:
        if bullet_down.x > WIDTH or bullet_down.x < 0 or bullet_down.y > HEIGHT or bullet_down.y < 0:
            bullets_down.remove(bullet_down)
    for bullet_up in bullets_up:
        if bullet_up.x > WIDTH or bullet_up.x < 0 or bullet_up.y > HEIGHT or bullet_up.y < 0:
            bullets_up.remove(bullet_up)

    if 5 > lvl > 0 or 10 > lvl > 5 or 15 > lvl > 10 or 20 > lvl > 15:
        for bullet_right in bullets_right:
            if bullet_right.x - 50 < mob1_x < bullet_right.x + 50 and bullet_right.y - 90< mob1_y < bullet_right.y + 50 or bullet_right.x == mob1_x and bullet_right.y == mob1_y:
                mob1_hp -= 10
                bullets_right.remove(bullet_right)

        for bullet_left in bullets_left:
            if bullet_left.x - 50 < mob1_x < bullet_left.x + 50 and bullet_left.y - 90< mob1_y < bullet_left.y + 50 or bullet_left.x == mob1_x and bullet_left.y == mob1_y:
                mob1_hp -= 10
                bullets_left.remove(bullet_left)

        for bullet_down in bullets_down:
            if bullet_down.x - 50 < mob1_x < bullet_down.x + 50 and bullet_down.y - 90< mob1_y < bullet_down.y + 50 or bullet_down.x == mob1_x and bullet_down.y == mob1_y:
                mob1_hp -= 10
                bullets_down.remove(bullet_down)

        for bullet_up in bullets_up:
            if bullet_up.x - 50 < mob1_x < bullet_up.x + 50 and bullet_up.y - 90< mob1_y < bullet_up.y + 50 or bullet_up.x == mob1_x and bullet_up.y == mob1_y:
                mob1_hp -= 10
                bullets_up.remove(bullet_up)
    if 5 > lvl > 1 or 10 > lvl > 5 or 15 > lvl > 10 or 20 > lvl > 15:
        for bullet_right in bullets_right:
            if bullet_right.x - 50 < mob2_x < bullet_right.x + 50 and bullet_right.y - 90< mob2_y < bullet_right.y + 50 or bullet_right.x == mob2_x and bullet_right.y == mob2_y:
                mob2_hp -= 10
                bullets_right.remove(bullet_right)

        for bullet_left in bullets_left:
            if bullet_left.x - 50 < mob2_x < bullet_left.x + 50 and bullet_left.y - 90< mob2_y < bullet_left.y + 50 or bullet_left.x == mob2_x and bullet_left.y == mob2_y:
                mob2_hp -= 10
                bullets_left.remove(bullet_left)

        for bullet_down in bullets_down:
            if bullet_down.x - 50 < mob2_x < bullet_down.x + 50 and bullet_down.y - 90< mob2_y < bullet_down.y + 50 or bullet_down.x == mob2_x and bullet_down.y == mob2_y:
                mob2_hp -= 10
                bullets_down.remove(bullet_down)

        for bullet_up in bullets_up:
            if bullet_up.x - 50 < mob2_x < bullet_up.x + 50 and bullet_up.y - 90< mob2_y < bullet_up.y + 50 or bullet_up.x == mob2_x and bullet_up.y == mob2_y:
                mob2_hp -= 10
                bullets_up.remove(bullet_up)
    
    if 5 > lvl > 2 or 10 > lvl > 5 or 15 > lvl > 10 or 20 > lvl > 15:
        for bullet_right in bullets_right:
            if bullet_right.x - 50 < mob3_x < bullet_right.x + 50 and bullet_right.y - 90< mob3_y < bullet_right.y + 50 or bullet_right.x == mob3_x and bullet_right.y == mob3_y:
                mob3_hp -= 10
                bullets_right.remove(bullet_right)

        for bullet_left in bullets_left:
            if bullet_left.x - 50 < mob3_x < bullet_left.x + 50 and bullet_left.y - 90< mob3_y < bullet_left.y + 50 or bullet_left.x == mob3_x and bullet_left.y == mob3_y:
                mob3_hp -= 10
                bullets_left.remove(bullet_left)

        for bullet_down in bullets_down:
            if bullet_down.x - 50 < mob3_x < bullet_down.x + 50 and bullet_down.y - 90< mob3_y < bullet_down.y + 50 or bullet_down.x == mob3_x and bullet_down.y == mob3_y:
                mob3_hp -= 10
                bullets_down.remove(bullet_down)

        for bullet_up in bullets_up:
            if bullet_up.x - 50 < mob3_x < bullet_up.x + 50 and bullet_up.y - 90< mob3_y < bullet_up.y + 50 or bullet_up.x == mob3_x and bullet_up.y == mob3_y:
                mob3_hp -= 10
                bullets_up.remove(bullet_up)
    #print(boss_x, boss_x + 100)
    if lvl == 5 or lvl == 10 or lvl == 15 or lvl == 20:
        for bullet_right in bullets_right:
            if boss_x < bullet_right.x < boss_x + 150 and boss_y < bullet_right.y < boss_y + 180 or bullet_right.x == boss_x and bullet_right.y == boss_y:
                boss_hp -= 10
                bullets_right.remove(bullet_right)

        for bullet_left in bullets_left:
            if boss_x < bullet_left.x < boss_x + 150 and boss_y < bullet_left.y < boss_y + 180 or bullet_left.x == boss_x and bullet_left.y == boss_y:
                boss_hp -= 10
                bullets_left.remove(bullet_left)

        for bullet_down in bullets_down:
            if boss_x < bullet_down.x < boss_x + 150 and boss_y < bullet_down.y < boss_y + 150 or bullet_down.x == boss_x and bullet_down.y == boss_y:
                boss_hp -= 10
                bullets_down.remove(bullet_down)

        for bullet_up in bullets_up:
            if boss_x < bullet_up.x < boss_x + 150 and boss_y < bullet_up.y < boss_y + 150 or bullet_up.x == boss_x and bullet_up.y == boss_y:
                boss_hp -= 10
                bullets_up.remove(bullet_up)




    keys_pressed = pygame.key.get_pressed()
    handle_bullets(bullets_right,bullets_down,bullets_left,bullets_up, right, mob1, mob1_hp,  bullet_right, bullet_left, bullet_up, bullet_down, mob2, mob2_hp, mob3, mob3_hp)

    rajzok(right, bullets_right,bullets_down,bullets_left,bullets_up, bullet_right, bullet_left, bullet_up, bullet_down)
pygame.quit()