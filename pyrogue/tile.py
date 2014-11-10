"""
    pyrogue.tile
    ~~~~~~~~~~~~

    This module represents drawable objects which are static - they are part of
    the environment and cannot be interacted with or destroyed.
"""

import colors

class Tile(object):
    """This takes a character, a color, and a tuple as the map position"""
    def __init__(self, obstacle, opaque=None):
        self.obstacle = obstacle
        if opaque is None:
            opaque = obstacle
        self.opaque = opaque

class Wall(Tile):
    """A wall"""
    def __init__(self):
        super().__init__(True)
        self.character = b'#'
        self.color = colors.dark_wall

class Floor(Tile):
    """A floor"""
    def __init__(self):
        super().__init__(False)
        self.character = b'.'
        self.color = colors.dark_floor

class UpStair(Tile):
    """Stairs that take you up a level"""
    def __init__(self):
        super().__init__(False)
        self.character = b'<'
        self.color = colors.white

class DownStair(Tile):
    """Stairs that take you down a level"""
    def __init__(self):
        super().__init__(False)
        self.character = b'<'
        self.color = colors.white
