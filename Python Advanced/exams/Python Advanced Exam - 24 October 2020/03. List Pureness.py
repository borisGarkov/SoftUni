# def best_list_pureness(numbers_list, k):
#     best_sum = 0
#     best_rotation = 0
#     for iteration in range(k + 1):
#         current_sum = 0
#         for num in numbers_list:
#             current_sum += (num * numbers_list.index(num))
#
#         if current_sum > best_sum:
#             best_sum = current_sum
#             best_rotation = iteration
#
#         numbers_list = numbers_list[-1:] + numbers_list[:-1]
#
#     return f"Best pureness {best_sum} after {best_rotation} rotations"

def best_list_pureness(numbers_list, k, best_sum=0, best_rotation=0):
    if k == 0:
        return f"Best pureness {best_sum} after {best_rotation} rotations"
    current_sum = 0
    current_rotation = k

    for num in numbers_list:
        current_sum += (num * numbers_list.index(num))

    if current_sum >= best_sum:
        best_sum = current_sum
        best_rotation = current_rotation

    numbers_list = numbers_list[-1:] + numbers_list[:-1]
    return best_list_pureness(numbers_list, k - 1, best_sum, best_rotation)


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
