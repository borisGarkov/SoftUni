n = int(input())
longest_intersection = set()


def convert_range_to_set(start, end) -> set:
    start = int(start)
    end = int(end)
    final_set = set(range(start, end + 1))
    return final_set


def check_longest_intersection(first_set, second_set) -> set:
    set_intersection = first_set.intersection(second_set)
    return set_intersection


for _ in range(n):
    data = input().split("-")
    first_range, second_range = data
    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")

    first_set = convert_range_to_set(first_start, first_end)
    second_set = convert_range_to_set(second_start, second_end)

    set_intersection = check_longest_intersection(first_set, second_set)
    if len(set_intersection) > len(longest_intersection):
        longest_intersection = set()
        longest_intersection = set_intersection

print(f"Longest intersection is [{', '.join([str(el) for el in longest_intersection])}] "
      f"with length {len(longest_intersection)}")
