
import random

class SixSidedDie:
    """This is SixSidedDie class consisting of 4 methods: init, roll, getFaceValue and repr"""

    def __init__(self):
        """This is a constructor function for SixSidedDie class where to define sides and FaceValue"""
        self.sides = 6
        self.FaceValue = 1

    def roll(self):
        """This is roll method that generates a random number as FaceValue in relation to the number of side"""
        self.FaceValue = random.randint(1, self.sides)
        return self.FaceValue

    def getFaceValue(self):
        """This is getFaceValue method that aims to return the value of thrown dice"""
        return self.FaceValue

    def __repr__(self):
        """This is repr method that returns the object representation"""
        return "{} ({})".format(self.__class__.__name__, self.FaceValue)


class TenSidedDie(SixSidedDie):
    """This is TensidedDie class which inherits from the base which is the SixSidedDie class"""

    def __init__(self):
        """This is an initializer method in TenSidedDie class to set a newly created object’s attributes"""
        super().__init__()                                  # super class
        self.sides = 10                                     # overwritten sides to 10


class TwentySidedDie(SixSidedDie):
    """This is TwentySidedDie class which inherits from the base which is the SixSidedDie class"""

    def __init__(self):
        """This is an initializer method in TwentySidedDie class to set a newly created object’s attributes"""
        super().__init__()                                  # super class
        self.sides = 20                                     # overwritten sides to 20


class Cup:
    """This is a cup class, its application is to hold any number of any types of dices"""

    def __init__(self):
        """This is a constructor function for cup class where initialize 1 for each type of dice"""
        self.__init__(1, 1, 1)

    def __init__(self, NumSixDie, NumTenDie, NumTwentyDie):
        """This is a init function for cup class where to collect each dice in a list"""

        self.list = []
        for num in range(NumSixDie):
            self.list.append(SixSidedDie())
        for num in range(NumTenDie):
            self.list.append(TenSidedDie())
        for num in range(NumTwentyDie):
            self.list.append(TwentySidedDie())

    def roll(self):
        """This is roll method that will roll dices then store values in the result"""

        result = 0
        for dice in self.list:
            result += dice.roll()

        self.result = result
        return self.result

    def getSum(self):
        """This is getSum method that aims to return the sum of all dices"""
        return self.result

    def __repr__(self):
        """This is repr method that returns the object representation"""
        return ",".join(repr(dice) for dice in self.list)


'''
print("Die Class")
a= SixSidedDie()
print(a.roll())
print(a.getFaceValue())
print(a)


print("Cup Class")
d = Cup(1,2,1)
print(d.roll())
print(d.getSum())
print(d)
'''