n = 5

for i in range(1, n + 1):
    # Centering spaces
    print(" " * (n - i), end="")

    if i == 1:
        print("1")
    elif i == n:
        # Bottom row prints 1 through n with spaces
        print(" ".join(str(x) for x in range(1, n + 1)))
    else:
        # First number is 1, last number is i
        inner_spaces = " " * (2 * i - 3)
        print(f"1{inner_spaces}{i}")