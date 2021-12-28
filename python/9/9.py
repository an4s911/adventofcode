from os import curdir, posix_fadvise
from sys import argv
from pprint import pprint
from time import sleep

filename = argv[1] if len(argv) > 1 else "9.in"

def print_row(array, col=None):
    for i in range(len(array)):
        if i == col:
            print("_", end='')
        else:
            print(array[i], end='')
    print()

def is_lowpoint(row, col, array):
    curr_num = array[row][col]

    if row in range(0, len(array) - 1) and curr_num >= array[row + 1][col]:
        return False

    elif row in range(1, len(array)) and curr_num >= array[row - 1][col]:
        return False
    
    if col in range(0, len(array[row]) - 1) and curr_num >= array[row][col + 1]:
        return False
    
    elif col in range(1, len(array[row])) and curr_num >= array[row][col - 1]:
        return False

    return True

# filename = "/home/anas/megasync/programming/challenges/adventofcode/python/9/9.in"
heightmap = [
    list(map(int, line)) for line in
    [line.strip('\n') for line in open(filename).readlines()]
]

# Part 1
def part1():
    lowpoints = []

    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            curr_num = heightmap[row][col]
            if is_lowpoint(row, col, heightmap):
                lowpoints.append(curr_num)
    
    print(sum(lowpoints) + len(lowpoints))


part1()
