from sys import argv

# Intro
filename = argv[1] if len(argv) > 1 else "5.in"
lines = [line.strip() for line in open(filename).readlines()]

# Part 1
intersects = dict()
for line in lines:
    start, end = line.split(" -> ")
    x1, y1 = list(map(int, start.split(',')))
    x2, y2 = list(map(int, end.split(',')))

    x = y = None

    if x1 == x2:
        step = 1 if y1 < y2 else -1
        range_start, range_end = y1, y2 + step
        x = x1
    elif y1 == y2:
        step = 1 if x1 < x2 else -1
        range_start, range_end = x1, x2 + step
        y = y1
    else:
        continue

    for i in range(range_start, range_end, step):
        x3 = i if x is None else x
        y3 = i if y is None else y
        points = (x3, y3)
        if points not in intersects:
            intersects[points] = 0
        intersects[points] += 1

# Visualization
# for y in range(10):
#     for x in range(10):
#         points = (x, y)
#         value = intersects.get(points, ".")
#         print(value, end="")
#     print()
count = 0
for value in intersects.values():
    if value >= 2:
        count += 1

print(count)
    
# Part 2
def add_intersect(existing_intersects: dict, x, y) -> None:
    if (x, y) not in existing_intersects:
        existing_intersects[(x, y)] = 0
    existing_intersects[(x, y)] += 1

intersects = dict()
for line in lines:
    start, end = line.split(" -> ")
    x1, y1 = list(map(int, start.split(',')))
    x2, y2 = list(map(int, end.split(',')))

    # print(f"---- {x1}, {y1} -> {x2}, {y2}")
    if x1 == x2:
        x = x1
        step = 1 if y1 <= y2 else -1
        for y in range(y1, y2 + step, step):
            add_intersect(intersects, x, y)
            # print((x, y))
        # print()
    elif y1 == y2:
        y = y1
        step = 1 if x1 <= x2 else -1
        for x in range(x1, x2 + step, step):
            add_intersect(intersects, x, y)
        #     print((x, y))
        # print()
    else:
        if x1 < x2 and y1 <=y2:
            n = x2 - x1 + 1
            assert n == y2 - y1 + 1
            x = x1
            y = y1
            for i in range(n):
                add_intersect(intersects, x, y)
                # print((x, y))
                x += 1
                y += 1
            # print()
        elif x1 > x2 and y1 > y2:
            n = x1 - x2 + 1
            assert n == y1 - y2 + 1
            x = x1
            y = y1
            for i in range(n):
                add_intersect(intersects, x, y)
                # print((x, y))
                x -= 1
                y -= 1
            # print()
        elif x1 < x2 and y1 > y2:
            n = x2 - x1 + 1
            assert n == y1 - y2 + 1
            x = x1
            y = y1
            for i in range(n):
                add_intersect(intersects, x, y)
                # print((x, y))
                x += 1
                y -= 1
            # print()
        elif x1 > x2 and y1 < y2:
            n = x1 - x2 + 1
            assert n == y2 - y1 + 1
            x = x1
            y = y1
            for i in range(n):
                add_intersect(intersects, x, y)
                # print((x, y))
                x -= 1
                y += 1
            # print()

# print(intersects)
# for y in range(10):
#     for x in range(10):
#         points = (x, y)
#         value = intersects.get(points, ".")
#         print(value, end="")
#     print()

count = 0
for point in intersects:
    if intersects[point] >= 2:
        count += 1

print(count)