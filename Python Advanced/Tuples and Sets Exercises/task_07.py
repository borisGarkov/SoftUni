n = int(input())
odd_set = set()
even_set = set()

for line_number in range(1, n + 1):
    line = input()
    sum_ascii = 0
    for i in line:
        sum_ascii += ord(i)

    sum_ascii //= line_number
    if sum_ascii % 2 == 0:
        even_set.add(sum_ascii)
    else:
        odd_set.add(sum_ascii)

sum_odd = sum(odd_set)
sum_even = sum(even_set)
odd_set = set([str(el) for el in odd_set])
even_set = set([str(el) for el in even_set])

if sum_even == sum_odd:
    print(", ".join(odd_set.union(even_set)))
elif sum_odd > sum_even:
    print(", ".join(odd_set.difference(even_set)))
else:
    print(", ".join(odd_set.symmetric_difference(even_set)))