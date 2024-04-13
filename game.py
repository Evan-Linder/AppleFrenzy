import pygame
import random

class Game:
    # game constants
    WIDTH, HEIGHT = 500, 500
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    APPLE_RADIUS = 7
    APPLE_SPAWN_DELAY = 1200
    FRAME_DELAY = 250 
    AVATAR_SPEED = 0.03 

    def __init__(self):
        # initialize
        pygame.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Apple Frenzy")
        self.clock = pygame.time.Clock()
        self.last_spawn_time = 0  # track the last time an apple was spawned.
        self.apples = []  # store the positions of spawned apples
        self.score = 0  # initialize score
        self.font = pygame.font.Font(None, 36)  # font for scoring text
        self.sprite_sheet_image = pygame.image.load('assets/Dino.png').convert_alpha()
        self.frame_width, self.frame_height = 24, 24
        self.scale = 3
        self.frame = 0  # current frame of the animation
        self.frame_count = 15  # total number of frames in the animation
        self.avatar_x = (self.WIDTH - self.frame_width * self.scale) // 2  # initial x-coordinate of the avatar
        self.avatar_y = (self.HEIGHT - self.frame_height * self.scale) // 2  # initial y-coordinate of the avatar
        self.is_moving = False  # flag to indicate if the character is moving
        self.last_frame_update = pygame.time.get_ticks()  # track the time of the last frame update

    def draw_apples(self):
        current_time = pygame.time.get_ticks()  # get the current time
        if current_time - self.last_spawn_time > self.APPLE_SPAWN_DELAY:  # check if enough time has passed since last spawn
            x = random.randint(0, self.WIDTH)  # choose a random x coordinate for apples
            y = random.randint(0, self.HEIGHT)  # choose a random y coordinate for apples, avoiding the bottom half of the window
            self.apples.append((x, y))
            self.last_spawn_time = current_time  # update last spawn time

        for apple_pos in self.apples:
            # Draw apple body
            pygame.draw.circle(self.win, self.RED, apple_pos, self.APPLE_RADIUS)
            # Draw apple stem
            pygame.draw.circle(self.win, self.GREEN, (apple_pos[0], apple_pos[1] - self.APPLE_RADIUS), 2)

            # Check for collision with dinosaur
            dino_rect = pygame.Rect(self.avatar_x, self.avatar_y, self.frame_width * self.scale, self.frame_height * self.scale)
            apple_rect = pygame.Rect(apple_pos[0] - self.APPLE_RADIUS, apple_pos[1] - self.APPLE_RADIUS, 2 * self.APPLE_RADIUS, 2 * self.APPLE_RADIUS)
            if dino_rect.colliderect(apple_rect):
                self.apples.remove(apple_pos)
                self.score += 1  # increment score when apple is picked up

    def draw_avatar(self):
        # Draw the current frame of the avatar animation at its current position
        self.win.blit(pygame.transform.scale(self.sprite_sheet_image.subsurface(pygame.Rect(self.frame * self.frame_width, 0, self.frame_width, self.frame_height)), (self.frame_width * self.scale, self.frame_height * self.scale)), (self.avatar_x, self.avatar_y))

    def update_animation(self):
        # Update the frame of the animation only when the character is moving and enough time has passed since the last update
        current_time = pygame.time.get_ticks()
        if self.is_moving and current_time - self.last_frame_update > self.FRAME_DELAY:
            self.frame = (self.frame + 1) % self.frame_count
            self.last_frame_update = current_time  # Update the last frame update time

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, self.RED)
        self.win.blit(score_text, (self.WIDTH * 0.4, 10))  # draw the score at (10, 10)

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            keys = pygame.key.get_pressed()
            # Move avatar based on pressed keys
            self.is_moving = False
            if keys[pygame.K_w]:
                self.avatar_y = max(self.avatar_y - self.AVATAR_SPEED, 0)  # Move up, ensuring it stays within the bounds
                self.is_moving = True
            if keys[pygame.K_s]:
                self.avatar_y = min(self.avatar_y + self.AVATAR_SPEED, self.HEIGHT - self.frame_height * self.scale)  # Move down, ensuring it stays within the bounds
                self.is_moving = True
            if keys[pygame.K_a]:
                self.avatar_x = max(self.avatar_x - self.AVATAR_SPEED, 0)  # Move left, ensuring it stays within the bounds
                self.is_moving = True
            if keys[pygame.K_d]:
                self.avatar_x = min(self.avatar_x + self.AVATAR_SPEED, self.WIDTH - self.frame_width * self.scale)  # Move right, ensuring it stays within the bounds
                self.is_moving = True  # Set is_moving to True when moving right
        
            self.win.fill((255, 255, 255))
            self.draw_apples()
            self.draw_avatar()
            self.update_animation()  # Update the animation frame
            self.draw_score()  # Draw the score text
            pygame.display.update()

        pygame.quit()









  




