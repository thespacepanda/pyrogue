"""
    pyrogue.player
    ~~~~~~~~~~~~~~

    This handles interaction from the player.
"""

import libtcodpy as libtcod

from entity import Entity

import colors

class Player(Entity):
    """
    This represents the player - it handles keypresses as well as all of the
    functionality offered by pyrogue.actor.Actor.
    """
    def __init__(self, pos):
        super().__init__(b'@', colors.WHITE, pos)
        self.exit = False
        self.key_map = {
            libtcod.KEY_UP: (self.move, (0, -1)),
            libtcod.KEY_DOWN: (self.move, (0, 1)),
            libtcod.KEY_LEFT: (self.move, (-1, 0)),
            libtcod.KEY_RIGHT: (self.move, (1, 0)),
            libtcod.KEY_ESCAPE: (self.quit, True),
            libtcod.KEY_ENTER: (self.fullscreen, None)
        }
        self.explored = []
        self.update_explored()
    def interact(self, world):
        """Handles key input."""
        key = libtcod.console_check_for_keypress(True)
        try:
            func, val = self.key_map[key.vk]
            if val is None:
                val = key
            if func == self.move:
                func(val, world)
            else:
                func(val)
        except KeyError:
            pass
    def update_explored(self):
        """
        Updates the list of explored tiles.
        """
        x, y = self.pos
        for width in range(x-5, x+6):
            for height in range(y-5, y+6):
                if (width, height) not in self.explored:
                    self.explored.append((width, height))
            
    def quit(self, sure):
        """Sets self.exit to True so that we can exit."""
        if sure:
            self.exit = True
    @staticmethod
    def fullscreen(key):
        """Toggles fullscreen for the root console."""
        if key.lalt:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
