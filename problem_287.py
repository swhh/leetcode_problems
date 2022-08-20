"""Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space."""

test_nums1 = [1, 3, 4, 2, 2]
test_nums2 = [3, 1, 3, 4, 2]


def find_duplicate(nums):
    return sum(nums) - (len(nums) * (len(nums) - 1)) / 2


print(find_duplicate(test_nums2))
