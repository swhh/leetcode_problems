"""Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them."""
from collections import Counter
s1 = "tree"
s2 = "Aabb"

def frequency_sort(s):
    counter = Counter(s)
    return ''.join(sorted(counter.elements(), reverse=True))

print(frequency_sort(s2))


    