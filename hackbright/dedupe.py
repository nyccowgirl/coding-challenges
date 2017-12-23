"""Return new list from items with duplicates removed.

For example::

    >>> deduped([1, 1, 1])
    [1]

Keep items in the order where they first appeared::

    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]

A list with no duplicates would return the same::

    >>> deduped([1, 2, 3])
    [1, 2, 3]

This should return a *new* list, not mutate the existing
list::

    >>> a = [1, 2, 3]
    >>> b = deduped(a)
    >>> a == b
    True

    >>> a is b
    False

An empty list should return an empty list::

    >>> deduped([])
    []

"""


def deduped(items):
    """Return new list from items with duplicates removed."""

    dedupe = []

    for item in items:
        if item not in dedupe:
            dedupe.append(item)

    return dedupe


# SOLUTION FILE:

# result = []

# for char in items:
#     if char not in result:
#         result.append(char)

# return result

# This would work, but it would be O(n ** 2) runtime, since, for every item, we’d be looking in the result list (which is a linear operation).

# You can solve this by using a set to keep track of what’s seen, and using a list to hold the results:

# dedupe.py
# def deduped(items):
#     """Return new list from items with duplicates removed."""

#     # START SOLUTION

#     # keep track of items we've seen
#     seen = set()

#     # list to hold our answer
#     result = []

#     for item in items:
#         if item not in seen:
#             result.append(item)
#             seen.add(item)

#     return result


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE NO DUPE!\n"
