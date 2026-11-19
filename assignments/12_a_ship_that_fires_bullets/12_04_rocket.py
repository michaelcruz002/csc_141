
# 12-4 Rocket: Move a rocket using the four arrow keys.
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rocket")

rocket = pygame.Rect(375, 265, 50, 70)
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        rocket.x += 5
    if keys[pygame.K_LEFT]:
        rocket.x -= 5
    if keys[pygame.K_UP]:
        rocket.y -= 5
    if keys[pygame.K_DOWN]:
        rocket.y += 5

    # Keep the rocket inside the screen.
    rocket.clamp_ip(screen.get_rect())

    screen.fill((0, 0, 0))

    # Draw the rocket.
    pygame.draw.polygon(screen, (255, 0, 0), [
        (rocket.centerx, rocket.top),
        (rocket.left, rocket.bottom),
        (rocket.right, rocket.bottom)
    ])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
