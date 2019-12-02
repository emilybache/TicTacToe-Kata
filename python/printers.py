

def print_board(board):
    """Prints any grid-like object with content at different x, y co-ordinates.

    The grid-like object must have attributes 'width' and 'height'.
    It must also define a method 'content_at(x, y)' which returns the string to be printed
    at that location with co-ordinates (x, y).
    """
    width_chars = max(len(str(board.width)), len(str(board.height)))
    x_coords = [_fixed_width(" ", width_chars)] + [_fixed_width(i, width_chars) for i in range(board.width)]
    all_content = [x_coords]
    for j in range(board.height):
        y_coords = [_fixed_width(j, width_chars)]
        row_contents = y_coords + [_fixed_width(board.content_at(i, j), width_chars) for i in range(board.width)]
        all_content.append(row_contents)

    all_rows = [" ".join(row) for row in all_content]
    all_rows.append("")
    return '.\n'.join(all_rows)


def _fixed_width(n, width):
    r = str(n)
    r += _whitespace(width - len(r))
    return r


def _whitespace(length):
    "Return a string of whitespace with the requested length"
    return " "*length


def _whitespace2(length):
    "Return a string of whitespace with the requested length"
    w = ""
    for i in range(length):
        w += " "
    return w
