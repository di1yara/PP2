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
square_mode = False
right_triangle_mode = False
equilateral_triangle_mode = False
rhombus_mode = False
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
    global circle_mode, rectangle_mode, square_mode, right_triangle_mode, equilateral_triangle_mode, rhombus_mode
    circle_mode = not circle_mode
    rectangle_mode = square_mode = right_triangle_mode = equilateral_triangle_mode = rhombus_mode = False

def toggle_rectangle_mode():
    global rectangle_mode, circle_mode, square_mode, right_triangle_mode, equilateral_triangle_mode, rhombus_mode
    rectangle_mode = not rectangle_mode
    circle_mode = square_mode = right_triangle_mode = equilateral_triangle_mode = rhombus_mode = False

def toggle_square_mode():
    global square_mode, circle_mode, rectangle_mode, right_triangle_mode, equilateral_triangle_mode, rhombus_mode
    square_mode = not square_mode
    circle_mode = rectangle_mode = right_triangle_mode = equilateral_triangle_mode = rhombus_mode = False

def toggle_right_triangle_mode():
    global right_triangle_mode, circle_mode, rectangle_mode, square_mode, equilateral_triangle_mode, rhombus_mode
    right_triangle_mode = not right_triangle_mode
    circle_mode = rectangle_mode = square_mode = equilateral_triangle_mode = rhombus_mode = False

def toggle_equilateral_triangle_mode():
    global equilateral_triangle_mode, circle_mode, rectangle_mode, square_mode, right_triangle_mode, rhombus_mode
    equilateral_triangle_mode = not equilateral_triangle_mode
    circle_mode = rectangle_mode = square_mode = right_triangle_mode = rhombus_mode = False

def toggle_rhombus_mode():
    global rhombus_mode, circle_mode, rectangle_mode, square_mode, right_triangle_mode, equilateral_triangle_mode
    rhombus_mode = not rhombus_mode
    circle_mode = rectangle_mode = square_mode = right_triangle_mode = equilateral_triangle_mode = False

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
    Button(520, 10, 100, 30, 'Rectangle', blue, toggle_rectangle_mode),
    Button(630, 10, 80, 30, 'Square', blue, toggle_square_mode),
    Button(720, 10, 80, 30, 'R-Tri', blue, toggle_right_triangle_mode),
    Button(10, 50, 120, 30, 'Eq-Triangle', blue, toggle_equilateral_triangle_mode),
    Button(140, 50, 80, 30, 'Rhombus', blue, toggle_rhombus_mode)
]

clear_screen()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if circle_mode or rectangle_mode or square_mode or right_triangle_mode or equilateral_triangle_mode or rhombus_mode:
                    shape_start = event.pos
                else:
                    drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if shape_start:
                    end_pos = event.pos
                    x1, y1 = shape_start
                    x2, y2 = end_pos

                    if circle_mode:
                        radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                        pygame.draw.circle(screen, brush_color, shape_start, radius, 2)
                    elif rectangle_mode:
                        rect_x = min(x1, x2)
                        rect_y = min(y1, y2)
                        rect_w = abs(x2 - x1)
                        rect_h = abs(y2 - y1)
                        pygame.draw.rect(screen, brush_color, (rect_x, rect_y, rect_w, rect_h), 2)
                    elif square_mode:
                        side = min(abs(x2 - x1), abs(y2 - y1))
                        pygame.draw.rect(screen, brush_color, (x1, y1, side, side), 2)
                    elif right_triangle_mode:
                        pygame.draw.polygon(screen, brush_color, [(x1, y1), (x1, y2), (x2, y2)], 2)
                    elif equilateral_triangle_mode:
                        height = abs(y2 - y1)
                        base = height / (3 ** 0.5) * 2
                        pygame.draw.polygon(screen, brush_color, [
                            (x1, y2),
                            (x1 + base / 2, y1),
                            (x1 + base, y2)
                        ], 2)
                    elif rhombus_mode:
                        center_x = (x1 + x2) // 2
                        center_y = (y1 + y2) // 2
                        dx = abs(x2 - x1) // 2
                        dy = abs(y2 - y1) // 2
                        pygame.draw.polygon(screen, brush_color, [
                            (center_x, center_y - dy),
                            (center_x + dx, center_y),
                            (center_x, center_y + dy),
                            (center_x - dx, center_y)
                        ], 2)
                drawing = False
                shape_start = None

        for button in buttons:
            button.check_action(event)

    if drawing and not (circle_mode or rectangle_mode or square_mode or right_triangle_mode or equilateral_triangle_mode or rhombus_mode):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_y > 90:
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)

    pygame.draw.rect(screen, gray, (0, 0, width, 90))
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()

