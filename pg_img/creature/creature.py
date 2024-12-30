import pygame
import os


class Creature(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        if args:
            self.rext.x += args[0][0]
            self.rect.y += args[0][1]

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Hero')
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()

    FPS = 60
    # clock =
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            keys = pygame.key.get_pressed()

            screen.fill('white')
            if keys[pygame.K_LEFT]:
                all_sprites.update((-10, 0))
            if keys[pygame.K_DOWN]:
                all_sprites.update((0, -10))
            if keys[pygame.K_RIGHT]:
                all_sprites.update((0, 10))
            if keys[pygame.K_UP]:
                all_sprites.update((0, 10))


            all_sprites.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()
