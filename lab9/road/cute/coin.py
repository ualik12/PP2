import pygame
import set
import random


class Coin:
    def __init__(self):
        self.width = 20
        self.acpect_ratio = 1
        self.height = self.width / self.acpect_ratio
        self.image = pygame.image.load(
            "/Users/ualihanbisenev/Desktop/File_cabinet/KBTU/PP2_Spring_for_clone/PP2-1-Spring-2024/pygame_ualik/road/images/coin.png"
        )
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = self.randomize_position()
        self.speed = set.SPEED
        self.price = random.randint(1, 5)
    
    def randomize_position(self):
        y = int(-self.height)
        x = random.randint(
            10 + self.rect.width, set.SCREEN_WIDTH - 10 - self.rect.width
        )
        return x, y

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > set.SCREEN_HEIGHT:
            self.__init__()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
