import sys
import os

# ugly trick to find this module
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# this code will execute on running
from procedural_pixel_art import (
    generate_random_grid,
    save_grid,
    generate_1_or_0,
    generate_5x10_grid,
    make_top_border,
    make_bottom_border,
    make_left_border,
    create_next_generation
)


# grid = generate_random_grid()
# save_grid(grid)


grid = generate_5x10_grid()
grid = make_top_border(grid)
grid = make_bottom_border(grid)
grid = make_left_border(grid)
# print(grid)
grid = create_next_generation(grid)
# print(grid)
grid = create_next_generation(grid)
# print(grid)
save_grid(grid)