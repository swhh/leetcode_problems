"""Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation."""
from functools import cache
s1 = "applepenapple"
wordDict1 = ["apple","pen"]
s2 = "catsandog"
wordDict2 = ["cats","dog","sand","and","cat"]
s3 = "catsanddog"


def word_break(s, word_dict):
    @cache
    def recursive_word_break(string):
        if not string:
            return True
        candidates = list(filter(lambda x: string.startswith(x), word_dict))
        if not candidates:
            return False
        return any(map(recursive_word_break, (string[len(word):] for word in candidates)))
    return recursive_word_break(s)

print(word_break(s2, wordDict2))


    

