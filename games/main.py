import pygame
from Game import Game

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500 

def main():
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Flappy Ball")
    pygame.mouse.set_visible(False)

    end = False
    game = Game(size)
 
    while not end:
        end = game.events()
        game.logic()
        game.draw(screen)
        pygame.time.delay(20)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()

