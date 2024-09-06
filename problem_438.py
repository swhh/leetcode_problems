"""Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""
from itertools import permutations
s = "cbaebabacd"
p = "abc"


def find_anagrams(s, p):
    """Return all indexes in s which are start of anagrams of p in s"""
    permutes = set(''.join(permute) for permute in permutations(p))
    return [i for i in range(len(s) - len(p)) if s[i: i + len(p)] in permutes]

print(find_anagrams(s, p))






                    

