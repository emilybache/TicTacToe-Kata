from grid import Grid
from printers import calculate_field_width


def read_grid(position):
    grid = create_grid(position)
    field_width = calculate_field_width(grid) + 1 # account for 1 padding in each field

    header_row = True
    for j, line in enumerate(position.splitlines()):
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
                grid.content[(i-1, j-1)] = piece

    return grid


def create_grid(position):
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
