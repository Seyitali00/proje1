import pygame

pygame.init()
ekran = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Test")

calisiyor = True
while calisiyor:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisiyor = False

pygame.quit()