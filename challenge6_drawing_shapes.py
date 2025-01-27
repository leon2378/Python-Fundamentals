class Shape:
    def __init__(self, width=5, height=5, printChar='#'):
        self.width = width
        self.height = height
        self.printChar = printChar

    def printRow(self, i):
        raise NotImplementedError("Will be implemented by children extending this class")

    def print(self):
        for i in range(self.height):
            self.printRow(i)


class Square(Shape):
    def printRow(self, i):
        # Print a full row of printChar repeated width times
        print(self.printChar * self.width)


class Triangle(Shape):
    def printRow(self, i):
        # Print i + 1 printChars to form a right-angled triangle
        print(self.printChar * (i + 1))