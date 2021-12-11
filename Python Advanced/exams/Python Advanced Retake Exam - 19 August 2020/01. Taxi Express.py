customers = list(map(int, input().split(", ")))
taxis = list(map(int, input().split(", ")))
total_time = 0

while True:
    customer = customers[0]
    taxi = taxis[-1]

    if taxi >= customer:
        total_time += customer
        customers = customers[1:]
    taxis.pop()

    if not taxis and customers:
        print("Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join(map(str, customers))}")
        break
    if not customers:
        print("All customers were driven to their destinations")
        print(f"Total time: {total_time} minutes")
        break
