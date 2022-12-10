from functools import cache

"""Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')"""


@cache
def min_distance(word1, word2):
    """Return minimum number of operations required to convert word1 into word2"""
    if word1 == word2:  # base cases
        return 0
    if not word1 and word2:
        return len(word1) + len(word2)
    dist = len(word1) - len(word2)
    if dist < 0:  # if word2 is bigger, swap words to reduce to first case
        word1, word2 = word2, word1
    if word1[0] == word2[0]:
        return min_distance(word1[1:], word2[1:])
    if dist:
        return 1 + min(min_distance(word1[1:], word2[1:]), min_distance(word1[1:], word2))
    return 1 + min(min_distance(word1[1:], word2[1:]), min_distance(word1[1:], word2), min_distance(word1, word2[1:]))


print(min_distance('intention', 'execution'))

