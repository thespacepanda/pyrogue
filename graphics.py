import libtcodpy as libtcod

class Stamp:
    """
    This class represents drawing the game to a given virtual console,
    which is blitted to the real console in main. You initialize this
    class with a virtual console, and an optional entity list. This
    class assumes that the entities have a character, a color, and
    x, y coordinates.
    """
    def __init__(self, entities=[], SCREEN_WIDTH=80, SCREEN_HEIGHT=50):
        self.entities = entities
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.console = libtcod.console_new(self.SCREEN_WIDTH,
                                           self.SCREEN_HEIGHT)         
        libtcod.console_set_custom_font(b'arial10x10.png',
                                        libtcod.FONT_TYPE_GREYSCALE |
                                        libtcod.FONT_LAYOUT_TCOD)
        libtcod.console_init_root(self.SCREEN_WIDTH, self.SCREEN_HEIGHT,
                                  b'python/libtcod tutorial', False)

        
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
        self.blit()
        self.flush()
        #self.clear()
        
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
        
    def blit(self):
        libtcod.console_blit(self.console, 0, 0, self.SCREEN_WIDTH,
                             self.SCREEN_HEIGHT, 0, 0, 0)
    def flush(self):
        libtcod.console_flush()
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
                        
    
