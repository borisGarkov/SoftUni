count = int(input())
p1 = 0
p2 = 0
p3 = 0

for i in range(1, count + 1):
    number = int(input())

    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

print(f"{(p1 / count) * 100:.2f}%\n{(p2 / count) * 100:.2f}%")
print(f"{(p3 / count) * 100:.2f}%")