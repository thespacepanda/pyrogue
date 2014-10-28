import libtcodpy as libtcod

from entity import Entity
from graphics import Show
from keys import handleKeys

#############################################
# Initialization & Main Loop
#############################################
 
# Global screen size
SCREEN_WIDTH  = 80
SCREEN_HEIGHT = 50

libtcod.console_set_custom_font(b'arial10x10.png',
                                libtcod.FONT_TYPE_GREYSCALE |
                                libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT,
                          b'python/libtcod tutorial', False)

# Make an off screen console that we can draw to, we will blit it on
# to the actual console in main
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

player = Entity(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, b'@', libtcod.white, con)
npc = Entity(SCREEN_WIDTH//2 + 3, SCREEN_HEIGHT//2, b'@', libtcod.yellow, con)

entities = [player, npc]

show = Show(con, entities)

while not libtcod.console_is_window_closed():

    show.draw()
    
    # Since we are drawing to an off-screen console, we need to "blit"
    # it to the actual console - this just means we copy it over
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    # This flushes the changes in the console to the screen itself
    libtcod.console_flush()
    
    show.clear()
    
    # Handle keys and exit game if needed
    exit = handleKeys(player)
    if exit:
        break
