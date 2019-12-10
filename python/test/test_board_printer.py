from approvaltests import verify

from grid import Grid
from grid_printer import print_grid


def test_print_empty_board():
    board = Grid(width=3, height=3)
    verify(print_grid(board))


def test_print_tic_tac_toe():
    board = Grid(width=3, height=3)
    board.content[(0, 0)] = "x"
    board.content[(2, 0)] = "o"
    board.content[(2, 2)] = "x"
    verify(print_grid(board))


def test_print_larger_grid():
    board = Grid(width=12, height=14)
    board.content[(0, 0)] = "x"
    board.content[(2, 0)] = "o"
    board.content[(8, 10)] = "x"
    verify(print_grid(board))
