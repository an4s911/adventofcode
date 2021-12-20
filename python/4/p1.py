from sys import argv
from typing import Iterable

filename = argv[1] if len(argv) > 1 else "input.txt"

def check_row_empty(row: Iterable) -> bool:
    for col_item in row:
        if col_item != "":
            return False
    return True

def check_row_wins(board: Iterable) -> bool:
    for row in board:
        if check_row_empty(row):
            return True
    return False

def check_col_empty(col_index: int, board: Iterable) -> bool:
    for row in board:
        if row[col_index] != "":
            return False
    return True

def check_col_wins(board: Iterable) -> bool:
    n = len(board)

    for col_index in range(n):
        if check_col_empty(col_index, board):
            return True
    return False

def check_win(board: Iterable) -> bool:
    return check_row_wins(board) or check_col_wins(board)

def who_wins(boards: Iterable) -> int or None:
    for board_index in range(len(boards)):
        if check_win(boards[board_index]):
            return board_index
    return None

with open(filename) as file:
    lines = [line.strip() for line in file.readlines()]

    draws = lines[0].split(',')

    i = 2

    boards = []

    while i < len(lines):
        curr_board = []

        for j in range(5):
            curr_board.append(lines[i + j].split())

        boards.append(curr_board)

        i += 6

    temp_boards = list(boards)
    winner_index = None

    for draw in draws:
        for board in temp_boards:
            for row in board:
                for col_index in range(len(row)):
                    if row[col_index] == draw:
                        row[col_index] = ""
        
        winner_index = who_wins(temp_boards)
        if winner_index is not None:
            winning_draw = int(draw)
            break
    
    sum_unmarked = 0

    for row in boards[winner_index]:
        for col in row:
            if col:
                sum_unmarked += int(col)

    print(sum_unmarked * winning_draw)


    







    # for board in temp_boards:
    #     for row in board:
    #         print("|", end="\t")
    #         for col in row:
    #             print(col, end="\t|\t")
    #         print("\n")
    #     print("-"*90)

    

    