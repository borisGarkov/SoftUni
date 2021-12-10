substrings_list = input().split(", ")
strings_list = input()

unique_substrings = [element for element in substrings_list if element in strings_list]

print(unique_substrings)
