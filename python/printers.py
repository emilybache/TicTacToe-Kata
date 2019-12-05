

def print_board(board):
    """Prints any grid-like object with content at different x, y co-ordinates.

    The grid-like object must have
    * attribute 'width'
    * attribute 'height'.
    * 'content_at(x, y)' which returns the single character to be printed at that location with co-ordinates (x, y).
    * attribute 'comment' (which may be empty). This is printed below the board.
    """
    field_width = calculate_field_width(board)
    x_coords = [_fixed_width(" ", field_width)] + [_fixed_width(i, field_width) for i in range(board.width)]
    all_content = [x_coords]
    for j in range(board.height):
        y_coords = [_fixed_width(j, field_width)]
        row_contents = y_coords + [_fixed_width(board.content_at(i, j), field_width) for i in range(board.width)]
        all_content.append(row_contents)

    all_rows = [" ".join(row) for row in all_content]
    all_rows.append("")
    board_string = '.\n'.join(all_rows)
    return board_string + board.comment


def calculate_field_width(board):
    return max(len(str(board.width)), len(str(board.height)))


def _fixed_width(s, width):
    "make a string from the object s and pad with whitespace up to width"
    r = str(s)
    r += _whitespace(width - len(r))
    return r


def _whitespace(length):
    "Return a string of whitespace with the requested length"
    return " "*length

