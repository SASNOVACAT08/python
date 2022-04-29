import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        w, h = [25, 25]
        self.ball = pygame.image.load('ball.png')
        self.image = self.ball
        self.rect = self.image.get_rect()
        self.rect.x = screen[0] // 2 - w
        self.rect.y = screen[1] // 2 - h
        self.isJump = False
        self.velocity = 0
        self.timeInJump = 10
        self.rotation = 0
        self.flap = pygame.mixer.Sound('flap.mp3')
    
    def update(self):
        self.rotation += 1
        ball = pygame.transform.rotate(self.ball, self.rotation)
        self.image = ball
        if not self.isJump:
          self.rect.y += 4 * (1 + self.velocity)
          self.velocity += 0.1
        else:
          self.timeInJump -= 1
          self.rect.y -= 4
          if self.timeInJump == 0:
              self.isJump = False
        

    def jump(self):
        self.flap.play()
        self.isJump = True
        self.velocity = 0
        self.timeInJump = 10