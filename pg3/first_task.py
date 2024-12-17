import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j]:
                    cell_width = 0
                else:
                    cell_width = 1
                pygame.draw.rect(screen, 'white', (
                    self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size),
                                 cell_width)


size = width, height = 480, 480
screen = pygame.display.set_mode(size)
board = Board(4, 3)
board.set_view(100, 100, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
