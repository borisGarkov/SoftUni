width = int(input())
length = int(input())

cake_size = width * length

cake_piece = input()
sum_cake = 0

while sum_cake < cake_size:

    if cake_piece != "STOP":
        sum_cake += int(cake_piece)

    if cake_piece == "STOP":
        print(f"{cake_size - sum_cake} pieces are left.")
        break

    if sum_cake > cake_size:
        print(f"No more cake left! You need {sum_cake - cake_size} pieces more.")
        break

    cake_piece = input()