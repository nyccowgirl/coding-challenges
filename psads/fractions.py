"""
Create Fraction class with operators that displays the results in fraction format.

>>> x = Fraction(1, 3)
>>> y = Fraction(1, 5)
>>> print x + y
8/15

>>> print x == y
False

>>> print x - y
2/15

>>> print x * y
1/15

>>> print x / y
5/3

>>> x > y
True

>>> x < y
False
"""


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):

        return str(self.num) + '/' + str(self.den)

    def show(self):

        print self.num + '/' + self.den

    def __add__(self, otherfraction):
        newnum = ((self.num * otherfraction.den) +
                  (self.den * otherfraction.num))
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __sub__(self, otherfraction):
        newnum = ((self.num * otherfraction.den) -
                  (self.den * otherfraction.num))
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __div__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum


################################################################################

if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
