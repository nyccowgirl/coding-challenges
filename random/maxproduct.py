"""Given list of integers, return the largest possible product of 3 numbers.

>>> max_product([3, 2, 1, 3, 4, 6, 5])
120

>>> max_product([-9, 2, 1, -7, 8, 7])
504

>>> max_product([-1, -5, 0, -200, 1])
1000

>>> max_product([-6, -5, -4, -3, -2, -1])
-6

>>> max_product([-100, -4, 0, -500])
0

"""

from heapq import nlargest, nsmallest
from operator import mul


def max_product(lst):
    """Given list of integers, return largest possible product of 3 numbers."""

    if len(lst) < 3:
        raise ValueError('list does not have 3 numbers')
    elif len(lst) == 3:
        max_product = reduce(mul, lst)
    else:
        top_three = nlargest(3, lst)
        bottom_two = nsmallest(2, lst)
        top_one = nlargest(1, lst)

        # Max product is either top 3 positive integers or top 1 positive integer
        # and bottom 2 negative integers
        a = reduce(mul, top_three)
        b = reduce(mul, bottom_two) * top_one[0]

        if a > b:
            max_product = a
        else:
            max_product = b

    return max_product


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. YIPPEE!\n"
