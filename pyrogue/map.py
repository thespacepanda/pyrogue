"""
    pyrogue.map
    ~~~~~~~~~~~

    This handles the generation of the dungeon.
"""

import math

class Point(object):
    """
    Abstract representation of a point in 2-dimensional space,
    originally used a tuple, but the added readability this gives is
    worth the overhead.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, destination):
        """
        This uses the Pythagorean theorem to calculate the distance
        from the given point. Be careful of rounding errors, returns
        a float.
        """
        run = destination.x - self.x
        rise = destination.y - self.y
        return math.sqrt(run**2 + rise**2)

class Rect(object):
    """
    Abstract representation of a rectangle. It takes a starting
    position (class Point), and an int representing the width, and an
    int representing the height.
    """
    def __init__(self, start, width, height):
        self.start = start
        self.width = width
        self.height = height
        self.area = None # Must initialize to None, we may not even
        self.vertices = None # need these right away
    def get_area(self):
        """Calculates the area of the rectangle."""
        if self.area is None:
            self.area = self.height * self.width
        return self.area
    def get_vertices(self):
        """Returns a 4-tuple of the points at each vertex."""
        if self.vertices is None:
            top_left = self.start
            top_right = Point(top_left.x + self.width, top_left.y)
            bottom_left = Point(top_left.x, top_left.y + self.height)
            bottom_right = Point(top_right.x, bottom_left.y)
            self.vertices = (top_left, top_right,
                             bottom_left, bottom_right)
        return self.vertices
