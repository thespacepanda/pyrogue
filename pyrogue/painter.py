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

        explored_tiles = world.player.explored

        for position in explored_tiles:
            x, y = position
            try:
                tile = world.tiles[position]
            except KeyError:
                continue
            
            libtcod.console_set_default_foreground(self.console, tile.color)
            libtcod.console_put_char(self.console, x, y, tile.character, libtcod.BKGND_NONE)
            try:
                entity = world.entities[position]
                libtcod.console_set_default_foreground(self.console, entity.color)
                libtcod.console_put_char(self.console, x, y, entity.character, libtcod.BKGND_NONE)
            except KeyError:
                continue
        self.paint_health(world)
        self._blit()
        self._flush()
    def paint_health(self, world):
        height = 48 # below map
        center_x = 40
        health = world.player.health
        start_x = center_x - (health // 2)
        end_x = start_x + health
        for width in range(start_x, end_x + 1):
            libtcod.console_set_default_foreground(self.console, colors.GREEN)
            libtcod.console_put_char(self.console, width, height, b'#', libtcod.BKGND_NONE)
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
