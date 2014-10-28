import libtcodpy as libtcod

class Show():
    """
    This class represents drawing the game to a given virtual console,
    which is blitted to the real console in main. You initialize this
    class with a virtual console and an optional list of entities to
    draw. This class assumes that the entities have a character, a
    color, and x, y coordinates.
    """
    def __init__(self, console, entities=[]):
        self.console = console
        self.entities = entities
    def draw(self):
        """
        Iterates through self.entities and draws each to the virtual
        console, respecting their internally defined color, character,
        and position.
        """
        for entity in self.entities:
            libtcod.console_set_default_foreground(self.console,
                                                   entity.color)
            libtcod.console_put_char(self.console, entity.x, entity.y,
                                     entity.char, libtcod.BKGND_NONE)
    def clear(self):
        """
        Iterates through self.entities and clears the position they
        are at - this needs to be called after the virtual console is
        blitted to the real console, and the real console is flushed
        to the screen. This makes sure that the entities only show in
        their true position every turn.
        """
        for entity in self.entities:
            libtcod.console_put_char(self.console, entity.x, entity.y,
                                    b' ', libtcod.BKGND_NONE)
    def addEntity(self, entity):
        """
        Adds a new entity to the internal list of entities to draw.
        """
        self.entities.append(entity)
    def removeEntity(self, entity):
        """
        Removes an entity from the internal list. Returns True if the
        entity was successfully removed, False if a ValueError is
        thrown (i.e. the entity isn't actually in the list).
        """
        try:
            self.entities.remove(entity)
            return True
        except ValueError:
            return False
                        
    
