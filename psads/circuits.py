"""
Create circuit simulation, using classes.
"""


class LogicGate:
    """Creates logic gate."""

    def __init__(self, n):
        """Instantiates two characteristics of label for identification and
        output line."""

        self.name = n
        self.output = None

    def getLabel(self):
        """Returns label of gate."""

        return self.name

    def getOutput(self):
        """Returns output value."""

        self.output = self.performGateLogic()

        return self.output


class BinaryGate(LogicGate):
    """Creates logic gate with two input lines/pins."""

    def __init__(self, n):
        """Adds two input lines from LogicGate class."""

        super().__init__(self, n)
        # Can be written in many ways (variations used below):
        # LogicGate.__init__(self, n)
        # super(LogicGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        """Obtains input from user if output of a gate that is connected to the
        input line/pin is not already provided in fromgate's output value in
        Connector class."""

        if self.pinA is None:
            return int(input('Enter Pin A input for gate ' + self.getLabel() + '-->'))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        """Obtains input from user if output of a gate that is connected to the
        input line/pin is not already provided in fromgate's output value in
        Connector class."""

        if self.pinB is None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        """Determines proper input line for each togate in Connector class.
        pinA is chosen by default if both input lines/pins are available."""

        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print "Cannot Connect: NO EMPTY PINS on this gate"


class AndGate(BinaryGate):
    """Creates AND gates"""

    def __init__(self, n):
        """Inherits two input lines from BinaryGate subclass."""

        super(AndGate, self).__init__(self, n)
        # BinaryGate.__init__(self, n)

    def performGateLogic(self):
        """Returns value of 1 if both input lines have value of 1; otherwise,
        returns 0."""

        a = self.getPinA()
        b = self.getPinB()

        if (a == 1) and (b == 1):
            return 1
        else:
            return 0


class NandGate(AndGate):
    """Creates Nand gates, similar to AND gates that have NOT attached to output."""

    def performGateLogic(self):
        """Inherits from AndGate and returns opposite value."""

        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


class OrGate(BinaryGate):
    """Creates OR gates"""

    def __init__(self, n):
        """Inherits two input lines from BinaryGate subclass."""

        super(OrGate, self).__init__(self, n)
        # BinaryGate.__init__(self, n)

    def performGateLogic(self):
        """Returns value of 0 if both input lines have value of 0; otherwise,
        returns 1."""

        a = self.getPinA()
        b = self.getPinB()

        if (a == 1) or (b == 1):
            return 1
        else:
            return 0


class NorGate(OrGate):
    """Creates Nor gates, similar to OR gates that have NOT attached to output."""

    def performGateLogic(self):
        """Inherits from OrGate and returns opposite value."""

        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


class UnaryGate(LogicGate):
    """Creates logic gate with single input line/pin."""

    def __init__(self, n):
        """Adds single input line from LogicGate class."""

        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        """Obtain input from user."""

        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        """Determines proper input line for each togate in Connector class."""

        if self.pin is None:
            self.pin = source
        else:
            print "Cannot Connect: NO EMPTY PINS on this gate"


class NotGate(UnaryGate):
    """Creates NOT gates"""

    def __init__(self, n):
        """Inherits single input line from UnaryGate subclass."""

        super(NotGate, self).__init__(self, n)
        # UnaryGate.__init__(self, n)

    def performGateLogic(self):
        """Returns output value as opposite of input line."""

        if self.getPin():
            return 0
        else:
            return 1


class Connector:
    """Creates connector."""

    def __init__(self, fgate, tgate):
        """Instantiates connector with to and from gates to connect output line
        of one gate to input line of another."""

        self.fromgate = fgate
        self.togate = tgate

        # Choose proper input line for connection
        tgate.setNextPin(self)

    def getFrom(self):
        """Returns fromgate output value."""

        return self.fromgate

    def getTo(self):
        """Returns togate output value."""

        return self.togate


################################################################################

if __name__ == '__main__':

    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print g4.getOutput()

    g2 = NandGate("G2")
    # with input 1 and 1, should get 0
    print g2.getOutput()
