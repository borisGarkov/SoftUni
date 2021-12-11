n = int(input())
sum_even = 0
sum_odd = 0
for i in range(n):
    cur_number = int(input())
    if i % 2 == 0:
        sum_even += cur_number
    if i % 2 == 1:
        sum_odd += cur_number
if sum_even == sum_odd:
    print('Yes')
    print(f'Sum = {sum_even}')
else:
    print('No')
    print(f'Diff = {abs(sum_even - sum_odd)}')