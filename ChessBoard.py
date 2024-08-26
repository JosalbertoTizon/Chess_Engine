import pygame
from Piece import *
from constants import *
from utils import *


class Tile:
    def __init__(self, pos_x, pos_y, width, height):
        self.position = (pos_x, pos_y)
        self.width = width
        self.height = height
        self.color = Colors.Dark_Green if (pos_x + pos_y) % 2 == 0 else Colors.Beige
        tile_pos_float = (pos_x * CHESS_TILE_WIDTH, pos_y * CHESS_TILE_HEIGHT)
        self.rect = pygame.Rect(tile_pos_float[0], tile_pos_float[1], width, height)
        self.current_piece = None

    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class ChessBoard:
    def __init__(self):
        self.board_array = [[None] * 8 for _ in range(8)]
        self.white_pieces = []
        self.black_pieces = []

        self.initialize_tiles()
        self.initialize_pieces()
        self.initialize_piece_references()

        self.chosen_piece = None
        self.possible_moves = []

    def update(self, screen, state, turn):
        if state == Game_State.CHOOSING_PIECE:
            pass
        elif state == Game_State.CHOOSING_MOVE:
            pass

        self.draw_everything(screen)

    def draw_everything(self, screen):
        for row in self.board_array:
            for tile in row:
                tile.update(screen)
        for piece in self.white_pieces:
            piece.update(screen)
        for piece in self.black_pieces:
            piece.update(screen)

    def initialize_tiles(self):
        for (i, row) in enumerate(self.board_array):
            for (j, tile) in enumerate(row):
                self.board_array[i][j] = Tile(i, j, CHESS_TILE_WIDTH, CHESS_TILE_HEIGHT)

    def initialize_pieces(self):
        # White pieces
        for i in range(8):
            piece = Pawn((i, 6), Piece_Color.WHITE)
            self.white_pieces.append(piece)

        # Adding white rooks, knights, bishops, queen, and king
        self.white_pieces.append(Rook((0, 7), Piece_Color.WHITE))
        self.white_pieces.append(Rook((7, 7), Piece_Color.WHITE))
        self.white_pieces.append(Knight((1, 7), Piece_Color.WHITE))
        self.white_pieces.append(Knight((6, 7), Piece_Color.WHITE))
        self.white_pieces.append(Bishop((2, 7), Piece_Color.WHITE))
        self.white_pieces.append(Bishop((5, 7), Piece_Color.WHITE))
        self.white_pieces.append(Queen((3, 7), Piece_Color.WHITE))
        self.white_pieces.append(King((4, 7), Piece_Color.WHITE))

        # Black pieces
        for i in range(8):
            piece = Pawn((i, 1), Piece_Color.BLACK)
            self.black_pieces.append(piece)

        # Adding black rooks, knights, bishops, queen, and king
        self.black_pieces.append(Rook((0, 0), Piece_Color.BLACK))
        self.black_pieces.append(Rook((7, 0), Piece_Color.BLACK))
        self.black_pieces.append(Knight((1, 0), Piece_Color.BLACK))
        self.black_pieces.append(Knight((6, 0), Piece_Color.BLACK))
        self.black_pieces.append(Bishop((2, 0), Piece_Color.BLACK))
        self.black_pieces.append(Bishop((5, 0), Piece_Color.BLACK))
        self.black_pieces.append(Queen((3, 0), Piece_Color.BLACK))
        self.black_pieces.append(King((4, 0), Piece_Color.BLACK))

    def initialize_piece_references(self):
        # Place white pieces on the board
        for piece in self.white_pieces:
            row, col = piece.position
            tile = self.board_array[row][col]
            tile.current_piece = piece

        # Place black pieces on the board
        for piece in self.black_pieces:
            row, col = piece.position
            tile = self.board_array[row][col]
            tile.current_piece = piece

    def process_click(self, mouse_button, mouse_position, state, turn):
        if mouse_button == 1:  # Left mouse button
            if state == Game_State.CHOOSING_PIECE:
                return self.choose_piece(mouse_position, turn)
            if state == Game_State.CHOOSING_MOVE:
                return self.choose_move(mouse_position, turn)

        if mouse_button == 3:  # Right mouse button
            if state == Game_State.CHOOSING_MOVE:
                self.unselect_piece()
                return Game_State.CHOOSING_PIECE, turn

        return state, turn

    def choose_piece(self, mouse_position, turn):
        if turn == Turn.WHITE:
            for piece in self.white_pieces:
                if piece.rect.collidepoint(mouse_position):
                    self.select_piece(piece)
                    return Game_State.CHOOSING_MOVE, Turn.WHITE
        else:
            for piece in self.black_pieces:
                if piece.rect.collidepoint(mouse_position):
                    self.select_piece(piece)
                    return Game_State.CHOOSING_MOVE, Turn.BLACK
        return Game_State.CHOOSING_PIECE, turn

    def choose_move(self, mouse_position, turn):
        for row in self.board_array:
            for tile in row:
                if tile.rect.collidepoint(mouse_position) and tile.position in self.possible_moves:
                    self.move_piece(tile)
                    return Game_State.CHOOSING_PIECE, turn.opposite_turn

        # If no valid move was chosen
        self.unselect_piece()
        return Game_State.CHOOSING_PIECE, turn

    def select_piece(self, piece):
        self.chosen_piece = piece
        self.possible_moves = piece.get_valid_moves(self)
        self.glow_possible_moves()

    def unselect_piece(self):
        self.unglow()
        self.possible_moves = []
        self.chosen_piece = None

    def move_piece(self, new_tile):
        previous_tile = self.board_array[self.chosen_piece.position[0]][self.chosen_piece.position[1]]
        previous_tile.current_piece = None
        self.chosen_piece.move(new_tile.position)
        new_tile.current_piece = self.chosen_piece
        self.unselect_piece()

    def is_tile_empty(self, position):
        (row, column) = position
        return self.board_array[row][column].current_piece is None

    def glow_possible_moves(self):
        if self.possible_moves is None:
            return
        for move in self.possible_moves:
            self.board_array[move[0]][move[1]].color = Colors.Glow

    def unglow(self):
        if self.possible_moves is None:
            return
        for move in self.possible_moves:
            if (move[0] + move[1]) % 2 == 0:
                self.board_array[move[0]][move[1]].color = Colors.Dark_Green
            else:
                self.board_array[move[0]][move[1]].color = Colors.Beige
