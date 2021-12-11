import sys
n = int(input())
max_number = -sys.maxsize
sum = 0

for i in range(1, n + 1):
    number = int(input())
    if number > max_number:
        max_number = number
    sum += number

sum -= max_number
if max_number == sum:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {abs(max_number - sum)}")