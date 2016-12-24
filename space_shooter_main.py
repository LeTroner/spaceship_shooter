import pygame
import sys
import time
import random
from classes import *
from process import process



pygame.init()#betoltes

SCREENWIDTH, SCREENHEIGHT = 800, 800

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),0,32)
clock = pygame.time.Clock() #ora a jatekhoz
FPS = 360
total_frames = 0

background = pygame.image.load("images/background.png")
spaceship = Spaceship(0 , SCREENHEIGHT - 30 ,'images/spaceship.png')
enemy =  Enemy( SCREENWIDTH * 0.4, 50 , 'images/enemy.png')
enemy_big = Enemy(SCREENWIDTH * 0.2, -50, 'images/enemy_big.png')



clr1 = (2,34,57)
clr2 = (8, 56, 199)
clr3 = (244, 36, 126)

#i = 0
# ==== ====== Main Program Loop ==== ====
while True:
    process(spaceship, FPS, total_frames)
    #LOGIC
    spaceship.motion(SCREENWIDTH,SCREENHEIGHT)
    Enemy.update_all(SCREENWIDTH)
    SpaceshipProjectile.movement()
    total_frames += 1
    #if totalFrames % fivesecondsinterval == 0: #ha lement 5 masodperc, kiirjon valamit
    #   pass

    #LOGIC
    #DRAW
        #RGB
    screen.blit((background), (0, 0))
    BaseClass.allsprites.draw(screen)
    SpaceshipProjectile.List.draw(screen)
    pygame.display.update()#parameter nelkul mindent, vele csak azt

    #DRAW
pygame.display.set_caption('Space Shooter') # ablak cime

clock.tick(FPS)#parameter-> framepersec