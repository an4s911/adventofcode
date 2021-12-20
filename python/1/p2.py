
filename = "input.txt"
# filename = "test.txt"

# My solution 
with open(filename) as input_file:
    input_lines = input_file.readlines()
    n = len(input_lines)
    prev_sum = None
    count = 0
    curr_char = 65
    for i in range(n):
        if i + 2 < n:
            b = [int(input_lines[i]), int(input_lines[i+1]), int(input_lines[i+2])]

            if prev_sum == None: 
                prev_sum = sum(b)
            else:
                if sum(b) > prev_sum:

                    count += 1
                prev_sum = sum(b)

print(count)

## Another solution (by Jonathan Paulson: Youtube & Github)
count = 0
lines = [int(x) for x in open(filename)]
for i in range(len(lines)):
    if i>=3 and lines[i] > lines[i-3]:
        count += 1
print(count)