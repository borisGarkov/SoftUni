money_trip = float(input())
money_in_hand = float(input())
days_count = 0
days_count_spend = 0

while days_count_spend < 5:
    days_count += 1
    action_type = input()
    money_save_spend = float(input())

    if action_type == "spend":
        money_in_hand -= money_save_spend
        days_count_spend += 1
        if money_in_hand < 0:
            money_in_hand = 0

    elif action_type == "save":
        money_in_hand += money_save_spend
        days_count_spend = 0

    if money_in_hand >= money_trip:
        print(f"You saved the money for {days_count} days.")
        break

    if days_count_spend == 5:
        print(f"You can't save the money.\n{days_count}")


