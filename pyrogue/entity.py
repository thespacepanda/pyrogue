"""
    pyrogue.entity
    ~~~~~~~~~~~~~~

    This module represents drawable objects which can be interacted with.
"""

#from pyrogue.drawable import Drawable

class Entity(object):
    """This takes a character, a color, and a map_position"""
    def __init__(self, character, color, pos):
        # Entities block eachother and light
        self.character = character
        self.color = color
        self.opaque = True
        self.obstacle = True
        self.pos = pos
        self.name = "Player"
    def move(self, vector, world):
        dx, dy = vector
        x, y = self.pos
        new_pos = (x+dx, y+dy)
        if not world.blocked(new_pos):
            me = world.entities.pop(self.pos)
            self.pos = new_pos
            world.entities[new_pos] = me
