import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Paint ')

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 12, self.rect.y + 5))
    
    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.action()

drawing = False
brush_color = black
circle_mode = False
rectangle_mode = False
shape_start = None

def set_black():
    global brush_color
    brush_color = black

def set_green():
    global brush_color
    brush_color = green

def set_red():
    global brush_color
    brush_color = red

def set_blue():
    global brush_color
    brush_color = blue

def clear_screen():
    screen.fill(white)

def toggle_circle_mode():
    global circle_mode, rectangle_mode
    circle_mode = not circle_mode
    rectangle_mode = False

def toggle_rectangle_mode():
    global rectangle_mode, circle_mode
    rectangle_mode = not rectangle_mode
    circle_mode = False

def exit_app():
    pygame.quit()
    sys.exit()

buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Red', red, set_red),
    Button(150, 10, 60, 30, 'Green', green, set_green),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(290, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(360, 10, 60, 30, 'Exit', gray, exit_app),
    Button(430, 10, 80, 30, 'Circle', blue, toggle_circle_mode),
    Button(520, 10, 100, 30, 'Rectangle', blue, toggle_rectangle_mode)
]

clear_screen()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if circle_mode or rectangle_mode:
                    shape_start = event.pos
                else:
                    drawing = True
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if circle_mode and shape_start:
                    end_pos = event.pos
                    radius = int(((end_pos[0] - shape_start[0]) ** 2 + (end_pos[1] - shape_start[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, brush_color, shape_start, radius, 2)
                elif rectangle_mode and shape_start:
                    end_pos = event.pos
                    rect_x = min(shape_start[0], end_pos[0])
                    rect_y = min(shape_start[1], end_pos[1])
                    rect_width = abs(end_pos[0] - shape_start[0])
                    rect_height = abs(end_pos[1] - shape_start[1])
                    pygame.draw.rect(screen, brush_color, (rect_x, rect_y, rect_width, rect_height), 2)
                drawing = False
                shape_start = None
        
        for button in buttons:
            button.check_action(event)
    
    if drawing and not circle_mode and not rectangle_mode:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_y > 50:
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)
    
    pygame.draw.rect(screen, gray, (0, 0, width, 50))
    for button in buttons:
        button.draw(screen)
    
    pygame.display.flip()
