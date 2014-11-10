import libtcodpy as libtcod

from entity import Entity
from graphics import Stamp
from keys import handleKeys

player = Entity(80//2, 50//2, b'@', libtcod.purple)
npc = Entity(80//2 + 3, 50//2, b'@', libtcod.yellow)

entities = [player, npc]

stamp = Stamp(entities)

while not libtcod.console_is_window_closed():

    stamp.draw()

    EXIT = handleKeys(player)
    if EXIT:
        break
    stamp.clear()
