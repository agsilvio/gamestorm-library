import gamestorm

num_tiles_x = 15
num_tiles_y = 7
screen_width = 1280
screen_height = 720

#these two lines are required
g = gamestorm.GameStorm()
g.init(num_tiles_x, num_tiles_y, screen_width, screen_height, title = 'Hello World')

#set up some stuff to draw soon!
g.set_all_tiles_background(25)

g.set_tile_symbol(6,4,196)
g.set_tile_symbol(7,4,196)
g.set_tile_symbol(8,4,196)
g.set_tile_cursor(7,4,1)

g.draw_text(2,1, 'Hello World!')

#perform the draw
g.draw()

#check for the exit event to quit
while True:
    events = g.get_events()
    if g.is_exit_button_pressed(events):
        g.quit()
        break

