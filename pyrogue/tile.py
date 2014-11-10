"""
    pyrogue.tile
    ~~~~~~~~~~~~

    This module represents drawable objects which are static - they are part of
    the environment and cannot be interacted with or destroyed.
"""

class Tile(object):
    """This takes a character, a color, and a tuple as the map position"""
    def __init__(self, obstacle, opaque=None):
        self.obstacle = obstacle
        if opaque is None:
            opaque = obstacle
        self.opaque = opaque
