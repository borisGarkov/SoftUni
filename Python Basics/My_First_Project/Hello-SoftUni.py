# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in numbers:
#     print(x)

# for x in range(1, 11, 1):
#     print(x)
# else:
#     print("Finished")

# a = int(input())
# size = a * a
# print(size)

# name = input()
# print(f"Hello, {name}!")

# task 3
# deposit = float(input())
# term_of_deposit = int(input())
# interest = float(input())
#
# sum = deposit + term_of_deposit * ((deposit * (interest / 100)) / 12)
# print(sum)


# task 8
lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = lenght * width * height
liters = volume * 0.001

result = liters * (1 - (percent * 0.01))

print(result)
