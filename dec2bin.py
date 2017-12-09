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
            out += "1"

        else:
            out += "0"

    return out



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
