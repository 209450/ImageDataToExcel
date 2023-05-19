class RectangleCoordinates:
    def __init__(self, x1, y1, x2, y2):
        self.top_left = (x1, y1)
        self.bottom_right = (x2, y2)

    @classmethod
    def from_box(cls, x1, y1, width_height):
        x2 = x1 + width_height[0]
        y2 = y1 + width_height[1]
        return cls(x1, y1, x2, y2)
