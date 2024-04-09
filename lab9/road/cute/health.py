import pygame

class Health:
    def __init__(self):
        self.width = 20
        self.aspect_ratio = 1
        self.height = self.width / self.aspect_ratio
        self.health_quantity = 3
        self.image = pygame.image.load("/Users/ualihanbisenev/Desktop/File_cabinet/KBTU/PP2_Spring_for_clone/PP2-1-Spring-2024/pygame_ualik/road/images/love.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.width))
        self.rect = self.image.get_rect()

    def render(self, center, screen):
        self.rect.center = center
        screen.blit(self.image, self.rect)