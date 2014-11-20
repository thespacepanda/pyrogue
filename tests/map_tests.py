"""
     tests.map_tests
     ~~~~~~~~~~~~~~~

     This module tests everything in pyrogue.map
"""

import unittest
import itertools

import pyrogue.map as m

class PointTest(unittest.TestCase):
    """
    This class abstracts over the functions which test the Point class.
    """
    def setUp(self):
        self.horizontal_points = []
        self.vertical_points = []
        self.diagonal_points = {
            # impossible to calculate with index, just using some
            # pythagorean triples.
            m.Point(3, 4): 5.0,
            m.Point(5, 12): 13.0,
            m.Point(8, 15): 17.0,
            m.Point(7, 24): 25.0,
            m.Point(20, 21): 29.0,
            m.Point(12, 35): 37.0,
            m.Point(9, 40): 41.0,
            m.Point(28, 45): 53.0,
            m.Point(11, 60): 61.0,
            m.Point(16, 63): 65.0
        }
        for point_y in range(10):
            # easy to calculate
            next_point = m.Point(0, point_y)
            self.horizontal_points.append(next_point)
        for point_x in range(10):
            # also easy to calculate
            next_point = m.Point(point_x, 0)
            self.vertical_points.append(next_point)
    def test_distance(self):
        """
        This tests the distance from a fixed point (the origin).
        """
        origin = m.Point(0, 0)
        for index, point in enumerate(self.horizontal_points):
            distance = origin.distance(point)
            self.assertEqual(distance, index)
        for index, point in enumerate(self.vertical_points):
            distance = origin.distance(point)
            self.assertEqual(distance, index)
        for point, hypotenuse in self.diagonal_points.items():
            distance = origin.distance(point)
            self.assertEqual(distance, hypotenuse)

class RectTest(unittest.TestCase):
    """
    This class abstracts over the functions that test the Rect class.
    """
    def setUp(self):
        # all rects will start at origin :p
        self.origin = m.Point(0, 0)
        self.rects = {
            # easier to set up simple rects than to generate en mass.
            # maps (width, height) tuples to area and vertices
            (1, 1): [
                1,
                (m.Point(0, 0), m.Point(1, 0),
                 m.Point(0, 1), m.Point(1, 1))
            ]
        }
        self.actual_rects = {}
        for width, height in self.rects:
            self.actual_rects[(width, height)] = m.Rect(self.origin,
                                                        width, height)
    def test_area(self):
        """
        Tests area function.
        """
        for rect in self.rects:
            self.assertEqual(self.actual_rects[rect].get_area(),
                             self.rects[rect][0])
    def test_vertices(self):
        """
        Tests vertex creation.
        """
        # have to turn into tuples to test equality
        for rect in self.rects:
            actual = self.actual_rects[rect].get_vertices()
            actual_tuples = [(point.x, point.y) for point in actual]
            derived = self.rects[rect][1]
            derived_tuples = [(point.x, point.y) for point in derived]
            self.assertEqual(actual_tuples, derived_tuples)

class CellTest(unittest.TestCase):
    """
    This class abstracts tests over the Cell class.
    """
    def setUp():
        self.walls = [m.Cell(x, y) for x in range(10)
                      for y in range(10)]
        self.floors = [m.Cell(x, y) for x in range(10)
                       for y in range(10)]
