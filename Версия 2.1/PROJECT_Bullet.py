import pygame
from PROJECT_Player import Player

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((0, 255, 0))
        self.rect = pygame.Rect(ship.rect.x + 8, ship.rect.y, 5, 5)
    def update(self):
        self.rect.y -= 5
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
class Fast_Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((0, 255, 0))
        self.rect = pygame.Rect(ship.rect.x + 8, ship.rect.y, 5, 5)
    def update(self):
        self.rect.y -= 12
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
class Big_Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))
        self.rect = pygame.Rect(ship.rect.x + 6, ship.rect.y, 10, 10)
    def update(self):
        self.rect.y -= 5
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
