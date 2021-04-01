

from numpy import random

ratList = []
catList = []
berriesBasket = []

def readParameter():
    """ Reading parameters in from a parameter file and store them in dictionary """

    parameters = {}

    with open("parameters.txt") as file:

        for parameter in file.readlines():
            parameter = parameter.strip('\n').split('=')
            parameters[parameter[0]] = parameter[1]

        return parameters


def getRain():
    """ Getting rain by drawing random samples from a normal distribution """

    rainChance = float(readParameter()["rain_chance"])
    rainMean = float(readParameter()["rain_mean"])
    rainStd = float(readParameter()["rain_std"])

    if random.rand() < rainChance:                              # random range (0,1] vs 0.3 chance of rain
        return 0
    return random.normal(rainMean, rainStd, size=(1, 1))[0][0]  # a single number from normal distribution


def initRatsList():
    """ Creating all rats in the list """

    ratsInit = int(readParameter()["rats_init"])                # initially rats = 10,000 on the island

    for i in range(ratsInit):
        rat = Rat(random.randint(0, ratsInit))
        ratList.append(rat)


def initCatsList():
    """ Creating all cats in the list """

    catsInit = int(readParameter()["cats_init"])               # initially cats = 1,000 on the island

    for _ in range(0, catsInit):
        cat = Cat(random.randint(0, catsInit))
        catList.append(cat)


def removeDead():
    """ Function to handle life cycle: berries persist 10 days, rats die in 3 days and cats die in 5 days if no eat"""

    for berry in berriesBasket:
        if not berry.isEatable():
            berriesBasket.remove(berry)

    for rat in ratList:
        if rat.isDead():
            ratList.remove(rat)

    for cat in catList:
        if cat.isDead():
            catList.remove(cat)


class Berry:
    """ Class to handle Berry if they are still edible """

    def __init__(self):
        self.ageDays = 0
        self.berryPersist = int(readParameter()["berry_persist"])

    def passDay(self):
        self.ageDays += 1

    def isEatable(self):
        return self.ageDays <= self.berryPersist


class Rat:
    """ Class to define rat's character and properties """

    def __init__(self, age):
        """ Initializing objects and getting parameters """

        self.eatDaysAgo = 0
        self.days = age
        self.berriesEaten = 0
        self.ratsBeginAge = int(readParameter()["rats_old_begin_age"])
        self.ratsOld_prob = float(readParameter()["rats_old_step_prob"])
        self.ratsBirth_initBerries = int(readParameter()["rats_birth_init_berries"])
        self.ratsBirth_stepBerries = int(readParameter()["rats_birth_step_berries"])
        self.litRatsBirth_lowerBound = int(readParameter()["rats_birth_litter_lower_bound"])
        self.litRatsBirth_upperBound = int(readParameter()["rats_birth_litter_upper_bound"])

    def passDay(self):
        """ Method to handle counter """

        self.days += 1
        self.eatDaysAgo += 1

    def tryEat(self):
        """ Method to run eating berries """

        berriesNum = len(berriesBasket)

        if berriesNum > 0:
            r = random.randint(0, berriesNum)
            self.eatDaysAgo = 0
            self.berriesEaten += 1
            del berriesBasket[r]

    def isDead(self):
        """ Method to consider if rat is dead from not eating and chance from old age """

        if self.eatDaysAgo >= 3:
            return True

        if self.days > self.ratsBeginAge:                                    # after 50 days rats have chance to die
            if random.rand() < 0.01 * self.ratsOld_prob * (self.days - 49):  # 5 % chance of dying from old age 50 days
                return True
        return False

    def givingBirth(self):
        """ Method to define rat giving birth after 10 berries then every 8 berries thereafter """

        if self.berriesEaten < self.ratsBirth_initBerries:
            return

        if (self.berriesEaten - self.ratsBirth_initBerries) % self.ratsBirth_stepBerries == 0:          # birth step = 8
            ratsBorn = random.randint(self.litRatsBirth_lowerBound, self.litRatsBirth_upperBound + 1)   # bound 6 - 10
            for rat in range(1, ratsBorn):
                ratList.append(Rat(0))


class Cat:
    """ Class to define cat's characters and properties """

    def __init__(self, days):
        """ Initializing objects and getting parameters """

        self.days = days
        self.eatDaysAgo = 0
        self.ratsEaten = 0
        self.catsCatch = float(readParameter()["cats_catch_coefficient"])
        self.islandArea = int(readParameter()["island_area"])
        self.catsNoEat_limit = int(readParameter()["cats_not_eat_days_limit"])
        self.catsBeginAge = int(readParameter()["cats_old_begin_age"])
        self.catsBegin_prob = float(readParameter()["cats_old_begin_prob"])
        self.catOld_step_prob = float(readParameter()["cats_old_step_prob"])
        self.catBirth_initRats = int(readParameter()["cats_birth_init_rats"])
        self.catBirth_step_rats = int(readParameter()["cats_birth_step_rats"])
        self.litCatsBirth_lowerBound = int(readParameter()["cats_birth_litter_lower_bound"])
        self.litCatsBirth_upperBound = int(readParameter()["cats_birth_litter_upper_bound"])

    def passDay(self):
        """ Method to handle counter """

        self.days += 1
        self.eatDaysAgo += 1

    def tryEat(self):
        """ Method to run simulation of cat attempting to eat a rat """

        ratsNum = len(ratList)
        if ratsNum > 0:
            if random.rand() < (self.catsCatch * ratsNum) / self.islandArea + self.days * self.catsNoEat_limit:
                r = random.randint(0, ratsNum)
                self.eatDaysAgo = 0
                self.ratsEaten += 1
                del ratList[r]

    def isDead(self):
        """ Method to consider if cat is dead from not eating and chance from old age """

        if self.eatDaysAgo >= self.catsNoEat_limit:
            return True

        if self.days > self.catsBeginAge:                               # after 2,000 days having 1% chance of dying
            if random.rand() < 0.01 * (self.catsBegin_prob + self.catOld_step_prob * (self.days - self.catsBeginAge)):
                return True
        return False

    def givingBirth(self):
        """ Method to define litter of cats after init rats eaten, following with step rats eaten """

        if self.ratsEaten < self.catBirth_initRats:                     # giving birth after 50 rats eaten
            return                                                      # then giving birth every 35 rats step

        if (self.ratsEaten - self.catBirth_initRats) % self.catBirth_step_rats == 0:
            rats_born = random.randint(self.litCatsBirth_lowerBound, self.litCatsBirth_upperBound + 1)
            for k in range(0, rats_born):
                catList.append(Cat(0))


def simulation():
    """ Simulation to show development of berries produced after rain and life cycle of cats and rats """

    rain = 0                                                           # rain at initial condition

    initRatsList()
    initCatsList()

    daysLimit = int(readParameter()["days_limit"])
    islandArea = int(readParameter()["island_area"])
    berryCoeff = float(readParameter()["berry_coefficient"])

    for i in range(1, daysLimit):

        newBerries = int(rain * islandArea * berryCoeff)                # berries produced after rain

        for berry in range(1, newBerries):
            berriesBasket.append(Berry())

        for berry in berriesBasket:
            berry.passDay()

        for rat in ratList:                                             # rats life cycle
            rat.tryEat()
            rat.givingBirth()
            rat.passDay()

        for cat in catList:                                             # cats life cycle
            cat.tryEat()
            cat.givingBirth()
            cat.passDay()

        rain = getRain()
        removeDead()

def writeOutput(daysLimit):

    out = open("fileInformation.txt", "w")
    out.write("By the end of Day " + str(daysLimit) + "\n")
    out.write("Berries population: " + str(len(berriesBasket)) + "\n")
    out.write("Rats population: " + str(len(ratList)) + "\n")
    out.write("Cats population: " + str(len(catList)) + "\n")
    out.close()

def main():

    simulation()
    daysLimit = int(readParameter()["days_limit"])

    print("By the end of Day {}".format(str(daysLimit)))
    print("Berries population: {} ea".format(str(len(berriesBasket))))
    print("Rats population: {} ea".format(str(len(ratList))))
    print("Cats population: {} ea".format(str(len(catList))))

    writeOutput(daysLimit)


if __name__ == "__main__":

    main()


