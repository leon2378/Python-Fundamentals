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



# Second Method
class Shape:
    width = 5
    height = 5
    printChar = '#'

    def printRow(self, i):
        raise NotImplementedError("Will be implemented by children extending this class")
    
    def print(self):
        for i in range(self.height):
            self.printRow(i)

class Square(Shape):
    def printRow(self, i):
        print(self.printChar * self.width)

class Triangle(Shape):
    def printRow(self, i):
        print(self.printChar * (i + 1))


# Third Method
class Shape:
    width = 5
    height = 5
    printChar = '#'

    def printRow(self, i):
        raise NotImplementedError("Will be implemented by children extending this class")
    
    def print(self):
        for i in range(self.height):
            self.printRow(i)

class Square(Shape):
    def printRow(self, i):
        print(self.printChar * self.width)

class Triangle(Shape):
    height = 5
    width = 2 * height

    def printRow(self, i):
        triangleWidth = i * 2 + 1
        padding = int((self.width - triangleWidth)/2)
        print(' '*padding + )