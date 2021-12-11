import itertools


def possible_permutations(numbers):
    for element in itertools.permutations(numbers):
        yield list(element)


[print(n) for n in possible_permutations([1, 2, 3])]
