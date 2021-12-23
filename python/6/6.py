from sys import argv

# Intro
filename = argv[1] if len(argv) > 1 else "6.in"
fishes = list(map(int, (open(filename).read().split(","))))

# Part 1
days = int(input("Number of days: "))
for day in range(days):
    # print(fishes)
    # input("Proceed?: ")
    n = len(fishes)
    for i in range(n):
        if fishes[i] > 0:
            fishes[i] -= 1
        else:
            fishes[i] = 6
            fishes.append(8)

print(len(fishes))


# Part 2