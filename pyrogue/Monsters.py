"""
    pyrogue.monsters
    ~~~~~~~~~~~~

    This module represents drawable objects which are not static - they can be interacted with.
"""

import colors

class Monsters(Entity):
    """This takes a character, a color, and a tuple as the map position"""
    def __init__(self, obstacle, opaque=None):
        self.obstacle = obstacle
            opaque = obstacle
        self.opaque = opaque

class SteamElephant(Monsters):
    """A Steam powered elephant used for hauling cargo"""
    def __init__(self):
        self.character = b'M;'
        self.color = colors.WHITE

class DrillSnake(Monster):
    """A mechanical snake with a drill head used for tunneling"""
    def __init__(self):
        self.character = b'~~:>'
        self.color = colors.GREEN

class Airship(Monster):
    """A Flying Machine used for security"""
    def __init__(self):
        self.character = b'><'
        self.color = colors.RED

class Locomonster(Monster):
    """A Train monster used for transportation"""
    def __init__(self):
        self.character = b'o=o=o=k'
        self.color = colors.YELLOW

class robug(Monster):
    """A giant mechanincal bug used for...I have no idea."""
    def __init__(self):
        self.character = b'mmmm"'
        self.color = colors.GREEN

