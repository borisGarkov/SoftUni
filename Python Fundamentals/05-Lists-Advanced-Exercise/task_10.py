def case_collect(items_list, item):
    if item not in items_list:
        items_list.append(item)


def case_drop(items_list, item):
    if item in items_list:
        items_list.remove(item)


def case_combine_items(items_list, old_item, new_item):
    if old_item in items_list:
        old_item_index = items_list.index(old_item)
        items_list.insert(old_item_index + 1, new_item)


def case_renew(items_list, item):
    if item in items_list:
        item_index = items_list.index(item)
        items_list += [items_list.pop(item_index)]


items = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break

    command = command.split(" - ")
    action = command[0]
    item = command[1]

    if action == "Collect":
        case_collect(items, item)
    elif action == "Drop":
        case_drop(items, item)
    elif action == "Combine Items":
        item = item.split(":")
        old_item = item[0]
        new_item = item[1]
        case_combine_items(items, old_item, new_item)
    elif action == "Renew":
        case_renew(items, item)

print(*items, sep=", ")
