
import random

class SimplePlotGenerator:
    """ Class Simple Plot Generator """

    def __init__(self):
        """ Constructor """

        self.sentence = "Something happens !!"

    def generate(self):
        """ Method Generate to produce plot """

        print(self.sentence)


class RandomPlotGenerator:
    """ Class Random Plot Generator """

    def __init__(self):
        """ constructor """

        self.file = None
        self.words = []
        self.fileNames = ["plot_names.txt", "plot_adjectives.txt", "plot_profesions.txt", "plot_verbs.txt",
                          "plot_adjectives_evil.txt", "plot_villian_job.txt", "plot_villains.txt"]

    def readFile(self):
        """ Method readFile to open files and randomly pick 1 word from each file """

        for file in self.fileNames:
            with open(file, 'r') as self.file:
                self.file = self.file.read().split('\n')
                self.file = random.choice(self.file)
                self.words.append(self.file)

        return self.words

    def generate(self):
        """ Method to generate a random plot """

        print("{}, a {} {}, must {} the {} {}, {}.".format(self.readFile()[0], self.readFile()[1], self.readFile()[2],
                                                           self.readFile()[3], self.readFile()[4], self.readFile()[5],
                                                           self.readFile()[6]))


class InteractivePlotGenerator(SimplePlotGenerator):
    """ Class Interactive Plot Generator is a child class of Simple Plot Generator
        This class will allow users to select 7 words to generate their own plot
    """

    def __init__(self):
        """ Constructor """

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
            self.file = self.file.read().split('\n')
            if self.file != '':
                self.file = random.sample(self.file, 5)
                self.words = dict(zip((i for i in range(5)), self.file))

        return self.words

    def selectChoices(self, wordsDict):
        """ Method selctChoice to ask users to select their word choices """

        try:

            selection = int(input("Enter here: "))

            if selection not in [0, 1, 2, 3, 4]:
                print("This is invalid number, please select again!")
                return self.selectChoices(wordsDict)
            else:
                return wordsDict.get(selection)

        except ValueError:
            print("This is invalid input, please try again!")
            return self.selectChoices(wordsDict)

    def generate(self):
        """ Method generate to organize other methods in generating a random plot """

        file = InteractivePlotGenerator()
        a = file.readFile(InteractivePlotGenerator().fileNames)
        print("Select name from the following list")
        print(a)
        a = file.selectChoices(a)
        print("You selected:", a)
        print("_____________________________________")

        b = file.readFile(InteractivePlotGenerator().fileAdj)
        print("Select adjective from the following list")
        print(b)
        b = file.selectChoices(b)
        print("You selected:", b)
        print("_____________________________________")

        c = file.readFile(InteractivePlotGenerator().fileProfesions)
        print("Select profession from the following list")
        print(c)
        c = file.selectChoices(c)
        print("You selected:", c)
        print("_____________________________________")

        d = file.readFile(InteractivePlotGenerator().fileVerbs)
        print("Select verb from the following list")
        print(d)
        d = file.selectChoices(d)
        print("You selected:", d)
        print("_____________________________________")

        e = file.readFile(InteractivePlotGenerator().fileAdjEvil)
        print("Select evil's adjective from the following list")
        print(e)
        e = file.selectChoices(e)
        print("You selected:", e)
        print("_____________________________________")

        f = file.readFile(InteractivePlotGenerator().fileVillianJob)
        print("Select Villain's job from the following list")
        print(f)
        f = file.selectChoices(f)
        print("You selected:", f)
        print("_____________________________________")

        g = file.readFile(InteractivePlotGenerator().fileVillains)
        print("Select Villain from the following list")
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
