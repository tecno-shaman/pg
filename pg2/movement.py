import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    FPS = 50
    running = True
    do_paint = False
    pygame.draw.rect(screen, (0, 255, 0), (0, 0, 100, 100))
    rect = (0, 0, 100, 100)
    down = False

    while running:

        for event in pygame.event.get():
            # screen.fill((0, 0, 0))
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                down = True
                pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                down = False
            if (down and rect[0] < pos[0] <= rect[0] + rect[2] and rect[1] < pos[1] <= rect[1] + rect[3] and
                    event.type == pygame.MOUSEMOTION):
                screen.fill((0, 0, 0))
                cur = event.pos
                rect = (rect[0] + cur[0] - pos[0], rect[1] + cur[1] - pos[1], rect[2], rect[3])
                pygame.draw.rect(screen, (0, 255, 0), rect)
                pos = cur

        pygame.display.flip()
    pygame.quit()
