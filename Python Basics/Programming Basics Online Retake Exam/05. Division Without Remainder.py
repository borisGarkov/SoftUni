number = int(input())
divisible_by_two = 0
divisible_by_three = 0
divisible_by_four = 0

for i in range(1, number + 1):
    current_number = int(input())

    if current_number % 2 == 0:
        divisible_by_two += 1
    if current_number % 3 == 0:
        divisible_by_three += 1
    if current_number % 4 == 0:
        divisible_by_four += 1

print(f"{(divisible_by_two / number) * 100:.2f}%")
print(f"{(divisible_by_three / number) * 100:.2f}%")
print(f"{(divisible_by_four / number) * 100:.2f}%")