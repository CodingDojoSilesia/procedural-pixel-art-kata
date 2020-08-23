import unittest

from procedural_pixel_art import (
    generate_random_grid,
    save_grid,
    generate_5x10_grid,
    make_top_border,
    make_bottom_border,
    make_left_border,
    is_cell_alive,
    check_status_and_neighbours,
    create_next_generation
)


def test__generate_random_grid():
    grid = generate_random_grid()
    assert len(grid) == 2
    assert len(grid[0]) == 2


def test__10x5_grid():
    grid = generate_5x10_grid()
    assert len(grid) == 10
    assert len(grid[0]) == 5


def test__top_grid_border():
    grid = generate_5x10_grid()
    grid = make_top_border(grid)
    assert grid[0] == ['X', 'X', 'X', 'X', 'X']
    assert len(grid) == 10


def test__bottom_grid_border():
    grid = generate_5x10_grid()
    bottom = len(grid) - 1
    grid = make_bottom_border(grid)
    assert grid[bottom] == ['X', 'X', 'X', 'X', 'X']
    assert len(grid) == 10


def test__left_grid_border():
    grid = generate_5x10_grid()
    grid = make_left_border(grid)
    for i in range(len(grid)):
        assert grid[i - 1][0] == 'X'


def test__is_cell_alive():
    assert is_cell_alive(counter=3, cell_status=1) == 1
    assert is_cell_alive(counter=4, cell_status=1) == 0
    assert is_cell_alive(counter=1, cell_status=0) == 1
    assert is_cell_alive(counter=2, cell_status=0) == 0


def test__check_cell_neighbourhood():
    grid_2_neighbours = [
        [1, 0, 0],
        [0, 1, 1],
        [0, 0, 0]
    ]
    output = check_status_and_neighbours(grid_2_neighbours, i=1, j=1)
    assert output['neighbours'] == 2


def test__check_border_neighbourhood():
    grid_2_neighbours = [
        ['X', 'X', 'X'],
        ['X', 1, 1],
        ['X', 0, 0]
    ]
    output = check_status_and_neighbours(grid_2_neighbours, i=1, j=1)
    assert output['neighbours'] == 1


def test__create_new_generation():
    input_grid = [
        ['X', 'X', 'X', 'X'],
        ['X', 1, 1, 0],
        ['X', 0, 1, 0],
        ['X', 0, 0, 1]
    ]
    output_grid = [
        ['X', 'X', 'X', 'X'],
        ['X', 1, 1, 0],
        ['X', 0, 1, 0],
        ['X', 1, 0, 0]
    ]
    assert create_next_generation(input_grid) == output_grid

