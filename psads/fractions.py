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
    """Determine common denominator in order to display lowest terms of fraction."""

    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n


class Fraction:
    """Creates fraction."""

    def __init__(self, top, bottom):
        """Instantiates fraction with numerator and denominator."""

        # Raises error if either top or bottom are not integers
        if not top.is_integer():
            raise TypeError('numerator must be an integer')
        elif not bottom.is_integer():
            raise TypeError('denominator must be an integer')

        # Converts fraction appropriately if denominator is negative integer so
        # that operators do not result in incorrect results
        if bottom < 0:
            if top < 0:
                top = abs(top)
                bottom = abs(bottom)
            else:
                top = -top
                bottom = abs(bottom)

        # Converts to lowest terms of fraction by calculating common denominator
        common = gcd(abs(top), abs(bottom))

        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        """Displays fraction object in string format."""

        return str(self.num) + '/' + str(self.den)

    def __repr__(self):
        """Displays fraction object."""

        return "<{}/{}>".format(self.num, self.den)

    def show(self):
        """Displays fraction."""

        print self.num + '/' + self.den

    def getNum(self):
        """Returns numerator."""

        return self.num

    def getDen(self):
        """Returns denominator."""

        return self.den

    def __add__(self, other):
        """Adds two fractions."""

        newnum = ((self.num * other.den) +
                  (self.den * other.num))
        newden = self.den * other.den

        return Fraction(newnum, newden)

    def __radd__(self, other):
        """Adds two fractions in case of TypeError in __add__ method."""

        if isinstance(other, int):
            other = Fraction(other, 1)

            return self.__add__(other)
        elif other == 0:
            return self
        else:
            return NotImplemented

    def __iadd__(self, other):
        """Adds two fractions."""

        return self.__add__(other)

    def __sub__(self, other):
        """Subtracts second fraction from the first."""

        newnum = ((self.num * other.den) -
                  (self.den * other.num))
        newden = self.den * other.den

        return Fraction(newnum, newden)

    def __mul__(self, other):
        """Multiplies two fractions."""

        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

    def __div__(self, other):
        """Divides first fraction by the second fraction."""

        newnum = self.num * other.den
        newden = self.den * other.num

        return Fraction(newnum, newden)

    def __eq__(self, other):
        """Validates if two fractions equal each other."""

        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __ne__(self, other):
        """Validates if two fractions are not equal each other."""

        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum != secondnum

    def __gt__(self, other):
        """Validates if first fraction is greater than second one."""

        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum

     def __ge__(self, other):
        """Validates if first fraction is greater than or equal to second one."""

        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum >= secondnum

    def __lt__(self, other):
        """Validates if first fraction is less than second one."""

        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __le__(self, other):
        """Validates if first fraction is less than or equal to second one."""

        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum <= secondnum

################################################################################

if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
