"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity."""

nums_one = [4,5,6,7,0,1,2]
nums_two = [1]
nums_three = [3, 4, 5, 6, 7, 1, 2]

def find_pivot(nums):
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return 0 if nums[0] < nums[1] else 1
    if nums[-1] > nums[0]:  # no rotations
        return 0
    midpoint = len(nums) // 2
    if nums[midpoint] > nums[0]:
        return find_pivot(nums[midpoint + 1:]) + midpoint + 1
    return find_pivot(nums[:midpoint + 1])

def binary_search(nums, target):
    if not len(nums):
        return -1
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    midpoint = len(nums) // 2
    if nums[midpoint] == target:
        return midpoint
    if nums[midpoint] > target:
        return binary_search(nums[:midpoint], target)
    result = binary_search(nums[midpoint + 1:], target)
    return result + midpoint + 1 if result != -1 else result

def search(nums, target):
    """Search for target in possibly rotated sorted array nums
    Approach: find pivot; perform binary search on correct side of pivot"""
    if len(nums) == 1:
        return 0 if nums[0] == target else -1 
    pivot = find_pivot(nums)
    if not pivot: # no rotations
        return binary_search(nums, target)
    if target < nums[0]:
        result = binary_search(nums[pivot:], target)
        return result + pivot if result != -1 else -1
    return binary_search(nums[:pivot], target)
    

print(search(nums_three, 6))
    