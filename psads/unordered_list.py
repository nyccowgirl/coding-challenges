class Node:
    """Create node class."""

    def __init__(self, initdata):
        """Instantiates node."""

        self.data = initdata
        self.next = None

    def getData(self):
        """Returns data of node."""

        return self.data

    def getNext(self):
        """Returns next node."""

        return self.next

    def setData(self, newdata):
        """Sets data for node."""

        self.data = newdata

    def setNext(self, newnext):
        """Sets next node."""

        self.next = newnext


class UnorderedList:
    """Creates unordered linked list."""

    def __init__(self):
        """Instantiates linkedlist."""

        self.head = None

    def isEmpty(self):

        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head

        while current.next is not None:
            current = current.getNext()

        current.next = Node(item)


# ALTERNATE SOLUTION:

# For O(1) append:

    # def __init__(self):

    #     self.head = None
    #     self.tail = None

    # def add(self, item):
    #     temp = Node(item)

    #     if self.isEmpty:
    #         self.tail = temp

    #     temp.setNext(self.head)
    #     self.head = temp

    # def append(self, item):
    #     temp = Node(item)
    #     if self.isEmpty:
    #         self.head = temp
    #         self.tail = temp
    #     else:
    #         self.tail.next = temp
    #         self.tail = temp


################################################################################

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
