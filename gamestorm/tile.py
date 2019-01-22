from .constants import *

class Tile:
    background = None
    symbol = None
    symbol_direction = None
    cursor = None

    def set_background(self, background):
        if not isinstance(background, int) or background <= 0:
            raise TypeError('"background" must be a positive integer.')

        self.background = background

    def set_symbol(self, symbol, direction):
        if not isinstance(symbol, int) or symbol < 0:
            raise TypeError('"symbol" must be a positive integer.')
        if not isinstance(direction, Direction):
            raise TypeError('"direction" must be a Direction enum key')

        self.symbol = symbol
        self.symbol_direction = direction


    def set_cursor(self, cursor):
        if not isinstance(cursor, int) or cursor <= 0:
            raise TypeError('"cursor" must be a positive integer.')

        self.cursor = cursor

    def get_background(self):
        return self.background

    def get_symbol(self):
        return self.symbol

    def get_symbol_direction(self):
        return self.symbol_direction

    def get_cursor(self):
        return self.cursor

    def clear_background(self):
        self.background = None

    def clear_symbol(self):
        self.symbol = None

    def clear_cursor(self):
        self.cursor = None

    def clear_everything(self):
        self.clear_background()
        self.clear_symbol()
        self.clear_cursor()
