"""
    pyrogue.weapon
    ~~~~~~~~~~~~

    This module represents drawable objects which are not static - they can be interacted with.
"""

import colors

from entity import Entity

class Weapon(Entity):
    """This takes a character, a color, and a tuple as the map position"""
    def __init__(self):
        self.obstacle = True
        self.opaque = True

class Sword(Weapon):
    """A sword"""
    def __init__(self):
        self.character = b'|'
        self.color = colors.RED

class Ax(Weapon):
    """An ax"""
    def __init__(self):
        self.character = b'T'
        self.color = colors.RED

class Spear(Weapon):
    """A Spear"""
    def __init__(self):
        self.character = b'--~'
        self.color = colors.RED

class Mace(Weapon):
    """A Mace"""
    def __init__(self):
        self.character = b'/*'
        self.color = colors.RED
WEAPON_TYPES = [Sword, Ax, Spear, Mace]