from collections import deque
quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))
while orders:
    order = orders.popleft()
    if quantity >= order:
        quantity -= order
    else:
        orders.appendleft(order)
        break

if len(orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
