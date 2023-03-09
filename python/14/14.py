import pprint
from sys import argv

filename = argv[1] if len(argv) > 1 else '14.test'

with open(filename, 'r') as f:
    pattern = list(f.readline().strip())
    # print(''.join(pattern))
    f.readline()

    rules = {}
    for line in f:
        line = line.strip()
        pair, result = line.split(' -> ')
        rules[tuple(pair)] = result
    # print(repr(pair), repr(result))
    # pprint.pprint(rules)


for i in range(10):
    new_pattern = []
    new_pattern.append(pattern[0])
    for i in range(len(pattern) - 1):

        # print(tuple(pattern[i: i + 2]))
        new_pattern.append(rules[tuple(pattern[i: i + 2])])
        new_pattern.append(pattern[i + 1])
    pattern = new_pattern

    # print(''.join(new_pattern))

unique_letters = list(set(pattern))
counts = {}
for letter in unique_letters:
    counts[letter] = pattern.count(letter)

result = max(counts.values()) - min(counts.values())

print(result)
