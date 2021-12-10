number = int(input())

for first in range(number):
    for second in range(number):
        for third in range(number):
            print(chr(first + 97) + chr(second + 97) + chr(third + 97))