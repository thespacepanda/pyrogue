"""
    pyrogue.monsters
    ~~~~~~~~~~~~

    This module represents drawable objects which are not static - they can be interacted with.
"""

import colors

from entity import Entity

class Monster(Entity):
    """This takes a character, a color, and a tuple as the map position"""
    def __init__(self):
        self.obstacle = True
        self.opaque = True

class SteamElephant(Monster):
    """A Steam powered elephant used for hauling cargo"""
    def __init__(self):
        self.character = b'E'
        self.color = colors.WHITE

class DrillSnake(Monster):
    """A mechanical snake with a drill head used for tunneling"""
    def __init__(self):
        self.character = b'S'
        self.color = colors.GREEN

class Airship(Monster):
    """A Flying Machine used for security"""
    def __init__(self):
        self.character = b'A'
        self.color = colors.RED

class Locomonster(Monster):
    """A Train monster used for transportation"""
    def __init__(self):
        self.character = b'L'
        self.color = colors.YELLOW

class Robug(Monster):
    """A giant mechanincal bug used for...I have no idea."""
    def __init__(self):
        self.character = b'R'
        self.color = colors.GREEN

MONSTER_TYPES = [SteamElephant, DrillSnake, Airship, Locomonster, Robug]
