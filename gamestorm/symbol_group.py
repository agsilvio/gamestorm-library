class SymbolGroup():
    '''
    This represents a collection of symbols. It is useful for when you want to define a shape of symbols once and use it multiple times. It is meant to be used with GameStorm.draw_symbol_group().
    '''

    def __init__(self, width_tiles, height_tiles):
        if not isinstance(width_tiles, int):
            raise TypeError('width_tiles must be a positive int')
        if not isinstance(height_tiles, int):
            raise TypeError('height_tiles must be a positive int')
        if width_tiles < 0:
            raise ValueError('width_tiles must be a positive int')
        if height_tiles < 0:
            raise ValueError('height_tiles must be a positive int')

        self.width_tiles = width_tiles
        self.height_tiles = height_tiles
        self.grid = []
        for x in range(self.width_tiles):
            self.grid.append([])
            for y in range(self.height_tiles):
                self.grid[x].append(None)

    def set_symbol(self, x, y, symbol):
        '''
        Set a symbol at the given position in this SymbolGroup

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 0) |The x coordinate of the SymbolGroup's tile to which you want to set a symbol.|
        | y | int (>= 0) |The y coordinate of the SymbolGroup's tile to which you want to set a symbol.|
        | symbol | int (>= 0) |The number ID of the symbol you want to set.|

        Returns:  
        | Type | Description |
        |---|---|
        | int | The ID of the background resource of the given tile. |
        '''
        if not isinstance(x, int):
            raise TypeError('x must be a positive int')
        if not isinstance(y, int):
            raise TypeError('y must be a positive int')
        if not None and not isinstance(symbol, int):
            raise TypeError('symbol must be a positive int')
        if x < 0 or x >= self.width_tiles:
            raise ValueError('x tile out of this symbol group\'s range')
        if y < 0 or y >= self.height_tiles:
            raise ValueError('y tile out of this symbol group\'s range')
        if symbol and symbol < 0:
            raise ValueError('symbol must be a positive int')

        self.grid[x][y] = symbol

    def set_all_symbols(self, symbol):
        '''
        Sets a symbol to all positions in this SymbolGroup

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | symbol | int (>= 0) |The number ID of the symbol you want to set.|

        Returns: None  
        '''
        if not None and not isinstance(symbol, int):
            raise TypeError('symbol must be a positive int')
        if symbol and symbol < 0:
            raise ValueError('y tile our of this symbol group\'s range')

        for x in range(self.width_tiles):
            for y in range(self.height_tiles):
                self.grid[x][y] = symbol

    def clear_symbol(self, x, y):
        '''
        Clears (sets to None) a symbol at the given position.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 0) |The x coordinate of the SymbolGroup's tile whose symbol should be cleared.|
        | y | int (>= 0) |The y coordinate of the SymbolGroup's tile whose symbol should be cleared.|

        Returns: None
        '''
        if not isinstance(x, int):
            raise TypeError('x must be a positive int')
        if not isinstance(y, int):
            raise TypeError('y must be a positive int')
        if x < 0 or x >= self.width_tiles:
            raise ValueError('x tile out of this symbol group\'s range')
        if y < 0 or y >= self.height_tiles:
            raise ValueError('y tile out of this symbol group\'s range')

        self.grid[x][y] = None


    def get_grid(self):
        '''
        Returns the grid that makes up this SymbolGroup.

        Arguments: None  

        Returns:  
        | Type | Description |
        |---|---|
        | int[][] | A two-dimensional array representing the SymbolGroup. If a symbol is present in a position, that position will contain an 'int'. Otherwise, it will contain 'None'. |
        '''
        return self.grid

        


