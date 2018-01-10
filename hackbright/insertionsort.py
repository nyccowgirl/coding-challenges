"""Given a list, sort it using insertion sort.

For example::

    >>> from random import shuffle
    >>> alist = range(1, 11)

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""

    i = len(alist) - 1

    def insert_rec(alist, i):

        if i > 0:
            insert_rec(alist, i - 1)
            x = alist[i]
            j = i - 1

            while j >= 0 and alist[j] > x:
                alist[j + 1] = alist[j]
                j -= 1

            alist[j + 1] = x

        return alist

    return insert_rec(alist, i)


# SOLUTION FILE:

# def insertion_sort(alist):
#     """Given a list, sort it using insertion sort."""

#     # START SOLUTION

#     for i in range(1, len(alist)):
#         # For each item in the list, starting at the second, find out
#         # how far to the left it goes--as soon as we find a number
#         # smaller than it, we've gone far enough back

#         j = i - 1
#         while j >= 0 and alist[j] > alist[i]:
#             j -= 1
#         j += 1

#         # now j in the position where we should move i to, and we should
#         # put everything over to the right after that

#         if j != i:
#             alist[j:i + 1] = alist[i:i + 1] + alist[j:i]

#     return alist


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE SORTING!\n"
