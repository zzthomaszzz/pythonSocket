import pygame
import client
from player import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player = Player(0, 0)
other_players = []
client = client.Client()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left = 1
            if event.key == pygame.K_d:
                player.right = 1
            if event.key == pygame.K_w:
                player.up = 1
            if event.key == pygame.K_s:
                player.down = 1
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left = 0
            if event.key == pygame.K_d:
                player.right = 0
            if event.key == pygame.K_w:
                player.up = 0
            if event.key == pygame.K_s:
                player.down = 0

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    player.update(dt)
    pygame.draw.rect(screen, "red", player.rect)

    client.send(["position", player.get_pos()])

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()