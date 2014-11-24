"""
    pyrogue.map
    ~~~~~~~~~~~

    This handles the generation of the dungeon.
"""

import math


class Cell(Point):
    """
    Maps points to their attributes on a given level.
    """
    def __init__(self, x, y):
        super().__init__(self, x, y)
        self.opaque = None # need None as a flag to show the cell
        self.obstacle = None # hasn't been touched.
        self.empty = None # if true - floor, else wall
        self.entities = []
    def wall(self):
        """
        Creates a wall in the cell.
        """
        # can't call this on something that is already a wall or floor
        assert self.empty is None
        self.empty = False
    def floor(self):
        """
        Creates a floor in the cell.
        """
        # same as wall()
        assert self.empty is None
        self.empty = True
