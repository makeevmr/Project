import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15 , 15))
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(0, randint(300,500), 15, 15)
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
