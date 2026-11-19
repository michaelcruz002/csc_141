
# 12-1 Blue Sky: Create a window with a blue background.
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blue Sky")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135, 206, 235))
    pygame.display.flip()

pygame.quit()
