from sys import argv

filename = argv[1] if len(argv) > 1 else "1.in"


LEFT = []
RIGHT = []


def add_to_list_sorted(x, L):
    L.append(x)
    L.sort()


def add_to_lists(x, y):
    add_to_list_sorted(x, LEFT)
    add_to_list_sorted(y, RIGHT)


with open(filename) as f:
    for i in f.readlines():
        x, y = list(map(lambda x: int(x), i.split()))
        add_to_lists(x, y)


if len(LEFT) != len(RIGHT):
    raise ValueError("Lists are not the same size")


n = len(LEFT)

DISTANCES = []

for i in range(n):
    DISTANCES.append(abs(RIGHT[i] - LEFT[i]))

print(sum(DISTANCES))


def count_num_in_list(num, L):
    return len(list(filter(lambda x: x == num, L)))


SIMILARITY = []

for i in LEFT:
    c = count_num_in_list(i, RIGHT)
    SIMILARITY.append(i * c)

print(sum(SIMILARITY))
