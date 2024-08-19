import pygame
from abc import ABC, abstractmethod
from utils import *


class ChessPiece(ABC):
    def __init__(self, position):
        self.rect = pygame.Rect(position[0], position[1], 50, 50)
        self.position = position

    @abstractmethod
    def get_valid_moves(self, board):
        pass

    @abstractmethod
    def move(self, new_position):
        pass

    @abstractmethod
    def update(self, screen):
        pass


class Pawn(ChessPiece):
    def __init__(self, position, color):
        super().__init__(position)
        self.color = color
        self.texture = scale_texture(pygame.image.load("Images/Pieces/" + "Pawn_" + color + ".png"), 1.2)

    def get_available_moves(self, board):
        available_moves = []
        for position in self.get_valid_moves(board):
            if board.is_tile_available(position):
                available_moves.append(position)
        return available_moves

    def get_valid_moves(self, board):
        pass

    def move(self, new_position):
        self.position = new_position
        [self.rect.x, self.rect.y] = new_position

    def update(self, screen):
        screen.blit(self.texture, self.rect)


class Rook(ChessPiece):
    def get_valid_moves(self, board):
        # Implement logic for rook's valid moves
        pass

    def move(self, new_position):
        # Implement the movement logic for a rook
        self.position = new_position

# pawn.get_valid_moves(board)
# rook.get_valid_moves(board)
