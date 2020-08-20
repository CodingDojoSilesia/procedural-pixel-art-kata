import sys
import os

# ugly trick to find this module
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# this code will execute on running
from procedural_pixel_art import generate_random_grid, save_grid

grid = generate_random_grid()
save_grid(grid)
