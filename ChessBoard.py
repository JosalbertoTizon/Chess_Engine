import pygame
from Piece import *
from constants import *
from utils import *


class Tile:
    def __init__(self, pos_x, pos_y, width, height, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.current_piece = None

    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class ChessBoard:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.white_pieces = []
        self.black_pieces = []

        self.initialize_tiles()
        self.initialize_pieces()

    def update(self, screen):
        for row in self.board:
            for tile in row:
                tile.update(screen)
        for piece in self.white_pieces:
            piece.update(screen)
        for piece in self.black_pieces:
            piece.update(screen)

    def initialize_tiles(self):
        for (i, row) in enumerate(self.board):
            for (j, tile) in enumerate(row):
                tile_xpos = i * SCREEN_WIDTH / 8
                tile_ypos = j * SCREEN_HEIGHT / 8
                tile_color = pygame.Color("#006400") if (i + j) % 2 == 0 else pygame.Color("#F5F5DC")
                self.board[i][j] = Tile(tile_xpos, tile_ypos, SCREEN_WIDTH / 8, SCREEN_HEIGHT / 8, tile_color)

    def initialize_pieces(self):
        piece = Pawn((100, 100), "white")
        self.white_pieces.append(piece)

    def process_click(self, mouse_position, turn):
        if turn == Turn.WHITE:
            for piece in self.white_pieces:
                if piece.rect.collidepoint(mouse_position):
                    self.select_piece(piece)
                    break
        else:
            for piece in self.black_pieces_pieces:
                if piece.rect.collidepoint(mouse_position):
                    self.select_piece(piece)
                    break

    def select_piece(self, piece):
        available_moves = piece.get_available_moves(self.board)
        pass

    def is_tile_available(self, position):
        return self.is_tile_empty(position) and self.is_tile_in_bounds(position)

    def is_tile_empty(self, position):
        (row, column) = position
        return self.board[row][column] is None

    def is_tile_in_bounds(self, position):
        (row, column) = position
        return abs(row) < 8 or abs(column) < 8

