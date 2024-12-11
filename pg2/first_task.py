import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    FPS = 50
    clock = pygame.time.Clock()
    running = True
    do_paint = False
    v = 10
    while running:

        for event in pygame.event.get():
            screen.fill((0, 0, 255))
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((0, 0, 255))
                do_paint = True
                r = 1
                pos = event.pos
        if do_paint:
            r += v * clock.tick() / 1000
            pygame.draw.circle(screen, (255, 255, 0), pos, int(r))
        pygame.display.flip()
    pygame.quit()
