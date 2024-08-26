import pygame
from abc import ABC, abstractmethod
from utils import *
from constants import *


class ChessPiece(ABC):
    def __init__(self, position, color, piece_type):
        self.position = position
        self.color = color
        color_str = "white" if self.color == Piece_Color.WHITE else "black"
        self.texture = scale_texture(pygame.image.load("Images/Pieces/" + piece_type + "_" + color_str + ".png"), 1)
        self.rect = self.texture.get_rect()
        self.move(self.position)

    @abstractmethod
    def get_valid_moves(self, chess_board):
        pass

    def filter_valid_moves(self, moves, chess_board):
        valid_moves = []
        for move in moves:
            if chess_board.is_tile_empty(move):
                valid_moves.append(move)
        return valid_moves

    def move(self, new_position):
        self.position = new_position
        new_pos_float = (self.get_pos_float(new_position)[0], self.get_pos_float(new_position)[1])
        tile_center_pos = (new_pos_float[0] + CHESS_TILE_WIDTH / 2, new_pos_float[1] + CHESS_TILE_HEIGHT / 2)
        self.rect.topleft = (
            tile_center_pos[0] - self.texture.get_width() / 2, tile_center_pos[1] - self.texture.get_height() / 2)

    def update(self, screen):
        screen.blit(self.texture, self.rect)

    def get_pos_float(self, position):
        return position[0] * SCREEN_WIDTH / 8, position[1] * SCREEN_HEIGHT / 8


class Pawn(ChessPiece):
    def __init__(self, position, color):
        piece_type = "Pawn"
        super().__init__(position, color, piece_type)

    def get_valid_moves(self, chess_board):
        front_direction = -1 if self.color == Piece_Color.WHITE else 1
        valid_moves = []
        if 0 <= self.position[1] + 1 * front_direction < 8:
            valid_moves.extend([(self.position[0], self.position[1] + 1 * front_direction)])
        filtered_moves = self.filter_valid_moves(valid_moves, chess_board)
        return filtered_moves

    def filter_valid_moves(self, moves, chess_board):
        return super().filter_valid_moves(moves, chess_board)
        # No additional behavior needed


class Rook(ChessPiece):
    def __init__(self, position, color):
        piece_type = "Rook"
        super().__init__(position, color, piece_type)

    def get_valid_moves(self, chess_board):
        valid_moves = []
        valid_moves.extend([(i, self.position[1]) for i in range(8) if i != self.position[0]])
        valid_moves.extend([(self.position[0], j) for j in range(8) if j != self.position[1]])
        filtered_moves = self.filter_valid_moves(valid_moves, chess_board)
        return filtered_moves

    def filter_valid_moves(self, moves, chess_board):
        valid_moves = super().filter_valid_moves(moves, chess_board)
        filtered_moves = []
        for i in range(self.position[0] + 1, 8):
            position = (i, self.position[1])
            if position in valid_moves:
                filtered_moves.append(position)
            else:
                break
        for i in range(self.position[0] - 1, -8, -1):
            position = (i, self.position[1])
            if position in valid_moves:
                filtered_moves.append(position)
            else:
                break
        for j in range(self.position[1] + 1, 8):
            position = (self.position[0], j)
            if position in valid_moves:
                filtered_moves.append(position)
            else:
                break
        for j in range(self.position[1] - 1, -8, -1):
            position = (self.position[0], j)
            if position in valid_moves:
                filtered_moves.append(position)
            else:
                break
        return filtered_moves


class Knight(ChessPiece):
    def __init__(self, position, color):
        piece_type = "Knight"
        super().__init__(position, color, piece_type)

    def get_valid_moves(self, chess_board):
        valid_moves = []
        for delta_i in range(-2, 3):
            if delta_i == 0:
                continue
            delta_j = 3 - abs(delta_i)
            if 0 <= self.position[0] + delta_i < 8 and 0 <= self.position[1] + delta_j < 8:
                valid_moves.extend([(self.position[0] + delta_i, self.position[1] + delta_j)])
            delta_j = -3 + abs(delta_i)
            if 0 <= self.position[0] + delta_i < 8 and 0 <= self.position[1] + delta_j < 8:
                valid_moves.extend([(self.position[0] + delta_i, self.position[1] + delta_j)])
        filtered_moves = self.filter_valid_moves(valid_moves, chess_board)
        return filtered_moves

    def filter_valid_moves(self, moves, chess_board):
        return super().filter_valid_moves(moves, chess_board)
        # No additional behavior needed


class Bishop(ChessPiece):
    def __init__(self, position, color):
        piece_type = "Bishop"
        super().__init__(position, color, piece_type)

    def get_valid_moves(self, chess_board):
        pass

    def _enforce_additional_rules(self, moves, chess_board):
        return moves


class Queen(ChessPiece):
    def __init__(self, position, color):
        piece_type = "Queen"
        super().__init__(position, color, piece_type)

    def get_valid_moves(self, chess_board):
        pass

    def _enforce_additional_rules(self, moves, chess_board):
        return moves


class King(ChessPiece):
    def __init__(self, position, color):
        piece_type = "King"
        super().__init__(position, color, piece_type)

    def get_valid_moves(self, chess_board):
        pass

    def _enforce_additional_rules(self, moves, chess_board):
        return moves
