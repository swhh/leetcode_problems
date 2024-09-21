"""Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval()."""
import operator

ADD = '+'
SUBTRACT = '-'
LEFT_PARENTHESIS = '('
RIGHT_PARENTHESIS = ')'
SPACE = ' '
op_dict = {ADD: operator.add, SUBTRACT: operator.sub}
OPS = {ADD, SUBTRACT}

s = "(11+(4+5+2)-3)+(-(3+4)+8)"
s2 = " 2-1 + 2 "
s3 =  "-(2 + 3)"
s4 = "(1+(4+5+2)-3)+(6+8)"
s5 = '-1'
s6 = '8 + (-(3 + 4))'
s7 = '-3 + 4'



def parse_exp(expr):
    """Parse arithmetic expression"""
    expr = ''.join(char for char in expr if char is not SPACE) # strip whitespace
    parse = []
    i = 0
    while i < len(expr):
        exp = ''
        if expr[i] in OPS: # is an operator
            exp = expr[i]
            i += 1
        elif expr[i].isnumeric(): # is a number
            while i < len(expr) and expr[i].isnumeric():
                exp += expr[i]
                i += 1
        else:  # is left parenthesis
            stack = [LEFT_PARENTHESIS]
            while True:
                i += 1
                next_char = expr[i]
                if next_char is LEFT_PARENTHESIS:
                    stack.append(next_char)
                elif next_char is RIGHT_PARENTHESIS:
                    stack.pop()
                    if not stack:
                        break
                exp += next_char
            i += 1
        parse.append(exp)
    return parse


def calculate(expr):
    """Recursively evaluate arithmetic expression"""
    if expr.isnumeric(): # base case
        return int(expr) 
    parse = parse_exp(expr)
    if parse[0] is SUBTRACT: # case where subtract is unitary operator
        result = -1 * calculate(parse[1])
        i = 2
    else:
        result = op_dict[parse[1]](calculate(parse[0]), calculate(parse[2]))
        i = 3
    for j in range(i, len(parse) - 1, 2):
        op, operand = parse[j], parse[j + 1]
        result = op_dict[op](result, calculate(operand))
    return result

print(calculate(s7))
