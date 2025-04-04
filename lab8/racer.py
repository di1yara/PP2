import pygame 
import sys
from pygame.locals import *
import random
import time
pygame.init()
pygame.mixer.init()  

#colors 
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
black=(0,0,0)

#main sizes
width=400
height=600
speed=5
score=0
clock=pygame.time.Clock()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Racer game")


#musics
pygame.mixer.music.load(r"C:\Users\HUAWEI\Desktop\PP2\Labs\lab8\CarX Music feat. SVRG - Drift and Bounce (Drift Racing 3).mp3")  
pygame.mixer.music.play(-1)  
pygame.mixer.music.set_volume(0.5)

#text
font = pygame.font.SysFont("Verdana", 30)
game_over = font.render("Game over", True, black)
game_over_rect=game_over.get_rect(center=(width//2,height//2))
background=pygame.image.load("AnimatedStreet.png")

#car1

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Enemy.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,width-40),0)



    def move(self):
        global score
        self.rect.move_ip(0,10)
        if(self.rect.bottom>height):
            score+=1
            self.rect.top=0
            self.rect.center=(random.randint(30,370),0)
    def draw(self,screen):
        screen.blit(self.image,self.rect)



#your car
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Player.png")
        self.rect=self.image.get_rect()
        self.rect.center=(160,520)

    def move(self):
        pressed_key=pygame.key.get_pressed()
        if self.rect.left>0:
            if pressed_key[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right<width:
            if pressed_key[K_RIGHT]:
                self.rect.move_ip(5,0)

    def draw(self,screen):
        screen.blit(self.image,self.rect)


p1=player()
e1=enemy()

enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)


inc_speed=pygame.USEREVENT+1
pygame.time.set_timer(inc_speed,1000)


runnning=False
background_y=0
while True:
    for event in pygame.event.get():
        if event.type==inc_speed:
            speed+=2
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    #move background
    screen.blit(background,(0,background_y))
    screen.blit(background,(0,background_y-600))

    background_y+=2
    if background_y>=600:
        background_y=0

    scores=font.render(str(score),True,black)
    screen.blit(scores,(10,10))

    for entity in all_sprites:
        screen.blit(entity.image,entity.rect)
        entity.move()
    

    #соқылуы
    if pygame.sprite.spritecollideany(p1,enemies):
        pygame.mixer.music.stop()  
        screen.fill(red)
        screen.blit(game_over,game_over_rect)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)
   