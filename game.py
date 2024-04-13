import pygame
import random

class Game:
    # game constants
    WIDTH, HEIGHT = 500, 500
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    APPLE_RADIUS = 7
    APPLE_SPAWN_DELAY = 1000

    def __init__(self):
        # initalize
        pygame.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.last_spawn_time = 0  # track the last time an apple was spawned.
        self.apples = []  # store the positions of spawned apples
        self.sprite_sheet_image = pygame.image.load('assets/Dino.png').convert_alpha()

    def draw_apples(self):
        current_time = pygame.time.get_ticks()  # get the current time
        if current_time - self.last_spawn_time > self.APPLE_SPAWN_DELAY:  # check if enough time has passed since last spawn
            x = random.randint(0, self.WIDTH)  # chose a random x cord for apples
            y = random.randint(0, self.HEIGHT)  # chose a random y cord for apples
            self.apples.append((x, y))
            self.last_spawn_time = current_time  # update last spawn time
        
        for apple_pos in self.apples:
            pygame.draw.circle(self.win, self.RED, apple_pos, self.APPLE_RADIUS)  # draw apples
    
    def draw_avatar(self, sheet, width, height, scale):
        avatar_image = pygame.Surface((width, height)).convert_alpha()  # Create a surface for the avatar image
        avatar_image.blit(sheet, (0, 0), (0, 0, width, height))  # Blit the portion of the sprite sheet onto the avatar surface
        avatar_image = pygame.transform.scale(avatar_image, (width * scale, height * scale))  # Scale the avatar image
        self.win.blit(avatar_image, (0, 0))  # Draw the scaled avatar image on the window surface
        image.set_colorkey(colour )
    
    def move_avatar(self,)

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.win.fill((255, 255, 255))
            self.draw_apples()
            self.draw_avatar(self.sprite_sheet_image, 24, 24, 3)  
            self.clock.tick(60)
            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    game = Game() 
    game.run_game()   
