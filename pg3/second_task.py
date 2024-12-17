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

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell_coords):
        if cell_coords[0] >= 0 and cell_coords[1] >= 0 and cell_coords[0] < len(self.board) and cell_coords[1] < len(
                self.board[0]):
            print(cell_coords)
        else:
            print(None)

    def get_cell(self, mouse_pos):
        i = (mouse_pos[0] - self.left) // self.cell_size
        j = (mouse_pos[1] - self.top) // self.cell_size
        return j, i


size = width, height = 480, 480
screen = pygame.display.set_mode(size)
# поле 5 на 7
board = Board(4, 3)
board.set_view(100, 100, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
