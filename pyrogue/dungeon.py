"""
    pyrogue.dungeon
    ~~~~~~~~~~~~~~~

    This module generates the dungeon for the game.
"""

from geometry import Rect, Point, to_point

import constants

class Dungeon(object):
    """
    This class represents the dungeon. When instantiated, it will
    lazily generate the dungeon as needed by the game (i.e. floors
    which have not been accessed will be generated as they are
    accessed.)
    """
    def __init__(self):
        self._rooms = []
        center_x = int(constants.MAP_WIDTH / 2)
        center_y = int(constants.MAP_WIDTH / 2)
        self.add_room(Room(Point(center_x, center_y), 10, 10))
    def add_room(self, room):
        """
        Takes care of adding rooms and walls simultaneously.
        """
        self._rooms.append(room)
        for wall in room.walls:
            self._walls.append(wall)

class Room(Rect):
    """
    This class represents a room in our dungeon - it has four walls
    and four corners.
    """
    def __init__(self, center, width, height):
        start_x = int(center.x - (width / 2))
        start_y = int(center.y - (height / 2))
        assert start_x >= 0
        assert start_y >= 0
        start = Point(start_x, start_y)

        super().__init__(start, width, height)

        end_x = self.start.x + width
        end_y = self.start.y + height
        self.end = Point(end_x, end_y)

        self.populate()

        _, self.top_right, self.bottom_left, _ = self.get_vertices()
        self.north = Wall(self.start, self.top_right)
        self.south = Wall(self.bottom_left, self.end)
        self.east = Wall(self.top_right, self.end)
        self.west = Wall(self.start, self.bottom_left)
        self.walls = [self.north, self.south, self.east, self.west]
    def populate(self):
        """
        This fills our internal list with the points between our
        start point and end point
        """
        x_values = range(self.start.x, self.end.x)
        y_values = range(self.start.y, self.end.y)
        # range() isn't inclusive, so we'll need to add the end
        # point after we're done
        self.points = [Point(x, y).to_tuple() for x in x_values
                       for y in y_values]
        self.points.append(self.end.to_tuple())
    def within(self, point):
        """
        Queries whether a point is inside the room.
        """
        return point.to_tuple() in self.points

class Wall(object):
    """
    This class represents a wall of a room and allows the user to
    query whether a point is on the wall, etc.
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.populate()
    def populate(self):
        """
        This fills our internal list with the points between our
        start point and end point
        """
        x_values = range(self.start.x, self.end.x)
        y_values = range(self.start.y, self.end.y)
        # range() isn't inclusive, so we'll need to add the end
        # point after we're done
        self.points = [Point(x, y).to_tuple() for x in x_values
                       for y in y_values]
        self.points.append(self.end.to_tuple())
    def within(self, point):
        """
        Queries whether a point is on the wall.
        """
        return point.to_tuple() in self.points
