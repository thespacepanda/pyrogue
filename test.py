import libtcodpy as libtcod

from entity import Entity
from graphics import Stamp
from keys import handleKeys

#############################################
# Initialization & Main Loop
#############################################

player = Entity(80//2, 50//2, b'@', libtcod.white)
npc = Entity(80//2 + 3, 50//2, b'@', libtcod.yellow)

entities = [player, npc]

stamp = Stamp(entities)

while not libtcod.console_is_window_closed():

    stamp.draw()
    
    # Since we are drawing to an off-screen console, we need to "blit"
    # it to the actual console - this just means we copy it over
    #libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    # This flushes the changes in the console to the screen itself
    #libtcod.console_flush()
    
    stamp.clear()
    
    # Handle keys and exit game if needed
    exit = handleKeys(player)
    if exit:
        break
