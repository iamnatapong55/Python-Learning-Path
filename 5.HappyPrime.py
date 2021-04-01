
def main():
    """This is a main function where enable the program to run endlessly until user desire to exit"""

    printIntro()
    while True:
        number = getInput()
        checkResult(number)
        if decision() != 1:
            break


def printIntro():
    """ This is an introduction part where describes what will you get from entering number """

    print("#########################################################")
    print("This is a program where you can check whether number is: ")
    print("Happy Prime, Sad Prime, Happy Non-Prime or Sad Non-Prime ")
    print("#########################################################")


def getInput():
    """ This is an input function where allows only an acceptable number into the program """

    try:
        number = int(input("Enter a positive integer here: "))
        if number < 0:                                          # prevent negative input that might fail the program
            print("Your input is invalid")
            return getInput()
        else:
            return number
    except ValueError:
        print("Your input is invalid")                          # prevent string input
        return getInput()


def checkPrime(number):
    """ This is a function to check number whether or not it is a prime number """

    if number < 2:                                              # prime number is greater than 1
        return False
    for i in range(2, number+1):
        if number % i == 0 and number != i:                     # number has other divisor
            return False
        elif number == i:                                       # allow to be divided by itself
            return True


def checkHappy(number):
    """ This function is to check the input number whether or not it is a happy number """

    res = []
    while True:
        square = []
        for i in str(number):                                   # convert int to str then iterate over the position
            multiply = int(i) * int(i)
            square.append(multiply)
        sumSquare = sum(square)
        if sumSquare == 1:                                      # if the sum square is 1 then happy
            return True
        elif sumSquare in res:                                  # having pattern in list
            return False
        number = sumSquare
        res.append(number)


def checkResult(number):
    """ This function is to determine cases whether the number falls into which categories """

    if checkPrime(number):
        if checkHappy(number):
            print("Number", number, "is a Happy Prime")         # Prime and happy
        else:
            print("Number", number, "is a Sad Prime")           # Prime but not happy
    else:
        if checkHappy(number):
            print("Number", number, "is a Happy Non-Prime")     # Not Prime but happy
        else:
            print("Number", number, "is a Sad Non-Prime")       # Not Prime and not happy


def decision():
    """ This function asks user if they want to continue or exit """

    try:
        continueOrNot = int(input("Enter '1' to try other number or '0' to exit: "))
        if continueOrNot == 1:
            print("*************************************")
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
