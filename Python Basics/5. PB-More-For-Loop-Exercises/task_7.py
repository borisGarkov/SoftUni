stadium_capacity = int(input())
fans_number = int(input())
fans_A = 0
fans_B = 0
fans_V = 0
fans_G = 0

for sector_number in range(fans_number):
    sector = input()

    if sector == "A":
        fans_A += 1
    elif sector == "B":
        fans_B += 1
    elif sector == "V":
        fans_V += 1
    elif sector == "G":
        fans_G += 1

print(f"{(fans_A / fans_number) * 100:.2f}%")
print(f"{(fans_B / fans_number) * 100:.2f}%")
print(f"{(fans_V / fans_number) * 100:.2f}%")
print(f"{(fans_G / fans_number) * 100:.2f}%")
print(f"{(fans_number / stadium_capacity) * 100:.2f}%")
