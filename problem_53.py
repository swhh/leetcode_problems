"""Given an integer array nums, find the 
contiguous subarray with the largest sum, and return its sum.
Provide both a n*log(n) divide and conquer algorithm and a linear time algorithm"""

from functools import cache

nums = [-2,1,-3, 4,-1,2,1,-5,4]
nums_2 = [5,4,-1,7,8]
nums_3 = [1]
nums_4 = [1, 4, -1, 2]
nums_5 = [13, -3, -25, 20, -3 -16, -23, 18, 20, -7, 12, -5, -22, 15, -4 ,7]
nums_6 = [-2, -3, 4, -1, -2, 1, 5, -3]

def calculate_max(*args):
    nums = args[0]
    return max(args[1:], key=lambda x: sum(nums[x[0]: x[1]]))

@cache
def recursive_max_subarray(nums: tuple[int]) -> tuple[int]:
    n = len(nums)
    if n == 1:
        return (0, 1)
    mid = n // 2
    a_start, a_end = recursive_max_subarray(nums[:mid])
    b_start, b_end = recursive_max_subarray(nums[mid:])
    b_start, b_end = mid + b_start, mid + b_end
    # 3 sub-cases a. both sub_arrays contiguous with mid point, b. one contiguous with mid_point c. no subarray contiguous with mid_point
    # case a
    if a_end == mid and b_start == mid:
        return calculate_max(nums, (a_start,a_end), (b_start,b_end), (a_start, b_end))
    # case b
    if a_end == mid or b_start == mid:
        if a_end == mid:
            c_start, c_end = recursive_max_subarray(nums[a_start: b_start - 1])
            c_start, c_end = c_start + a_start, c_end + a_start  
        else:
            c_start, c_end = recursive_max_subarray(nums[a_end + 1: b_end])
            c_start, c_end = c_start + a_end + 1, c_end + a_end + 1   
        return calculate_max(nums, (a_start,a_end), (b_start,b_end), (c_start, c_end), (a_start, b_end))
    # case c
    c_start, c_end = recursive_max_subarray(nums[a_start: b_start])
    d_start, d_end = recursive_max_subarray(nums[a_end: b_end])
    c_start, c_end = c_start + a_start, c_end + a_start
    d_start, d_end = d_start + a_end, d_end + a_end

    return calculate_max(nums, (a_start,a_end), (b_start,b_end), (c_start, c_end), (d_start, d_end))

def max_sub_array(nums: list[int]) -> int:
    """Divide and conquer algorithm in O(n*log(n)) time to find max sub array in list of ints"""
    n = len(nums)
    if n == 1:
        return nums[0]
    start, end = recursive_max_subarray(tuple(nums))
    return sum(nums[start: end])


    
def linear_max_sub_array(nums: list[int]) -> int:
    """Linear time algorithm to calculate max subarray"""
    i = current_sum = 0  
    max_sum = float('-inf')
    while i < len(nums):
        num = nums[i]
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0: # start again 
            current_sum = 0   
        i += 1
    return max_sum

   

print(linear_max_sub_array(nums_5))
    
