"""The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]"""

from collections import Counter
LENGTH = 10

s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s2 = "AAAAAAAAAAAAA"

def find_repeated_dna_sequences(s):
    sequences = (s[i:i + LENGTH] for i in range(len(s) - LENGTH))
    counter = Counter(sequences)
    return list(seq for seq, num in counter.items() if num > 1)

print(find_repeated_dna_sequences(s2))