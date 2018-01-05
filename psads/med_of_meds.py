"""Given a list of numbers in random order, write an algorithm that works in
O(nlog(n)) to find the kth smallest number in the list."""

from heapq import nsmallest


def k_small(k, alist):
    """Determine kth smallest number in a list.

    >>> k_small(3, [4, 8, 2, 3, 9, 11])
    4
    """

    return nsmallest(k, alist)


# ALTERNATIVE SOLUTION:

# def k_small(k, alist):
#     new_lst = sorted(alist)

#     x = new_lst[k - 1]

#     return k


# Improve solution to be linear - study median of medians algorithm
# https://brilliant.org/wiki/median-finding-algorithm/

# def median_of_medians(k, alist):
#     """Implements median of medians algorithm not accounting for dupes.
#     >>> a = [1, 2, 3, 4, 5, 1000, 8, 9, 99]
#     >>> b = [1, 2, 3, 4, 5, 6]
#     >>> median_of_medians(a, 0)
#     1

#     >>> median_of_medians(a, 7)
#     99

#     >>> median_of_medians(b, 4)
#     5
# """

#     # Divide list into sublists of len 5
#     sublists = [alist[i:i + 5] for i in range(0, len(alist), 5)]

#     # Alternate code
#     # sublists = []
#     # idx = 0

#     # while (idx + 5) < (len(alist) - 1):
#     #     sublists.append(alist[idx:idx + 5])
#     #     idx += 5

#     # sublists.append(alist[idx:])

#     medians = [sorted(sublist)[len(sublist) / 2] for sublist in sublists]

#     # Alternate code

#     # medians = []

#     # for sublst in new_lst:
#     #     medians.append(select(sublst, int((len(sublst) - 1) / 2)))

#     if len(medians) <= 5:
#         pivot = sorted(medians)[len(medians) / 2]
#     else:
#         # The pivot is the median of the medians
#         pivot = median_of_medians(medians, len(medians) / 2)

#     # Partitioning step
#     low = [i for i in alist if i < pivot]  # To find k highest, swap high/low
#     high = [i for i in alist if i > pivot]

#     j = len(low)

#     if k < j:
#         return median_of_medians(low, k)
#     elif k > j:
#         return median_of_medians(high, k - j - 1)
#     else: # pivot = j
#         return pivot


# def median_of_medians(k, alist):
#     """Implements median of medians algorithm accounting for dupes."""

#     # For small list, sorting and k smallest is insignificant so similar to linear
#     if len(alist) < 10:
#         alist.sort()
#         return alist[k]

#     # Divide list into sublists of len 5
#     sublists = [alist[i:i + 5] for i in range(0, len(alist), 5)]
#     medians = [sorted(sublist)[len(sublist) / 2] for sublist in sublists]

#     pivot = select(medians, int((len(medians) - 1 ) / 2))

#     low = []
#     same = []
#     high = []

#     for i in alist:
#         if i < pivot:
#             low.append(i)
#         elif i > pivot:
#             high.append(i)
#         else:
#             same.append(i)

#     if j < len(low):
#         return select(low, k)
#     elif j < len(same) + len(low):
#         return same[0]
#     else:
#         return select(high, k - len(low) - len(same))


################################################################################

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
