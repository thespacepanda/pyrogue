"""
    pyrogue.main
    ~~~~~~~~~~~~

    This runs the game Pyrogue.
"""

import libtcodpy as libtcod

from world import World
from painter import Painter

def main():
    """The main game loop."""
    world = World()
    painter = Painter()
    player = world.player
    while not libtcod.console_is_window_closed():
        world.update()
        painter.paint(world)
        player.interact()
        if player.exit:
            break
        painter.new_canvas()

if __name__ == "__main__":
    main()
