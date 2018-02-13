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


class OrderedList:
    """Creates ordered linked list."""

    def __init__(self):
        """Instantiates linkedlist."""

        self.head = None

    def isEmpty(self):
        """Checks if list is empty."""

        return self.head is None

    def add(self, item):
        """Adds item to list based on ascending order."""

        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)

        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        """Calculates size of list."""

        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        """Searches list for specified item."""

        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def remove(self, item):
        """Removes specified item and relinks list."""

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


################################################################################

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
