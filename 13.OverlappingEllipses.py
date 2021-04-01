

from Assignment0701 import WarAndPeacePseudoRandomNumberGenerator


class Point:
    """ Class Point is to define coordinate x and y on ellipses """

    def __init__(self, x, y):
        """ Constructor """

        self.x = x
        self.y = y


class Ellipse:
    """ Class Ellipse is to take 2 points together with the width of the long axis """

    def __init__(self, p1, p2, w):
        """ Constructor """

        self.p1 = p1
        self.p2 = p2
        self.w = w

    def isInEllipse(self, point):
        """ This method is to check whether or not the point is within overlap area
            It utilizes the property of 2a = sqt(PF1^2 + PF2^2)
            So if the sum (which is likely to be 2a) less/equal the 2a of that ellipse
            The point is assumed to happen in the ellipse
        """

        d1 = self.distance(self.p1, point)
        d2 = self.distance(self.p2, point)
        return (d1 + d2) <= self.w

    def distance(self, p1, p2):
        """ Method to calculate distance between 2 points """

        return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5


class Box:
    """ Class Box is to define box dimension for locating Ellipses """

    def __init__(self, ellipse1, ellipse2):
        """ Constructor """

        self.ellipse1 = ellipse1
        self.ellipse2 = ellipse2
        self.calculateBox()
        self.ranDom = WarAndPeacePseudoRandomNumberGenerator()

    def calculateBox(self):
        """ This method is to define box dimension and calculate area """

        xList = [self.ellipse1.p1.x, self.ellipse1.p2.x, self.ellipse2.p1.x, self.ellipse2.p2.x]
        yList = [self.ellipse1.p1.y, self.ellipse1.p2.y, self.ellipse2.p1.y, self.ellipse2.p2.y]
        widthList = [self.ellipse1.w, self.ellipse2.w]

        # find the outer most possible of ellipses
        minX = min(xList)
        maxX = max(xList)
        minY = min(yList)
        maxY = max(yList)
        maxW = max(widthList)
        maxW = maxW / 2

        # define the box boundary
        x1 = minX - maxW
        x2 = maxX + maxW
        y1 = minY - maxW
        y2 = maxY + maxW

        # locate edges of the box
        self.bottomLeft = Point(x1, y1)
        self.bottomRight = Point(x2, y1)
        self.topLeft = Point(x1, y2)
        self.topRight = Point(x2, y2)

        # calculate width and height for area calculation
        self.boxWidth = x2 - x1
        self.boxHeight = y2 - y1

    def getPointInBox(self):
        """ This method utilizes PRNG function in the previous assignment for generating random numbers as points
            The random number can be any number in (0,1]
            In worst case of (x,y) = (0,0)
            The bottomLeft position will define the lowest possible coordinate in the quadrant3
        """

        x = self.ranDom.random()
        x = (x * self.boxWidth) + self.bottomLeft.x
        y = self.ranDom.random()
        y = (y * self.boxHeight) + self.bottomLeft.y

        return Point(x, y)

    def getArea(self):
        """ This method is for simple area calculation of square box """

        return self.boxWidth * self.boxHeight

    def isPointInEllipses(self, p):
        """ This method is to verify if point is in both Ellipses """

        return self.ellipse1.isInEllipse(p) and self.ellipse2.isInEllipse(p)


def calculateAreaOfOverlap(boxArea, numOverlap, constant):
    """ This function is to calculate the area of overlap portion """

    return boxArea * (numOverlap / constant)


def computeOverlapOfEllipse(ell1, ell2):
    """ This function is to take two ellipses' points and returns area of the overlap
        1. Random (x,y) of 100K points are generated to entire box area
        2. Find num of point in potential overlap area
        3. Calculate the portion of overlap out of entire box area
    """

    box = Box(ell1, ell2)
    boxArea = box.getArea()
    pointInBox = 100000
    numOverlap = 0

    for i in range(pointInBox):             # iterate over many times as possible, using 100k
        p = box.getPointInBox()             # generating 100K points in box
        if box.isPointInEllipses(p):        # evaluate if point in both ellipse
            numOverlap += 1                 # add number of overlap points in variable

    return calculateAreaOfOverlap(boxArea, numOverlap, pointInBox)


def printIntroduction():
    """ Function to print general introduction of program """

    print("##################################################################")
    print("### This program is to calculate the overlap area of two ellipses ")
    print("### Users have to define coordinates of foci in both ellipses     ")
    print("### Foci are two points in ellipse that define shape and curvature")
    print("##################################################################")


def inputXCoord():
    """" Function to get input for x coordinate """

    try:
        p1X = int(input("Enter x coordinate for Ellipse's focal point: "))
        return p1X
    except ValueError:
        print("Please enter valid number")
        return inputXCoord()


def inputYCoord():
    """" Function to get input for y coordinate """

    try:
        p1Y = int(input("Enter y coordinate for Ellipse's focal point: "))
        return p1Y
    except ValueError:
        print("Please enter valid number")
        return inputYCoord()


def inputWidth(p1, p2):
    """" Function to get input for width """

    try:
        width = int(input("Now enter the width between these 2 point: "))
        if width < Ellipse(p1, p2, width).distance(p1, p2):
            print("Enter wider length")
            return inputWidth(p1, p2)
        else:
            return width
    except ValueError:
        print("Please enter valid number")
        return inputWidth(p1, p2)


def buildingEllipse():
    """ This buildingEllipse function is to organize all inputs, and display input summary """

    print("Read instruction and enter each coordinate carefully")
    print("____________________________________________________")
    print("This is the first coordinate of Ellipse 1's focal point")
    p1x = inputXCoord()
    p1y = inputYCoord()

    print("This is the second coordinate of Ellipse 1's focal point")
    p2x = inputXCoord()
    p2y = inputYCoord()

    p1 = Point(p1x, p1y)
    p2 = Point(p2x, p2y)
    width1 = inputWidth(p1, p2)
    print("Your first Ellipse consists of F1:({}, {}), F2:({}, {}), Width: {}".format(p1x, p1y, p2x, p2y, width1))

    print("____________________________________________________")
    print("This is the first coordinate of Ellipse 2's focal point")
    p3x = inputXCoord()
    p3y = inputYCoord()
    p3 = Point(p3x, p3y)

    print("This is the second coordinate of Ellipse 2's focal point")
    p4x = inputXCoord()
    p4y = inputYCoord()
    p4 = Point(p4x, p4y)

    width2 = inputWidth(p1, p2)
    print("Your second Ellipse consists of F1:({}, {}), F2:({}, {}), Width: {}".format(p1x, p1y, p2x, p2y, width2))

    el1 = Ellipse(p1, p2, width1)
    el2 = Ellipse(p3, p4, width2)

    return el1, el2


def printOverlap(el1, el2):
    """ This printOverlap function is to report the overlap area in unit """

    print("Please wait !! System is processing")
    overlap = computeOverlapOfEllipse(el1, el2)
    print("=============================================")
    print("The overlap area is {} unit".format(overlap))
    print("=============================================")


def main():
    """ This is main function """

    printIntroduction()
    el1, el2 = buildingEllipse()
    printOverlap(el1, el2)


if __name__ == "__main__":

    main()
