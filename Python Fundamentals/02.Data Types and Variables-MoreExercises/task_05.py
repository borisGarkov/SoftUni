n_lines = int(input())

count_open = 0
count_close = 0
double_open = 0
double_close = 0

for _ in range(n_lines):
    current_char = input()
    if current_char == "(":
        count_open += 1
        double_open += 1
        double_close = 0
    elif current_char == ")":
        count_close += 1
        double_close += 1
        double_open = 0

    if double_open == 2:
        break

if count_open == count_close:
    print("BALANCED")
else:
    print("UNBALANCED")
