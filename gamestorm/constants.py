from enum import Enum

class ResourceType(Enum):
    BACKGROUND = 1
    SYMBOL = 2
    CURSOR = 3
    MUSIC = 4
    SOUNDFX = 5
    
class Direction(Enum):
    LEFT = 1
    UP = 2
    DOWN = 3
    RIGHT = 4


class TileSize(Enum):
    SMALL=32
    MEDIUM=48
    LARGE=72


class ClearOperation(Enum):
    SYMBOL = 1
    BACKGROUND = 2
    CURSOR = 3
    ALL = 4

class GamepadButton(Enum):
    B1 = 1
    B2 = 2
    B3 = 0
    B4 = 3
    B5 = 4
    B6 = 5
    START = 8
    SELECT = 9

class DebugMode(Enum):
    NONE = 1
    GRID = 2
    GRID_AND_COORDS = 3

char_to_filename = {}
#lower case
char_to_filename['a'] = 11
char_to_filename['b'] = 12
char_to_filename['c'] = 13
char_to_filename['d'] = 14
char_to_filename['e'] = 15
char_to_filename['f'] = 16
char_to_filename['g'] = 17
char_to_filename['h'] = 18
char_to_filename['i'] = 19
char_to_filename['j'] = 20
char_to_filename['k'] = 21
char_to_filename['l'] = 22
char_to_filename['m'] = 23
char_to_filename['n'] = 24
char_to_filename['o'] = 25
char_to_filename['p'] = 26
char_to_filename['q'] = 27
char_to_filename['r'] = 28
char_to_filename['s'] = 29
char_to_filename['t'] = 30
char_to_filename['u'] = 31
char_to_filename['v'] = 32
char_to_filename['w'] = 33
char_to_filename['x'] = 34
char_to_filename['y'] = 35
char_to_filename['z'] = 36
#upper case
char_to_filename['A'] = 11
char_to_filename['B'] = 12
char_to_filename['C'] = 13
char_to_filename['D'] = 14
char_to_filename['E'] = 15
char_to_filename['F'] = 16
char_to_filename['G'] = 17
char_to_filename['H'] = 18
char_to_filename['I'] = 19
char_to_filename['J'] = 20
char_to_filename['K'] = 21
char_to_filename['L'] = 22
char_to_filename['M'] = 23
char_to_filename['N'] = 24
char_to_filename['O'] = 25
char_to_filename['P'] = 26
char_to_filename['Q'] = 27
char_to_filename['R'] = 28
char_to_filename['S'] = 29
char_to_filename['T'] = 30
char_to_filename['U'] = 31
char_to_filename['V'] = 32
char_to_filename['W'] = 33
char_to_filename['X'] = 34
char_to_filename['Y'] = 35
char_to_filename['Z'] = 36

#numbers
char_to_filename['0'] = 1 
char_to_filename['1'] = 2
char_to_filename['2'] = 3
char_to_filename['3'] = 4
char_to_filename['4'] = 5
char_to_filename['5'] = 6
char_to_filename['6'] = 7
char_to_filename['7'] = 8
char_to_filename['8'] = 9
char_to_filename['9'] = 10

#special chars
char_to_filename['\''] = 38
char_to_filename['\\'] = 40
char_to_filename['&'] = 37
char_to_filename['*'] = 39
char_to_filename[':'] = 41
char_to_filename[','] = 42
char_to_filename['$'] = 43
char_to_filename['"'] = 44
char_to_filename['='] = 45
char_to_filename['!'] = 46
char_to_filename['/'] = 47
char_to_filename['-'] = 48
char_to_filename['['] = 51
char_to_filename['('] = 49
char_to_filename['`'] = 50
char_to_filename['<'] = 52
char_to_filename['#'] = 53
char_to_filename['%'] = 54
char_to_filename['.'] = 55
char_to_filename['+'] = 56
char_to_filename['?'] = 57
char_to_filename[']'] = 59
char_to_filename[')'] = 58
char_to_filename['>'] = 60
char_to_filename[';'] = 61
char_to_filename[' '] = 62


DEFAULT_TILES_X = 15
DEFAULT_TILES_Y = 10
DEFAULT_TILE_SIZE = TileSize.MEDIUM
DEFAULT_CURSOR = 2
DEFAULT_DIRECTION = Direction.UP
DEBUG_TEXT_OFFSET = 5
DEBUG_TEXT_SIZE = 10

EMPTY_BACKGROUND = 999

