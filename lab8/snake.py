import pygame
import sys
import random

pygame.init()
cell_size = 10

screen_size = 500
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Snake")


black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)


snake_pos = [100, 100]
snake_body = [[100, 100], [90, 100], [80, 100]]
direction = 'RIGHT'
change_to = direction


def generate_food(count):
    food_positions = []
    while len(food_positions) < count:
        food_x = random.randint(0, (screen_size // cell_size) - 1) * cell_size
        food_y = random.randint(0, (screen_size // cell_size) - 1) * cell_size
        if [food_x, food_y] not in snake_body and [food_x, food_y] not in food_positions:
            food_positions.append([food_x, food_y])
    return food_positions

food_count = 1 
food_positions = generate_food(food_count)


score = 0
level = 1
speed = 10
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
    
    direction = change_to

   
    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size

   
    if snake_pos[0]<0:
        snake_pos[0]=500-cell_size
    elif snake_pos[0]>=500:
        snake_pos[0]=0
    elif snake_pos[1]<0:
        snake_pos[0]=500-cell_size
    elif snake_pos[1]>=500:
        snake_pos[1]=0


    snake_body.insert(0, list(snake_pos))
    
    for food in food_positions:
        if snake_pos == food:
            score += 1
            food_positions.remove(food)
            if not food_positions: 
                food_count = min(level + 1, 5)  
                food_positions = generate_food(food_count)
                level += 1
                speed += 2
            break
    else:
        snake_body.pop()  
    
  
    for block in snake_body[1:]:
        if snake_pos == block:
            running = False
    
   
    screen.fill(black)
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))
    for food in food_positions:
        pygame.draw.rect(screen, red, pygame.Rect(food[0], food[1], cell_size, cell_size))
    
    
    font = pygame.font.SysFont("Arial", 20)
    score_text = font.render(f"Score: {score}  Level: {level}", True, white)
    screen.blit(score_text, [10, 10])
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()
