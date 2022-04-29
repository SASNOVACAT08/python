import pygame

class Border(pygame.sprite.Sprite):
    def __init__(self, size, color, pos_y, pos_x=0):
        super().__init__()
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    