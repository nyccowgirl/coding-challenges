"""Split a string by splitter and return list of splits.

This should work like the built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implement that.

"""


def split(astring, splitter):
    """Split a string by splitter and return list of splits."""

    if not splitter:
        return [astring]

    lst = []

    # .find(splitter, optional index to start)

    i = 0  # index starting point

    while i <= len(astring):
        split_idx = astring.find(splitter, i)
        if split_idx != -1:
            lst.append(astring[i:split_idx])
            i = split_idx + len(splitter)
        else:
            lst.append(astring[i:])
            break

    return lst

    # version without .find(), include another variable to track index


# SOLUTION FILE:

# def split(astring, splitter):
#     """Split astring by splitter and return list of splits."""

#     # START SOLUTION

#     out = []
#     index = 0

#     while index <= len(astring):

#         curr_index = index
#         index = astring.find(splitter, index)

#         if index != -1:
#             out.append(astring[curr_index:index])
#             index += len(splitter)

#         else:
#             # couldn't find any more instances of splitter in astring
#             out.append(astring[curr_index:])
#             break

#     return out


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FINE SPLITTING!\n"
