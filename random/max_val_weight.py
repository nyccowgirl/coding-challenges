"""Cake Thief. You are a master cake thief and have broken into a cake vault.
Each cake has a weight and a monetary value stored in a tuple, For example:
# weights 7 kilograms and has a value of 160 pounds.
(7, 160)

You brought a duffel bag that can hold a limited weight and you want to make off
with the most valuable haul.

Write a function max_duffel_bag_value() that takes a list of cake type tuples
and a weight capacity and returns the maximum monetary value the duffel bag can
hold.

For example:

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20
max_duffel_bag_value(cake_tuples, capacity)
# returns 555 - (6 of the middle cake types and 1 of the last cake type).

Weights and values can be any non-negative integers."""


def max_duffel_bag_value(cake_tuples, capacity):
    """Returns max value duffel bag can hold.

    >>> max_duffel_bag_value([(7, 160), (3, 90), (2, 15)], 20)
    555
    """

    val_weight = []

    for i in cake_tuples:
        val_weight[i] = (i, (cake_tuples[i][1] / cake_tuples[i][0]))

    # max_idx = val_weight.index(max(val_weight))
    sorted(val_weight, key=lambda x: x[1])

    weight = 0
    value = 0

    for i, item in enumerate(val_weight):
        while weight <= capacity:
            if (capacity - weight) >= cake_tuples[item[0]][0]:
                weight += cake_tuples[item[0]][0]
                value += cake_tuples[item[0]][1]
            else:
                break

    return value


################################################################################

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
