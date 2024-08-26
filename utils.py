from enum import Enum
import pygame


class Turn(Enum):
    WHITE = 0
    BLACK = 1

    @property
    def opposite_turn(self):
        if self == Turn.WHITE:
            return Turn.BLACK
        elif self == Turn.BLACK:
            return Turn.WHITE

class Game_State(Enum):
    CHOOSING_PIECE = 0
    CHOOSING_MOVE = 1

class Piece_Color(Enum):
    WHITE = 0
    BLACK = 1

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


Colors = {
    "Dark_Green": pygame.Color(0, 100, 0),
    "Beige": pygame.Color(245, 245, 220),
    "Glow": pygame.Color(255, 204, 102, 200)
}

Colors = dotdict(Colors)


def scale_texture(texture, scale_factor):
    final_width = int(texture.get_width() * scale_factor)
    final_height = int(texture.get_height() * scale_factor)
    return pygame.transform.scale(texture, (final_width, final_height))
