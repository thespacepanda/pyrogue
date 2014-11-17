"""
    pyrogue.map
    ~~~~~~~~~~~

    This module implements the map for a single level.
"""

import random

class Map(object):
    """The two-dimensional matrix which represents the map."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [] # two-dimensional matrix

    def mark_cells_unvisited(self):
        """This creates the map and marks all cells unvisited."""
        self.cells = [
            [
                False for column in range(self.width)
            ]
            for row in range(self.height)
        ]

    def random_mark_visited(self):
        """This marks a random cell as visited."""
        column = random.randrange(self.width)
        row = random.randrange(self.height)
        self.cells[column][row] = True
        return (column, row)

    def out_of_bounds(self, point):
        """
        This queries whether a point is out of the bounds of the map.
        """
        column, row = point
        return ((column < 0) or (column >= self.width) or
                ((row < 0) or (row >= self.height)))

    def has_adjacent_in_direction(self, point, direction):
        """
        This queries whether a point has an adjacent cell in the
        given direction.
        """
        return not self.out_of_bounds(add_points(point, direction))

    def adjacent_in_direction_visited(self, point, direction):
        """
        This queries whether the adjacent cell in the given direction
        has been marked as visited.
        """
        if not self.has_adjacent_in_direction(point, direction):
            raise Exception("Adjacent point doesn't exist.")
        column, row = add_points(point, direction)
        return self.cells[column][row]

    def __iter__(self):
        return self.cells.__iter__()

    def __getitem__(self, point):
        column, row = point
        return self.cells[column][row]

    def __setitem__(self, point, value):
        column, row = point
        self.cells[column][row] = value

class Generator(object):
    """This generates a new map."""
    def __init__(self, width, height):
        self.map = Map(width, height)
        self.current_cell = None

    def generate(self):
        """This handles the construction of our map and returns it."""
        self.map.mark_cells_unvisited()
        self.current_cell = self.map.random_mark_visited()
        direction_gen = directions()
        direction = direction_gen.__next__()
        return self.map

    def get_current_cell(self):
        """Returns the current cell."""
        return self.current_cell

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)

def add_points(point, direction):
    """This adds a point and direction piece-wise."""
    column, row = point
    width, height = direction
    return (column + width, row + height)

def directions():
    """Random direction generator; exhaustive."""
    direction_list = [NORTH, SOUTH, EAST, WEST]
    while direction_list:
        length = len(direction_list)
        yield direction_list.pop(random.randrange(length))
