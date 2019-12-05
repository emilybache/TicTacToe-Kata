from approvaltests import verify

from grid_reader import read_grid
from grid_printer import print_grid


def test_read_empty_board():
    position = """\
  0 1 2.
0      .
1      .
2      .
"""
    grid = read_grid(position)
    assert grid.width == 3
    assert grid.height == 3


def test_read_pieces():
    position = """\
  0 1 2.
0 x    .
1   o  .
2 x    .
"""
    grid = read_grid(position)
    verify(print_grid(grid))


def test_read_larger_grid():
    position = """\
   0  1  2  3  4  5  6  7  8  9  10 11.
0  x     o                            .
1                                     .
2                                     .
3                                     .
4                                     .
5                                     .
6                                     .
7                                     .
8                                     .
9                                     .
10                         x          .
11                                    .
12                                    .
13                                    .
"""
    grid = read_grid(position)
    verify(print_grid(grid))
