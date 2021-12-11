def my_function(items: list = [1, 2], boo: bool = True):
    result = sum(items)

    if boo:
        items.append(result)

    return result, items


print(my_function())
print(my_function())
print(my_function())

print(my_function(boo=False))

# 1 - 3, [1,2,3]
# 2 - 3, [1,2]
