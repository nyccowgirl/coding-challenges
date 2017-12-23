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


# ALTERNATIVE SOLUTION:

# def max_product(lst):

#     if len(lst) < 3:
#         raise ValueError('list does not have 3 numbers')
#     elif len(lst) == 3:
#         max_product = lst[0] * lst[1] * lst[2]
#     else:
#         # Do not need to remove last items (e.g., max_three or min_two) as it
#         # would result in error in situation where list has 4 numbers only.
#         max_one = max(lst)
#         lst.remove(max_one)
#         max_two = max(lst)
#         lst.remove(max_two)
#         max_three = max(lst)

#         min_one = min(lst)
#         lst.remove(min_one)
#         min_two = min(lst)

#         a = max_one * max_two * max_three
#         b = min_one * min_two * max_one

#         if a > b:
#             max_product = a
#         else:
#             max_product = b

#     return max_product


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. YIPPEE!\n"
