"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    dist_lst = []

    for i in range(num_holes):
        if i in cafes:
            dist_lst.append(0)
        else:
            min_dist = num_holes
            for item in cafes:
                if abs(i - item) < min_dist:
                    min_dist = abs(i - item)
            dist_lst.append(min_dist)

    return max(dist_lst)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
