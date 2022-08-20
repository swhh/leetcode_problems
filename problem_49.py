from collections import Counter

strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
test_output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]


def anagrams(str1, str2):
    return Counter(str1) == Counter(str2)


def group_anagrams(strs):
    """Group into anagrams"""
    output = []
    for string in strs:
        found = False
        for words in output:
            if anagrams(string, words[0]):
                words.append(string)
                found = True
                break
        if not found:
            output.append([string])
    return output
