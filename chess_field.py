import pygame
import random

def draw(screen):
    screen.fill((255, 255, 255))


def draw_rect(screen):
    # pygame.draw.rect(screen, 'red', (1, 1, width - 2, height - 2))
    d = size / n
    for row in range(n):
        for col in range(n):
            if (row + col) % 2 != 0:
                pygame.draw.rect(screen, 'white', (col * d, row * d, d, d))


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    try:
        width, n = map(int, input().split())
        height = width
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
        draw_rect(screen)
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
