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

# Part 2
def count_flowing_into(row, col, array, checked=[]):
    curr_num = array[row][col]

    if curr_num == 9:
        return 0
    if (row, col) in checked:
        return 0
    checked.append((row, col))

    count = 1

    # if row in range(0, len(array) - 1) and curr_num == array[row + 1][col] - 1:
    if row in range(0, len(array) - 1):
        count += count_flowing_into(row + 1, col, array, checked)

    # if row in range(1, len(array)) and curr_num == array[row - 1][col] - 1:
    if row in range(1, len(array)):
        count += count_flowing_into(row - 1, col, array, checked)
    
    # if col in range(0, len(array[row]) - 1) and curr_num == array[row][col + 1] - 1:
    if col in range(0, len(array[row]) - 1):
        count += count_flowing_into(row, col + 1, array, checked)
    
    # if col in range(1, len(array[row])) and curr_num == array[row][col - 1] - 1:
    if col in range(1, len(array[row])):
        count += count_flowing_into(row, col - 1, array, checked)

    return count

def part2():
    basins = []

    checked = []
    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            # if is_lowpoint(row, col, heightmap): 
            basins.append(count_flowing_into(row, col, heightmap, checked))
        print(basins)
        input("(your input): ")
            # print(checked)
    
    basins.sort()
    input("YOUR INPUT: ")
    print(basins)
    input("Your input: ")

    count_9 = 0
    for row in heightmap:
        for col in row:
            if col == 9:
                count_9 += 1
    
    print("Height: ", len(heightmap))
    print("Length: ", len(heightmap[0]))
    print("Count 9: ", count_9)

    # top_3_basins = basins[:3]

    product = 1
    for i in range(3):
        product *= basins.pop()

    print(product)

part2()