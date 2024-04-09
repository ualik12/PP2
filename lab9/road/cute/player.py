import pygame
import set

class Player:
    def __init__(self):
        self.width = 60
        self.aspect_ratio = 0.5
        self.height = self.width / self.aspect_ratio
        self.image = pygame.image.load(
            "/Users/ualihanbisenev/Desktop/File_cabinet/KBTU/PP2_Spring_for_clone/PP2-1-Spring-2024/pygame_ualik/road/images/cars/car_green.png"
        )
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (set.SCREEN_WIDTH // 2, set.SCREEN_HEIGHT - 100)
        self.MOVEMENT_SPEED = set.SPEED * 4

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.move_ip(-self.MOVEMENT_SPEED, 0)
        if pressed[pygame.K_RIGHT]:
            if self.rect.right < set.SCREEN_WIDTH:
                self.rect.move_ip(self.MOVEMENT_SPEED, 0)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)