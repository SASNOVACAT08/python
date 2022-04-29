import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, y_size, y_pos, x_pos, rotate):
        super().__init__()
        pipe = pygame.image.load("pipe.png")
        if rotate == 0:
            pipe = pygame.transform.rotate(pipe, 0)
        elif rotate == 180:
            pipe = pygame.transform.rotate(pipe, 180)
        if rotate == 360:
            self.image = pygame.Surface([54, y_size], pygame.SRCALPHA)
            self.image.fill((0, 0, 0, 0))
        else:
            self.image = pipe
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self):
        self.rect.x -= 2