
# 12-6 Sideways Shooter: Move a ship and shoot bullets to the right.
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sideways Shooter")

ship = pygame.Rect(40, 280, 60, 40)
bullets = []
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(ship.right, ship.centery, 15, 5)
                bullets.append(bullet)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        ship.y -= 5

    if keys[pygame.K_DOWN]:
        ship.y += 5

    # Keep the ship inside the screen.
    ship.clamp_ip(screen.get_rect())

    # Move bullets and remove them when they leave the screen.
    for bullet in bullets[:]:
        bullet.x += 8

        if bullet.left > 800:
            bullets.remove(bullet)

    screen.fill((0, 0, 0))

    # Draw the spaceship.
    pygame.draw.polygon(screen, (0, 150, 255), [
        (ship.right, ship.centery),
        (ship.left, ship.top),
        (ship.left, ship.bottom)
    ])

    # Draw the bullets.
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
