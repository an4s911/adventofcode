from sys import argv
from copy import deepcopy

# Intro
filename = argv[1] if len(argv) > 1 else "6.in"
fishes = list(map(int, (open(filename).read().split(","))))

# Part 1
def part1(days):
    # days = 80
    temp_fishes = deepcopy(fishes)
    for _ in range(days):
        # print(fishes)
        # input("Proceed?: ")
        n = len(temp_fishes)
        for i in range(n):
            if temp_fishes[i] > 0:
                temp_fishes[i] -= 1
            else:
                temp_fishes[i] = 6
                temp_fishes.append(8)

    print(len(temp_fishes))


# Part 2
def part2(days):
    fish_count = {i:0 for i in range(9)}

    for fish in fishes:
        fish_count[fish] += 1

    # days = 256
    for _ in range(days):
        old0 = fish_count[0]
        for i in range(0, 6):
            fish_count[i] = fish_count[i + 1]
        fish_count[6] = old0 + fish_count[7]
        fish_count[7] = fish_count[8]
        fish_count[8] = old0

    print(sum(fish_count.values()))

part1(80)
part2(256)