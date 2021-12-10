shops_list = input().split()
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "Include":
        shop = command[1]
        shops_list.append(shop)
    elif command[0] == "Visit":
        direction, number = command[1:]
        number = int(number)
        if number <= len(shops_list):
            if direction == "first":
                shops_list = shops_list[number:]
            else:
                shops_list = shops_list[::-1]
                shops_list = shops_list[number:]
                shops_list = shops_list[::-1]

    elif command[0] == "Prefer":
        index_1, index_2 = command[1:]
        index_1 = int(index_1)
        index_2 = int(index_2)
        if index_1 in range(0, len(shops_list)) and index_2 in range(0, len(shops_list)):
            shops_list[index_1], shops_list[index_2] = shops_list[index_2], shops_list[index_1]
    elif command[0] == "Place":
        shop, index = command[1:]
        index = int(index)
        if index + 1 in range(len(shops_list)):
            shops_list.insert(index + 1, shop)

print("Shops left:")
print(*shops_list)
