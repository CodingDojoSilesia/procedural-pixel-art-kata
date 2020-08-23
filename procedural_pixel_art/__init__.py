import array
from datetime import datetime
import random
import copy

def generate_random_grid():
    return [
        [0, 1],
        [1, 0],
    ]


def grid_to_array(grid):
    """
    Used in save_grid function

    """
    for row in grid:
        for cell in row:
            if cell == 1:
                yield from [0, 0, 255]  # blue color
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


# Req 1

def generate_1_or_0():
    return random.randint(0, 1)


def generate_5x10_grid():
    grid = []
    subgrid = []
    for i in range(10):
        for j in range(5):
            subgrid.append(generate_1_or_0())
        grid.append(subgrid)
        subgrid = []
    return grid


def make_top_border(grid):
    for i in range(len(grid[0])):
        grid[0][i] = 'X'
    return grid


def make_bottom_border(grid):
    bottom = len(grid) - 1
    for i in range(len(grid[0])):
        grid[bottom][i] = 'X'
    return grid


def make_left_border(grid):
    for i in range(len(grid)):
        grid[i-1][0] = 'X'
    return grid


# Req 2

def is_cell_alive(counter, cell_status):
    if cell_status == 1:
        if counter in (2, 3):
            return 1
        else:
            return 0
    elif cell_status == 0:
        if counter <= 1:
            return 1
        else:
            return 0
    else:
        return 0


def check_status_and_neighbours(grid,i,j):
    counter = 0
    for row in range(-1,2):
        for column in range(-1,2):
            try:
                neighbour_status = grid[i+row][j+column]
            except IndexError:
                continue
            if neighbour_status == 1:
                if row == 0 and column == 0:
                    pass
                else:
                    counter += 1
    cell_status = grid[i][j]
    return {'status': cell_status, 'neighbours': counter}


def create_next_generation(grid):
    new_grid = copy.copy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                continue
            status_and_neighbours = check_status_and_neighbours(grid, i, j)
            new_grid[i][j] = is_cell_alive(
                status_and_neighbours['neighbours'],
                status_and_neighbours['status']
            )
    return new_grid


if __name__ == "__main__":
    # this code will execute on running
    grid = generate_random_grid()
    save_grid(grid)
