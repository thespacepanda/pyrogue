import unittest

import pyrogue.tile
import pyrogue.world

class AdjacentTiles(unittest.TestCase):
    """This test is designed to catch negative positions"""
    def setUp(self):
        keys = [(x, y) for x in range(80)
                for y in range(45)]
        self.level = dict.fromkeys(keys, pyrogue.tile.Floor())
    def test_adjacents(self):
        adjmap = {}
        for tile in self.level:
            adjmap[tile] = list(pyrogue.world.Map.get_adjacents(tile))
        flattened = adjmap.values()
        for adjacents in flattened:
            for x, y in adjacents:
                self.assertTrue(x >= 0)
                self.assertTrue(y >= 0)

if __name__ == "__main__":
    unittest.main()
