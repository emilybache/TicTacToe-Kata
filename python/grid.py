class Grid:
    """Data model for a 2 dimensional grid of single character data.

    A Grid has a height and width, and contents placed at x,y co-ordinates.
    The content at a particular co-ordinate is a single character string, which may be whitespace (but not a newline character).
    x co-ordinates increase across from left to right.
    y co-ordinates increase downwards from top to bottom.
    """
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.content = {}

    def content_at(self, x, y):
        return self.content.get((x, y), " ")

    def update_content_at(self, x, y, content):
        self.content[(x, y)] = content
