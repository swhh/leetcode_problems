"""Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space."""

test_nums1 = [1, 2, 0]
test_nums2 = [3, 4, 1]
test_nums3 = [7, 8, 9, 11, 12]
test_nums4 = [1, 3, 4, 2, 2]
test_nums5 = [3, 1, 3, 3, 4, 2, 3, 2]
test_nums6 = [5, 6, 1, 4, 3, 2, 10, 7, 8]


def first_missing_positive(nums):
    """Find first missing positive in list of ints nums in O(n) time and O(1) extra space"""
    min_pos = min(num for num in nums if num > 0)
    if not min_pos or min_pos > 1:
        return 1
    n = sum(1 for _ in (num for num in nums if num > 0))  # first missing positive integer must be between 1 and n + 1
    i = j = 0
    previous = False
    while i < n:
        num = nums[j]
        if previous:
            nums[j] = True
        if num is True or not 1 <= num <= n:
            i += 1
            j = i
            previous = False
        else:
            j = num - 1
            previous = True

    return next((i + 1 for i, x in enumerate(nums) if x is not True), n + 1)


print(first_missing_positive(test_nums1))







