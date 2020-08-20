import sys
import os

# ugly trick to find this module
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# this code will execute on running
import procedural_pixel_art

grid = procedural_pixel_art.generate_random_grid()
grid = procedural_pixel_art.do_step(grid)
grid = procedural_pixel_art.do_step(grid)
grid = procedural_pixel_art.make_mirror(grid)
grid = procedural_pixel_art.make_border(grid)
procedural_pixel_art.save_grid(grid)
