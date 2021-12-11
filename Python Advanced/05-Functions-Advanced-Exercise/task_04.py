def get_sum_of_numbers(numbers):
    negatives = sum(list(filter(lambda x: x < 0, numbers)))
    positives = sum(list(filter(lambda x: x >= 0, numbers)))
    return positives, negatives


def print_result(positives, negatives):
    if abs(negatives) > positives:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(el) for el in input().split()]
positives, negatives = get_sum_of_numbers(numbers)
print(negatives)
print(positives)
print_result(positives, negatives)
