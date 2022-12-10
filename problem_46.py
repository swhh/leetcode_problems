from itertools import permutations
# Given an array nums of distinct integers,
# return all the possible permutations. You can return the answer in any order.

test_nums = [1, 2, 3]
test_output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


def permutes(nums):
    permutes_n = permutations(range(len(nums)))
    return [[nums[i] for i in permute] for permute in permutes_n]


print(permutes(test_nums))
