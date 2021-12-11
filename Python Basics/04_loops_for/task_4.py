count = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, count + 1):
    number = int(input())

    if number < 200:
        p1 += 1
    elif number <= 399:
        p2 += 1
    elif number <= 599:
        p3 += 1
    elif number <= 799:
        p4 += 1
    else:
        p5 += 1

print(f"{(p1 / count) * 100:.2f}%\n{(p2 / count) * 100:.2f}%")
print(f"{(p3 / count) * 100:.2f}%\n{(p4 / count) * 100:.2f}%")
print(f"{(p5 / count) * 100:.2f}%")