"""Calculate possible change from combinations of dimes and pennies.

Given an infinite supply of dimes and pennies, find the different
amounts of change can be created with exact `num_coins` coins?

For example, when num_coins = 3, you can create:

    3 = penny + penny + penny
   12 = dime + penny + penny
   21 = dime + dime + penny
   30 = dime + dime + dime

For example:

    >>> coins(0) == {0}
    True

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True


Let's make sure it works when we can spend over 10 pennies::

    >>> coins(11) == {65, 101, 38, 74, 11, 110, 47, 83, 20, 56, 92, 29}
    True

"""


def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """

    change = set()
    iterator = 0

    while num_coins >= 0:
        change.add((num_coins * 1) + (iterator * 10))
        num_coins -= 1
        iterator += 1

    return change


# ALTERNATIVE SOLUTION:


# def coins(num_coins):
#     """Find change from combinations of `num_coins` of dimes and pennies.

#     This should return a set of the unique amounts of change possible.
#     """

#     change = set()

#     def adj_coins(num, result=0, change):
#         """Calculates total result based on recursion."""

        # print ('add_coins was called with num_coins_remaining={},
        #        total_so_far={}, results_set={}'.format(left, total, results))

#         if num == 0:
#             change.add(result)
#         else:
#             adj_coins(num - 1, result + 1, change)
#             adj_coins(num - 1, result + 10, change)

#     adj_coins(num_coins, 0, change)

#     return change


# SOLUTION FILE:

# def add_coins(left, total, results):
#     """Add combos coins to total.

#     If this is the last time we can add coins, return change.

#     Otherwise, recursively call until that condition.

#         >>> results = set()
#         >>> add_coins(left=1, total=0, results=results)
#         >>> results == set([1, 10])
#         True
#     """

#     DIME = 10
#     PENNY = 1

#     if left == 0:
#         # Base Case
#         # We've added all the coins we're supposed to, so keep
#         # track of this total of change and stop recursing
#         results.add(total)
#         return

#     # Fork into two recursions, one adding a dime and another a penny
#     # For each, we'll have 1 fewer coin to add afterwards, so left -= 1
#     add_coins(left - 1, total + DIME, results)
#     add_coins(left - 1, total + PENNY, results)

# This is called by coins:

# coins.py
# def coins(num_coins):
#     """Find change from combinations of `num_coins` of dimes and pennies.

#     This should return a set of the unique amounts of change possible.
#     """

#     # START SOLUTION

#     results = set()

#     add_coins(left=num_coins, total=0, results=results)

#     return results

# Non-Recursive Solution
# There’s an easier way, though.

# Imagine that you have 5 coins to spend. If you use three of them as dimes, you know that you’ll have exactly two left for use as pennies. So you can simply calculate 3 × 10 + 2 × 1 = 32.

# coins.py
# def coins_simpler(num_coins):
#     """Find change from combinations of `num_coins` of dimes and pennies.

#     This should return a set of the unique amounts of change possible.

#         >>> coins_simpler(0) == {0}
#         True

#         >>> coins_simpler(1) == {1, 10}
#         True

#         >>> coins_simpler(2) == {2, 11, 20}
#         True

#         >>> coins_simpler(3) == {3, 12, 21, 30}
#         True

#         >>> coins_simpler(4) == {4, 13, 22, 31, 40}
#         True

#     Let's make sure it works when we can spend over 10 pennies::

#         >>> coins_simpler(11) == {65, 101, 38, 74, 11, 110, 47, 83, 20, 56, 92, 29}
#         True
#     """

#     results = set()

#     for ndimes in range(num_coins + 1):
#         npennies = num_coins - ndimes
#         results.add(ndimes * 10 + npennies)

#     return results


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAN TAKE THAT TO THE BANK!\n"
