destination = input()

while destination != "End":

    if destination == "End":
        break

    destination_budget = float(input())
    total = 0

    while total < destination_budget:

        saved_money = float(input())
        total += saved_money

    print(f"Going to {destination}!")
    destination = input()
