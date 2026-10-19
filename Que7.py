rows = 5

for i in range(1, rows + 1):
    # Leading spaces
    print("  " * (rows - i), end="")

    # Ascending from 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")

    # Descending from i-1 down to 1
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()