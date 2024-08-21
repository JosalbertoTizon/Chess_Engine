import sys
import pygame
from ChessBoard import ChessBoard
from constants import *
from utils import *


class ChessGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.chess_board = ChessBoard()
        # White pieces go first
        self.turn = Turn.WHITE
        self.state = Game_State.CHOOSING_PIECE

    def step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                (self.state, self.turn) = self.chess_board.process_click(event.button, mouse_position, self.state, self.turn)

        self.screen.fill((0, 0, 0))
        self.chess_board.update(self.screen, self.state, self.turn)
        pygame.display.flip()
