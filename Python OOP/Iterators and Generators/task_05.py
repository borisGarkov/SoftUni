def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            number = i / 2
            yield number

    def take(n, seq):
        nums = []
        for i in seq:
            if len(nums) == n:
                return nums
            nums.append(i)

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
