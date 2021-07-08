from collections import deque

bullet_price = int(input())
barrel_bullets = int(input())
bullets = deque([int(el) for el in input().split()])
locks = deque([int(el) for el in input().split()])
intelligence = int(input())
attempts = 0
initial_bullets_amount = len(bullets)

while True:
    if not bullets or not locks:
        break

    current_lock = locks[0]
    attempts += 1
    current_bullet = bullets.pop()
    if current_bullet <= current_lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if attempts % barrel_bullets == 0 and bullets:
        print("Reloading!")
    if not bullets and locks:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break

if bullets or not locks:
    bullet_cost = bullet_price * (initial_bullets_amount - len(bullets))
    intelligence -= bullet_cost
    print(f"{len(bullets)} bullets left. Earned ${intelligence}")