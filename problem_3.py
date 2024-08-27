"""Given a string s, find the length of the longest 
substring
 without repeating characters."""


s = "pwwkew"
t = "abcabcbb"
k = 'bbbbbb'
l = "ckilbkd"
m = "tmmzuxt"
n = "jbpnbwwd"
o = "anviaj"
edge = " "

def length_of_longest_substring(s: str) -> int:
    """Returns longest substring with no repeat chars in s in O(N) time"""
    char_place_last_seen = {
        char: -1 for char in set(s)
    }
    i = j = 0
    longest = 0
    while i < len(s):
        char = s[i]
        if j <= char_place_last_seen[char] < i: # if already seen in current substring j: i
            if len(s[j: i]) > longest:
                longest = len(s[j:i])
            j = char_place_last_seen[char] + 1  # update start of substring j to be after repeat char
        if i == len(s) - 1:                     # if at end of string
            if len(s[j: i + 1]) > longest:
                longest = len(s[j:i + 1])
        char_place_last_seen[char] = i         
        i += 1
    return longest

print(length_of_longest_substring(s))





