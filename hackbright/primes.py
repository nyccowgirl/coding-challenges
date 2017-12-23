"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    prime = []

    nums = range(2, 100)
    for i in range(2, 8):
        nums = filter(lambda x: x == i or x % i, nums)

    while count > len(prime):
        prime.append(nums.pop(0))

    return prime


# SOLUTION FILE:

#     def is_prime(num):
#     """Is num a prime number?

#     num will always be a positive integer.

#     >>> is_prime(0)
#     False

#     >>> is_prime(1)
#     False

#     >>> is_prime(2)
#     True

#     >>> is_prime(3)
#     True

#     >>> is_prime(4)
#     False

#     >>> is_prime(7)
#     True

#     >>> is_prime(25)
#     False
#     """

#     assert num >= 0, "Num should be a positive integer!"

#     # definition: 0 and 1 are not prime
#     if num < 2:
#         return False

#     # definition: 2 is prime
#     if num == 2:
#         return True

#     # if it's divisible by 2, it's not prime
#     # (We do this as a special case, so that after this we can check
#     # only odd numbers -- all even numbers are divisible by 2)
#     if num % 2 == 0:
#         return False

#     # see if number is prime -- we'll do this by checking
#     # to see if there's any odd number 3 .. sqrt(num)
#     # that evenly divides num (why square root? think about it!)

#     n = 3

#     while n * n <= num:
#         if num % n == 0:
#             return False
#         # Go to next odd number
#         n += 2

#     return True
# it treats 2 as a special case (2 is a prime number) and multiples of 2 are not.
# it then only has to check whether the number is divisible by prime numbers
# it only checks up to sqrt(num) – why? Think about it!
# We then made a primes function:

# def primes(count):
#     """Return count number of prime numbers, starting at 2."""

#     # START SOLUTION

#     primes = []
#     num = 2

#     while count > 0:

#         if is_prime(num):
#             primes.append(num)
#             count -= 1

#         num += 1

#     return primes


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
