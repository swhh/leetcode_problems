from collections import Counter

def min_window_substring(strArr): 
  n_string, k_string = strArr
  if k_string in n_string:
    return k_string
  shortest = n_string
  n = len(n_string)
  for i in range(n):
    remaining = Counter(k_string)
    j = i
    while j < n:
      char = n_string[j]
      if remaining.get(char, None):
        remaining[char] -= 1
        if not any(remaining.values()):
          shortest = n_string[i: j + 1] if (j - i + 1) < len(shortest) else shortest
          break
      j += 1
  return shortest