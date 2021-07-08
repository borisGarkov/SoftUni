from collections import deque

cups_capacity = deque([int(el) for el in input().split()])
bottles = deque([int(el) for el in input().split()])
wasted_water = 0

while True:
    if not cups_capacity:
        bottles = list(bottles)
        bottles = bottles[::-1]
        print(f"Bottles: {' '.join([str(el) for el in bottles])}")
        break
    if not bottles:
        print(f"Cups: {' '.join([str(el) for el in cups_capacity])}")
        break
    current_bottle = bottles.pop()
    current_cup = cups_capacity[0]
    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
        cups_capacity.popleft()
    else:
        cups_capacity[0] -= current_bottle

print(f"Wasted litters of water: {wasted_water}")