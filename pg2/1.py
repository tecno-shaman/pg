import pygame
import random

def draw_stars(screen):
    for i in range(10000):
        color = pygame.Color(random.randrange(256), random.randrange(256), random.randrange(256))
        screen.fill(color,
                    (random.random() * width,
                     random.random() * height, 1, 1))

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    x_pos = -20
    y_pos = random.randrange(height)

    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        # отрисовка и изменение свойств объектов
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (x_pos, y_pos), 20)
        x_pos += 1

        if x_pos > width + 20:
            x_pos = -20
            y_pos = random.randrange(height)
        draw_stars(screen)

        # обновление экрана
        pygame.display.flip()
    pygame.quit()