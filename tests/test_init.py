from gamestorm import *
import unittest2 as unittest

class TestInit(unittest.TestCase):
    NUM_TILES_X = 4
    NUM_TILES_Y = 6
    TILE_SIZE = TileSize.MEDIUM
    DEBUG = DebugMode.GRID

    def test_init_when_already_initialized(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)
        with self.assertRaises(RuntimeError):
            g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)
        g.quit()

    def test_valid_init(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE, debug_mode = self.DEBUG)

        self.assertEquals(g.num_tiles_x, self.NUM_TILES_X)
        self.assertEquals(g.num_tiles_y, self.NUM_TILES_Y)
        self.assertEquals(g.tile_size, self.TILE_SIZE)
        self.assertEquals(g.debug_mode, self.DEBUG)

        g.quit()

    #num_tiles_x field
    def test_none_num_tiles_x(self):
        TEST_NUM_TILES_X = None
        g = gamestorm.GameStorm()
        with self.assertRaises(TypeError):
            g.init(TEST_NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()
        
    def test_zero_num_tiles_x(self):
        TEST_NUM_TILES_X = 0
        g = gamestorm.GameStorm()
        with self.assertRaises(ValueError):
            g.init(TEST_NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()

    def test_negative_num_tiles_x(self):
        TEST_NUM_TILES_X = -4
        g = gamestorm.GameStorm()
        with self.assertRaises(ValueError):
            g.init(TEST_NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()

    def test_wrong_type_double_num_tiles_x(self):
        TEST_NUM_TILES_X = 4.212
        g = gamestorm.GameStorm()
        with self.assertRaises(TypeError):
            g.init(TEST_NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()

    def test_wrong_type_string_num_tiles_x(self):
        TEST_NUM_TILES_X = 'asd'
        g = gamestorm.GameStorm()
        with self.assertRaises(TypeError):
            g.init(TEST_NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()

    #num_tiles_y field
    def test_none_num_tiles_y(self):
        TEST_NUM_TILES_Y = None
        g = gamestorm.GameStorm()
        with self.assertRaises(TypeError):
            g.init(self.NUM_TILES_X, TEST_NUM_TILES_Y, self.TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()

    def test_zero_num_tiles_y(self):
        TEST_NUM_TILES_Y = 0
        g = gamestorm.GameStorm()
        with self.assertRaises(ValueError):
            g.init(self.NUM_TILES_X, TEST_NUM_TILES_Y, self.TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()

    def test_negative_num_tiles_y(self):
        TEST_NUM_TILES_Y = -6
        g = gamestorm.GameStorm()
        with self.assertRaises(ValueError):
            g.init(self.NUM_TILES_X, TEST_NUM_TILES_Y, self.TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()

    def test_wrong_type_double_num_tiles_y(self):
        TEST_NUM_TILES_Y = 6.123
        g = gamestorm.GameStorm()
        with self.assertRaises(TypeError):
            g.init(self.NUM_TILES_X, TEST_NUM_TILES_Y, self.TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()

    def test_wrong_type_string_num_tiles_y(self):
        TEST_NUM_TILES_Y = 'qwe'
        g = gamestorm.GameStorm()
        with self.assertRaises(TypeError):
            g.init(self.NUM_TILES_X, TEST_NUM_TILES_Y, self.TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()
    
    #tile_size field
    def test_none_tile_size(self): 
        TEST_TILE_SIZE = None
        g = gamestorm.GameStorm()
        with self.assertRaises(TypeError):
            g.init(self.NUM_TILES_X, self.NUM_TILES_Y, TEST_TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()

    def test_wrong_type_double_tile_size(self):
        TEST_TILE_SIZE = 3.221
        g = gamestorm.GameStorm()
        with self.assertRaises(TypeError):
            g.init(self.NUM_TILES_X, self.NUM_TILES_Y, TEST_TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()

    def test_wrong_type_string_num_tiles_y(self):
        TEST_TILE_SIZE = 'asd'
        g = gamestorm.GameStorm()
        with self.assertRaises(TypeError):
            g.init(self.NUM_TILES_X, self.NUM_TILES_Y, TEST_TILE_SIZE, debug_mode = self.DEBUG)
        g.quit()

    #debug field
    def test_omit_debug(self): 
        EXPECTED_DEBUG = DebugMode.NONE
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)
        self.assertEquals(g.debug_mode, EXPECTED_DEBUG)
        g.quit()

    def test_none_debug(self): 
        TEST_DEBUG = None
        g = gamestorm.GameStorm()
        with self.assertRaises(TypeError):
            g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE, debug_mode = TEST_DEBUG)
        g.quit()

    def test_wrong_type_double_debug(self):
        TEST_DEBUG = 3.22
        g = gamestorm.GameStorm()
        with self.assertRaises(TypeError):
            g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE, debug_mode = TEST_DEBUG)
        g.quit()

    def test_wrong_type_string_debug(self):
        TEST_DEBUG = 'asdf'
        g = gamestorm.GameStorm()
        with self.assertRaises(TypeError):
            g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE, debug_mode = TEST_DEBUG)
        g.quit()

    #order
    def test_quit_before_init(self):
        g = gamestorm.GameStorm()
        g.quit()


