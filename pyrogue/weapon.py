"""
    pyrogue.weapon
    ~~~~~~~~~~~~

    This module represents drawable objects which are not static - they can be interacted with.
"""

import colors

class Weapon(Entity):
    """This takes a character, a color, and a tuple as the map position"""
    def __init__(self, obstacle, opaque=None):
        self.obstacle = obstacle
        if opaque is None:
            opaque = obstacle
        self.opaque = opaque

class Sword(Weapon):
    """A sword"""
    def __init__(self):
        super().__init__(True)
        self.character = b'|'
        self.color = colors.RED

class Ax(Weapon):
    """An ax"""
    def __init__(self):
        super().__init__(False)
        self.character = b'T'
        self.color = colors.RED

class Spear(Weapon):
    """A Spear"""
    def __init__(self):
        super().__init__(False)
        self.character = b'--~'
        self.color = colors.RED

class Mace(Weapon):
    """A Mace"""
    def __init__(self):
        super().__init__(False)
        self.character = b'/O'
        self.color = colors.RED