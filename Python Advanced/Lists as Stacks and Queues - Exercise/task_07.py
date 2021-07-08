from collections import deque
from datetime import datetime, timedelta

data = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")
robots = []
available_robots = deque()
products = deque()

for el in data:
    robot = {}
    robot["name"] = el.split("-")[0]
    robot["process_time"] = int(el.split("-")[1])
    robot["available_at"] = time
    robots.append(robot)
    available_robots.append(robot)

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    time = time + timedelta(seconds=1)
    current_product = products.popleft()
    if available_robots:
        current_robot = available_robots.popleft()
        current_robot["available_at"] = time + timedelta(seconds=current_robot["process_time"])
        robot = [el for el in robots if el == current_robot][0]
        robot["available_at"] = time + timedelta(seconds=current_robot["process_time"])
        print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= r["available_at"]:
                available_robots.append(r)
        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()
            current_robot["available_at"] = time + timedelta(seconds=current_robot["process_time"])
            robot = [el for el in robots if el == current_robot][0]
            robot["available_at"] = time + timedelta(seconds=current_robot["process_time"])
            print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
