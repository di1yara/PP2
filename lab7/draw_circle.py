import  pygame

pygame.init()
screen=pygame.display.set_mode((300,300))
pygame.display.set_caption("Draw circle")
red = (200,0,0)

x= 150
y = 150
radius = 25
speed=20

running = True
while running:
     pygame.time.delay(50)
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False

     keys = pygame.key.get_pressed()
     if keys[pygame.K_LEFT] and x - radius - speed >= 0:
         x -= speed
     if keys[pygame.K_RIGHT] and x + radius + speed <= 300:
         x += speed
     if keys[pygame.K_UP] and y - radius - speed >= 0:
         y -= speed
     if keys[pygame.K_DOWN] and y + radius + speed <= 300:
         y += speed
     screen.fill((255,255,255))
     pygame.draw.circle(screen, red, (x, y), radius)
     pygame.display.update()
pygame.quit()