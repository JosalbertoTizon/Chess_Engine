import pygame
from constants import *


class Tile:
    def __init__(self, pos_x, pos_y, width, height, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(pos_x, pos_y, width, height)

    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class ChessBoard:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]

        self.initialize_tiles()
        self.initialize_pieces()


    def update(self, screen):
        for row in self.board:
            for tile in row:
                tile.update(screen)

    def initialize_tiles(self):
        for (i, row) in enumerate(self.board):
            for (j, tile) in enumerate(row):
                tile_xpos = i * SCREEN_WIDTH / 8
                tile_ypos = j * SCREEN_HEIGHT / 8
                tile_color = pygame.Color("#006400") if (i + j) % 2 == 0 else pygame.Color("#F5F5DC")
                self.board[i][j] = Tile(tile_xpos, tile_ypos, SCREEN_WIDTH / 8, SCREEN_HEIGHT / 8, tile_color)

    def initialize_pieces(self):
        pass