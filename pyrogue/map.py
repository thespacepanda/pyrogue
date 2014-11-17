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
        self.visited_cells = [] # list of points (tuples)

    def mark_cells_unvisited(self):
        """This creates the map and marks all cells unvisited."""
        self.cells = [
            [
                Cell(False) for column in range(self.width)
            ]
            for row in range(self.height)
        ]

    def random_mark_visited(self):
        """This marks a random cell as visited."""
        column = random.randrange(self.width)
        row = random.randrange(self.height)
        self.visited((column, row))
        return (column, row)

    def visited(self, point):
        """Marks the given cell as visited."""
        if self.out_of_bounds(point):
            raise Exception("Point {} out of bounds.".format(point))
        if self[point].get_visited():
            raise Exception("Point {} already visited.".format(point))
        self[point].touch()
        self.visited_cells.append(point)

    def random_visited_cell(self, not_point):
        """Gets random visited cell that is not the one passed in."""
        if len(self.visited_cells) == 0:
            raise Exception("No visited cells.")
        maybe = random.choice(self.visited_cells)
        while maybe == not_point:
            # a little non-deterministic, but it works
            maybe = random.choice(self.visited_cells)
        assert maybe != not_point
        return maybe

    def corridor(self, point, direction):
        """
        Carves a corridor from the given point in the given direction.
        """
        if not self.has_adjacent_in_direction(point, direction):
            raise Exception(
                "No adjacent points in {}".format(direction)
            )
        target = add_points(point, direction)

        if direction == NORTH:
            self[point].north()
            self[target].south()
        elif direction == SOUTH:
            self[point].south()
            self[target].north()
        elif direction == EAST:
            self[point].east()
            self[target].west()
        elif direction == WEST:
            self[point].west()
            self[target].east()

        return target

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
        new_point = add_points(point, direction)
        return self[new_point].get_visited()

    def all_cells_visited(self):
        """Queries whether we have visited all cells in the map."""
        return len(self.visited_cells) == (self.width * self.height)

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

        while not self.map.all_cells_visited():
            direction_gen = directions()
            direction = direction_gen.__next__()

            while (not self.map.has_adjacent_in_direction(
                    self.current_cell, direction
            )) or self.map.adjacent_in_direction_visited(
                self.current_cell, direction
            ):
                try:
                    direction = direction_gen.__next__()
                except StopIteration:
                    self.current_cell = self.map.random_visited_cell(
                        self.current_cell
                    )
                    direction_gen = directions()
                    direction = direction_gen.__next__()

            self.current_cell = self.map.corridor(self.current_cell,
                                                  direction)
            self.map.visited(self.current_cell)

        return self.map

    def get_current_cell(self):
        """Returns the current cell."""
        return self.current_cell

class Cell(object):
    """This class represents a single cell in the dungeon."""
    def __init__(self, visited):
        self.visited = visited # Boolean
        self.north_side = True
        self.south_side = True
        self.east_side = True
        self.west_side = True
    def touch(self):
        """Utility method for clearly setting visited to True."""
        self.visited = True
    def get_visited(self):
        """Returns visited status."""
        return self.visited
    def set_visited(self, visited):
        """Sets visited status to the passed value."""
        self.visited = visited
    def north(self, wall=False):
        """Sets whether there's a wall to the north side"""
        self.north_side = wall
    def south(self, wall=False):
        """Sets whether there's a wall to the south side"""
        self.south_side = wall
    def east(self, wall=False):
        """Sets whether there's a wall to the east side"""
        self.east_side = wall
    def west(self, wall=False):
        """Sets whether there's a wall to the west side"""
        self.west_side = wall

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
