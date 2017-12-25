"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""

from operator import add, sub, mul, div, mod, xor


def calc(s):
    """Evaluate expression."""

    s = s.split(' ')
    operator = {'+': add, '-': sub, '*': mul, '/': div, '%': mod, '^': xor}

    while s:
        if s[-1].isdigit():
            a = int(s.pop())
            if s[-1].isdigit():
                b = int(s.pop())
                result = operator[s.pop()](b, a)
            else:
                result = operator[s.pop()](a, result)

    return result


# SOLUTION FILE:

# def calc(s):
#     """Evaluate expression."""

#     # START SOLUTION

#     # Convert to list of tokens
#     #
#     # For example: "+ 1 2" -> ["+", "1", "2"]
#     tokens = s.split()

#     # Start with right-most number (in a well-formed polish notation
#     # expression, it must ALWAYS end with a number)
#     operand2 = int(tokens.pop())

#     while tokens:
#         # Grab the right-most number
#         operand1 = int(tokens.pop())

#         # Grab the right-most operand
#         operator = tokens.pop()

#         # Do the math and use the result as our "right-hand" value
#         # for the next time we do math

#         if operator == "+":
#             operand2 = operand1 + operand2

#         elif operator == "-":
#             operand2 = operand1 - operand2

#         elif operator == "*":
#             operand2 = operand1 * operand2

#         elif operator == "/":
#             operand2 = operand1 / operand2

#     # The final result is the result of the most recent operation

#     return operand2


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n"
