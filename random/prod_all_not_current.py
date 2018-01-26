from operator import mul


def products_all_nums_but_current(lst):
    """Given a list of integers you want to find the product of all the
    integers except the integer at the current index.
    Write a function that takes a list of integers and returns a
    list of products.

    DO NOT USE DIVISION

    >>> products_all_nums_but_current([1, 2, 3, 4])
    [24, 12, 8, 6]

    >>> products_all_nums_but_current([2, 4, 0, 1])
    [0, 0, 8, 0]

    >>> products_all_nums_but_current([3, 3, 3])
    [9, 9, 9]

    >>> products_all_nums_but_current([])
    []

    >>> products_all_nums_but_current([1])
    [1]
    """

    prod_lst = []

    if len(lst) <= 1:
        return lst

    for i in range(len(lst)):
        if i == 0:
            prod_lst.append(reduce(mul, lst[i + 1:]))
        elif i == (len(lst) - 1):
            prod_lst.append(reduce(mul, lst[:-1]))
        else:
            prod_lst.append(reduce(mul, lst[:i]) * reduce(mul, lst[i + 1:]))

    return prod_lst


#  ALTERNATE SOLUTION:
# def products_all_nums_but_current(lst):
#     """Linear runtime"""

#     if len(lst) <= 1:
#         return lst

#     # Create list with items with length of original list
#     prod = [1] * len(lst)
#     n = len(prod)

#     # For each integer, calculate product of all integers before it
#     back = 1
#     for i in range(0, n):
#         prod[i] = prod[i] * back
#         back = back * lst[i]

#     # For each integer, multiply product of all integers after it to existing
#     # calculation in order to determine product of all integers in list except
#     # for current integer
#     front = 1
#     for i in range(n - 1, -1, -1):
#         prod[i] = prod[i] * front
#         front = front * lst[i]

#     return prod


################################################################################

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
