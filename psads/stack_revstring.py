"""Write a function revstring(mystr) that uses a stack to reverse the characters
in a string."""


class Stack:
    """Creates stack"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def revstring(mystr):
    """Utilize stack to reverse characters in a string.

    >>> revstring('hello')
    'olleh'

    >>> revstring('apple')
    'elppa'

    >>> revstring('x')
    'x'

    >>> revstring('1234567890')
    '0987654321'
    """

    rev_str = Stack()

    for ch in mystr:
        rev_str.push(ch)

    new_str = ''

    while not rev_str.isEmpty():
        new_str += rev_str.pop()

    return new_str


################################################################################

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
