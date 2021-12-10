toms_list = input().split(", ")
numbers = int(input())


def case_add(toms_list, card_name):
    if card_name in toms_list:
        print("Card is already bought")
    else:
        print("Card successfully bought")
        toms_list.append(card_name)
    return toms_list


def case_remove(toms_list, card_name):
    if card_name in toms_list:
        print("Card successfully sold")
        toms_list.remove(card_name)
    else:
        print("Card not found")
    return toms_list


def case_remove_at(toms_list, index):
    if index in range(len(toms_list)):
        toms_list.pop(index)
        print("Card successfully sold")
    else:
        print("Index out of range")
    return toms_list


def case_insert(toms_list, index, card):
    if index in range(len(toms_list)) and card not in toms_list:
        toms_list.insert(index, card)
        print("Card successfully bought")
    elif index in range(len(toms_list)) and card in toms_list:
        print("Card is already bought")
    else:
        print("Index out of range")
    return toms_list


for number in range(1, numbers + 1):
    data = input()

    if data.split(", ")[0] == "Insert":
        command, index, card = data.split(", ")
        index = int(index)

        toms_list = case_insert(toms_list, index, card)

    else:
        command, value = data.split(", ")

        if command == "Add":
            toms_list = case_add(toms_list, value)
        elif command == "Remove":
            toms_list = case_remove(toms_list, value)
        elif command == "Remove At":
            index = int(value)
            toms_list = case_remove_at(toms_list, index)

print(", ".join(toms_list))
