
def coprime_test_loop():

    """
    This function intends to ask two numbers for passing values to co-prime function, then return result for display
    """

    # while True loop will execute the loop body infinitely
    while True:
        # try and except blocks to handle error from inappropriate value such as string in this case
        try:
            # value from input will be directly passed to co-prime function
            num1 = int(input("Enter the first integer: "))
            num2 = int(input("Enter the second integer: "))

            # after computation, the coprime function return value to this function
            secondFunc = coprime(num1, num2)
            if secondFunc == True:
                print("The interger " + str(num1) + " and " + str(num2) + " are co-prime ")
                # convert int to str for concatenation
            else:
                print("The interger " + str(num1) + " and " + str(num2) + " are not co-prime ")
        except ValueError:
            print("Sorry, the value is not an integer")

        # prompt to ask user if they want to continue or exit
        goOrNot = input("Please enter to continue or type 0 to exit: ")
        if goOrNot == "0":
            print("You exited the program, Good Bye!")
            # break mechanism will allow user to exit from while loop/program
            break;
        elif goOrNot == "":
            print("**************************************")


def coprime(num1, num2):

    """
    This function will evaluate whether or not the values are co-prime.
    """

    # since numbers cannot be divided by 0 and divisor should not be 1 for not a coprime
    for value in range(2, num1 + 1):
        # if remainders of two value are 0, meaning 1 is not only the biggest positive divisor
        if num1 % value == 0 and num2 % value == 0:
            return False
    # numbers that don't fall into if condition, will have only 1 as biggest divisor, they are co-prime
    return True


if __name__ == "__main__":

    print("*************************")
    print("Welcome to co-prime test")
    print("*************************")
    coprime_test_loop()
