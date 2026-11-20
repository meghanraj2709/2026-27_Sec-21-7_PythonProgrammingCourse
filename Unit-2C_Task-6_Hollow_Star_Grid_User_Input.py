rows = 5

for a in range(1, rows + 1):
    for b in range(1, rows + 1):
        if (
            a == 1
            or a == rows
            or b == 1
            or b == rows
        ):
            print ("*", end=" ")
        else:
            print(" ", end=" ")
    print()