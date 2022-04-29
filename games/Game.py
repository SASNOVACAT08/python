from random import randint
import pygame
from Border import Border
from Player import Player
from Pipe import Pipe

class Game(object):
    def __init__(self, screen):
        self.game_over = False
        self.background = pygame.image.load("background.png")
        self.score = 0
        self.screen = screen
        self.player_sprites = pygame.sprite.Group()
        self.pipe_sprites = pygame.sprite.Group()
        self.score_sprites = pygame.sprite.Group()
        self.border_sprites = pygame.sprite.Group()
        self.deleter_sprites = pygame.sprite.Group()
        self.player = Player(screen)
        self.player_sprites.add(self.player)
        self.ground = Border([1000, 10], (0, 255, 0, 0), screen[1])
        self.sky = Border([1000, 10], (0, 0, 255, 0), -10)
        self.border_sprites.add(self.ground)
        self.border_sprites.add(self.sky)
        self.deleter = Border([10, 1000], (255, 0, 0), 0, -100)
        self.deleter_sprites.add(self.deleter)
        self.generatePipe()
        self.ting = pygame.mixer.Sound("ting.mp3")
        pygame.time.set_timer(pygame.USEREVENT, 2500)

    def generatePipe(self):
        screen = self.screen
        size_score = 170
        dist = screen[0]
        size_top = randint(20, screen[1]//1.3) - 588
        size_bottom = screen[1] + size_top + size_score
        pipe_top = Pipe(size_top, size_top, dist, 180)
        pipe_bottom = Pipe(size_bottom, size_bottom, dist, 0)
        pipe_score = Pipe(size_score, size_top + 588, dist + 54, 360)
        self.pipe_sprites.add(pipe_top)
        self.pipe_sprites.add(pipe_bottom)
        self.score_sprites.add(pipe_score)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.generatePipe()
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
            if self.game_over and (event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)):
                self.__init__(self.screen)
        return False
 
    def logic(self):
        if not self.game_over:
            self.player_sprites.update()
            self.pipe_sprites.update()
            self.score_sprites.update()
            hit = pygame.sprite.spritecollide(self.player, self.pipe_sprites, False) or pygame.sprite.spritecollide(self.player, self.border_sprites, False)
            if hit:
                self.game_over = True
                pygame.time.set_timer(pygame.USEREVENT, 0)
            score = pygame.sprite.spritecollide(self.player, self.score_sprites, False)
            if score:
                self.score_sprites.remove(score[0])
                self.ting.play()
                self.score+=1
            delete = pygame.sprite.spritecollide(self.deleter, self.pipe_sprites, False)
            if delete:
                self.pipe_sprites.remove(delete)

        
 
    def draw(self, screen):
        
        screen.blit(self.background, (0, 0))
        if not self.game_over:
            self.player_sprites.draw(screen)
            self.border_sprites.draw(screen)
            self.pipe_sprites.draw(screen)
            self.score_sprites.draw(screen)
            self.deleter_sprites.draw(screen)
            font = pygame.font.SysFont("Arial", 50)
            text = font.render(str(self.score), True, (0, 0, 0))
            screen.blit(text, (10, 10))
        else:
            font = pygame.font.SysFont("Arial", 50)
            scoring = font.render("Score : " + str(self.score), True, (0, 0, 0))
            screen.blit(scoring, (screen.get_width()/2 - scoring.get_width()/2, screen.get_height()/2 + scoring.get_height()/2 - 150))
            text = font.render("Game Over", True, (0, 0, 0))
            screen.blit(text, (screen.get_width()/2 - text.get_width()/2, screen.get_height()/2 - text.get_height()/2))
            font_restart = pygame.font.SysFont("Arial", 20)
            restart_text = font_restart.render("Cliquez n'importe où pour relancer (ou espace)", True, (0, 0, 0))
            screen.blit(restart_text, (screen.get_width()/2 - restart_text.get_width()/2, screen.get_height()/2 + restart_text.get_height()/2 + 50))
        
        pygame.display.flip()