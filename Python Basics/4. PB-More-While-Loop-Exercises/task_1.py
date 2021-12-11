detergent_quantity = int(input())
user_input = input()

count = 0
dishes_number = 0
pots_number = 0
total_detergent = detergent_quantity * 750

while user_input != "End":
    count += 1

    if count > 2:
        count = 0
        total_detergent -= (int(user_input) * 15)
        pots_number += int(user_input)

    else:
        total_detergent -= (int(user_input) * 5)
        dishes_number += int(user_input)

    if total_detergent < 0:
        break

    user_input = input()

if total_detergent >= 0:
    print(f"Detergent was enough!\n{dishes_number} dishes and"
          f" {pots_number} pots were washed.\n"
          f"Leftover detergent {total_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")