for count in range(0, 10, 1):
    print()
    for count_a in range(count+1):
        print("*", end="")
    for count_space_a in range(count, 11, 1):
        print(" ", end="")
    for count_b in range(count, 11):
        print("*", end="")
    for count_space_b in range(0, count, 1):
        print(" ", end="")
    for count_space_c in range(0, count, 1):
        print(" ", end="")
    for count_c in range(count, 11):
        print("*", end="")

