"""Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram."""
from itertools import combinations, chain
heights = [2,1,5,6,2,3]
heights2 = [2,4]
heights3 = [2,2,5,6,2,3]
heights4 = [2,1,5,6,2,3,2,2]

def area(array):
    return min(array) * len(array)

def largest_rectangle_area_brute_force(heights):
    """Brute force algo to find max rectangular area in heights"""
    return max((max(area(heights[i:i + j + 1]) for j in range(len(heights) - i)) for i in range(len(heights))))


def subarrays_without_min_num(heights, min_num):
    """Find indices of subarrays in heights that do not include min_num"""
    n = len(heights)
    min_places = (i for i in range(n) if heights[i] == min_num)
    sub_arrays = []
    start = 0
    for i in min_places:
        if i - start > 0:
            sub_arrays.append((start, i))
        start = i + 1
    if start < n:
        sub_arrays.append((start, n))    
    return sub_arrays

def next_is_smaller(heights):
    next_smaller = {i for i in range(len(heights) - 1) if heights[i] > heights[i + 1]}
    next_smaller.add(len(heights) - 1) # include final height
    return next_smaller

def previous_is_smaller(heights):
    return {i for i in range(1, len(heights)) if heights[i - 1] < heights[i]}


def largest_rectangle_area(heights):
    """Find largest rectangular area in heights by only looking at subarrays without the min 
    and that start and end with heights bigger than their neighbours"""
    min_num = min(heights)
    min_max_area = min_num * len(heights) # min max area
    candidate_locations = subarrays_without_min_num(heights, min_num) # find subarrays that do not include heights' min num
    next_smaller, previous_smaller = next_is_smaller(heights), previous_is_smaller(heights)
    def candidate_substrings(start, end):
        return (heights[i: j + 1] for i, j in combinations(range(start, end), 2) if i in previous_smaller and j in next_smaller)
    substrings = (candidate_substrings(start, end) for start, end in candidate_locations) # find substrings where start and end bigger than non-substring neighbours
    return max(min_max_area, max(area(substring) for substring in chain.from_iterable(substrings))) # max area is either whole array or in subarray excl min num



print(largest_rectangle_area(heights3))
