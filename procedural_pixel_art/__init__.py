import array
from datetime import datetime
from random import choice
from itertools import product

WIDTH = 5
HEIGHT = 10
X = -1

MOORE = [
    (dx, dy)
    for dx, dy in product([-1, 0, 1], repeat=2)
    if (dx, dy) != (0, 0)
]

NEUMANN = [
    (-1,  0),
    ( 1,  0),
    ( 0,  1),
    ( 0, -1),
]


def generate_x_row():
    return [[X] * WIDTH]


def generate_random_row():
    return [X] + [choice([0, 1]) for _ in range(WIDTH - 1)]


def generate_random_grid(generate_row=generate_random_row):
    rows = [generate_row() for _ in range(HEIGHT - 2)]
    return generate_x_row() + rows + generate_x_row()


def do_step(grid):
    return [
        [
            change_cell_for_do_step(x, y, grid)
            for x in range(WIDTH)
        ]
        for y in range(HEIGHT)
    ]


def change_cell_for_do_step(x, y, grid):
    cell = get_cell_from_grid(x, y, grid)
    if cell == X:
        return X

    alive_neighbors = sum(
        get_cell_from_grid(x + dx, y + dy, grid) == 1
        for dx, dy in MOORE
    )

    if cell == 1 and alive_neighbors in (2, 3):
        return 1
    elif cell == 0 and alive_neighbors in (0, 1):
        return 1
    else:
        return 0


def get_cell_from_grid(x, y, grid):
    #if x < 0 or x >= WIDTH:
    if x < 0 or x >= len(grid[0]):
        return 0
    #if y < 0 or y >= HEIGHT:
    if y < 0 or y >= len(grid):
        return 0
    return grid[y][x]


def make_mirror(grid):
    return [mirror_row(row) for row in grid]


def mirror_row(row):
    left_row = row
    right_row = row[::-1]  # magic python here
    return left_row + right_row


def make_border(grid):
    return [
        [
            make_border_for_cell(cell, x, y, grid)
            for x, cell in enumerate(row)
        ]
        for y, row in enumerate(grid)
    ]


def make_border_for_cell(cell, x, y, grid):
    if cell == 1:
        return 1

    any_neighbor_is_alive = any(
        get_cell_from_grid(x + dx, y + dy, grid) == 1
        for dx, dy in NEUMANN
    )

    return 2 if any_neighbor_is_alive else 0


def grid_to_array(grid):
    """
    Used in save_grid function

    """
    for row in grid:
        for cell in row:
            if cell == 1:
                yield from [255, 0, 0]  # red color
            elif cell == 2:
                yield from [255, 255, 0]  # yellow color
            else:
                yield from [0, 0, 0]  # black color


def save_grid(grid):
    """
    Save grid to a file.

    """
    # PPM header
    width = len(grid[0])
    height = len(grid)
    maxval = 255
    ppm_header = f"P6 {width} {height} {maxval}\n"
    # PPM image data (filled with blue)

    # generate flat data from grid to image

    image = array.array("B", grid_to_array(grid))
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    with open(f"generated_pixel_art_{timestamp}.ppm", "wb") as fp:
        fp.write(bytearray(ppm_header, "ascii"))
        image.tofile(fp)


if __name__ == "__main__":
    # this code will execute on running
    grid = generate_random_grid()
    save_grid(grid)
