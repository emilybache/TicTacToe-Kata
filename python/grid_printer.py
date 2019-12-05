

def print_grid(grid):
    """Prints any grid-like object with content at different x, y co-ordinates.

    The grid object must have:
    * attribute 'width'
    * attribute 'height'.
    * 'content_at(x, y)' which returns the single character to be printed at that location with co-ordinates (x, y).
    * attribute 'comment' (which may be empty). This is printed below the grid.
    """
    field_width = calculate_field_width(grid)
    x_coords = [_fixed_width(" ", field_width)] + [_fixed_width(i, field_width) for i in range(grid.width)]
    all_content = [x_coords]
    for j in range(grid.height):
        y_coords = [_fixed_width(j, field_width)]
        row_contents = y_coords + [_fixed_width(grid.content_at(i, j), field_width) for i in range(grid.width)]
        all_content.append(row_contents)

    all_rows = [" ".join(row) for row in all_content]
    all_rows.append("")
    grid_string = '.\n'.join(all_rows)
    return grid_string + grid.comment


def calculate_field_width(grid):
    """Given a grid with width and height, what should the fixed width of fields be for printing"""
    return max(len(str(grid.width)), len(str(grid.height)))


def _fixed_width(s, width):
    "make a string from the object s and pad with whitespace up to width"
    r = str(s)
    r += _whitespace(width - len(r))
    return r


def _whitespace(length):
    "Return a string of whitespace with the requested length"
    return " "*length

