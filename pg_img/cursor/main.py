import pygame
import os

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Кастомный курсор")
background_color = (0, 0, 0)


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        pygame.quit()
        exit()
    return pygame.image.load(fullname)


cursor_image = load_image("arrow.png")
cursor_image = pygame.transform.scale(cursor_image, (30, 30))

pygame.mouse.set_visible(False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)

    if pygame.mouse.get_focused():
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(cursor_image, mouse_pos)

    pygame.display.flip()
pygame.quit()
