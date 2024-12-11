import pygame
import random

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0
    v = 500  # пикселей в секунду
    FPS = 60
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
        if x_pos > width + 20:
            x_pos = -20
            y_pos = random.randrange(height)

        x_pos += v / FPS  # v * t в секундах
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()