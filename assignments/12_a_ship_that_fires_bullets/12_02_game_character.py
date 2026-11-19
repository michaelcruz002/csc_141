
# 12-2 Game Character: Display a character in the center.
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Character")

blue = (135, 206, 235)

# Create a simple character image.
image = pygame.Surface((80, 120))
image.fill(blue)

pygame.draw.circle(image, (255, 220, 180), (40, 25), 20)
pygame.draw.rect(image, (255, 0, 0), (20, 45, 40, 50))
pygame.draw.rect(image, (0, 0, 255), (20, 95, 15, 25))
pygame.draw.rect(image, (0, 0, 255), (45, 95, 15, 25))

pygame.image.save(image, "character.bmp")

class Character:
    def __init__(self):
        self.image = pygame.image.load("character.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center

    def draw(self):
        screen.blit(self.image, self.rect)


character = Character()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(blue)
    character.draw()
    pygame.display.flip()

pygame.quit()
