shops = input().split()
commands_number = int(input())


def remove_first_shops(shops_list, shops_number):
    if shops_number <= len(shops_list):
        shops_list = shops_list[::-1]
        for _ in range(shops_number):
            shops_list.pop()
        shops_list = shops_list[::-1]
    return shops_list


def remove_last_shops(shops_list, shops_number):
    if shops_number <= len(shops_list):
        for _ in range(shops_number):
            shops_list.pop()
    return shops_list


def swap_shops_places(shops_list, first_shop, second_shop):
    if first_shop in range(len(shops_list)) and second_shop in range(len(shops_list)):
        shops_list[first_shop], shops_list[second_shop] = shops_list[second_shop], shops_list[first_shop]
    return shops_list


def insert_shops(shops_list, shop, shop_index):
    if shop_index in range(len(shops_list)):
        shops_list.insert(shop_index + 1, shop)
    return shops_list


for _ in range(commands_number):
    data = input().split()

    if data[0] == "Include":
        command, shop = data
        shops.append(shop)
    else:
        command, first_item, second_item = data
        second_item = int(second_item)

        if command == "Visit":
            if first_item == "first":
                shops = remove_first_shops(shops, second_item)
            else:
                shops = remove_last_shops(shops, second_item)
        elif command == "Prefer":
            first_item = int(first_item)
            shops = swap_shops_places(shops, first_item, second_item)
        elif command == "Place":
            shops = insert_shops(shops, first_item, second_item)

print("Shops left:")
print(*shops)
