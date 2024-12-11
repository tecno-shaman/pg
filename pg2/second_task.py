import pygame
from random import randrange

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    FPS = 50
    clock = pygame.time.Clock()
    running = True
    do_paint = False
    v = 100
    R = 10
    list_circle = []
    while running:
        t = clock.tick()

        for event in pygame.event.get():
            screen.fill((0, 0, 0))
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((0, 0, 0))
                x, y = event.pos
                list_circle.append([(x, y), R, (randrange(256), randrange(256), randrange(256)), (-1, -1)])

        screen.fill((0, 0, 0))
        for c in list_circle:
            pygame.draw.circle(screen, c[2], c[0], c[1])
        for c in list_circle:
            x, y = c[0]
            dx, dy = c[3]
            x += dx * v * t / 1000
            y += dy * v * t / 1000
            if x - R <= 0:
                x = R
                dx = 1
            if x + R >= width:
                x = width - R
            if y - R <= 0:
                y = runningdy = 1
            if y + R >= height:
                y = runningdy = height - R
                dy -= 1
            c[0] = x, y
            c[3] = dx, dy

        pygame.display.flip()
    pygame.quit()
