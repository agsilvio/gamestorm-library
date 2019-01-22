from gamestorm import symbol_group as sg
import unittest2 as unittest


class TestSymbolGroup(unittest.TestCase):
    WIDTH_TILES = 3
    HEIGHT_TILES = 4

    def test_valid_init(self):
        s = sg.SymbolGroup(self.WIDTH_TILES, self.HEIGHT_TILES)

    def test_invalid_init(self):
        with self.assertRaises(ValueError):
            s = sg.SymbolGroup(-1, self.HEIGHT_TILES)
        with self.assertRaises(ValueError):
            s = sg.SymbolGroup(self.WIDTH_TILES, -1)
        with self.assertRaises(TypeError):
            s = sg.SymbolGroup(None, self.HEIGHT_TILES)
        with self.assertRaises(TypeError):
            s = sg.SymbolGroup(self.WIDTH_TILES, None)
        with self.assertRaises(TypeError):
            s = sg.SymbolGroup('asd', self.HEIGHT_TILES)
        with self.assertRaises(TypeError):
            s = sg.SymbolGroup(self.WIDTH_TILES, 'asd')

    
    def test_get_grid(self):
        s = sg.SymbolGroup(self.WIDTH_TILES, self.HEIGHT_TILES)
        grid = s.get_grid()

        self.assertEquals(self.WIDTH_TILES, len(grid))
        self.assertEquals(self.HEIGHT_TILES, len(grid[0]))

