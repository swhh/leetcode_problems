"""Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b."""

from functools import cache

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
t1 = "aabcc"
t2 = "dbbca" 
t3 = "aadbbbaccc"
r1 = "aabc"
r2 = "abad"
r3 = "aabadabc"
p1 ="aa"
p2 = "ab"
p3 = "aaba"

@cache
def common_prefix(str1, str2):
    return ''.join(a for a, b in zip(str1, str2) if a == b)

@cache
def is_interleave(s1, s2, s3, turn=None):
    if len(s3) != len(s1) + len(s2):
        return False # base case
    if s1 == s2 == s3 == '':
        return True  # base case
    if not s1 or not s2:
        left = s1 if s1 else s2
        return left == s3 # base case
    
    if turn is True:
        prefix = common_prefix(s1, s3) # s1 turn
        if prefix:
            return any(is_interleave(s1[i:], s2, s3[i:], turn= not turn) for i in range(1, len(prefix) + 1))
        return False
    elif turn is False:
        prefix = common_prefix(s2, s3) # s2 turn
        if prefix:
            return any(is_interleave(s1, s2[i:], s3[i:], turn= not turn) for i in range(1, len(prefix) + 1))
        return False
    else:
        prefix1, prefix2 = common_prefix(s1, s3), common_prefix(s2, s3) # try s1 or s2
        a = b = False
        if prefix1:
            turn = False
            a = any(is_interleave(s1[i:], s2, s3[i:], turn=turn) for i in range(1, len(prefix1) + 1))
        if prefix2:
            turn = True
            b = any(is_interleave(s1, s2[i:], s3[i:], turn=turn) for i in range(1, len(prefix2) + 1))
        return a or b


print(is_interleave(p1, p2, p3))

    
        

    
    
    