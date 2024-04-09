import pygame
import set
import player
import coin
import math

pygame.init()
screen = pygame.display.set_mode(
    (set.SCREEN_WIDTH, set.SCREEN_HEIGHT), flags=pygame.SCALED, vsync=1
)

FPS = 60
clock = pygame.time.Clock()
running = True

player = player.Player()
coin = coin.Coin()

coins = 0
scroll = 0
speed = set.SPEED

font = pygame.font.Font("/Users/ualihanbisenev/Library/Fonts/Comic Sans MS.ttf", 40)

bg = pygame.image.load(
    "/Users/ualihanbisenev/Desktop/File_cabinet/KBTU/PP2_Spring_for_clone/PP2-1-Spring-2024/pygame_ualik/road/images/bg.png"
)
BG_WIDTH = set.SCREEN_WIDTH
BG_ASPECT_RATIO = bg.get_width() / bg.get_height()
BG_HEIGHT = math.ceil(set.SCREEN_HEIGHT / BG_ASPECT_RATIO)
bg = pygame.transform.scale(bg, (BG_WIDTH, BG_HEIGHT))
COPIES = math.ceil(set.SCREEN_HEIGHT / bg.get_height()) + 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(set.WHITE)
    scroll = (scroll + speed // 1.5) % bg.get_height()
    for i in range(COPIES):
        screen.blit(bg, (0, scroll + (i - 1) * (bg.get_height() - 1)))

    coins_counter = font.render(str(coins), True, set.BLACK)
    screen.blit(coins_counter, (set.SCREEN_WIDTH - 50, 10))

    player.draw(screen)
    coin.draw(screen)
    coin.ChangeSpeed(speed)
    player.move()
    coin.move()

    if player.rect.colliderect(coin.rect):
        coin.__init__()
        coins += 1
    
    pygame.display.flip()
    clock.tick(FPS)
