import unittest

from procedural_pixel_art import (
    generate_random_grid,
    save_grid,
    do_step,
    make_mirror,
    make_border,
    X,
)


def test__generate_random_grid():
    grid = generate_random_grid()

    assert len(grid) == 10
    assert len(grid[0]) == 5
    assert any(0 in row for row in grid)
    assert any(1 in row for row in grid)
    assert all(
        isinstance(val, int)
        for row in grid
        for val in row
    )
    assert _col(grid, 0) == [X] * 5
    assert _col(grid, 9) == [X] * 5
    assert _row(grid, 0) == [X] * 10


def test__do_step__still_alive_condition():
    grid = generate_random_grid(_empty_row)

    grid[3][3] = 1  # cell to be alive
    grid[3][4] = 1  # two alive neigbors
    grid[4][3] = 1

    new_grid = do_step(grid)

    # I'M STILL ALIVE
    # I'M STILL ALIVE
    assert new_grid[3][3] == 1 # AH AH AH STILL ALIIIVEEEE


def test__do_step__regeneration_condition():
    grid = generate_random_grid(_empty_row)

    grid[3][3] = 0  # dead cell
    grid[3][4] = 1  # one alive neighbor

    new_grid = do_step(grid)

    assert new_grid[3][3] == 1


def test__do_step__still_dead_condition():
    grid = generate_random_grid(_empty_row)

    grid[3][3] = 0  # dead cell
    grid[3][4] = 1  # two alive neigbors
    grid[4][3] = 1

    new_grid = do_step(grid)

    assert new_grid[3][3] == 0  # two neighbors, still dead


def test__mirror():
    grid = generate_random_grid(_empty_row)

    # row 2, one alive cell
    grid[2][3] = 1

    # row 3, two alive cells
    grid[3][2] = 1
    grid[3][3] = 1

    new_grid = make_mirror(grid)

    assert all(len(row) == 10 for row in new_grid)

    assert _col(new_grid, 0) == [X] * 10
    assert _col(new_grid, 1) == [X] + [0] * 8 + [X]
    assert _col(new_grid, 2) == [X, 0, 0, 1, 0, 0, 1, 0, 0, X]
    assert _col(new_grid, 3) == [X, 0, 1, 1, 0, 0, 1, 1, 0, X]


def test__make_border():
    grid = generate_random_grid(_empty_row)

    grid[3][3] = 1

    new_grid = make_border(grid)

    assert grid[3][3] == 1   # center

    assert new_grid[2][3] == 2
    assert new_grid[3][2] == 2
    assert new_grid[4][3] == 2
    assert new_grid[3][4] == 2


def _empty_row():
    return [X, 0, 0, 0, 0]


def _col(grid, x):
    return grid[x]


def _row(grid, x):
    return [r[x] for r in grid]
