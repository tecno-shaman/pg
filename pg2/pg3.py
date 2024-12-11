import pygame
import random

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    FPS = 50
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, (255, 0, 0), event.pos, 20)

        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()