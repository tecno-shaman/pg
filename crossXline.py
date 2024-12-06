import pygame
import random

def draw(screen):
    screen.fill((0, 0, 0))


def draw_line(screen):
    pygame.draw.line(screen, 'white', (0, 0), (width - 1, height - 1), 5)
    pygame.draw.line(screen, 'white', (0, height - 1), (width - 1, 0), 5)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    try:
        width, height = map(int, input().split())
        size = width, height
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Крест')
        # формирование кадра:
        # команды рисования на холсте
        draw(screen)
        draw_line(screen)
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
    except Exception:
        print('Неправильный формат ввода')
        pygame.quit()
