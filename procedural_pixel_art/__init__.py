import array
from datetime import datetime


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


if __name__ == "__main__":
    # this code will execute on running
    grid = generate_random_grid()
    save_grid(grid)
