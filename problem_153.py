"""Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time."""

test_array1 = [4, 5, 6, 7, 0, 1, 2]
test_array2 = [3, 4, 5, 1, 2]


def find_min(nums):
    if len(nums) == 1:
        return nums[0]
    if nums[-1] > nums[0]:  # no rotations
        return nums[0]
    if len(nums) == 2:
        return nums[0] if nums[0] < nums[1] else nums[1]    
    midpoint = len(nums) // 2
    if nums[midpoint] > nums[0]:
        return find_min(nums[midpoint + 1:])
    return find_min(nums[:midpoint + 1])


print(find_min(test_array1))
