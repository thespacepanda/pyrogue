"""
    pyrogue.Jewelry
    ~~~~~~~~~~~~

    This module represents drawable objects which are not static - they can be interacted with.
"""

import colors

class Jewelry(Entity):
    """Models jewelry"""
    def __init__(self):
        self.obstacle = False
        self.opaque = False

class Gear(Jewelry):
    """A gear from a robot"""
    def __init__(self):
        self.character = b'*'
        self.color = colors.YELLOW

class Diamond(Jewelry):
    """A Diamond"""
    def __init__(self):
        self.character = b'*'
        self.color = colors.RED

class Pearl(Jewelry):
    """A Pearl"""
    def __init__(self):
        self.character = b'*'
        self.color = colors.WHITE

class Wire(Jewelry):
    """Wire from a robot"""
    def __init__(self):
        self.character = b'-'
        self.color = colors.RED
class Coal(Jewelry):
    """Coal for making steam to run machines"""
    def __init__(self):
        self.character = b'%'
        self.color = colors.RED

