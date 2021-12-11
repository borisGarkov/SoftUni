number = int(input())

for row in range(1, number + 1):

    for col in reversed(range(1, (number - row) + 1)):
        print(" ", end="")

    for col in range(1, row + 1):
        print("* ", end="")

    print()

for row in reversed(range(1, number)):
    for col in range(1, (number - row) + 1):
        print(" ", end="")

    for col in reversed(range(1, row + 1)):
        print("* ", end="")

    print()
