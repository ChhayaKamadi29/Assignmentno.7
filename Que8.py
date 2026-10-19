n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

    middle_spaces = 2 * (n - i) - 1
    if middle_spaces > 0:
        print("  " * middle_spaces, end="")

    start = i - 1 if i == n else i
    for j in range(start, 0, -1):
        print(j, end=" ")

    print()