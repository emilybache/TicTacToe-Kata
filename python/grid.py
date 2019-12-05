class Grid:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.content = {}
        self.comment = ""

    def content_at(self, x, y):
        return self.content.get((x, y), " ")