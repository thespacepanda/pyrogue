import libtcodpy as libtcod

class Entity():
    """
    This class represents anything that can be drawn as a character on
    the screen - the player, a monster, a potion, etc.
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # move by a given change in x and y
        self.x += dx
        self.y += dy
