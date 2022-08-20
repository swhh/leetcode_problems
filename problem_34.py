# find first and last positions of an element in a sorted array in log(n) time

test_nums = [5, 7, 7, 7, 8, 8, 8, 8, 10, 11]


def search_range(nums, target):
    """Return list of first and last positions of target in sorted nums in log(n) time"""
    n = len(nums)
    if n == 0:
        return [-1, -1]
    if n == 1:
        if nums[0] == target:
            return [0, 0]
        return [-1, -1]
    mid_point = n // 2
    if target < nums[mid_point]:
        return search_range(nums[:mid_point], target)
    elif target > nums[mid_point]:
        lower, higher = search_range(nums[mid_point + 1:], target)
        if lower == -1:
            return [lower, higher]
        return [lower + mid_point + 1, higher + mid_point + 1]
    else:
        first_half = search_range(nums[:mid_point], target)
        second_half = search_range(nums[mid_point + 1:], target)
        lower = first_half[0] if first_half[0] > -1 else mid_point
        higher = second_half[1] + mid_point + 1 if second_half[1] > -1 else mid_point
        return [lower, higher]


print(search_range(test_nums, 8))



