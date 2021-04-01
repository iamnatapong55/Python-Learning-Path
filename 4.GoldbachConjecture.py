
def main():
    """This is a main function consisting of 4 functions"""

    printIntro()
    numbers = rangeNumber()
    primes = primeNum(numbers)
    goldBach(primes)


def printIntro():
    """This is a printIntro function to inform the details"""

    print("####################################################")
    print("Goldbach's Conjecture for all integers from 1 - 100 ")
    print("####################################################")


def rangeNumber():
    """This is rangeNumber function to allow flexibility in editing the range of interest in the future"""

    num1 = 1
    num2 = 100
    numbers = range(num1, num2)                         # this range not include 100
    return numbers


def primeNum(numbers):
    """This function is to store the list of prime number"""

    primes = []
    for number in numbers:
        if checkPrime(number):                           # utilize checkPrime function
            primes.append(number)                        # keep prime in the list
    return primes


def checkPrime(number):
    """This function is to determine prime number"""

    if number < 2:                                      # prime number is greater than 1
        return False
    for i in range(2, number+1):
        if number % i == 0 and number != i:             # number has other divisor
            return False
        elif number == i:                               # allow to be divided by itself
            return True



def goldBach(primes):
    """This function is to determine goldbach's conjecture"""

    for even in range(4, 101, 2):                       # Gold-bach is every even integer greater than 2, 100 inclusive
        for prime in primes:                            # iterate 1st prime in the list
            diff = even - prime                         # find 2nd number
            if diff in primes:                          # 2nd number should contain prime condition as well
                print(str(even) + ' = ' + str(prime) + ' + ' + str(diff))
                break                                   # to allow single line of Gold-bach


if __name__ == "__main__":
    main()
