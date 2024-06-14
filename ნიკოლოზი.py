import pygame
import sys
from random import randint, choice

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

GREEN = (50, 209, 93)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("anti ping pong")
background = pygame.image.load("back.png")


class Enemy:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = randint(0, WINDOW_WIDTH - self.width)
        self.y = randint(0, WINDOW_HEIGHT - self.height)
        self.color = choice([YELLOW, BLUE])
        self.speed = 3

    def move(self):
        self.x += self.speed
        if self.x > WINDOW_WIDTH:
            self.x = -self.width
            self.y = randint(0, WINDOW_HEIGHT - self.height)

    def draw(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

enemies = [Enemy() for _ in range(10)]

player_width = 10
player_height = 100
player_x = 600
player_y = 350
player_speed = 5

running = True
game_over = False

while running:
    window.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < WINDOW_HEIGHT - player_height:
            player_y += player_speed


        for enemy in enemies:
            enemy.move()
            enemy.draw()

            # Collision detection between player and enemy
            if player_x < enemy.x + enemy.width and player_x + player_width > enemy.x \
                    and player_y < enemy.y + enemy.height and player_y + player_height > enemy.y:
                    enemy.x -= 2 * enemy.speed



    else:

        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, RED)
        window.blit(text, (200, 250))



    pygame.draw.rect(window, RED, (player_x, player_y, player_width, player_height))


    pygame.display.update()

    pygame.time.Clock().tick(120)

pygame.quit()
sys.exit()