import pygame
MOVE_SPEED = 4
WIDTH = 22
HEIGTH = 32
COLOR = (255, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = pygame.Surface((WIDTH, HEIGTH))
        self.image.fill(COLOR)
        self.rect = pygame.Rect(x, y, WIDTH, HEIGTH)
    def update(self, left, rigth):
        if left:
            self.xvel = -MOVE_SPEED
        if rigth:
            self.xvel = MOVE_SPEED
        if left == False and rigth == False:
            self.xvel = 0
        self.rect.x += self.xvel
        if self.rect.x + WIDTH >= 800:
            self.rect.x = 800 - WIDTH
        if self.rect.x <= 0:
            self.rect.x = 0
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
