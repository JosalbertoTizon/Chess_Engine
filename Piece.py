from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, color, position):
        self.color = color
        self.position = position

    @abstractmethod
    def get_valid_moves(self, board):
        pass

    @abstractmethod
    def move(self, new_position):
        pass


class Pawn(ChessPiece):
    def get_valid_moves(self, board):
        # Implement logic for pawn's valid moves
        pass

    def move(self, new_position):
        # Implement the movement logic for a pawn
        self.position = new_position


class Rook(ChessPiece):
    def get_valid_moves(self, board):
        # Implement logic for rook's valid moves
        pass

    def move(self, new_position):
        # Implement the movement logic for a rook
        self.position = new_position


# Example of using the classes
pawn = Pawn('white', (1, 0))
rook = Rook('black', (0, 0))

# pawn.get_valid_moves(board)
# rook.get_valid_moves(board)
