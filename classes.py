import pygame, math, random
from random import randint



class BaseClass(pygame.sprite.Sprite):# inherit from this, collision, draw etc..

    allsprites = pygame.sprite.Group() #list-like

    def __init__(self, x, y ,  image_string):

        pygame.sprite.Sprite.__init__(self) # this gives us acces to image, rect etc
        BaseClass.allsprites.add(self)

        # self.image # image itself
        # self.rect #rect of an image, height, width

        self.image = pygame.image.load(image_string)
        self.rect  = self.image.get_rect()#datas of the image
        self.rect.x = x
        self.rect.y = y
        #self.rect.width/rect

    def destroy(self, ClassName): #whenever we want to delete smthng
        #remove sprite from the list, and local list

        ClassName.List.remove(self)
        BaseClass.allsprites.remove(self)
        del self

class Spaceship(BaseClass):

    List = pygame.sprite.Group() #list of spaceships which makes easier to draw multiple objects
    going_up = True
    def __init__(self, x, y , image_string):

        BaseClass.__init__(self, x, y , image_string)
        Spaceship.List.add(self)
        self.velx, self.vely = 0.0, 0.0
        self.jumping, self.go_down = False, False # jump = true either going up / down


    def motion(self, SCREENWIDTH, SCREENHEIGHT):

        #since the image is bouncy at the sides
        predicted_locationx = self.rect.x + self.velx
        predicted_locationy = self.rect.y - self.vely

        if predicted_locationx < 0.0 :
            self.velx = 0.0
        elif predicted_locationx + self.rect.width > SCREENWIDTH:
            self.velx = 0.0
        if predicted_locationy < 75:
            self.vely = 0.0
        elif predicted_locationy + self.rect.height > SCREENHEIGHT:
            self.vely = 0.0

        #self.__jump(SCREENHEIGHT)

        self.rect.x += self.velx
        self.rect.y -= self.vely
    def __jump(self,SCREENHEIGHT): #if wanted to have gravity

        max_jump = 75 #maximum horizontal line

        if self.jumping:

            if self.rect.y < max_jump:
                self.go_down = True

            if self.go_down:
                self.rect.y += self.vely #downwards

                predicted_location = self.rect.y + self.vely #while going d, check where we are going

                if predicted_location + self.rect.height > SCREENHEIGHT:
                    self.jumping = False
                    self.go_down = False

            else:
                self.rect.y -= self.vely

class Enemy(BaseClass):

    List = pygame.sprite.Group()#list containing all enemies
    def __init__(self,  x, y , image_string):
        BaseClass.__init__(self, x, y , image_string)
        Enemy.List.add(self)
        self.health = 100
        self.half_health = self.health / 2.0
        self.vely = 1
        self.amplitude, self.period = randint(5, 10), randint (1, 2) / 100.0

    @staticmethod
    def update_all(SCREENHEIGHT):
        #similar to draw(screen), but it cannot have any parameter // update() method

        for enemy in Enemy.List:

            enemy.enemy(SCREENHEIGHT)

            if enemy.health <= 0:
                enemy.destroy(Enemy)


    def enemy(self, SCREENHEIGHT):

        if self.rect.y> SCREENHEIGHT:
            #self.image = pygame.transform.flip( self.image, True, False) #transforms the image itself
            self.rect.y = -30

        self.rect.y += self.vely

        # sine curve --- a *sin(bx+ c) + y, a amplitude, b periode, c shift

        #self.rect.x = self.amplitude * math.sin(self.rect.y * self.period) + 140


'''    @staticmethod  #i can call it using class name, class method, not object method, no slef
    def movement(SCREENHEIGHT):
        for enemy in Enemy.List:
            enemy.enemy(SCREENHEIGHT)'''

class SpaceshipProjectile(pygame.sprite.Sprite):

    List = pygame.sprite.Group()
    normal_list = [] #its almsot the same, but easier to manipulate


    def __init__(self, x , y , image_string):

        pygame.sprite.Sprite.__init__(self)  #it wouldnt work without this

        self.image = pygame.image.load(image_string)

        self.rect = self.image.get_rect()  # datas of the image

        self.rect.x = x
        self.rect.y = y


        self.rect.width
        self.rect.height

        try:
            last_element = SpaceshipProjectile.normal_list[-1]
            difference = abs(self.rect.y - last_element.rect.y)

            if difference < self.rect.height + 10:
                return

        except Exception:
            pass

        SpaceshipProjectile.normal_list.append(self)
        SpaceshipProjectile.List.add(self)
        self.vely = None
    @staticmethod
    def movement(): #looping thru all the projectiles, which will be in the list

        for projectile in SpaceshipProjectile.List:
            projectile.rect.y -= projectile.vely
            if projectile.rect.y < -100: #ez legyen - y dimenzioja a kepnek
                SpaceshipProjectile.List.remove(projectile)

