from sys import argv
from typing import Iterable
from copy import deepcopy

filename = argv[1] if len(argv) > 1 else "input.txt"

def check_row_empty(row: list) -> bool:
    for col_item in row:
        if col_item != "":
            return False
    return True

def check_row_wins(board: list) -> bool:
    for row in board:
        if check_row_empty(row):
            return True
    return False

def check_col_empty(col_index: int, board: list) -> bool:
    for row in board:
        if row[col_index] != "":
            return False
    return True

def check_col_wins(board: list) -> bool:
    n = len(board)

    for col_index in range(n):
        if check_col_empty(col_index, board):
            return True
    return False

def check_win(board: list) -> bool:
    return check_row_wins(board) or check_col_wins(board)

def who_wins(boards: list) -> int or None:
    for board_index in range(len(boards)):
        if check_win(boards[board_index]):
            return board_index
    return None

def losing_boards(boards: list) -> list:
    losing = []
    for board in boards:
        if not check_win(board):
            losing.append(board)
    return losing

# Intro
lines = [line.strip() for line in open(filename).readlines()]
draws = lines[0].split(',')
i = 2
boards = []
while i < len(lines):
    curr_board = []
    for j in range(5):
        curr_board.append(lines[i + j].split())
    boards.append(curr_board)
    i += 6


# Part 1
temp_boards1 = deepcopy(boards)
winner_index = None

for draw in draws:
    for board in temp_boards1:
        for row in board:
            for col_index in range(len(row)):
                if row[col_index] == draw:
                    row[col_index] = ""
    
    winner_index = who_wins(temp_boards1)
    if winner_index is not None:
        winning_draw1 = int(draw)
        break

sum_unmarked1 = 0

for row in temp_boards1[winner_index]:
    for col in row:
        if col:
            sum_unmarked1 += int(col)

print(sum_unmarked1 * winning_draw1)


# Part 2
temp_boards2 = deepcopy(boards)
loser_index = None

for draw in draws:
    for board in temp_boards2:
        for row in board:
            for col_index in range(len(row)):
                if row[col_index] == draw:
                    row[col_index] = ""
    
    if len(temp_boards2) == 1:
        if check_win(temp_boards2[0]):
            winning_draw2 = int(draw)
            break
        else:
            continue

    temp_boards2 = losing_boards(temp_boards2)
    
sum_unmarked2 = 0

for row in temp_boards2[0]:
    for col in row:
        sum_unmarked2 += int(col) if col else 0

print(sum_unmarked2 * winning_draw2)