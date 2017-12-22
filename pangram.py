"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True

    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""

    sent_set = set(sentence.lower())

    alpha = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z'])

    for char in alpha:
        if char in sent_set:
            continue
        else:
            return False

    return True


# SOLUTION FILE:

# def is_pangram(sentence):
#     """Given a string, return True if it is a pangram, False otherwise."""

#     # START SOLUTION

#     used = {char.lower() for char in sentence if char.isalpha()}
#     return len(used) == 26


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
