from sys import argv

filename = argv[1] if len(argv) == 2 else "input.txt"

with open(filename, "r") as file:
    lines = file.readlines()
    n = len(lines[0].strip())

    bitsox = bitsco = [line.strip() for line in lines]

    for i in range(n):
        count1 = count0 = 0

        for bit in bitsox:
            if bit[i] == "1":
                count1 += 1
            else:
                count0 += 1
        
        if count1 > count0:
            bitsox = [bit for bit in bitsox if bit[i] == "1"]

        elif count0 > count1:
            bitsox = [bit for bit in bitsox if bit[i] == "0"]

        else:
            bitsox = [bit for bit in bitsox if bit[i] == "1"]

        if len(bitsox) == 1:
            ox_ans = int(bitsox[0], 2)
            break

    for i in range(n):
        count1 = count0 = 0

        for bit in bitsco:
            if bit[i] == "1":
                count1 += 1
            else:
                count0 += 1
        
        if count1 > count0:
            bitsco = [bit for bit in bitsco if bit[i] == "0"]

        elif count0 > count1:
            bitsco = [bit for bit in bitsco if bit[i] == "1"]

        else:
            bitsco = [bit for bit in bitsco if bit[i] == "0"]
        
        if len(bitsco) == 1:
            co_ans = int(bitsco[0], 2)
            break

print(ox_ans * co_ans)