
def main():
    '''
    This is a main function that consists of other 5 functions
    It keeps asking for input until user wish to exit
    '''
    printIntro()
    while True:
        fileNum = getInput()
        sortedList = readFile(fileNum)
        StemAndLeaf(sortedList)
        if decision() != 1:
            break;

def printIntro():

    print("################################################")
    print("\t\tWelcome to DSC 430")
    print("This program will illustrate Stem and Leaf Plot")                      # Introduction and greeting
    print("\t\tLet's get started")
    print("################################################")

def getInput():

    fileNum = input("Which data file would you like to select? [File: 1/2/3]: ")  # get input from user
    if fileNum not in ['1', '2', '3']:                                            # input error handling
        print("***** Only number 1, 2 or 3 are allowed, please try again *****")
        return getInput()                                                         # return to ask question again
    return fileNum                                                                # return chosen file number

def readFile(fileNum):

    infile = open("StemAndLeaf" + fileNum + ".txt", "r")                          # open chosen file
    lineList = infile.readlines()                                                 # read all lines as list
    infile.close()

    lst = []                                                                      # create empty list
    for i in range(len(lineList)):
        lst.append(int(lineList[i].strip()))                                      # remove newline character
    sortedList = sorted(lst)                                                      # sort value in list
    return sortedList

def StemAndLeaf(sortedList):

    count = 0
    leafRow = ""
    for number in sortedList:
        stem = number // 10                                                         # stem 15 // 10 = 1.5 => 1
        leaf = number % 10                                                          # leaf 15 % 10 = 5
        leafRow += " " + str(leaf)                                                  # add leaf values
        if count == len(sortedList) - 1 or stem < int(sortedList[count + 1] // 10): # condition to plot
            print(str(stem) + "|" + leafRow)                                        # plot stem and leaf
            leafRow = ""                                                            # empty space for new line
        count += 1

def decision():
    '''
    This function asks user if they want to continue or exit
    It also handles errors due to integer and string
    '''
    try:
        continueOrNot = int(input("Enter '1' to continue or '0' to exit: "))        # input to continue ot exit
        if continueOrNot == 1:
            print("*************************************")
            return 1
        elif continueOrNot == 0:
            print("You exited the program, Have a great day!")
            return 0
        elif continueOrNot not in [0, 1]:                                           # handling error due to invalid int
            print("Your input is invalid")
            return decision()
    except ValueError:                                                              # handling error due to invalid str
        print("Your input is invalid")
        return decision()


if __name__ == "__main__":
    main()
