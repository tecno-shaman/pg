import pygame
import random
import os


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        pygame.quit()
        exit()
    return pygame.image.load(fullname)


class Bomb(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(*group)
        self.image = load_image('bomb.png')
        self.image_boom = load_image('boom.png')

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100)
        self.rect.y = random.randrange(100)

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom
