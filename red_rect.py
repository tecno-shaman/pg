import pygame
import random

def draw(screen):
    screen.fill((255, 255, 255))


def draw_rect(screen):
    pygame.draw.rect(screen, 'red', (1, 1, width - 2, height - 2))


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    try:
        width, height = map(int, input().split())
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
