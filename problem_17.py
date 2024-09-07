"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters."""
from string import ascii_lowercase
from itertools import product

digits = "23"

numbers_to_letters_dict = {
    str(num): ascii_lowercase[(num - 2) * 3: (num - 2) * 3 + 3] for num in range(2, 7)
}
numbers_to_letters_dict['7'] = ascii_lowercase[15: 19]
numbers_to_letters_dict['8'] = ascii_lowercase[19:22]
numbers_to_letters_dict['9'] = ascii_lowercase[22:]


def letter_combinations(digits:str) -> list[str]:
    letter_groups = (numbers_to_letters_dict[digit] for digit in digits)
    return list(''.join(combo) for combo in product(*letter_groups))

print(letter_combinations(digits))




