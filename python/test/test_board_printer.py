from approvaltests import verify

from printers import print_board


class Grid:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.content = {}

    def content_at(self, x, y):
        return self.content.get((x, y), " ")


def test_print_empty_board():
    board = Grid(width=3, height=3)
    verify(print_board(board))


def test_print_tic_tac_toe():
    board = Grid(width=3, height=3)
    board.content[(0, 0)] = "x"
    board.content[(2, 0)] = "o"
    board.content[(2, 2)] = "x"
    verify(print_board(board))


def test_print_larger_grid():
    board = Grid(width=12, height=14)
    board.content[(0, 0)] = "x"
    board.content[(2, 0)] = "o"
    board.content[(8, 10)] = "x"
    verify(print_board(board))
