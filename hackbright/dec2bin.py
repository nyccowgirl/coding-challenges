"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin_backwards(0)
    '0'

    >>> dec2bin_backwards(1)
    '1'

    >>> dec2bin_backwards(2)
    '10'

    >>> dec2bin_backwards(4)
    '100'

    >>> dec2bin_backwards(15)
    '1111'

For example, using our alternate solution::

    >>> dec2bin_forwards(0)
    '0'

    >>> dec2bin_forwards(1)
    '1'

    >>> dec2bin_forwards(2)
    '10'

    >>> dec2bin_forwards(4)
    '100'

    >>> dec2bin_forwards(15)
    '1111'

"""


def dec2bin_backwards(num):
    """Convert a decimal number to binary representation."""

    lst = []

    new_num = num

    binary = ''

    if new_num == 0:
        binary = '0'
    else:
        while new_num > 0:
            remainder = new_num % 2
            lst.append(str(remainder))
            new_num = new_num / 2

        binary = ''.join(reversed(lst))

    return binary


def dec2bin_forwards(num):

    # lst = [int(x) for x in str(num)]
    out = ''

    # Figure out how many bits this will have
    num_bits = 1

    while 2 ** num_bits <= num:
        num_bits += 1

    for position in range(num_bits - 1, -1, -1):

        if 2 ** position <= num:
            num -= 2 ** position
            out += '1'

        else:
            out += '0'

    return out


# SOLUTION FILE:

# One solution:

# def dec2bin_backwards(num):
#     """Convert a decimal number to binary representation."""

#     # Work backwards, finding the least-significant-bit first,
#     # moving up to the most-significant bit.
#     #
#     # At the end, print the list of bits reversed

#     result = []
#     place = 0

#     while place == 0 or num >= 2 ** place:

#         if num % (2 ** (place + 1)):
#             num -= 2 ** place
#             result.append("1")

#         else:
#             result.append("0")
#         place += 1

#     return "".join(reversed(result))
# Another solution:

# def dec2bin_forwards(num):
#     """Convert a decimal number to binary representation."""

#     # Work forwards. Figure out how many bits there will be,
#     # so you know what power of two the left-most bit will have.
#     #
#     # Calculate each bit, from most-significant to least, adding
#     # to a string answer.

#     out = ""

#     # Figure out how many bits this will have
#     num_bits = 1

#     while 2 ** num_bits <= num:
#         num_bits += 1

#     for position in range(num_bits - 1, -1, -1):

#         if 2 ** position <= num:
#             num -= 2 ** position
#             out += "1"

#         else:
#             out += "0"

#     return out

# A third possibility:

# def dec2bin_division(num):
#     """Convert a decimal number to binary representation."""

#     # Work from right to left, from 1's place up to 2^n's place
#     #
#     # Use mod to tell you if each digit should be a zero or a one
#     #
#     # Then divide by two to move onto the next digit

#     if num == 0:
#         return "0"

#     reversed_digits = []

#     while num > 0:
#         # num % 2 will be 0 or 1
#         reversed_digits.append(str(num % 2))
#         num /= 2

#     return "".join(reversed(reversed_digits))


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
