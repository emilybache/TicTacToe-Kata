from grid import Grid
from grid_printer import calculate_field_width


def read_grid(printed_grid):
    """
    If you have printed a grid using 'print_grid', you can parse it into a Grid object using this function
    :param printed_grid: the string previously created with 'print_grid'
    :return: a Grid object initialized with the contents of the printed grid
    """
    grid = _empty_grid_with_same_dimensions_as(printed_grid)
    _update_grid_content(grid, printed_grid)
    return grid


def _empty_grid_with_same_dimensions_as(printed_grid):
    contents = []
    for line in printed_grid.splitlines():
        line = line.replace(".", "")
        line = line.strip()
        fields = line.split()
        if fields:
            contents.append(fields)
    width = max([len(row) for row in contents])  # width is of longest row
    height = len(contents) - 1  # ignore header row when counting height
    grid = Grid(width, height)
    return grid


def _update_grid_content(grid, printed_grid):
    field_width = _field_width_with_padding(grid)
    rows_and_header = printed_grid.splitlines()
    # ignore header row that contains co-ordinate labels
    rows = rows_and_header[1:]
    for j, line in enumerate(rows):
        line = line.replace(".", "")
        fields_and_label = _fixed_width_chunks(line, field_width)
        # ignore first field on each line that contains co-ordinate label
        label, fields = next(fields_and_label), fields_and_label
        for i, field in enumerate(fields):
            piece = field.strip()
            if piece:
                grid.update_content_at(i, j, piece)


def _field_width_with_padding(grid):
    # add extra for 1 padding in each field
    return calculate_field_width(grid) + 1


def _fixed_width_chunks(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))
