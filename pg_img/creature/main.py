import pygame
import os

pygame.init()

size = width, height = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creature")
background_color = (255, 255, 255)


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        pygame.quit()
        exit()
    return pygame.image.load(fullname)


creature_image = load_image("creature.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)

        

    pygame.display.flip()
pygame.quit()
