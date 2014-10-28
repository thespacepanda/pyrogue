import libtcodpy as libtcod

class Entity():
    """
    This class represents anything that can be drawn as a character on
    the screen - the player, a monster, a potion, etc.
    """
    def __init__(self, x, y, char, color, console):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.console = console

    def move(self, dx, dy):
        # move by a given change in x and y
        self.x += dx
        self.y += dy

    def draw(self):
        # set the color and then draw the character that represents
        # this object at its position
        libtcod.console_set_default_foreground(self.console, self.color)
        libtcod.console_put_char(self.console, self.x, self.y,
                                 self.char, libtcod.BKGND_NONE)

    def clear(self):
        # erase the character that represents this object
        libtcod.console_put_char(self.console, self.x, self.y,
                                 b' ', libtcod.BKGND_NONE)
