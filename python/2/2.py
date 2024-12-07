from sys import argv

filename = argv[1] if len(argv) > 1 else "2.in"


def is_safe(L: list[int]):
    inc: bool = L[1] > L[0]

    for i in range(len(L) - 1):
        if (L[i + 1] > L[i]) != inc:
            return False
        if abs(L[i] - L[i + 1]) not in [1, 2, 3]:
            return False
    return True


def is_safe_bad_single(L: list[int]):
    if is_safe(L):
        return True

    for i in range(len(L)):
        filtered = []
        for j in range(len(L)):
            if j != i:
                filtered.append(L[j])
        if is_safe(filtered):
            return True


with open(filename) as f:
    safe_count = 0
    for i in f.readlines():
        x = is_safe(list(map(lambda x: int(x), i.split())))
        print("Safe" if x else "Unsafe")
        safe_count += 1 if x else 0
    print(safe_count)

with open(filename) as f:
    safe_count = 0
    for i in f.readlines():
        x = is_safe_bad_single(list(map(lambda x: int(x), i.split())))
        print("Safe" if x else "Unsafe")
        safe_count += 1 if x else 0
    print(safe_count)
