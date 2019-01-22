from .constants import *
from .tile import *
from .symbol_group import *
import pkg_resources
import sys, os.path

import pygame

class GameStorm:

    #private methods
    def _validate_text(self, text):
        validation_string = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&*()-+=[];:\'"`/\\?<>,.'
        for char in text:
            if char not in validation_string:
                return False
        return True

    def _rotate_symbol_group(self, symbol_group, direction):
       if not isinstance(symbol_group, SymbolGroup):
           raise TypeError('"symbol_group" must be an instance of SymbolGroup')
       if not isinstance(direction, Direction):
           raise TypeError('"direction" must be an instance of Direction')

       grid = symbol_group.get_grid()

       if direction is Direction.UP:
           return grid
       elif direction is Direction.LEFT:
           return self._rotate_clockwise_by_degree(grid, 270)
       elif direction is Direction.RIGHT:
           return self._rotate_clockwise_by_degree(grid, 90)
       elif direction is Direction.DOWN:
           return self._rotate_clockwise_by_degree(grid, 180)

       return rotated_grid
       
    def _rotate_clockwise_by_degree(self, grid, degree=90):
       if degree not in [0, 90, 180, 270, 360]:
           raise ValueError('"degree" must be 90, 180, or 270')
       return grid if not degree else self._rotate_clockwise_by_degree(list(zip(*grid[::-1])), degree-90)

    def _raise_exception_if_not_initialized(self):
        if not hasattr(self, 'initialized') or not self.initialized:
            raise RuntimeError("This GameStorm instance is not yet initialized.")

    def _check_keyup_event_in_events(self, key, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return True
        return False

    def _check_joybutton_event_in_events(self, button, events):
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == button.value:
                    return True
        return False

    def _check_joyaxis_event_in_events(self, direction, events):
        if not self._gamepad_is_present():
            return False

        axis = None
        value = None

        if (direction == Direction.UP):
            axis = 1
            value = -1
            pass
        elif (direction == Direction.DOWN):
            axis = 1
            value = 1
            pass
        elif (direction == Direction.LEFT):
            axis = 0
            value = -1
            pass
        elif (direction == Direction.RIGHT):
            axis = 0
            value = 1
            pass

        for event in events:
            if event.type == pygame.JOYAXISMOTION:
                if direction is Direction.UP or direction is Direction.LEFT:
                    if event.axis is axis and event.value <= value:
                        return True
                elif direction is Direction.DOWN or direction is Direction.RIGHT:
                    if event.axis is axis and event.value >= value:
                        return True
        return False

    def _perform_clear_operation_on_all_tiles(self, clear_operation):
        if not isinstance(clear_operation, ClearOperation):
            raise TypeError('"clear_operation" must be an instance of ClearOperation enum.')

        grid = self.grid
        for x in range(self.num_tiles_x):
            for y in range(self.num_tiles_y):
                tile = grid[x][y]
                if clear_operation is ClearOperation.SYMBOL:
                    tile.clear_symbol()
                elif clear_operation is ClearOperation.BACKGROUND:
                    tile.clear_background()
                elif clear_operation is ClearOperation.CURSOR:
                    tile.clear_cursor()
                elif clear_operation is ClearOperation.ALL:
                    tile.clear_everything()

    def _gamepad_is_present(self):
        return hasattr(self, 'gamepad') and self.gamepad is not None

    def _get_tile_at_x_y(self, x, y):
        return self.grid[x][y]

    def _get_path_to_resource(self, index, resource_type):
        if not isinstance(resource_type, ResourceType):
            raise TypeError('"resource_type" must be an instance of ResourceType enum.')

        folder_name = ''
        extension = ''
        if resource_type is ResourceType.BACKGROUND:
            folder_name = 'background'
            extension = 'png'
        elif resource_type is ResourceType.SYMBOL:
            folder_name = 'symbol'
            extension = 'png'
        elif resource_type is ResourceType.CURSOR:
            folder_name = 'cursor'
            extension = 'png'
        elif resource_type is ResourceType.MUSIC:
            folder_name = 'music'
            extension = 'ogg'
        elif resource_type is ResourceType.SOUNDFX:
            folder_name = 'soundfx'
            extension = 'ogg'

        resources_path = 'resources/' + folder_name + '/' + str(index) + '.' + extension

        #check for resource override
        path_of_launching_script = sys.path[0]
        potential_resource_override = os.path.join(path_of_launching_script, resources_path) 
        if os.path.isfile(potential_resource_override):
            return potential_resource_override
        else:
            return pkg_resources.resource_filename("gamestorm", resources_path)

    #public methods
    def clear_tile_background(self, x, y):
        '''
        Clears (sets to None) the background of the given tile in the grid.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |

        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        tile = self._get_tile_at_x_y(x, y)
        tile.clear_background()
    
    def clear_tile_symbol(self, x, y):
        '''
        Clears (sets to None) the symbol of the given tile in the grid.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |

        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        tile = self._get_tile_at_x_y(x, y)
        tile.clear_symbol()

    def clear_tile_cursor(self, x, y):
        '''
        Clears (sets to None) the cursor of the given tile in the grid.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |

        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        tile = self._get_tile_at_x_y(x, y)
        tile.clear_cursor()
    
    def clear_tile_everything(self, x, y):
        '''
        Clears (sets to None) the background, symbol, and cursor of the given tile in the grid.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |

        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        tile = self._get_tile_at_x_y(x, y)
        tile.clear_everything()
    
    def get_tile_background(self, x, y):
        '''
        Returns the background of the given tile in the grid.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |

        Returns:  
        | Type | Description |
        |---|---|
        | int | The ID of the background resource of the given tile. |
        '''
        self._raise_exception_if_not_initialized()
        tile = self._get_tile_at_x_y(x, y)
        return tile.get_background()
    
    def get_tile_symbol(self, x, y):
        '''
        Returns the symbol of the given tile in the grid.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |

        Returns:  
        | int | The ID of the symbol resource of the given tile. |
        '''
        self._raise_exception_if_not_initialized()
        tile = self._get_tile_at_x_y(x, y)
        return tile.get_symbol()
    
    def get_tile_cursor(self, x, y):
        '''
        Returns the cursor of the given tile in the grid.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |

        Returns:  
        | int | The ID of the cursor resource of the given tile. |
        '''
        self._raise_exception_if_not_initialized()
        tile = self._get_tile_at_x_y(x, y)
        return tile.get_cursor()

    def set_tile_cursor(self, x, y, cursor):
        '''
        Sets the cursor of the given tile in the grid.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |
        | cursor | int (>= 1) | The ID of the cursor resource to set for the given tile. |

        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        tile = self._get_tile_at_x_y(x, y)
        tile.set_cursor(cursor)

    def set_tile_background(self, x, y, background):
        '''
        Sets the background of the given tile in the grid.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |
        | background | int (>= 1) | The ID of the background resource to set for the given tile. |

        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        tile = self._get_tile_at_x_y(x, y)
        tile.set_background(background)

    def set_tile_symbol(self, x, y, symbol, direction = DEFAULT_DIRECTION):
        '''
        Sets the symbol of the given tile in the grid. It can be oriented in one of the for orientations.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |
        | symbol | int (>= 1) | The ID of the symbol resource to set for the given tile. |
        | direction | Direction | The desired orientation of the symbol. Can be `Direction.UP`, `Direction.DOWN`, `Direction.LEFT`, `Direction.RIGHT`. Defaults to `Direction.UP`|

        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        tile = self._get_tile_at_x_y(x, y)
        tile.set_symbol(symbol, direction)
    
    def set_all_tiles_background(self, background):
        '''
        Sets the background of all the tiles in the grid.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |
        | background | int (>= 1) | The ID of the background resource to set for the given tile. |

        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        grid = self.grid
        for x in range(self.num_tiles_x):
            for y in range(self.num_tiles_y):
                tile = grid[x][y]
                tile.set_background(background)

    def clear_all_tiles_everything(self):
        '''
        Clears the background, symbol, and cursor of all the tiles in the grid.

        Arguments: None  
        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        self._perform_clear_operation_on_all_tiles(ClearOperation.ALL)

    def clear_all_tiles_symbol(self):
        '''
        Clears the symbol of all the tiles in the grid.

        Arguments: None  
        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        self._perform_clear_operation_on_all_tiles(ClearOperation.SYMBOL)

    def clear_all_tiles_background(self):
        '''
        Clears the background of all the tiles in the grid.

        Arguments: None  
        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        self._perform_clear_operation_on_all_tiles(ClearOperation.BACKGROUND)
    
    def clear_all_tiles_cursor(self):
        '''
        Clears the cursor of all the tiles in the grid.

        Arguments: None  
        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        self._perform_clear_operation_on_all_tiles(ClearOperation.CURSOR)


    def get_events(self):
        '''
        Returns (and clears) the list of unread PyGame events (key presses, gamepad button presses, etc.). This list needs to be supplied to other event analisys methods and should be called before doing those.

        Arguments: None  
        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        return pygame.event.get()

    def is_left_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the 'left' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the 'left' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        left_joystick_pressed = self._check_joyaxis_event_in_events(Direction.LEFT, events)
        left_key_pressed = self._check_keyup_event_in_events(pygame.K_LEFT, events)
        return left_key_pressed or left_joystick_pressed

    def is_right_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the 'right' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the 'right' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        right_joystick_pressed = self._check_joyaxis_event_in_events(Direction.RIGHT, events)
        right_key_pressed = self._check_keyup_event_in_events(pygame.K_RIGHT, events)
        return right_key_pressed or right_joystick_pressed

    def is_up_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the 'up' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the 'up' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        up_joystick_pressed = self._check_joyaxis_event_in_events(Direction.UP, events)
        up_key_pressed = self._check_keyup_event_in_events(pygame.K_UP, events)
        return up_key_pressed or up_joystick_pressed

    def is_down_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the 'down' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the 'down' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        down_joystick_pressed = self._check_joyaxis_event_in_events(Direction.DOWN, events)
        down_key_pressed = self._check_keyup_event_in_events(pygame.K_DOWN, events)
        return down_key_pressed or down_joystick_pressed

    def is_start_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the 'start' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the 'start' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        start_joystick_pressed = self._check_joybutton_event_in_events(GamepadButton.START, events)
        start_key_pressed = self._check_keyup_event_in_events(pygame.K_RETURN, events)
        return start_key_pressed or start_joystick_pressed

    def is_select_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the 'select' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the 'select' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        select_joystick_pressed = self._check_joybutton_event_in_events(GamepadButton.SELECT, events)
        select_key_pressed = self._check_keyup_event_in_events(pygame.K_TAB, events)
        return select_key_pressed or select_joystick_pressed

    def is_1_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the '1' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the '1' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        b1_joystick_pressed = self._check_joybutton_event_in_events(GamepadButton.B1, events)
        b1_key_pressed = self._check_keyup_event_in_events(pygame.K_1, events)
        return b1_key_pressed or b1_joystick_pressed

    def is_2_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the '2' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the '2' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        b2_joystick_pressed = self._check_joybutton_event_in_events(GamepadButton.B2, events)
        b2_key_pressed = self._check_keyup_event_in_events(pygame.K_2, events)
        return b2_key_pressed or b2_joystick_pressed

    def is_3_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the '3' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the '3' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        b3_joystick_pressed = self._check_joybutton_event_in_events(GamepadButton.B3, events)
        b3_key_pressed = self._check_keyup_event_in_events(pygame.K_3, events)
        return b3_key_pressed or b3_joystick_pressed

    def is_4_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the '4' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the '4' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        b4_joystick_pressed = self._check_joybutton_event_in_events(GamepadButton.B4, events)
        b4_key_pressed = self._check_keyup_event_in_events(pygame.K_4, events)
        return b4_key_pressed or b4_joystick_pressed

    def is_5_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the '5' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the '5' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        b5_joystick_pressed = self._check_joybutton_event_in_events(GamepadButton.B5, events)
        b5_key_pressed = self._check_keyup_event_in_events(pygame.K_5, events)
        return b5_key_pressed or b5_joystick_pressed

    def is_6_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the '6' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the '6' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        b6_joystick_pressed = self._check_joybutton_event_in_events(GamepadButton.B6, events)
        b6_key_pressed = self._check_keyup_event_in_events(pygame.K_6, events)
        return b6_key_pressed or b6_joystick_pressed

    def is_exit_button_pressed(self, events):
        '''
        Returns true if a key-down event or gamepad button down event for the 'exit' button exists in the given events list.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | events | EventList | List of pygame events. |

        Returns:  
        | Type | Description |
        |---|---|
        | Boolean | True if the 'exit' button has been pressed. |
        '''
        self._raise_exception_if_not_initialized()
        for event in events:
            if event.type == pygame.QUIT:
                return True
        return self._check_keyup_event_in_events(pygame.K_ESCAPE, events)

    def play_music(self, music):
        '''
        Starts a music resource playing.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | music | int (>= 1) | The ID of the music resource to be played. |

        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        if not isinstance(music, int) or music <= 0:
            raise TypeError('"music" must be a positive integer.')

        path = self._get_path_to_resource(music, ResourceType.MUSIC)
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)

    def stop_current_music(self):
        '''
        Stops the currently playing music.

        Arguments: None  
        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        pygame.mixer.music.stop()

    def pause_current_music(self):
        '''
        Pauses the currently playing music. Unlike 'stop', this music can be resumed.

        Arguments: None  
        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        pygame.mixer.music.pause()

    def resume_current_music(self):
        '''
        Resumes playback of the currently paused music.

        Arguments: None
        Returns: None
        '''
        self._raise_exception_if_not_initialized()
        pygame.mixer.music.unpause()

    def play_soundfx(self, soundfx):
        '''
        Plays a SoundFX resource.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | soundfx | int (>= 1) | The ID of the SoundFX resource to be played. |

        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        if not isinstance(soundfx, int) or soundfx <= 0:
            raise TypeError('"soundfx" must be a positive integer.')

        sound_library = self.sound_library
        sound = sound_library.get(soundfx)
        if sound == None:
            path = self._get_path_to_resource(soundfx, ResourceType.SOUNDFX)
            sound = pygame.mixer.Sound(path)
            sound_library[soundfx] = sound
        sound.play()

    def stop_soundfx(self, soundfx):
        '''
        Stops playback of the given SoundFX resource.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | soundfx | int (>= 1) | The ID of the SoundFX resource to be stopped. |

        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        if not isinstance(soundfx, int) or soundfx <= 0:
            raise TypeError('"soundfx" must be a positive integer.')

        sound = self.sound_library.get(soundfx)
        if not sound:
            return
        sound.stop()

    def stop_all_soundfx(self):
        '''
        Stops playback of all currently playing SoundFX.

        Arguments: None  
        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        for (soundfx, sound) in self.sound_library.items():
            sound.stop()

    def pause_all_sound(self):
        '''
        Pauses playback of all currently playing music and SoundFX resources. Unlike 'stop', this playback can be resumed.

        Arguments: None  
        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        pygame.mixer.pause()
        pygame.mixer.music.pause()

    def resume_all_sound(self):
        '''
        Resumes playback of all currently paused music and SoundFX resources.

        Arguments: None  
        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        pygame.mixer.unpause()
        pygame.mixer.music.unpause()

    def stop_all_sound(self):
        '''
        Stops playback of all currently playing music and SoundFX resources.

        Arguments: None  
        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        pygame.mixer.stop()
        pygame.mixer.music.stop()


    def draw_text(self, x, y, text):
        '''
        Draws the given text, starting at the given tile.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |
        | text | String | The text to draw. The only valid characters are: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&*()-+=[];:\'"`/\\?<>,.`|

        Returns: None  
        '''
        self._raise_exception_if_not_initialized()

        if not self._validate_text(text):
            raise ValueError("The given text is not valid. See documentation for `draw_text()`")

        local_x = x
        num_tiles_x = self.num_tiles_x
        num_tiles_y = self.num_tiles_y
        for char in text:
            if local_x < 0 or local_x >= num_tiles_x:
                continue
            if y < 0 or y >= num_tiles_y:
                continue

            char_filename = char_to_filename[char]
            self.set_tile_symbol(local_x, y, char_filename)
            local_x += 1

    def quit(self):
        '''
        Gracefully stop the GameStorm system.

        Arguments: None  
        Returns: None  
        '''
        pygame.quit()

    def init(self, num_tiles_x = DEFAULT_TILES_X, num_tiles_y = DEFAULT_TILES_Y, tile_size = DEFAULT_TILE_SIZE, title = 'GameStorm', debug_mode = DebugMode.NONE):
        '''
        Initialize the GameStorm system. This must be called before any other GameStorm methods.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | num_tiles_x | int (>= 1) | The desired width, in tiles, of the grid. Defaults to 15 if not supplied. |
        | num_tiles_y | int (>= 1) | The desired height, in tiles, of the grid. Defaults to 10 if not supplied. |
        | tile_size | TileSize | The desired size of each tile. Each tile is square, so this value is applied to both the width and height of the tile. This value can be one of `TileSize.SMALL`, `TileSize.MEDIUM`, or `TileSize.LARGE`. Defaults to `TileSize.MEDIUM` if not supplied. |
        | title | String | The desired title of the game window. |
        | debug_mode | DebugMode | Whether to draw the debugging visuals. These are a pink grid - at the border of each row/column - and number markings for each row and column header. The possible values are `DebugMode.NONE`, `DebugMode.GRID` (grid only), and `DebugMode.GRID_AND_COORDS`.|

        Returns: None  
        '''
        if hasattr(self, 'initialized') and self.initialized:
            raise RuntimeError("GameStorm has already been initialized.")

        #validate num_tiles_x
        if not isinstance(num_tiles_x, int):
            raise TypeError('"num_tiles_x" must be an instance of int.')
        if num_tiles_x < 1:
            raise ValueError('The value of "num_tiles_x" must be at least 1.')

        #validate num_tiles_y
        if not isinstance(num_tiles_y, int):
            raise TypeError('"num_tiles_y" must be an instance of int.')
        if num_tiles_y < 1:
            raise ValueError('The value of "num_tiles_y" must be at least 1.')

        #validate tile_size
        if not isinstance(tile_size, TileSize):
            raise TypeError('"tile_size" must be an instance of TileSize Enum.')

        #validate debug
        if not isinstance(debug_mode, DebugMode):
            raise TypeError('"debug_mode" must be an instance of DebugMode.')


    
        self.initialized = False
        self.num_tiles_x = DEFAULT_TILES_X
        self.num_tiles_y = DEFAULT_TILES_Y
        self.tile_size = DEFAULT_TILE_SIZE

        self.grid = []

        self.window_created = False
        self.window = None

        self.sound_library = {}

        self.num_tiles_x = num_tiles_x
        self.num_tiles_y = num_tiles_y
        self.tile_size = tile_size
        self.debug_mode = debug_mode
        self.title = title


        pygame.init()
        #init of font must come before usage
        pygame.font.init()
        self.debug_font = pygame.font.SysFont('Arial', DEBUG_TEXT_SIZE)

        pygame.mixer.init()
        pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.gamepad = pygame.joystick.Joystick(0)
            self.gamepad.init()

        #set up internal grid
        for x in range(self.num_tiles_x):
            self.grid.append([])
            for y in range(self.num_tiles_y):
                self.grid[x].append(Tile())

        self.initialized = True

    def draw(self):
        '''
        Draws the constructed grid. This method accounts for all of the grid's symbols, backgrounds, and cursors, and draws them to a window.

        Arguments: None  
        Returns: None  
        '''
        self._raise_exception_if_not_initialized()
        int_tile_size = self.tile_size.value

        if not self.window_created:
            pixel_width = int_tile_size * self.num_tiles_x
            pixel_height = int_tile_size * self.num_tiles_y
            size = pixel_width, pixel_height
            self.window = pygame.display.set_mode(size)
            self.window_created = True

        
        window = self.window
        tile_rect = (int_tile_size, int_tile_size)
        grid = self.grid
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                pixel_x_pos = int_tile_size * x
                pixel_y_pos = int_tile_size * y
                tile = grid[x][y]
                background = tile.get_background()
                symbol = tile.get_symbol()
                symbol_direction = tile.get_symbol_direction()
                cursor = tile.get_cursor()
                if background:
                    bg_to_use = background
                else:
                    bg_to_use = EMPTY_BACKGROUND
                path = self._get_path_to_resource(bg_to_use, ResourceType.BACKGROUND)
                bg_img = pygame.image.load(path)
                bg_img = pygame.transform.scale(bg_img, tile_rect)
                bg_img_rect = bg_img.get_rect()
                self.window.blit(bg_img,(pixel_x_pos, pixel_y_pos), bg_img_rect)

                if symbol:
                    path = self._get_path_to_resource(symbol, ResourceType.SYMBOL)
                    symbol_img = pygame.image.load(path)
                    symbol_img = pygame.transform.scale(symbol_img, tile_rect)
                    if symbol_direction is not Direction.UP:
                        if symbol_direction is Direction.LEFT:
                            rotation_degrees = 270
                        elif symbol_direction is Direction.RIGHT:
                            rotation_degrees = 90
                        elif symbol_direction is Direction.DOWN:
                            rotation_degrees = 180
                        symbol_img = pygame.transform.rotate(symbol_img, rotation_degrees)
                    symbol_img_rect = symbol_img.get_rect()
                    window.blit(symbol_img,(pixel_x_pos, pixel_y_pos), symbol_img_rect)
                if cursor:
                    path = self._get_path_to_resource(cursor, ResourceType.CURSOR)
                    cursor_img = pygame.image.load(path)
                    cursor_img = pygame.transform.scale(cursor_img, tile_rect)
                    cursor_img_rect = cursor_img.get_rect()
                    window.blit(cursor_img,(pixel_x_pos, pixel_y_pos), cursor_img_rect)

        if not self.debug_mode == DebugMode.NONE:
            debug_colour = (255,0,200)
            num_tiles_x = self.num_tiles_x
            num_tiles_y = self.num_tiles_y
            window_width = num_tiles_x * int_tile_size
            window_height = num_tiles_y * int_tile_size
            for x in range(num_tiles_x):
                if not x:
                    continue
                start_pos = (x * int_tile_size, 0)
                end_pos = (x * int_tile_size, window_height) 
                pygame.draw.line(window, debug_colour, start_pos, end_pos, 1)

            for y in range(num_tiles_y):
                if not y:
                    continue
                start_pos = (0, y * int_tile_size)
                end_pos = (window_width, y * int_tile_size) 
                pygame.draw.line(window, debug_colour, start_pos, end_pos, 1)

            if self.debug_mode is DebugMode.GRID_AND_COORDS:
                for x in range(num_tiles_x):
                    for y in range(num_tiles_y):
                        line1 = self.debug_font.render('x ' + str(x), False, debug_colour)
                        line2 = self.debug_font.render('y ' + str(y), False, debug_colour)
                        x_pos_1 = x * int_tile_size + DEBUG_TEXT_OFFSET
                        y_pos_1 = y * int_tile_size + DEBUG_TEXT_OFFSET
                        x_pos_2 = x * int_tile_size + DEBUG_TEXT_OFFSET
                        y_pos_2 = y * int_tile_size + DEBUG_TEXT_OFFSET + DEBUG_TEXT_SIZE
                        window.blit(line1,(x_pos_1, y_pos_1))
                        window.blit(line2,(x_pos_2, y_pos_2))

        pygame.display.set_caption(self.title)
        pygame.display.flip()

    def apply_symbol_group(self, x, y, symbol_group, direction = Direction.UP):
        '''
        Sets the given SymbolGroup's symbols to those of the tiles starting at the given coordinates. The orientation of the symbol can be given by supplying a value for direction.

        Arguments:  
        | Name | Type | Description |
        |---|---|---|
        | x | int (>= 1) | The x coordinate of the tile in the grid. |
        | y | int (>= 1) | The y coordinate of the tile in the grid. |
        | symbol_group | SymbolGroup | The SymbolGroup to draw. |
        | direction | Direction | The desired orientation of the SymbolGroup. Can be `Direction.UP`, `Direction.DOWN`, `Direction.LEFT`, `Direction.RIGHT`. Defaults to `Direction.UP`|

        Returns: None
        '''
        self._raise_exception_if_not_initialized()

        if not isinstance(x, int):
            raise TypeError('"x" must be positive integer.')
        if x < 0:
            raise ValueError('"x" must be positive integer.')
        if not isinstance(y, int):
            raise TypeError('"y" must be positive integer.')
        if y < 0:
            raise ValueError('"y" must be positive integer.')

        rotated_grid = self._rotate_symbol_group(symbol_group, direction)

        for x_pos in range(len(rotated_grid)):
            for y_pos in range(len(rotated_grid[0])):
                symbol = rotated_grid[x_pos][y_pos]
                if symbol:
                    actual_x_pos = x + x_pos
                    actual_y_pos = y + y_pos
                    self.set_tile_symbol(actual_x_pos, actual_y_pos, symbol)
