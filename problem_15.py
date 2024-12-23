"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""
from bisect import bisect_left

nums = [-1,0,1,2,-1,-4]
sorted_nums = [-4, -1, -1, 0, 1, 2]

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None

def three_sum(nums):
    if min(nums) > 0:
        return []
    if max(nums) < 0:
        return []
    nums = sorted(nums)
    triplets = []
    n = len(nums)
    i = 0
    j = n - 1
    turn = True
    seen = set()
    while i + 1 < j and nums[i] < 0 and nums[j]:
        two_sum = nums[i] + nums[j]
        k = index(nums[i + 1: j], -two_sum)
        if k is not None:
            tup = (nums[i], nums[k + i + 1], nums[j])
            if tup not in seen:
                seen.add(tup)
                triplets.append(list(tup))
        if turn:
            i += 1
        else:
            j -= 1
        turn = not turn
    return triplets


print(three_sum(nums))
    


    
    