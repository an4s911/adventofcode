from pprint import pprint
from sys import argv

filename = argv[1] if len(argv) > 1 else '13.in'


def print_sheet(sheet):
    for num, line in enumerate(sheet):
        print(f"{num}".ljust(4, "-") + "> " + ''.join(line))
    print('\n\n')


dot_cordinates = []
instructions = []

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line[0].isdigit():
            dot_cordinates.append(tuple(int(i) for i in line.split(',')))
        else:
            instructions.append(line)

x_len = max(dot_cordinates, key=lambda x: x[0])[0] + 1
y_len = max(dot_cordinates, key=lambda x: x[1])[1] + 1

# 2D array where the indexes are (y, x), where ys are the rows
# and xs are the columns
sheet = []

for i in range(y_len):
    sheet.append([])
    for j in range(x_len):
        sheet[i].append('.')


for coordinate in dot_cordinates:
    sheet[coordinate[1]][coordinate[0]] = '#'


def compare_and_return_dot(a, b):
    if a == '#':
        return a
    return b


def get_colum_from_sheet(col_index, sheet):
    pass


def fold_sheet_y(sheet,  coordinate):
    # for i in range(x_len):
    #     sheet[coordinate][i] = '-'

    y_len = len(sheet)
    x_len = len(sheet[0])

    for col_index in range(x_len):
        for row_index in range(y_len - 1, -1, -1):

            backward_row_index = 2 * coordinate - row_index

            sheet[backward_row_index][col_index] = compare_and_return_dot(
                sheet[backward_row_index][col_index],
                sheet[row_index][col_index]
            )

            if row_index == coordinate:
                break

    if y_len % 2 == 1:
        coordinate += 1

    return sheet[:coordinate]


def fold_sheet_x(sheet,  coordinate):
    # for i in range(y_len):
    #     sheet[i][coordinate] = '|'
    y_len = len(sheet)
    x_len = len(sheet[0])

    for row_index in range(y_len):
        for col_index in range(x_len - 1, -1, -1):
            backward_col_index = 2 * coordinate - col_index

            sheet[row_index][backward_col_index] = compare_and_return_dot(
                sheet[row_index][col_index],
                sheet[row_index][backward_col_index]
            )

            if col_index == coordinate:
                break

    if x_len % 2 == 1:
        coordinate += 1

    for row_index in range(len(sheet)):
        sheet[row_index] = sheet[row_index][:coordinate]

    return sheet


def get_dots_count(sheet):
    count = 0
    x_len = len(sheet[0])
    y_len = len(sheet)
    for row_index in range(y_len):
        for col_index in range(x_len):
            if sheet[row_index][col_index] == '#':
                count += 1

    return count


def fold_sheet(sheet, direction, coordinate):
    if direction == 'y':
        sheet = fold_sheet_y(sheet, coordinate)
    elif direction == 'x':
        # print(coordinate)
        sheet = fold_sheet_x(sheet, coordinate)

    print(get_dots_count(sheet))

    # for i in range(6):
    #     for j in range(40):
    #         print(sheet[i][j], end='')
    #     print()

    return sheet


# print_sheet(sheet)
instructions = [
    (i.split()[2].split('=')[0], int(i.split()[2].split('=')[1])) for i in instructions
]

for num, instruction in enumerate(instructions):
    sheet = fold_sheet(sheet, instruction[0], instruction[1])
    # print(get_dots_count(sheet))
    if num == 11:
        print_sheet(sheet)
        break
