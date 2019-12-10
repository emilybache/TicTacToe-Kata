from grid import Grid
from grid_printer import calculate_field_width


def read_grid(printed_grid):
    """
    If you have printed a grid using 'print_grid', you can parse it into a Grid object using this function
    :param printed_grid:
    :return: a Grid object initialized with the contents of the printed grid
    """
    grid = _create_grid_with_dimensions(printed_grid)
    field_width = calculate_field_width(grid) + 1 # account for 1 padding in each field

    header_row = True
    for j, line in enumerate(printed_grid.splitlines()):
        if header_row:
            header_row = False
            continue
        line = line.replace(".", "")
        fields_and_label = _chunkstring(line, field_width)
        label = True
        for i, field in enumerate(fields_and_label):
            if label:
                label = False
                continue
            piece = field.strip()
            if piece:
                grid.update_content_at(i-1, j-1, piece)

    return grid


def _create_grid_with_dimensions(position):
    contents = []
    for line in position.splitlines():
        line = line.replace(".", "")
        line = line.strip()
        fields = line.split()
        if fields:
            contents.append(fields)
    width = max([len(row) for row in contents])  # header row should be longest
    height = len(contents) - 1  # ignore header row when counting height
    grid = Grid(width, height)
    return grid


def _chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))
