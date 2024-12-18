import pygame
import random


def draw_stars(screen):
    for i in range(10000):
        color = pygame.Color(random.randrange(256), random.randrange(256), random.randrange(256))
        screen.fill(color,
                    (random.random() * width,
                     random.random() * height, 1, 1))


def draw(screen):
    screen.fill((0, 0, 0))


def draw_text(screen):
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!", True, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)


def draw_line(screen):
    pygame.draw.line(screen, 'white', (0, 0), (width - 1, height - 1), 5)
    pygame.draw.line(screen, 'white', (0, height - 1), (width - 1, 0), 5)


def draw_square(screen):
    color = pygame.Color(50, 150, 50)
    # рисуем "тень"
    pygame.draw.rect(screen, color,
                     (20, 20, 100, 100), 0)
    hsv = color.hsva
    # увеличиваем параметр Value, который влияет на яркость
    color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3])
    # рисуем сам объект
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Всякая всячина')
    # формирование кадра:
    # команды рисования на холсте
    draw(screen)
    draw_stars(screen)
    draw_line(screen)
    draw_text(screen)
    draw_square(screen)
    # смена (отрисовка) кадра:
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
