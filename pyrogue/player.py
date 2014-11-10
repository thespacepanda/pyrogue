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
        super().__init__(b'@', colors.white, pos)
        self.exit = False
        self.key_map = {
            libtcod.KEY_UP: (self.move, (0, -1)),
            libtcod.KEY_DOWN: (self.move, (0, 1)),
            libtcod.KEY_LEFT: (self.move, (-1, 0)),
            libtcod.KEY_RIGHT: (self.move, (1, 0)),
            libtcod.KEY_ESCAPE: (self.quit, True),
            libtcod.KEY_ENTER: (self.fullscreen, None)
        }
    def interact(self, world):
        """Handles key input."""
        key = libtcod.console_wait_for_keypress(True)
        func, val = self.key_map[key.vk]
        if val is None:
            val = key
        if func == self.move:
            func(val, world)
        else:
            func(val)
    def quit(self, sure):
        """Sets self.exit to True so that we can exit."""
        if sure:
            self.exit = True
    @staticmethod
    def fullscreen(key):
        """Toggles fullscreen for the root console."""
        if key.lalt:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
