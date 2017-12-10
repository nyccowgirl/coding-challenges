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


# def rev(s):
#     """Reverse word-order in string, preserving spaces."""

#     # START SOLUTION

#     # A token is either a word or a series of spaces --- so,
#     # for example, we would turn "    hello kitty "
#     # into the tokens = ["    ", "hello", " ", "kitty", " "].

#     # The current token we're building up.
#     current_token = ''

#     # List of tokens found so far
#     tokens = []

#     # True when we're collecting spaces
#     # False when we're collecting non-spaces
#     in_space = None

#     for letter in s:

#         if letter == " ":
#             if not in_space:
#                 # Switch from space -> letter: add the current
#                 # (letter-y) token and restart our current_token
#                 tokens.append(current_token)
#                 current_token = ''
#                 in_space = True

#         else:
#             if in_space:
#                 # Switch from letter -> space: add the current
#                 # (space-y) token and restart our current_token
#                 tokens.append(current_token)
#                 current_token = ''
#                 in_space = False

#         # Add this letter to our current_token
#         current_token += letter

#     # Finished, add the ending token to our list
#     tokens.append(current_token)

#     # Reverse tokens as string ['hi', ' ', 'world'] -> "world hi"
#     return ''.join(reversed(tokens))


# def rev2(s):
#     """Reverse word-order in string, preserving spaces."""

#     # Splitting on space will give us both the words and empty strings - there
#     # will be an empty string each time two spaces are next to each other
#     #
#     # Then we just reverse the order and put the spaces back in

#     return " ".join(reversed(s.split(" ")))


# import re

# def rev(s):
#     """Turn "    hello  kitty " -> " kitty  hello   "."""

#     tokens = re.findall(" +|[^ ]+", s)
#     return "".join(reversed(tokens))


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB! ***\n"
