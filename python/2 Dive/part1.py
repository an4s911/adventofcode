
with open("input.txt", 'r') as input_file:
    hor_pos = 0
    depth = 0

    input_lines = input_file.readlines()

    count = 1
    for keyword, value in [line.split() for line in input_lines]:
        value = int(value)
        if keyword == "forward":
            hor_pos += value
        elif keyword == "down":
            depth += value
        elif keyword == "up":
            depth -= value
print(hor_pos, depth)

print(hor_pos*depth)