from gamestorm import *
import unittest2 as unittest

class TestTileOperations(unittest.TestCase):

    NUM_TILES_X = 7
    NUM_TILES_Y = 10
    TILE_SIZE = TileSize.MEDIUM

    X_TILE_1 = 2
    Y_TILE_1 = 3

    X_TILE_2 = 4
    Y_TILE_2 = 5

    SYMBOL_1 = 6
    BACKGROUND_1 = 7
    CURSOR_1 = 8
    SYMBOL_2 = 9
    BACKGROUND_2 = 10
    CURSOR_2 = 11


    def test_get_tile_out_of_bounds(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)
        with self.assertRaises(IndexError):
            g._get_tile_at_x_y(self.NUM_TILES_X + 10, self.NUM_TILES_Y)
        with self.assertRaises(IndexError):
            g._get_tile_at_x_y(self.NUM_TILES_X, self.NUM_TILES_Y + 10)
        with self.assertRaises(IndexError):
            g._get_tile_at_x_y(-10, self.NUM_TILES_Y)
        with self.assertRaises(IndexError):
            g._get_tile_at_x_y(self.NUM_TILES_X, -10)
        g.quit()

    def test_tile_operations_when_grid_uninitialized(self):
        g = gamestorm.GameStorm()
        with self.assertRaises(RuntimeError):
            g.clear_tile_background(2, 2)
        with self.assertRaises(RuntimeError):
            g.clear_tile_symbol(2, 2)
        with self.assertRaises(RuntimeError):
            g.clear_tile_cursor(2, 2)
        with self.assertRaises(RuntimeError):
            g.clear_tile_everything(2, 2)
        with self.assertRaises(RuntimeError):
            g.get_tile_background(2, 2)
        with self.assertRaises(RuntimeError):
            g.get_tile_symbol(2, 2)
        with self.assertRaises(RuntimeError):
            g.get_tile_cursor(2, 2)
        with self.assertRaises(RuntimeError):
            g.set_tile_cursor(2, 2, 3)
        with self.assertRaises(RuntimeError):
            g.set_tile_background(2, 2, 4)
        with self.assertRaises(RuntimeError):
            g.set_tile_symbol(2, 2, 2)
        with self.assertRaises(RuntimeError):
            g.set_all_tiles_background(4)
        with self.assertRaises(RuntimeError):
            g.clear_all_tiles_everything()
        with self.assertRaises(RuntimeError):
            g.clear_all_tiles_symbol()
        with self.assertRaises(RuntimeError):
            g.clear_all_tiles_background()
        with self.assertRaises(RuntimeError):
            g.clear_all_tiles_cursor()
        with self.assertRaises(RuntimeError):
            g.get_events()
        with self.assertRaises(RuntimeError):
            g.is_left_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.is_right_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.is_up_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.is_down_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.is_start_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.is_select_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.is_1_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.is_2_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.is_3_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.is_4_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.is_5_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.is_6_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.is_exit_button_pressed(None)
        with self.assertRaises(RuntimeError):
            g.play_music(2)
        with self.assertRaises(RuntimeError):
            g.stop_current_music()
        with self.assertRaises(RuntimeError):
            g.pause_current_music()
        with self.assertRaises(RuntimeError):
            g.resume_current_music()
        with self.assertRaises(RuntimeError):
            g.play_soundfx(2)
        with self.assertRaises(RuntimeError):
            g.stop_soundfx(2)
        with self.assertRaises(RuntimeError):
            g.stop_all_soundfx()
        with self.assertRaises(RuntimeError):
            g.pause_all_sound()
        with self.assertRaises(RuntimeError):
            g.resume_all_sound()
        with self.assertRaises(RuntimeError):
            g.stop_all_sound()
        with self.assertRaises(RuntimeError):
            g.draw_text(2, 2, 'asd')
        with self.assertRaises(RuntimeError):
            g.draw()
        with self.assertRaises(RuntimeError):
            g.apply_symbol_group(2, 2, 2)
        g.quit()

    #valid case tests
    def test_clear_all_tiles_symbol(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)

        #set tile 1
        g.set_tile_background(self.X_TILE_1, self.Y_TILE_1, self.BACKGROUND_1)
        g.set_tile_symbol(self.X_TILE_1, self.Y_TILE_1, self.SYMBOL_1)
        g.set_tile_cursor(self.X_TILE_1, self.Y_TILE_1, self.CURSOR_1)

        g.clear_all_tiles_symbol()

        #get tile 1 again
        actualBg1 = g.get_tile_background(self.X_TILE_1, self.Y_TILE_1)
        actualSym1 = g.get_tile_symbol(self.X_TILE_1, self.Y_TILE_1)
        actualCur1 = g.get_tile_cursor(self.X_TILE_1, self.Y_TILE_1)

        self.assertIsNone(actualSym1)

        self.assertEqual(self.BACKGROUND_1, actualBg1)
        self.assertEqual(self.CURSOR_1, actualCur1)
        g.quit()

    def test_clear_all_tiles_background(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)

        #set tile 1
        g.set_tile_background(self.X_TILE_1, self.Y_TILE_1, self.BACKGROUND_1)
        g.set_tile_symbol(self.X_TILE_1, self.Y_TILE_1, self.SYMBOL_1)
        g.set_tile_cursor(self.X_TILE_1, self.Y_TILE_1, self.CURSOR_1)

        g.clear_all_tiles_background()

        #get tile 1 again
        actualBg1 = g.get_tile_background(self.X_TILE_1, self.Y_TILE_1)
        actualSym1 = g.get_tile_symbol(self.X_TILE_1, self.Y_TILE_1)
        actualCur1 = g.get_tile_cursor(self.X_TILE_1, self.Y_TILE_1)

        self.assertIsNone(actualBg1)

        self.assertEqual(self.SYMBOL_1, actualSym1)
        self.assertEqual(self.CURSOR_1, actualCur1)
        g.quit()

    def test_clear_all_tiles_cursor(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)

        #set tile 1
        g.set_tile_background(self.X_TILE_1, self.Y_TILE_1, self.BACKGROUND_1)
        g.set_tile_symbol(self.X_TILE_1, self.Y_TILE_1, self.SYMBOL_1)
        g.set_tile_cursor(self.X_TILE_1, self.Y_TILE_1, self.CURSOR_1)

        g.clear_all_tiles_cursor()

        #get tile 1 again
        actualBg1 = g.get_tile_background(self.X_TILE_1, self.Y_TILE_1)
        actualSym1 = g.get_tile_symbol(self.X_TILE_1, self.Y_TILE_1)
        actualCur1 = g.get_tile_cursor(self.X_TILE_1, self.Y_TILE_1)

        self.assertIsNone(actualCur1)

        self.assertEqual(self.SYMBOL_1, actualSym1)
        self.assertEqual(self.BACKGROUND_1, actualBg1)
        g.quit()

    def test_clear_tile_symbol(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)

        #set tile 1
        g.set_tile_background(self.X_TILE_1, self.Y_TILE_1, self.BACKGROUND_1)
        g.set_tile_symbol(self.X_TILE_1, self.Y_TILE_1, self.SYMBOL_1)
        g.set_tile_cursor(self.X_TILE_1, self.Y_TILE_1, self.CURSOR_1)

        g.clear_tile_symbol(self.X_TILE_1, self.Y_TILE_1)

        #get tile 1 again
        actualBg1 = g.get_tile_background(self.X_TILE_1, self.Y_TILE_1)
        actualSym1 = g.get_tile_symbol(self.X_TILE_1, self.Y_TILE_1)
        actualCur1 = g.get_tile_cursor(self.X_TILE_1, self.Y_TILE_1)

        self.assertIsNone(actualSym1)

        self.assertEqual(self.CURSOR_1, actualCur1)
        self.assertEqual(self.BACKGROUND_1, actualBg1)
        g.quit()

    def test_clear_tile_cursor(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)

        #set tile 1
        g.set_tile_background(self.X_TILE_1, self.Y_TILE_1, self.BACKGROUND_1)
        g.set_tile_symbol(self.X_TILE_1, self.Y_TILE_1, self.SYMBOL_1)
        g.set_tile_cursor(self.X_TILE_1, self.Y_TILE_1, self.CURSOR_1)

        g.clear_tile_cursor(self.X_TILE_1, self.Y_TILE_1)

        #get tile 1 again
        actualBg1 = g.get_tile_background(self.X_TILE_1, self.Y_TILE_1)
        actualSym1 = g.get_tile_symbol(self.X_TILE_1, self.Y_TILE_1)
        actualCur1 = g.get_tile_cursor(self.X_TILE_1, self.Y_TILE_1)

        self.assertIsNone(actualCur1)

        self.assertEqual(self.SYMBOL_1, actualSym1)
        self.assertEqual(self.BACKGROUND_1, actualBg1)
        g.quit()

    def test_clear_tile_background(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)

        #set tile 1
        g.set_tile_background(self.X_TILE_1, self.Y_TILE_1, self.BACKGROUND_1)
        g.set_tile_symbol(self.X_TILE_1, self.Y_TILE_1, self.SYMBOL_1)
        g.set_tile_cursor(self.X_TILE_1, self.Y_TILE_1, self.CURSOR_1)

        g.clear_tile_background(self.X_TILE_1, self.Y_TILE_1)

        #get tile 1 again
        actualBg1 = g.get_tile_background(self.X_TILE_1, self.Y_TILE_1)
        actualSym1 = g.get_tile_symbol(self.X_TILE_1, self.Y_TILE_1)
        actualCur1 = g.get_tile_cursor(self.X_TILE_1, self.Y_TILE_1)

        self.assertIsNone(actualBg1)

        self.assertEqual(self.SYMBOL_1, actualSym1)
        self.assertEqual(self.CURSOR_1, actualCur1)
        g.quit()

    def test_clear_tile_everything(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)

        #set tile 1
        g.set_tile_background(self.X_TILE_1, self.Y_TILE_1, self.BACKGROUND_1)
        g.set_tile_symbol(self.X_TILE_1, self.Y_TILE_1, self.SYMBOL_1)
        g.set_tile_cursor(self.X_TILE_1, self.Y_TILE_1, self.CURSOR_1)

        g.clear_tile_everything(self.X_TILE_1, self.Y_TILE_1)

        #get tile 1 again
        actualBg1 = g.get_tile_background(self.X_TILE_1, self.Y_TILE_1)
        actualSym1 = g.get_tile_symbol(self.X_TILE_1, self.Y_TILE_1)
        actualCur1 = g.get_tile_cursor(self.X_TILE_1, self.Y_TILE_1)

        self.assertIsNone(actualBg1)
        self.assertIsNone(actualSym1)
        self.assertIsNone(actualCur1)
        g.quit()

    def test_set_and_get_tile_background(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)
        g.set_tile_background(self.X_TILE_1, self.Y_TILE_1, self.BACKGROUND_1)
        actualBg1 = g.get_tile_background(self.X_TILE_1, self.Y_TILE_1)
        self.assertEqual(self.BACKGROUND_1, actualBg1)
        g.quit()

    def test_set_and_get_tile_symbol(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)
        g.set_tile_symbol(self.X_TILE_1, self.Y_TILE_1, self.SYMBOL_1)
        actualSym1 = g.get_tile_symbol(self.X_TILE_1, self.Y_TILE_1)
        self.assertEqual(self.SYMBOL_1, actualSym1)
        g.quit()

    def test_set_and_get_tile_cursor(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)
        g.set_tile_cursor(self.X_TILE_1, self.Y_TILE_1, self.CURSOR_1)
        actualCur1 = g.get_tile_cursor(self.X_TILE_1, self.Y_TILE_1)
        self.assertEqual(self.CURSOR_1, actualCur1)
        g.quit()

    def test_set_all_tiles_background(self):
        g = gamestorm.GameStorm()
        RANDOM_X_COORD_1 = 3
        RANDOM_Y_COORD_1 = 6
        RANDOM_X_COORD_2 = 2
        RANDOM_Y_COORD_2 = 7

        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)
        g.set_all_tiles_background(self.BACKGROUND_1)

        actualBg1 = g.get_tile_background(RANDOM_X_COORD_1, RANDOM_Y_COORD_1)
        actualBg2 = g.get_tile_background(RANDOM_X_COORD_2, RANDOM_Y_COORD_2)
        self.assertEqual(self.BACKGROUND_1, actualBg1)
        self.assertEqual(self.BACKGROUND_1, actualBg2)
        g.quit()

    #test invalid inputs
    def test_invalid_inputs(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)

        #clear all
        with self.assertRaises(TypeError):
            g._perform_clear_operation_on_all_tiles()
        with self.assertRaises(TypeError):
            g._perform_clear_operation_on_all_tiles('asd')
        with self.assertRaises(TypeError):
            g._perform_clear_operation_on_all_tiles(None)
        with self.assertRaises(TypeError):
            g._perform_clear_operation_on_all_tiles(1)

        #get tile
        with self.assertRaises(TypeError):
            g._get_tile_at_x_y('asd', self.Y_TILE_1)
        with self.assertRaises(TypeError):
            g._get_tile_at_x_y(self.X_TILE_1, 'asd')
        with self.assertRaises(TypeError):
            g._get_tile_at_x_y(None, self.Y_TILE_1)
        with self.assertRaises(TypeError):
            g._get_tile_at_x_y(self.X_TILE_1, None)
        with self.assertRaises(TypeError):
            g._get_tile_at_x_y(self.X_TILE_1)

        #set all tiles background
        with self.assertRaises(TypeError):
            g.set_all_tiles_background()
        with self.assertRaises(TypeError):
            g.set_all_tiles_background(None)
        with self.assertRaises(TypeError):
            g.set_all_tiles_background('asd')
        g.quit()

    def test_set_get_clear_all(self):
        g = gamestorm.GameStorm()
        g.init(self.NUM_TILES_X, self.NUM_TILES_Y, self.TILE_SIZE)

        #set tile 1
        g.set_tile_background(self.X_TILE_1, self.Y_TILE_1, self.BACKGROUND_1)
        g.set_tile_symbol(self.X_TILE_1, self.Y_TILE_1, self.SYMBOL_1)
        g.set_tile_cursor(self.X_TILE_1, self.Y_TILE_1, self.CURSOR_1)

        #set tile 2
        g.set_tile_background(self.X_TILE_2, self.Y_TILE_2, self.BACKGROUND_2)
        g.set_tile_symbol(self.X_TILE_2, self.Y_TILE_2, self.SYMBOL_2)
        g.set_tile_cursor(self.X_TILE_2, self.Y_TILE_2, self.CURSOR_2)

        #test that setting works by getting

        #get tile 1
        actualBg1 = g.get_tile_background(self.X_TILE_1, self.Y_TILE_1)
        actualSym1 = g.get_tile_symbol(self.X_TILE_1, self.Y_TILE_1)
        actualCur1 = g.get_tile_cursor(self.X_TILE_1, self.Y_TILE_1)

        #get tile 2
        actualBg2 = g.get_tile_background(self.X_TILE_2, self.Y_TILE_2)
        actualSym2 = g.get_tile_symbol(self.X_TILE_2, self.Y_TILE_2)
        actualCur2 = g.get_tile_cursor(self.X_TILE_2, self.Y_TILE_2)

        self.assertEquals(self.BACKGROUND_1, actualBg1)
        self.assertEquals(self.SYMBOL_1, actualSym1)
        self.assertEquals(self.CURSOR_1, actualCur1)

        self.assertEquals(self.BACKGROUND_2, actualBg2)
        self.assertEquals(self.SYMBOL_2, actualSym2)
        self.assertEquals(self.CURSOR_2, actualCur2)

        #clear all
        g.clear_all_tiles_everything()

        #get tile 1 again
        actualBg1 = g.get_tile_background(self.X_TILE_1, self.Y_TILE_1)
        actualSym1 = g.get_tile_symbol(self.X_TILE_1, self.Y_TILE_1)
        actualCur1 = g.get_tile_cursor(self.X_TILE_1, self.Y_TILE_1)

        #get tile 2 again
        actualBg2 = g.get_tile_background(self.X_TILE_2, self.Y_TILE_2)
        actualSym2 = g.get_tile_symbol(self.X_TILE_2, self.Y_TILE_2)
        actualCur2 = g.get_tile_cursor(self.X_TILE_2, self.Y_TILE_2)

        self.assertIsNone(actualBg1)
        self.assertIsNone(actualSym1)
        self.assertIsNone(actualCur1)

        self.assertIsNone(actualBg2)
        self.assertIsNone(actualSym2)
        self.assertIsNone(actualCur2)

        #set all tiles background
        g.set_all_tiles_background(self.BACKGROUND_2)

        #get tiles
        actualBg1 = g.get_tile_background(self.X_TILE_1, self.Y_TILE_1)
        actualBg2 = g.get_tile_background(self.X_TILE_2, self.Y_TILE_2)

        self.assertEquals(self.BACKGROUND_2, actualBg1)
        self.assertEquals(self.BACKGROUND_2, actualBg2)

