import unittest

from procedural_pixel_art import (
    generate_random_grid,
    save_grid,
)


def test__generate_random_grid():
    grid = generate_random_grid()
    assert len(grid) == 10
    assert len(grid[0]) == 5

