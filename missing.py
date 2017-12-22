"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8

    """

    # nums_set = set(x + 1 for x in range(max_num))

    nums_set = set(nums)

    for i in range(max_num + 1):
        if i + 1 not in nums_set:
            return i + 1


#SOLUTION FILE:

# def missing_number_scan(nums, max_num):
#     """Given a list of numbers 1...max_num, find which one is missing.

#     *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
#     *max_num*: Largest potential number in list

#     >>> missing_number_scan([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
#     8
#     """

#     # 1st solution: Initial solution: keep track of what you've
#     #               seen in a separate list

#     seen = [False] * max_num

#     for n in nums:
#         seen[n - 1] = True

#     # The False value is the one we haven't seen

#     return seen.index(False) + 1

# This solution is O(n) and requires additional storage.


# def missing_number_sort(nums, max_num):
#     """Given a list of numbers 1...max_num, find which one is missing.

#     *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
#     *max_num*: Largest potential number in list

#     >>> missing_number_sort([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
#     8
#     """

#     # 2nd solution: if we can't create another data structure
#     #               sort and scan for missing number

#     nums.append(max_num + 1)
#     nums.sort()
#     last = 0

#     for i in nums:
#         if i != last + 1:
#             return last + 1
#         last += 1

#     raise Exception("None are missing!")


# For a simple O(n log n) solution, you could sort the numbers first, then scan them to see which one is missing

# def missing_number_sum(nums, max_num):
#     """Given a list of numbers 1...max_num, find which one is missing.

#     *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
#     *max_num*: Largest potential number in list

#     >>> missing_number_sum([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
#     8
#     """

#     # 3rd solution: find missing number by comparing expected sum vs actual

#     expected = sum(range(max_num + 1))

#     # Alternatively, there's a math formula that finds the sum of 1..n
#     # https://en.wikipedia.org/wiki/Arithmetic_progression#Sum
#     #
#     # expected = ( n + 1 ) * ( n / 2 )
#     #

#     return expected - sum(nums)

# This solution is O(n) and requires no additional lists.


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"
