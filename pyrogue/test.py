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
    
    exit = handleKeys(player)
    if exit:
        break
    stamp.clear()
