"""You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, let expression, add expression, mult expression, or an assigned variable. Expressions always evaluate to a single integer.
(An integer could be positive or negative.)
A let expression takes the form "(let v1 e1 v2 e2 ... vn en expr)", where let is always the string "let", then there are one or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let expression is the value of the expression expr.
An add expression takes the form "(add e1 e2)" where add is always the string "add", there are always two expressions e1, e2 and the result is the addition of the evaluation of e1 and the evaluation of e2.
A mult expression takes the form "(mult e1 e2)" where mult is always the string "mult", there are always two expressions e1, e2 and the result is the multiplication of the evaluation of e1 and the evaluation of e2.
For this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally, for your convenience, the names "add", "let", and "mult" are protected and will never be used as variable names.
Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on the scope.
"""
ADD = 'add'
MULT = 'mult'
LET = 'let'


def parse_exp(expr):
    expr = expr[1:-1]
    parse, i = ([expr[:4]], 5) if expr.startswith(MULT) else ([expr[:3]], 4)
    while i < len(expr):
        exp = ''
        if expr[i] == ' ':
            i += 1
        if not expr[i:].startswith('('):
            while i < len(expr) and expr[i] != ' ':
                exp += expr[i]
                i += 1
        else:
            stack = ['(']
            i += 1
            exp += '('
            while stack:
                next_char = expr[i]
                if next_char == '(':
                    stack.append(next_char)
                if next_char == ')':
                    stack.pop()
                exp += next_char
                i += 1
        parse.append(exp)
    return parse


def is_variable(expr):
    if expr == ADD or expr == LET or expr == MULT:
        return False
    if expr[:1].isalpha() and expr.isalnum():
        return True


def evaluate(expr, values=None):
    if expr.isnumeric():
        return int(expr)
    if is_variable(expr):
        return values[expr]
    stack = parse_exp(expr)
    op = stack.pop(0)
    if not values:
        values = dict()
    if op == ADD:
        return evaluate(stack.pop(0), values=values.copy()) + evaluate(stack.pop(0), values=values.copy())
    if op == MULT:
        return evaluate(stack.pop(0), values=values.copy()) * evaluate(stack.pop(0), values=values.copy())
    while len(stack) > 1:
        exp = stack.pop(0)
        values[exp] = evaluate(stack.pop(0), values=values.copy())
    return evaluate(stack.pop(0), values=values.copy())


print(evaluate('(add 2 3)'))











