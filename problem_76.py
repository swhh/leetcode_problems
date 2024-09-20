"""Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique."""
from collections import Counter
from itertools import combinations
s = "ADOBECODEBANC"
t = "ABC"


def min_window(s, t):
    """Find minimum substring in s that contains t"""
    t_dict = Counter(t)
    chars = set(t)

    def issubstring(string):
        s_dict = Counter(string)
        return all(s_dict.get(char, 0) >= t_dict.get(char, 0) for char in chars)
    
    if not issubstring(s):
        return ''  
    n, k = len(s), len(t) 
    min_window = s
    positions = set(i for i in range(n) if s[i] in chars)
    possible_substrings = ((s[i: j + 1] for i, j in combinations(positions, 2) if j - i >= k)) # all substrings that start and end with some chars and are at least length k
    for substring in possible_substrings:
        if len(substring) < len(min_window) and issubstring(substring):
            min_window = substring
    return min_window


print(min_window(s, t))

            






        

            