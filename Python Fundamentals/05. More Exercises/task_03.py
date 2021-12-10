string_to_read = list(input())
numbers_list = [int(char) for char in string_to_read if char.isdigit()]
non_numbers_list = [char for char in string_to_read if not char.isdigit()]
take_list = [numbers_list[index_digit] for index_digit in range(len(numbers_list)) if index_digit % 2 == 0]
skip_list = [numbers_list[index_digit] for index_digit in range(len(numbers_list)) if index_digit % 2 != 0]

for index in take_list:
    get_string = non_numbers_list[1:index]
    print(get_string)
