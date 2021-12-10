a = 0
b = 1
c = 1
n = int(input())
numbers_list = [1, 1]

for _ in range(2, n):
    d = a + b + c
    a = b
    b = c
    c = d
    numbers_list.append(d)

print(*numbers_list)