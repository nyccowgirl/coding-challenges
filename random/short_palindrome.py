def shortest_palendrome(astring):
    """ Given a string, convert it into a palindrome by adding characters to the
    beginning of it. Find and return the shortest possible palindrome you can
    make by performing this transformation.

    >>> shortest_palendrome('aacecaaa')
    'aaacecaaa'

    >>> shortest_palendrome('abcd')
    'dcbabcd'

    >>> shortest_palendrome('ab')
    'bab'

    >>> shortest_palendrome('')
    ''

    """

    if len(astring) <= 1:
        return astring
    elif astring == astring[::-1]:
        return astring
    else:
        return astring[-1] + shortest_palendrome(astring[:-1]) + astring[-1]

    return astring


################################################################################

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
