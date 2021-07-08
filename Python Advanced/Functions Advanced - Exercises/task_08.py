def even_odd(*args):
    command = list(args).pop()
    array = list(args)[:-1]
    if command == "even":
        return list(filter(lambda x: x % 2 == 0, array))
    return list(filter(lambda x: not x % 2 == 0, array))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
