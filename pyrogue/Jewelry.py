"""
    pyrogue.Jewelry
    ~~~~~~~~~~~~

    This module represents drawable objects which are not static - they can be interacted with.
"""

import colors

class Jewelry(Entity):
    """This takes a character, a color, and a tuple as the map position"""
    def __init__(self, obstacle, opaque=None):
        self.obstacle = obstacle
        if opaque is None:
            opaque = obstacle
        self.opaque = opaque

class Gear(Jewelry):
    """A gear from a robot"""
    def __init__(self):
        self.character = b'*'
        self.color = colors.YELLOW

class Diamond(Jewelry):
    """A Diamond"""
    def __init__(self):
        self.character = b'<>'
        self.color = colors.RED

class Pearl(Jewelry):
    """A Pearl"""
    def __init__(self):
        self.character = b'O'
        self.color = colors.WHITE

class Wire(Jewelry):
    """Wire from a robot"""
    def __init__(self):
        self.character = b'&'
        self.color = colors.RED
class Coal(Jewelry):
    """Coal for making steam to run machines"""
    def __init__(self):
        self.character = b'C'
        self.color = colors.RED

