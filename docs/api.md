GameStorm
==


Classes
----------

### class `GameStorm()`

No documentation for this class

Methods:

#### def `apply_symbol_group(x, y, symbol_group, direction=1)`

Sets the given SymbolGroup's symbols to those of the tiles starting at the given coordinates. The orientation of the symbol can be given by supplying a value for direction.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 
 symbol_group | SymbolGroup | The SymbolGroup to draw. 
 direction | Direction | The desired orientation of the SymbolGroup. Can be `Direction.UP`, `Direction.DOWN`, `Direction.LEFT`, `Direction.RIGHT`. Defaults to `Direction.UP`

Returns: None

#### def `clear_all_tiles_background()`

Clears the background of all the tiles in the grid.

Arguments: None
Returns: None

#### def `clear_all_tiles_cursor()`

Clears the cursor of all the tiles in the grid.

Arguments: None
Returns: None

#### def `clear_all_tiles_everything()`

Clears the background, symbol, and cursor of all the tiles in the grid.

Arguments: None
Returns: None

#### def `clear_all_tiles_symbol()`

Clears the symbol of all the tiles in the grid.

Arguments: None
Returns: None

#### def `clear_tile_background(x, y)`

Clears (sets to None) the background of the given tile in the grid.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 

Returns: None

#### def `clear_tile_cursor(x, y)`

Clears (sets to None) the cursor of the given tile in the grid.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 

Returns: None

#### def `clear_tile_everything(x, y)`

Clears (sets to None) the background, symbol, and cursor of the given tile in the grid.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 

Returns: None

#### def `clear_tile_symbol(x, y)`

Clears (sets to None) the symbol of the given tile in the grid.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 

Returns: None

#### def `draw()`

Draws the constructed grid. This method accounts for all of the grid's symbols, backgrounds, and cursors, and draws them to a window.

Arguments: None
Returns: None

#### def `draw_text(x, y, text)`

Draws the given text, starting at the given tile.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 
 text | String | The text to draw. The only valid characters are: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&*()-+=[];:'"`/\?<>,.`|

Returns: None

#### def `get_events()`

Returns (and clears) the list of unread PyGame events (key presses, gamepad button presses, etc.). This list needs to be supplied to other event analisys methods and should be called before doing those.

Arguments: None
Returns: None

#### def `get_tile_background(x, y)`

Returns the background of the given tile in the grid.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 

Returns:

 Type | Description 
---|---
 int | The ID of the background resource of the given tile. 

#### def `get_tile_cursor(x, y)`

Returns the cursor of the given tile in the grid.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 

Returns:

Type | Description 
---|---
 int | The ID of the cursor resource of the given tile. 

#### def `get_tile_symbol(x, y)`

Returns the symbol of the given tile in the grid.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 

Returns:

Type | Description 
---|---
 int | The ID of the symbol resource of the given tile. 

#### def `init(num_tiles_x=1, num_tiles_y=1, tile_size=1, title=GameStorm, debug_mode=DEBUG_MODE.NONE)`

Initialize the GameStorm system. This must be called before any other GameStorm methods.

Arguments:

 Name | Type | Description 
---|---|---
 num_tiles_x | int (>= 1) | The desired width, in tiles, of the grid. Defaults to 15 if not supplied. 
 num_tiles_y | int (>= 1) | The desired height, in tiles, of the grid. Defaults to 10 if not supplied. 
 tile_size | TileSize | The desired size of each tile. Each tile is square, so this value is applied to both the width and height of the tile. This value can be one of `TileSize.SMALL`, `TileSize.MEDIUM`, or `TileSize.LARGE`. Defaults to `TileSize.MEDIUM` if not supplied. 
 title | String | The desired title of the game window. 
 debug_mode | DebugMode | Whether to draw the debugging visuals. These are a pink grid - at the border of each row/column - and number markings for each row and column header. The possible values are `DEBUG_MODE.NONE`, `DEBUG_MODE.SIMPLE` (grid only), and `DEBUG_MODE.GRID_AND_COORDS`.

Returns: None

#### def `is_1_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the '1' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the '1' button has been pressed. 

#### def `is_2_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the '2' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the '2' button has been pressed. 

#### def `is_3_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the '3' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the '3' button has been pressed. 

#### def `is_4_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the '4' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the '4' button has been pressed. 

#### def `is_5_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the '5' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the '5' button has been pressed. 

#### def `is_6_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the '6' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the '6' button has been pressed. 

#### def `is_down_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the 'down' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the 'down' button has been pressed. 

#### def `is_exit_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the 'exit' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the 'exit' button has been pressed. 

#### def `is_left_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the 'left' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the 'left' button has been pressed. 

#### def `is_right_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the 'right' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the 'right' button has been pressed. 

#### def `is_select_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the 'select' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the 'select' button has been pressed. 

#### def `is_start_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the 'start' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the 'start' button has been pressed. 

#### def `is_up_button_pressed(events)`

Returns true if a key-down event or gamepad button down event for the 'up' button exists in the given events list.

Arguments:

 Name | Type | Description 
---|---|---
 events | EventList | List of pygame events. 

Returns:

 Type | Description 
---|---
 Boolean | True if the 'up' button has been pressed. 

#### def `pause_all_sound()`

Pauses playback of all currently playing music and SoundFX resources. Unlike 'stop', this playback can be resumed.

Arguments: None
Returns: None

#### def `pause_current_music()`

Pauses the currently playing music. Unlike 'stop', this music can be resumed.

Arguments: None
Returns: None

#### def `play_music(music)`

Starts a music resource playing.

Arguments:

 Name | Type | Description 
---|---|---
 music | int (>= 1) | The ID of the music resource to be played. 

Returns: None

#### def `play_soundfx(soundfx)`

Plays a SoundFX resource.

Arguments:

 Name | Type | Description 
---|---|---
 soundfx | int (>= 1) | The ID of the SoundFX resource to be played. 

Returns: None

#### def `quit()`

Gracefully stop the GameStorm system.

Arguments: None
Returns: None

#### def `resume_all_sound()`

Resumes playback of all currently paused music and SoundFX resources.

Arguments: None
Returns: None

#### def `resume_current_music()`

Resumes playback of the currently paused music.

Arguments: None
Returns: None

#### def `set_all_tiles_background(background)`

Sets the background of all the tiles in the grid.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 
 background | int (>= 1) | The ID of the background resource to set for the given tile. 

Returns: None

#### def `set_tile_background(x, y, background)`

Sets the background of the given tile in the grid.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 
 background | int (>= 1) | The ID of the background resource to set for the given tile. 

Returns: None

#### def `set_tile_cursor(x, y, cursor)`

Sets the cursor of the given tile in the grid.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 
 cursor | int (>= 1) | The ID of the cursor resource to set for the given tile. 

Returns: None

#### def `set_tile_symbol(x, y, symbol, direction=1)`

Sets the symbol of the given tile in the grid. It can be oriented in one of the for orientations.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 1) | The x coordinate of the tile in the grid. 
 y | int (>= 1) | The y coordinate of the tile in the grid. 
 symbol | int (>= 1) | The ID of the symbol resource to set for the given tile. 
 direction | Direction | The desired orientation of the symbol. Can be `Direction.UP`, `Direction.DOWN`, `Direction.LEFT`, `Direction.RIGHT`. Defaults to `Direction.UP`

Returns: None

#### def `stop_all_sound()`

Stops playback of all currently playing music and SoundFX resources.

Arguments: None
Returns: None

#### def `stop_all_soundfx()`

Stops playback of all currently playing SoundFX.

Arguments: None
Returns: None

#### def `stop_current_music()`

Stops the currently playing music.

Arguments: None
Returns: None

#### def `stop_soundfx(soundfx)`

Stops playback of the given SoundFX resource.

Arguments:

 Name | Type | Description 
---|---|---
 soundfx | int (>= 1) | The ID of the SoundFX resource to be stopped. 

Returns: None


SymbolGroup
============

Classes
----------

### class `SymbolGroup()`

This represents a collection of symbols. It is useful for when you want to define a shape of symbols once and use it multiple times. It is meant to be used with `GameStorm.draw_symbol_group()`.

Methods:

#### def `clear_symbol(x, y)`

Clears (sets to None) a symbol at the given position.

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 0) |The x coordinate of the SymbolGroup's tile whose symbol should be cleared.
 y | int (>= 0) |The y coordinate of the SymbolGroup's tile whose symbol should be cleared.

#### def `get_grid()`

Returns the grid that makes up this SymbolGroup.

#### def `set_all_symbols(symbol)`

Sets a symbol to all positions in this SymbolGroup

Arguments:

 Name | Type | Description 
---|---|---
 symbol | int (>= 0) |The number ID of the symbol you want to set.

#### def `set_symbol(x, y, symbol)`

Set a symbol at the given position in this SymbolGroup

Arguments:

 Name | Type | Description 
---|---|---
 x | int (>= 0) |The x coordinate of the SymbolGroup's tile to which you want to set a symbol.
 y | int (>= 0) |The y coordinate of the SymbolGroup's tile to which you want to set a symbol.
 symbol | int (>= 0) |The number ID of the symbol you want to set.

