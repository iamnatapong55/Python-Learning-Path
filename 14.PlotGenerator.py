

import random

class SimplePlotGenerator:
    """ Class Simple Plot Generator to display plot of 'Something happens' """

    def __init__(self):
        """ Constructor """

        self.sentence = "Something happens !!"

    def generate(self):
        """ Method Generate to produce plot """

        print(self.sentence)


class RandomPlotGenerator:
    """ Class Random Plot Generator to display a random plot """

    def __init__(self):
        """ constructor """

        self.file = None
        self.words = []
        self.fileNames = ["plot_names.txt", "plot_adjectives.txt", "plot_profesions.txt", "plot_verbs.txt",
                          "plot_adjectives_evil.txt", "plot_villian_job.txt", "plot_villains.txt"]

    def readFile(self):
        """ Method readFile to open files and randomly pick 1 word from each file """

        for file in self.fileNames:                                     # iterate all files in list of self.fileNames

            with open(file, 'r') as self.file:                          # open then close file
                self.file = self.file.read().strip('').split('\n')      # read, clean nd arrange
                self.file = random.choice(self.file)                    # randomly pick 1 word
                self.words.append(self.file)                            # store each word from different file in list

        return self.words

    def generate(self):
        """ Method to generate a random plot, unpack list by indexing """

        print("{}, a {} {}, must {} the {} {}, {}.".format(self.readFile()[0], self.readFile()[1], self.readFile()[2],
                                                           self.readFile()[3], self.readFile()[4], self.readFile()[5],
                                                           self.readFile()[6]))


class InteractivePlotGenerator(SimplePlotGenerator):
    """ Class Interactive Plot Generator is a child class of Simple Plot Generator
        This class will allow users to select 7 words to generate their own plot
    """

    def __init__(self):
        """ Constructor to extend superclass """

        super().__init__()
        self.file = None
        self.words = None
        self.dict = None
        self.fileNames = "plot_names.txt"
        self.fileAdj = "plot_adjectives.txt"
        self.fileProfesions = "plot_profesions.txt"
        self.fileVerbs = "plot_verbs.txt"
        self.fileAdjEvil = "plot_adjectives_evil.txt"
        self.fileVillianJob = "plot_villian_job.txt"
        self.fileVillains = "plot_villains.txt"

    def readFile(self, files):
        """ Method readFile to open files and randomly pick 5 word from each file """

        with open(files, 'r') as self.file:

            self.file = self.file.read().strip('').split('\n')
            self.file = random.sample(self.file, 5)                         # random.sample to display a random 5 words
            self.words = dict(zip((i for i in range(5)), self.file))        # pack words in dictionary

        return self.words

    def selectChoices(self, wordsDict):
        """ Method selectChoice to ask users for selecting their word choices """

        try:

            selection = int(input("Enter here: "))                          # input int from dictionary list

            if selection not in [0, 1, 2, 3, 4]:                            # only 5 numbers from dict list are allowed
                print("This is invalid number, please select again!")
                return self.selectChoices(wordsDict)                        # if wrong number, ask to enter again
            else:
                return wordsDict.get(selection)

        except ValueError:

            print("This is invalid input, please try again!")
            return self.selectChoices(wordsDict)                            # if wrong format, ask to enter again

    def generate(self):
        """ Method generate to organize other methods in generating a random plot, this method overrode superclass """

        file = InteractivePlotGenerator()
        a = file.readFile(self.fileNames)
        print("Select number from the following name list")
        print(a)
        a = file.selectChoices(a)
        print("You selected:", a)
        print("_____________________________________")

        b = file.readFile(self.fileAdj)
        print("Select number from the following adjective list")
        print(b)
        b = file.selectChoices(b)
        print("You selected:", b)
        print("_____________________________________")

        c = file.readFile(self.fileProfesions)
        print("Select number from the following profession list")
        print(c)
        c = file.selectChoices(c)
        print("You selected:", c)
        print("_____________________________________")

        d = file.readFile(self.fileVerbs)
        print("Select number from the following verb list")
        print(d)
        d = file.selectChoices(d)
        print("You selected:", d)
        print("_____________________________________")

        e = file.readFile(self.fileAdjEvil)
        print("Select number from the following evil's adjective list")
        print(e)
        e = file.selectChoices(e)
        print("You selected:", e)
        print("_____________________________________")

        f = file.readFile(self.fileVillianJob)
        print("Select number from the following Villain's job list")
        print(f)
        f = file.selectChoices(f)
        print("You selected:", f)
        print("_____________________________________")

        g = file.readFile(self.fileVillains)
        print("Select number from the following Villain list")
        print(g)
        g = file.selectChoices(g)
        print("You selected:", g)
        print("_____________________________________")

        self.printResult(a, b, c, d, e, f, g)

    def printResult(self, a, b, c, d, e, f, g):
        """ Method printResult to display final plot """

        print("This is your plot: ")
        print("\t")
        print("***  {}, a {} {}, must {} the {} {}, {}. ***".format(a, b, c, d, e, f, g))
        print("\t")
        print("Thank you very much !")


def printIntro():
    """ Function printIntro to print introduction and greeting """

    print("####################################################################")
    print("Hi there!, this is a plot generator that can create basic plot ideas")
    print("This program will allow users to select 7 elements for the narrative")
    print("####################################################################")


def main():
    """ Main function to organize final elements in code """

    printIntro()
    pq = SimplePlotGenerator()
    pq.generate()

    print("Below is a sample of plot")
    pq = RandomPlotGenerator()
    pq.generate()

    print("_____________________________________________________________________")
    print("Next, you will be asked to select your own plot.")
    print("_____________________________________________________________________")
    pq = InteractivePlotGenerator()
    pq.generate()


if __name__ == "__main__":
    main()
