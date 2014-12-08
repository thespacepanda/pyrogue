"""
    pyrogue.world
    ~~~~~~~~~~~~~

    This module represents the world of the game, which handles all game logic
    outside of player input and drawing to the screen.
"""

import player
import tile
import constants
import dungeon
import monsters
import weapon

import random

class World(object):
    """The game world, including all tiles and entities."""
    def __init__(self):
        self._map = Map()
        starting_pos = self._starting_pos()
        self.tiles = self._map.current_level.tiles
        self.valid_tiles = self._map.current_level.empty_tiles
        self.player = player.Player(starting_pos)
        self.entities = {starting_pos: self.player}
        self.spawn_monsters()
    def _starting_pos(self):
        """This puts the player beside some upward stairs"""
        stairs = (pos for pos in self._map.current_level.up_stairs)
        for stair in stairs:
            for position in self._map.get_adjacents(stair):
                if self._map.is_empty(position):
                    return position
        raise Exception("Nowhere to put player...")
    def update(self):
        for pos in self.entities.copy():
            if self.entities[pos].health <= 0:
                if self.entities[pos] == self.player:
                    self.player.quit(True)
                del self.entities[pos]
        for tile in self.player.explored:
            try:
                monster = self.entities[tile]
                try:
                    new_pos = monster.follow(self.player.pos)
                    monster.move(new_pos, self)
                except AttributeError:
                    pass
            except KeyError:
                continue
        self.player.regen()
    def blocked(self, pos):
        return not self._map.is_empty(pos) or pos in self.entities
    def spawn_monsters(self):
        """
        This spawns a random number of enemies in the empty space.
        """
        for monster in range(10):
            monster_class = random.choice(monsters.MONSTER_TYPES)
            position = random.choice([tile for tile in self.valid_tiles])
            self.entities[position] = monster_class(position)
    def spawn_weapons(self):
        """
        This spawns a random number of weapons in the empty space.
        """
        for weapon in range(10):
            weapon_class = random.choice(weapon.WEAPON_TYPES)
            position = random.choice([tile for tile in self.valid_tiles])
            self.entities[position] = weapon_class()
class Map(object):
    """The game map, over all the levels."""
    def __init__(self):
        self.levels = 10
        self.current_level = Level()
        self.old_levels = []
    @staticmethod
    def get_adjacents(position):
        """Returns a generator of all points adjacent to a point."""
        pos_x, pos_y = position
        return ((a, b) for a in range(pos_x-1, pos_x+2)
                for b in range(pos_y-1, pos_y+2)
                if (a != pos_x or b != pos_y)
                and (a >= 0 and b >= 0))
    def is_empty(self, position):
        return self.current_level.is_empty(position)
    def next_level(self):
        if self.levels:
            down_stairs = self.current_level.down_stairs
            self.current_level = Level(down_stairs)

class Level(object):
    """A single level, has more meta-data than just a matrix."""
    def __init__(self, down_stairs=None):
        self.dungeon = dungeon.Dungeon()
        self.tiles = self.dungeon.tiles
        self.valid_tiles = [tile for room in self.dungeon._rooms for tile in room.points]
        self.empty_tiles = [tile for tile in self.valid_tiles if self.is_empty(tile)]
        self.stair_limit = 4
        if down_stairs is None:
            self.up_stairs = self.stair_gen("up")
        self.down_stairs = self.stair_gen("down")
    def is_empty(self, position):
        return not self.tiles[position].obstacle
    def stair_gen(self, direction):
        if direction == "up":
            stair = tile.UpStair
        else:
            stair = tile.DownStair
        stairs = []
        valid_tiles = [tile for room in self.dungeon._rooms for tile in room.points]
        empty_tiles = [tile for tile in valid_tiles if self.is_empty(tile)]
        for _ in range(self.stair_limit):
            new_stair = random.choice(empty_tiles)
            stairs.append(new_stair)
            self.tiles[(new_stair)] = stair()
        return stairs
