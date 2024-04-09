import pygame
import set
import snake_s
import food


pygame.init()
screen = pygame.display.set_mode((set.SCREEN_WIDTH, set.SCREEN_HEIGHT))

clock = pygame.time.Clock()
# our class
snake = snake_s.Snake()
food_1 = food.Food()

def draw_grid():
    for i in range(0, set.SCREEN_HEIGHT, set.CELL):
        for j in range(0, set.SCREEN_WIDTH, set.CELL):
            pygame.draw.rect(screen, set.GRAY, (i, j, set.CELL, set.CELL), 1)

running = True
counter = 0
counter_fon = 0

font = pygame.font.Font("/Users/ualihanbisenev/Library/Fonts/Comic Sans MS.ttf", 40)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # move our snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            if event.key == pygame.K_RIGHT:
                snake.dx = 1 
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1 
                snake.dy = 0
    screen.fill(set.COLORS[counter_fon])

    snake.move()
    for i in range(len(snake.body) - 1, 0, -1):
        if food_1.pos.x == snake.body[i].x and food_1.pos.y == snake.body[i].y:
            food_1.regenerate()
    if snake.check_collision(food_1):
        counter += 1
        food_1.regenerate()

    coins_counter = font.render(str(counter), True, set.GRAY)
    screen.blit(coins_counter, (set.SCREEN_WIDTH - 50, 10))
    coins_counter_fon = font.render(str(counter_fon), True, set.GRAY)
    screen.blit(coins_counter_fon, (set.SCREEN_WIDTH - 50, set.CELL))
    
    if counter >= 4 and counter <8:
        counter_fon = 1
    if counter >= 8 and counter <12:
        counter_fon = 2
    if counter >= 12:
        counter_fon = 3

    snake.draw(screen)
    food_1.draw(screen)
    draw_grid()

    pygame.display.flip()
    clock.tick(set.FPS + counter_fon * 5)