import pygame
import set
import os
import random


class Enemy:
    def __init__(self):
        self.width = 60
        self.aspect_ratio = 0.5
        self.height = self.width / self.aspect_ratio
        self.colors = os.listdir("/Users/ualihanbisenev/Desktop/File_cabinet/KBTU/PP2_Spring_for_clone/PP2-1-Spring-2024/pygame_ualik/road/images/cars")
        try:
            self.image = pygame.image.load("/Users/ualihanbisenev/Desktop/File_cabinet/KBTU/PP2_Spring_for_clone/PP2-1-Spring-2024/pygame_ualik/road/images/cars/" + str(random.choice(self.colors)))
        except pygame.error as e:
            self.image = pygame.image.load("/Users/ualihanbisenev/Desktop/File_cabinet/KBTU/PP2_Spring_for_clone/PP2-1-Spring-2024/pygame_ualik/road/images/cars/" + str(random.choice(self.colors)))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = self.randomize_position()
        self.speed = set.SPEED

    def randomize_position(self):
        y = int(-self.height)
        x = random.randint(
            10 + self.rect.width, set.SCREEN_WIDTH - 10 - self.rect.width
        )
        return x, y

    def update(self):
        try:
            self.image = pygame.image.load("/Users/ualihanbisenev/Desktop/File_cabinet/KBTU/PP2_Spring_for_clone/PP2-1-Spring-2024/pygame_ualik/road/images/cars/" + str(random.choice(self.colors)))
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.image = pygame.transform.rotate(self.image, 180)
        except pygame.error as e:
            # print('Error loading image:', e)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.image = pygame.transform.rotate(self.image, 0)
        self.rect.center = self.randomize_position()

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > set.SCREEN_HEIGHT:
            self.update()

    def ChangeSpeed(self, speed):
        self.speed = speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)