rows = 5

for i in range(1, rows + 1):
    print("  " * (rows - i), end="")

    start = i
    peak = 2 * i - 1

    for val in range(start, peak + 1):
        print(val, end=" ")

    for val in range(peak - 1, start - 1, -1):
        print(val, end=" ")

    print()