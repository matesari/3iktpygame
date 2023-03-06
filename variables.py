import pygame
import random
import os

GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
TRANSPARENT = (0, 0, 0, 0)
right_hit = pygame.USEREVENT + 1

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
WIDTH, HEIGHT = 900, 500
CHARACTER_WIDTH, CHARACTER_HEIGHT = 110, 90
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
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
dmg_up_txt = False
hp_up_txt = False
speed_up_txt = False
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
chest = pygame.Rect(400, 200, CHARACTER_WIDTH, CHARACTER_HEIGHT)
chest_opened = pygame.Rect(400, 200, CHARACTER_WIDTH, CHARACTER_HEIGHT)
right = pygame.Rect(700, 100, CHARACTER_WIDTH, CHARACTER_HEIGHT)
mob1 = pygame.Rect(mob1_x, mob1_y, MOB_WIDTH, MOB_HEIGHT)
mob2 = pygame.Rect(mob2_x, mob2_y, MOB_WIDTH, MOB_HEIGHT)
mob3 = pygame.Rect(mob3_x, mob3_y, MOB_WIDTH, MOB_HEIGHT)
boss = pygame.Rect(boss_x, boss_y, CHARACTER_HEIGHT * 2, CHARACTER_HEIGHT * 2)