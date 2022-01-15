from copy import deepcopy
from pprint import pprint
from sys import argv

filename = argv[1] if len(argv) > 1 else '11.in'
lines = [line.strip('\n') for line in open(filename).readlines()]


grid = []

for line in lines:
    grid.append([int(num) for num in line])


# Part 1
def increment(grid, start_row=0, start_col=0, end_row=None, end_col=None):
    # increment all elements in grid by 1
    # if end_row and end_col are given then increment from start_row, start_col to end_row, end_col
    if end_row is None:
        end_row = len(grid)
    if end_col is None:
        end_col = len(grid[0])

    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            # if row, col is within the grid
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                grid[row][col] += 1


def increment_adjacent(grid, row, col, flashed):
    # incremenet adjacent elements in grid by 1 including diagonals
    # only the ones near the given row, col
    # using the increment function
    increment(grid, row-1, col-1, row+1, col+1)
    # increment then flash
    flash(grid, flashed)


def flash(grid, flashed):
    # flash elements in the grid that are greater than 9
    # and add row, col to the flashed list
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 9 and (row, col) not in flashed:
                flashed.append((row, col))
                # incremenet all adjacent elements of row, col
                increment_adjacent(grid, row, col, flashed)


def clear_flashed(grid, flashed):
    # set all flashed elements in grid to 0
    # note: each item in flashed is a tuple (row, col)
    for row, col in flashed:
        grid[row][col] = 0


def part1():
    temp_grid = deepcopy(grid)

    # initialize total flashed to 0
    total_flashed = 0
    for i in range(100):
        flashed = []
        increment(temp_grid)
        flash(temp_grid, flashed)
        clear_flashed(temp_grid, flashed)
        # add length of flashed to total flashed
        total_flashed += len(flashed)

    print(total_flashed)


part1()
