import pygame
import random

def draw(screen):
    screen.fill((0, 0, 0))


def draw_dummy(screen):
    # pygame.draw.rect(screen, 'red', (1, 1, width - 2, height - 2))
    color = {0: 'red', 1: 'blue', 2: 'green'}
    for i in range(n):
        pygame.draw.circle(screen, color[i % 3], (size[0] / 2, size[0] / 2), w * (n - i))


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    try:
        w, n = map(int, input().split())
        width = height = w * n * 2

    except ValueError:
        print('Неправильный формат ввода')
        pygame.quit()
    except Exception as ex:
        print(ex)
        pygame.quit()
    else:
        size = width, height
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Крест')
        # формирование кадра:
        # команды рисования на холсте
        draw(screen)
        draw_dummy(screen)
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
