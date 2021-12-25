from sys import argv
from itertools import permutations

# Intro
filename = argv[1] if len(argv) > 1 else "8.in"
lines = [(left.split(), right.split())
    for left, right
    in [line.strip('\n').split(' | ') for line in open(filename).readlines()]
    ]

# Part 1
def part1():
    count = 0
    for _, output in lines:
        for pattern in output.split():
            if len(pattern) in [2, 3, 4, 7]:
                count += 1
    print(count)

part1()

# Part 2
def part2():

    digit_keys = [
        set("abcefg"),
        set("cf"),
        set("acdeg"),
        set("acdfg"),
        set("bcdf"),
        set("abdfg"),
        set("abdefg"),
        set("acf"),
        set("abcdefg"),
        set("abcdfg")
    ]

    ans = 0

    def decode_pattern(pattern, key):
        new_pattern = ""
        for ch in pattern:
            new_pattern += key[ch]
        return new_pattern

    for inp, out in lines:
        for sigma in permutations("abcdefg"):
            key = {}
            for char in "abcdefg":
                key[char] = sigma["abcdefg".index(char)]
            
            correct_keys = True
            for pattern in inp:
                new_pattern = decode_pattern(pattern, key)

                # print(pattern, new_pattern)
                # print(set(new_pattern) in digit_keys)
                # print()
                # input()
                if set(new_pattern) not in digit_keys:
                    correct_keys = False

                # if key['a'] == 'c':
                #     if key['b'] == 'f':
                #         if key['c'] == 'g':
                #             if key['d'] == 'a':
                #                 input()
            
            if not correct_keys:
                continue

            num = ""
            for pattern in out:
                new_pattern = decode_pattern(pattern, key)
                num += str(digit_keys.index(set(new_pattern))) 
            print(num)
            
            ans += int(num)
            break

    print(ans)

part2()
