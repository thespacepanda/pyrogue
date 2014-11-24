"""
    pyrogue.dungeon
    ~~~~~~~~~~~~~~~

    This module generates the dungeon for the game.
"""

from geometry import Rect, Point, to_point

import constants

import random

class Dungeon(object):
    """
    This class represents the dungeon. When instantiated, it will
    lazily generate the dungeon as needed by the game (i.e. floors
    which have not been accessed will be generated as they are
    accessed.)
    """
    def __init__(self):
        self._rooms = []
        self._walls = []
        self._doors = []

        self.width_range = []
        self.height_range = []

        center_x = int(constants.MAP_WIDTH / 2)
        center_y = int(constants.MAP_WIDTH / 2)

        self.add_room(Room(Point(center_x, center_y), 10, 10))

        self.build()
    def add_room(self, room):
        """
        Takes care of adding rooms and walls simultaneously.
        """
        self._rooms.append(room)
        for wall in room.walls:
            self._walls.append(wall.to_tuple())
        start = room.start
        end = room.end
        self.width_range.append((start.x, end.x))
        self.height_range.append((start.y, end.y))
    def can_add(self, room):
        """
        Queries whether there is space to add the room.
        """
        x_lower, x_upper = room.start.x, room.end.x
        y_lower, y_upper = room.start.y, room.end.y

        if x_lower < 0 or y_lower < 0:
            return False
        if x_upper > constants.MAP_WIDTH or y_upper > constants.MAP_HEIGHT:
            return False

        x_flag = False
        y_flag = False

        for low, up in self.width_range:
            if x_lower <= low and x_upper >= up:
                x_flag = True
                break
        for low, up in self.height_range:
            if y_lower <= low and y_upper >= up:
                y_flag = True
                break

        if x_flag and y_flag:
            return False
        else:
            return True
    def build(self):
        """
        Bulk of generation algorithm; chooses random wall and
        builds adjacent room.
        """
        while len(self._walls) > 0:
            # we will remove walls from the list once we build
            # beside them
            current_wall = to_wall(random.choice(self._walls))
            print("current wall is: {}".format(current_wall))
            width = random.randrange(2, 10)
            height = random.randrange(2, 10)
            print("size is: {}, {}".format(width, height))
            room = room_from_wall(current_wall, width, height)
            print("room is: {}".format(room))

            if self.can_add(room):
                print("CAN ADD")
                self._walls.remove(current_wall.to_tuple())
                print("removed wall")
                self.add_room(room)
                print("added room")
            else:
                print("couldn't add room")
                print("WALLS: {}".format(len(self._walls)))
                continue

def room_from_wall(wall, width, height):
    """
    Returns a room of the specified size that has the given wall.
    """
    wall_center = wall.center
    if wall.north:
        center_y = int(wall_center.y - (height / 2))
        room = Room(Point(wall_center.x, center_y), width, height)
    elif wall.south:
        center_y = int(wall_center.y + (height / 2))
        room = Room(Point(wall_center.x, center_y), width, height)
    elif wall.east:
        center_x = int(wall_center.x + (width / 2))
        room = Room(Point(center_x, wall_center.y), width, height)
    elif wall.west:
        center_x = int(wall_center.x - (width / 2))
        room = Room(Point(center_x, wall_center.y), width, height)
    return room

class Room(Rect):
    """
    This class represents a room in our dungeon - it has four walls
    and four corners.
    """
    def __init__(self, center, width, height):
        start_x = int(center.x - (width / 2))
        start_y = int(center.y - (height / 2))
        start = Point(start_x, start_y)

        self.center = center

        super().__init__(start, width, height)

        end_x = self.start.x + width
        end_y = self.start.y + height
        self.end = Point(end_x, end_y)

        self.populate()

        _, self.top_right, self.bottom_left, _ = self.get_vertices()
        self.north = Wall("North", self.start, self.top_right)
        self.south = Wall("South", self.bottom_left, self.end)
        self.east = Wall("East", self.top_right, self.end)
        self.west = Wall("West", self.start, self.bottom_left)
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
    def __init__(self, direction, start, end):
        self.direction = direction
        self.north = False
        self.south = False
        self.east = False
        self.west = False
        if direction == "North":
            self.north = True
        elif direction == "South":
            self.south = True
        elif direction == "East":
            self.east = True
        elif direction == "West":
            self.west = True

        self.start = start
        self.end = end

        center_x = int(start.x + (end.x - start.x) / 2)
        center_y = int(start.y + (end.y - start.y) / 2)
        self.center = Point(center_x, center_y)

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
    def to_tuple(self):
        """
        Returns a tuple representation of itself.
        """
        return (self.direction,
                (self.start.x, self.start.y),
                (self.end.x, self.end.y))

def to_wall(tup):
    """
    Reconstructs wall from tuple.
    """
    direction, start, end = tup
    return Wall(direction, to_point(start), to_point(end))
