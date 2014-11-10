"""
    pyrogue.drawable
    ~~~~~~~~~~~~~~~~

    This module represents any drawable character in the game, and is the super
    class of Entity and Tile.
"""

class Drawable(object):
    """This takes a character, a color, and a tuple as the map position"""
    def __init__(self, character, color, map_position, obstacle, opaque=None):
        self.character = character
        self.color = color
        self.map_position = map_position
        self.obstacle = obstacle
        if opaque is None:
            opaque = obstacle
        self.opaque = opaque
