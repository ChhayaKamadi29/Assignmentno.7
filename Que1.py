
n = 5

for i in range(1, n + 1):
    spaces_outside = " " * (n - i)
    if i == 1:
        print(spaces_outside + "*")
    else:
        spaces_inside = " " * (2 * i - 3)
        print(spaces_outside + "*" + spaces_inside + "*")


for i in range(n, 0, -1):
    spaces_outside = " " * (n - i)
    if i == 1:
        print(spaces_outside + "*")
    else:
        spaces_inside = " " * (2 * i - 3)
        print(spaces_outside + "*" + spaces_inside + "*")