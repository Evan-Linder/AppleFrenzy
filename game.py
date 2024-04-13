
import pygame
import random

class Game:
# game constants
    WIDTH,HEIGHT = 800,500
    WHITE = (255,255,255)
    RED = (255,0,0)
    APPLE_RADIUS = 7

    def __init__(self):
        # initalize
        pygame.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    
    def draw_apples(self):
        x = random
        pygame.draw.circle(self.win, self.RED, (x,y),self.APPLE_RADIUS)

        





    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
            self.win.fill((255,255,255))
            self.draw_apples()
        pygame.quit()  





if __name__ == "__main__":
    game = Game() 
    game.run_game()      