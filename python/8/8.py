from sys import argv
from itertools import permutations

# Intro
filename = argv[1] if len(argv) > 1 else "8.in"
lines = [(left.split(), right.split())
    for left, right
    in [line.strip('\n').split(' | ') for line in open(filename).readlines()]
    ]

# Part 1
def part1():
    count = 0
    for _, output in lines:
        for pattern in output.split():
            if len(pattern) in [2, 3, 4, 7]:
                count += 1
    print(count)
part1()

# Part 2
