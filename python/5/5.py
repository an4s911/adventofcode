from sys import argv

filename = argv[1] if len(argv) > 1 else "5.in"

lines = [line.strip() for line in open(filename).readlines()]

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
        # for i in range(y1, y2 + step, step):
        #     x, y = x1, i
    elif y1 == y2:
        step = 1 if x1 < x2 else -1
        range_start, range_end = x1, x2 + step
        y = y1
        # for i in range(x1, x2 + step, step):
        #     x, y = i, y1
    else:
        
        continue

    for i in range(range_start, range_end, step):
        x3 = i if x is None else x
        y3 = i if y is None else y
        points = (x3, y3)
        # print(points)
        if points not in intersects:
            intersects[points] = 0
        intersects[points] += 1

# for y in range(10000):
#     for x in range(10000):
#         points = (x, y)
#         value = intersects.get(points, ".")
#         print(value, end="")
#     print()
count = 0
for value in intersects.values():
    if value >= 2:
        count += 1

print(count)
    
# print(intersects)