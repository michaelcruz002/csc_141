
# 12-3 Pygame Documentation: Practice drawing shapes with Pygame.
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Practice")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0, 0), (200, 300), 50)
    pygame.draw.rect(screen, (0, 0, 255), (400, 250, 100, 100))
    pygame.draw.line(screen, (0, 255, 0), (100, 100), (700, 100), 5)

    pygame.display.flip()

pygame.quit()
