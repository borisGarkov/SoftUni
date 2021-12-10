numbers_list = [int(number) for number in input().split()]
string_list = list(input())
string_output = ""

for number in numbers_list:
    sum_digits = sum(int(digit) for digit in str(number))

    if sum_digits >= len(string_list):
        sum_digits = sum_digits - len(string_list)

    get_index = string_list.pop(sum_digits)
    string_output += get_index

print(string_output)