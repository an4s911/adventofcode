import pprint
from sys import argv

filename = argv[1] if len(argv) > 1 else '14.in'

with open(filename, 'r') as f:
    pattern = list(f.readline().strip())
    # print(''.join(pattern))
    f.readline()

    rules = {}
    for line in f:
        line = line.strip()
        pair, result = line.split(' -> ')
        rules[pair] = result


class Count:

    def __init__(self):
        self.dict = {}

    def add_count(self, pair, count=1):
        if pair not in self.dict:
            self.dict[pair] = 0
        self.dict[pair] += count

    def get_count_for_letters(self):
        letters_count = {}
        count_f = 0
        for num, pair in enumerate(self.dict):

            # print(f"{pair} -> {rules[pair]}")

            # if pair[0] == 'F':
            #     print(num, "Pair[0] is F")
            #     count_f += self.dict[pair]

            # if pair[1] == 'F':
            #     print(num, "Pair[1] is F")

            if pair[0] not in letters_count:
                letters_count[pair[0]] = 0
            letters_count[pair[0]] += self.dict[pair]

            # if letters_count[pair[0]] == 538921731593:
            #     print(pair)

            if rules[pair] == 'F':
                count_f += self.dict[pair]

            if rules[pair] not in letters_count:
                letters_count[rules[pair]] = 0
            letters_count[rules[pair]] += self.dict[pair]

        letters_count[pattern[-1]] += 1

        return letters_count


def solve(steps):
    counts = Count()

    for i in range(len(pattern) - 1):
        counts.add_count(pattern[i] + pattern[i + 1])
    for i in range(steps - 1):
        new_counts = Count()

        for pair in counts.dict:

            new_counts.add_count(pair[0] + rules[pair], counts.dict[pair])
            new_counts.add_count(rules[pair] + pair[1], counts.dict[pair])

        # print("*" * 20)

        counts = new_counts

    # print(new_counts.dict)

    # print(counts.dict)
    # print(counts.get_count_for_letters())

    letter_counts = counts.get_count_for_letters()

    values = letter_counts.values()
    # print(letter_counts)
    max_value = max(values)
    min_value = min(values)

    # print(max_value, min_value)
    print(max_value - min_value)


solve(10)  # Part 1
solve(40)  # Part 2
