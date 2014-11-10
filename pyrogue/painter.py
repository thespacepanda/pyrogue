"""
    pyrogue.painter
    ~~~~~~~~~~~~~~~

    This module handles all painting to the screen.
"""

import libtcodpy as libtcod

import constants
import colors

class Painter(object):
    """This takes a world and prints it to the screen."""
    def __init__(self):
        self.width = constants.WINDOW_WIDTH
        self.height = constants.WINDOW_HEIGHT
        self.console = libtcod.console_new(self.width, self.height)
        libtcod.console_set_custom_font(b'arial10x10.png',
                                        libtcod.FONT_TYPE_GREYSCALE |
                                        libtcod.FONT_LAYOUT_TCOD)
        libtcod.console_init_root(self.width, self.height, b'Pyrogue', False)
    def paint(self, world):
        """Iterates through drawables in world and paints them to the screen."""
        #camera = world.player.get_camera()

        for entity in world.entities:
            x, y = entity.pos
            libtcod.console_set_default_foreground(self.console, entity.color)
            libtcod.console_put_char(self.console, x, y, entity.character,
                                     libtcod.BKGND_NONE)
        for position, tile in world.tiles.items():
            x, y = position
            if tile.opaque:
                libtcod.console_set_char_background(self.console, x, y,
                                                    colors.dark_wall,
                                                    libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(self.console, x, y,
                                                    colors.dark_floor,
                                                    libtcod.BKGND_SET)
        self._blit()
        self._flush()
    def _blit(self):
        """Blits self.console to the root console."""
        libtcod.console_blit(self.console, 0, 0, self.width,
                             self.height, 0, 0, 0)
    @staticmethod
    def _flush():
        """Flushes the root console to the screen."""
        libtcod.console_flush()
    def new_canvas(self):
        """Blanks self.console so that old positions don't remain next frame."""
        libtcod.console_clear(self.console)
