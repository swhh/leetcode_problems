"""Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n."""

def count_digit_one(n):
    """Count all ones in all numbers less than or equal to n"""
    if not n:
        return 0
    num_str = str(n)
    length = len(num_str)
    if length == 1:
        return 1
    one_digit_less_count = (length - 1) * 10 ** (length - 2) # count all ones for numbers with one fewer digit
    count = one_digit_less_count
    current_digit_count = count_digit_one(int(num_str[1:]))  # add ones for numbers with n's highest digit assuming highest digit is not one
    count += (current_digit_count)
    if num_str[0] == '1': # if lead digit is one
        count += (int(num_str[1:]) + 1)
    else:   # if lead digit is not one
        count += (one_digit_less_count * (int(num_str[0]) - 1)) 
        count += (int('9' * (length - 1)) + 1) # add extra ones for when lead digit is one
    return count
    
def count_ones_brute_force(n):
    count = 0
    for i in range(1, n + 1):
        total = sum(1 for char in str(i) if char == '1')
        count += total
    return count

print(count_ones_brute_force(100), count_digit_one(100))