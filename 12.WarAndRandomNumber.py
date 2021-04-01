

import time
from statistics import mean

class WarAndPeacePseudoRandomNumberGenerator:

    def __init__(self, seed=None):
        """ Constructor """

        self.seed = seed
        self.fileName = "war-and-peace.txt"
        self.file = None

    def getTime(self):
        """" This method is to get base number from time in second since epoch """

        return int(round(time.time() * (10 ** 6)))              # convert floating point num to int

    def getRandomValue(self):
        """ This method is to get random number based on seed value,
            if no seed then random number based on time """

        if self.seed is None:
            timeStr = str(self.getTime())                       # this time base will generate random num
            tmp = int(timeStr[-5:])                             # last 5 digits allows pseudo random number pattern
        else:
            tmp = self.seed                                     # random number from seed will be fixed

        return (tmp + 24579) % 99999

    def getCharacterAt(self, indexVal):
        """ This method utilizes rb mode to handle contents in binary form """

        binaryStr = " "
        result = None

        with open(self.fileName, 'rb') as self.file:

            while binaryStr.isspace():

                self.file.seek(indexVal)                       # handle file at position indexVal
                binaryStr = self.file.read(1)                  # read in as 1 byte or 8 bits
                indexVal += 1

                try:
                    result = binaryStr.decode("ascii")         # decode with ascii for english and get str
                except UnicodeError:                           # error due to out of ascii
                    binaryStr = " "

        return result                                          # return string

    def convertBinaryStrToNum(self, binaryStr):
        """ This method is to convert binary string to integer """

        result = 0
        divisor = 2

        for i in range(len(binaryStr)):
            result += int(binaryStr[i]) * (1 / divisor)
            divisor = divisor * 2                              # upgrade divisor

        return result

    def random(self):
        """ This method is to generate random number based on binary sequence """

        randomNum = self.getRandomValue()
        binaryStr = ""

        while len(binaryStr) < 8:

            start = self.getCharacterAt(randomNum)                          # string 1
            end = self.getCharacterAt(randomNum + self.getRandomValue())    # string 2
            bit = ""
            if start > end:                                                 # string comparison
                bit = "1"                                                   # add bit = 1 if true
            if start < end:
                bit = "0"                                                   # add bit = 0 if true
            randomNum += self.getRandomValue()
            binaryStr += bit

        return self.convertBinaryStrToNum(binaryStr)                        # return with int


def printStat(lst):
    """ This function is to print min, max and mean in format with 4 decimal """

    print("#############################################")
    print("10,000 random numbers are generated")
    print("Min  is: {:.7f}".format(min(lst)))
    print("Max  is: {:.7f}".format(max(lst)))
    print("Mean is: {:.7f}".format(mean(lst)))
    print("#############################################")

def main():
    """ This main function is to display the application of class and method"""

    prng0 = WarAndPeacePseudoRandomNumberGenerator()
    r = prng0.random()
    print("#############################################")
    print("Random number without seed is {:.7f}".format(r))
    lst = []
    for i in range(10000):
        lst.append(prng0.random())
    printStat(lst)

    seedVal = 12345
    prng1 = WarAndPeacePseudoRandomNumberGenerator(seedVal)
    r1 = prng1.random()
    print("Random number with seed: {} is {:.7f} ".format(seedVal, r1))
    lst2 = []
    for i in range(10000):
        lst2.append(prng1.random())
    printStat(lst2)


if __name__ == "__main__":

    main()







