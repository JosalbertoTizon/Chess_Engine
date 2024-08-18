from enum import Enum


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
