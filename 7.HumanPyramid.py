

def main():
    """This is a main function where allows user to restart new round"""

    printIntro()
    while True:
        row, col = getInput()
        printResult(row, col)
        if decision() != 1:
            break


def printIntro():
    """This is a printIntro function where describe the structure of human pyramid and its condition"""

    print("####__________________________________________________###")
    print("##### Below is an example of Human Pyramid position #####")
    print("#########################################################")
    print("########################( 0,0 )##########################")
    print("###################( 1,0 )####( 1,1 )####################")
    print("##############( 2,0 )####( 2,1 )####( 2,2 )##############")
    print("#########( 3,0 )####( 3,1 )####( 3,2 )####( 3,3 )########")
    print("###( 4,0 )####( 4,1 )####( 4,2 )####( 4,3 )####( 4,4 )###")
    print("####__________________________________________________###")
    print("### Note that default weight is 128 pounds per person ###")
    print("####### The layout inside bracket is (row, column) ######")


def getInput():
    """This is a getInput function where allows user to enter row and column"""

    try:

        row = int(input("Enter row number: "))
        if row < 0:
            print("Please enter positive integer or 0")
            return getInput()
        col = int(input("Enter column number: "))
        if col < 0:
            print("Please enter positive integer or 0")
            return getInput()
        elif col > row:
            print("Column must be less than or equal row")
            return getInput()
        return row, col

    except ValueError:
        print("Please enter only integer")
        return getInput()


def humanPyramid(row, col):
    """This is a humanPyramid function where computes the weight on person's back for each position"""

    weight = 128                                                     # set weight at 128 pounds

    try:

        if row == 0:                                                 # base case
            return 0
        elif col == 0:                                               # first person holding only one person's weight
            return weight + humanPyramid(row - 1, col) / 2           # represent on the left
        elif row == col:                                             # last person holding only one person's weight
            return weight + humanPyramid(row - 1, col - 1) / 2       # represent on the right
        else:                                                        # holding two person left and right
            return weight + humanPyramid(row - 1, col - 1) / 2 + humanPyramid(row - 1, col) / 2

    except RecursionError:                                           # when input is larger than 10^4
        print("Your input is too large for the current setting, please try again")
        return getInput()
    except KeyboardInterrupt:                                        # when input is not integer
        print("You interrupted the program, please try again")
        return getInput()


def printResult(row, col):
    """This is a printResult function where formatted to display with 2 precision"""

    print("Weight on his back is: {0:.2f} pounds".format(humanPyramid(row, col)))


def decision():
    """This is a decision function where asks user if they wish to continue or exit"""

    try:

        continueOrNot = int(input("Enter '1' to try other row and column or '0' to exit: "))
        if continueOrNot == 1:
            print("*********************************************************")
            return 1
        elif continueOrNot == 0:
            print("You exited the program, Have a great day!")
            return 0
        elif continueOrNot not in [0, 1]:
            print("Your input is invalid")
            return decision()

    except ValueError:
        print("Your input is invalid")
        return decision()


if __name__ == "__main__":
    main()
