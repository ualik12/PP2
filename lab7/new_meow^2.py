import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),flags = pygame.SCALED, vsync = 1)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)     

FPS = 60
clock = pygame.time.Clock()
running = True
screen.fill(WHITE)

MOVEMENT_SPEED = 15
CIRCLE_RADIUS = 35
INITIAL_X = 100
INITIAL_Y = 100

clock = pygame.time.Clock()
x = INITIAL_X
y = INITIAL_Y


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y = max(CIRCLE_RADIUS, y - MOVEMENT_SPEED)
    if pressed[pygame.K_DOWN]:
        y = min(SCREEN_HEIGHT - CIRCLE_RADIUS, y + MOVEMENT_SPEED)
    if pressed[pygame.K_LEFT]:
        x = max(CIRCLE_RADIUS, x - MOVEMENT_SPEED)
    if pressed[pygame.K_RIGHT]:
        x = min(SCREEN_WIDTH - CIRCLE_RADIUS, x + MOVEMENT_SPEED)
    if pressed[pygame.K_r]:
        MOVEMENT_SPEED += 5
    if pressed[pygame.K_s]:
        MOVEMENT_SPEED -= 5
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), CIRCLE_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)