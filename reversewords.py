"""Reverse word order, keeping spaces.

As a simple case, an empty string returns an empty string:

    >>> rev("")
    ''

A simple word is also the same:

    >>> rev("hello")
    'hello'

Here, we reverse the order of the words, preserving the space between:

    >>> rev("hello world")
    'world hello'

Here, we reverse the worlds, preserving space---so it it should start with
the 3 spaces that came after world, etc:

    >>> rev(" hello  world   ")
    '   world  hello '

"""


def rev(s):
    """Reverse word-order in string, preserving spaces."""

    lst = []

    i = 0
    new_s = ''

    while i <= len(s):
        idx = s.find(' ')
        if idx != -1:
            lst.append(s[i:idx])
            i = idx
        else:
            lst.append(s[i:])

    for item in reversed(lst):
        new_s = new_s + item

    return new_s


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB! ***\n"
