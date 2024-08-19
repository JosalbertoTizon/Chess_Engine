from enum import Enum
import pygame

class Turn(Enum):
    WHITE = 0
    BLACK = 1


class ChessPiece(Enum):
    KING = 1
    QUEEN = 2
    ROOK = 3
    BISHOP = 4
    KNIGHT = 5
    PAWN = 6

def scale_texture(texture, scale_factor):
    final_width = int(texture.get_width() * scale_factor)
    final_height = int(texture.get_height() * scale_factor)
    return pygame.transform.scale(texture, (final_width, final_height))
