clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())
running_sum = 0
racks_count = 1

while clothes_stack:
    if running_sum + clothes_stack[-1] <= rack_capacity:
        running_sum += clothes_stack.pop()
    else:
        running_sum = 0
        racks_count += 1

print(racks_count)