"""
    pyrogue.actor
    ~~~~~~~~~~~~~

    This represents entities that can do actions.
"""

from entity import Entity

class Actor(Entity):
    """This is an entity which can interact with entities."""
    def act(self):
        """If the player is visible, actors will chase him"""
        if player in self.visible_actors:
            self.follow(player.map_position)
    def follow(self, entity):
        self_x, self_y = self.map_position
        entity_x, entity_y = entity.map_position
        delta_x, delta_y = (0, 0)
        if self_x > entity_x:
            delta_x = -1
        else:
            delta_x = 1
        if self_y > entity_y:
            delta_y = -1
        else:
            delta_y = 1
        self.move(delta_x, delta_y)
    def move(self, delta_x, delta_y):
        """This takes a change in x and y and updates self.map_position"""
        current_x, current_y = self.map_position
        self.map_position = (current_x + delta_x,
                             current_y + delta_y)
