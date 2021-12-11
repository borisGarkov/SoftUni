number = int(input())

print("+ ", end="")
for i in range(1, (number - 2) + 1):
    print("- ", end="")
print("+")

for i in range(1, (number - 2) + 1):
    print("| ", end="")

    for j in range(1, (number - 2) + 1):
        print("- ", end="")

    print("|")
            # print()

print("+ ", end="")
for i in range(1, (number - 2) + 1):
    print("- ", end="")
print("+")
