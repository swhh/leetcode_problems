from collections import defaultdict

"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.
"""


def get_places(s, t):
    places = defaultdict(set)
    letters = set(t)
    for i in range(len(s)):
        if s[i] in letters:
            places[s[i]].add(i)
    return places


def num_distinct(s, t, index=0, places=None):
    if not t or len(t) > len(s):
        return 0
    if len(t) == 1:
        if places:
            return sum(1 for i in places[t] if i >= index)
        return s.count(t)
    if s == t:
        return 1
    total = 0
    if not places:
        places = get_places(s, t)
    for i in places[t[0]]:
        if i >= index:
            total += num_distinct(s[i - index + 1:], t[1:], index=i + 1, places=places)
    return total


print(num_distinct("rabbbit", "b"))
