
# 12-5 Keys: Print the key number whenever a key is pressed.
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Keyboard Test")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            print(event.key)

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
