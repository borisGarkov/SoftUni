products_list = input().split("!")


def case_urgent(product, products_list):
    if product not in products_list:
        products_list.insert(0, product)


def case_unnecessary(product, products_list):
    if product in products_list:
        products_list.remove(product)


def case_correct(old_item, new_item, products_list):
    if old_item in products_list:
        get_index = products_list.index(old_item)
        products_list[get_index] = new_item


def case_rearrange(product, products_list):
    if product in products_list:
        products_list.remove(product)
        products_list.append(product)


while True:
    command = input()

    if command == "Go Shopping!":
        break

    if command.split()[0] != "Correct":
        action, product = command.split()
    else:
        action, old_item, new_item = command.split()

    if action == "Urgent":
        case_urgent(product, products_list)
    elif action == "Unnecessary":
        case_unnecessary(product, products_list)
    elif action == "Correct":
        case_correct(old_item, new_item, products_list)
    elif action == "Rearrange":
        case_rearrange(product, products_list)

print(", ".join(products_list))
