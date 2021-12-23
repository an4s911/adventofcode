from sys import argv

# Intro
filename = argv[1] if len(argv) > 1 else "7.in"

# Part 1
def part1():
    # positions
    positions = list(map(int, open(filename).read().split(",")))
    
    fuel = 0
    ans = None
    for j in positions:
        # j = 16
        for i in positions:
            fuel += i - j if i >= j else j - i
        # print(fuel)
        if not ans or fuel < ans:
            ans = fuel
            # pos = j
        fuel = 0
    print(ans)

part1()

# Part 2
def part2():
    positions = list(map(int, open(filename).read().split(",")))
    
    fuel = 0
    ans = None
    for j in range(1, max(positions) + 1):
        for i in positions:
            curr_diff = i - j if i >= j else j - i 
            sum_diff = curr_diff * (curr_diff + 1) // 2
            fuel += sum_diff
        # print(j)
        if not ans or fuel < ans:
            ans = fuel
            # pos = j
        fuel = 0
    print(ans)

part2()