"""Given a string s, return the longest palindromic substring in s."""
from functools import cache
s_one = "babad"
s_two = "cbbd"
s_three = "ddddd"
s_four = "abbafdsgagas"
s_five = "sfsdafabbbba"
s_six = s_five * 6
s_seven = 'abba'

@cache
def longest_palindrome(s):
    n = len(s)
    if n <= 1:
        return s
    if s[0] == s[n - 1]:
        result = longest_palindrome(s[1:n - 1])
        if result == s[1: n - 1]:
            return s
        
    return max(longest_palindrome(s[1:]),longest_palindrome(s[:n - 1]), key=lambda x: len(x))
    
    

print(longest_palindrome(s_one))


