for i in range(0, 6):

    for j in range(6, 0, -1):
        if i < j:
            print(" ", end=" ")
        else:
            print("*", end=" ")

    print()