import pygame
import time
import math
pygame.init()

#басты экран параметрлері
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Mickey clock")
#Мискеу маус сағаты импорттау
fon = pygame.image.load('images/Mickey_without_hands.PNG')
fon = pygame.transform.scale(fon, (800, 800))
#Оң және солқолдарды импорттау
right_hand = pygame.image.load('images/mickey_right.PNG')
left_hand=pygame.image.load('images/mickey_left.PNG')
center_x ,center_y = 400,400
clock = pygame.time.Clock()
running = True
#қайта жаңарту үшін цикл
while running:
    current_time=time.localtime()
    second=current_time.tm_sec
    minute=current_time.tm_min

#мин және секунд бұрыш арқылы аламыз
    min_angle = minute*6+(second*(360/60)/60)
    sec_angle = second*6

#цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#микки маус суретін шығару
    screen.blit(fon, (0, 0))
#Оң қолды минут арқылы айналдыру
    rotated_r=pygame.transform.rotate(pygame.transform.scale(right_hand,(800,800)),-min_angle)
    r_hand_rect=rotated_r.get_rect(center=(center_x,center_y+12))
    screen.blit(rotated_r,r_hand_rect)
#Сол қолды секунд арқфлы айналдыру
    rotated_l= pygame.transform.rotate(pygame.transform.scale(left_hand, (800,800)), -sec_angle)
    l_hand_rect = rotated_l.get_rect(center=(center_x, center_y + 10))
    screen.blit(rotated_l, l_hand_rect)

#экран жаңарту
    pygame.display.flip()
    pygame.time.wait(1000)
    clock.tick(60)

pygame.quit()