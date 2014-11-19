"""
    pyrogue.main
    ~~~~~~~~~~~~

    This runs the game Pyrogue.
"""

import pyrogue.libtcodpy as libtcod

from pyrogue.world import World
from pyrogue.painter import Painter


def main():
    """The main game loop."""
    world = World()
    painter = Painter()
    player = world.player
    while not libtcod.console_is_window_closed():
        world.update()
        painter.paint(world)
        player.interact(world)
        if player.exit:
            break
        painter.new_canvas()

if __name__ == "__main__":
    main()
