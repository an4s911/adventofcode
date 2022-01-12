from os import close
from sys import argv
from copy import deepcopy
from pprint import pprint

filename = argv[1] if len(argv) > 1 else '10.in'
lines = [line.strip('\n') for line in open(filename).readlines()]

# Part 1
closing_brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def part1():
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    found = []
    temp_lines = deepcopy(lines)
    for line in lines:
        stack = []
        for i in range(len(line)):
            element = line[i]
            if element in closing_brackets:
                stack.append(closing_brackets[element])
            else:
                expected = stack.pop()
                if (expected != element):
                    found.append(element)
                    temp_lines.remove(line)

    # pprint(lines)
    # print()
    # pprint(temp_lines)
    sum_illegal = 0
    for elem in found:
        sum_illegal += points[elem]

    print(sum_illegal)


part1()

# Part 2


def part2():
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    expected_chars = []
    temp_lines = deepcopy(lines)
    for line in lines:
        stack = []
        for i in range(len(line)):
            element = line[i]
            if element in closing_brackets:
                stack.append(closing_brackets[element])
            else:
                expected = stack.pop()
                if (expected != element):
                    # expected_chars.append(expected)
                    temp_lines.remove(line)

        if line in temp_lines:
            expected_chars.append(stack[::-1])
        # print(stack)

    # pprint(expected_chars)
    scores = []

    for closing in expected_chars:
        score = 0
        for elem in closing:
            score *= 5
            score += points[elem]
        scores.append(score)

    scores.sort()

    # pprint(scores)
    print(scores[len(scores)//2])


part2()

# def opens_and_closes(open_brac, close_brac):
#     if brackets[open_brac] + brackets[close_brac] == 0:
#         return True
#     return False


# def is_valid(string):
#     chain = ""
#     for i in string:
#         if brackets[i] > 0:
#             chain += i
#         else:
#             # print("Hey")
#             # print(chain[-1], i)
#             if opens_and_closes(chain[-1], i):
#                 chain = chain[:-1]
#         # print(chain)

#     return chain == ""


# def test_cases():
#     check_trues = [
#         '[]',
#         '[[[]]]',
#         '[][[][]]',
#         '([])',
#         '{()()()}',
#         '<([{}])>',
#         '[<>({}){}[([])<>]]',
#         '(((((((((())))))))))'
#     ]

#     check_falses = [
#         '(]',
#         '{()()()>',
#         '(((()))}',
#         '<([]){()}[{}])'
#     ]
#     for pattern in check_trues:
#         assert is_valid(pattern)

#     for pattern in check_falses:
#         assert not is_valid(pattern)

#     print("All tests complete")


# if __name__ == "__main__":
#     test_cases()
