import pygame, sys, classes, random

def process(spaceship, FPS, total_frames):
    # PROCESSESblack = (0,0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # PROCESSES
    keys = pygame.key.get_pressed() #returns a list of all the keys containing pressed ones

    if keys[pygame.K_d]:
        #spaceship.going_right = True

        #spaceship.image = pygame.image.load('shoot.png') because it would remain
        spaceship.velx = 1.0
    elif keys[pygame.K_a]:
       #spaceship.going_right = False
        #spaceship.image = pygame.image.load('shoot.png') if want to change the img when pressing down a key
        spaceship.velx = -1.0
    else:
        spaceship.velx = 0.0

    if keys[pygame.K_w]:

        #spaceship.jumping = True
        #spaceship.image = pygame.image.load('images/spaceship_forward.png')
        spaceship.going_up = True
        spaceship.vely = 1.0


    elif keys[pygame.K_s]:
        #spaceship.image = pygame.image.load("images/spaceship_backward.png")
        spaceship.vely = -1.0
        spaceship.going_up = False


    else:
        spaceship.vely = 0.0
        #spaceship.image = pygame.image.load("images/spaceship.png")

    if keys[pygame.K_SPACE]:
        spaceship.image = pygame.image.load("images/spaceship_shoot.png")
        p = classes.SpaceshipProjectile(spaceship.rect.x, spaceship.rect.y, "images/projectile/projectile1.png")
        if spaceship.going_up:
            p.vely = 1.7
        else:
            #p.image = pygame.transform.flip(p.image, True, False)
            p.vely = 1
    else:
        spaceship.image = pygame.image.load("images/spaceship.png")

    spawn(FPS, total_frames, "images/enemy.png")
    spawn(FPS, total_frames * 0.4, "images/enemy_big.png")
    collisions() # call this or else wont work!
    #PROCESSING
def spawn(FPS, total_frames, image_string):

    four_seconds = FPS * 4 #aprox spawn every 4 seconds

    if total_frames % four_seconds == 0:

        x, y = random.randint(1, 640), -200

        '''x = 1

        if r == 2:
            x = 640 - 35'''

        classes.Enemy(x , y, image_string)
        #classes.Enemy(r, t, 'images/enemy_big.png')


def collisions():

    #pygame.sprite.groupcollide(G1, G2, dokill, dokill) first group, second, when collide, remove obj in group 1 and group 2
    #looping thru enemies
    for enemy in classes.Enemy.List:

        enemy_proj = pygame.sprite.spritecollide(enemy, classes.SpaceshipProjectile.List, True) #if enemy hit projectile return a list of all the projectiles that hit, prem remove projectile from the list

        if len(enemy_proj) > 0: #1 proj hit!
            for hit in enemy_proj:
                enemy.health -= enemy.half_health
            enemy.image = pygame.image.load("images/explosion.png")
