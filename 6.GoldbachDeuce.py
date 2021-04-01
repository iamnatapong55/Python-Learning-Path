
def main():
    """This is a main function where allows program to re-generate a random list if no pair found"""

    printIntro()
    i = getInput_i()
    target = getInput_n()
    while True:
        sortedNum = randomNumber(i)
        if GoldBachDeuce(sortedNum, target):
            break


def printIntro():
    """This is a printIntro function, giving an overview of how program works"""

    print("#################################################################")
    print("This program will consider the random number between 1 - 100 only")
    print("......Thus, target sum number will allow only less than 200......")
    print("#################################################################")


def getInput_i():
    """This is a getInput_i function where to collect no. of random number in a list"""

    try:
        i = int(input("Enter no. of random number you want to generate:  "))
        if i < 2 or i > 100:                                # control too large number, out of random range
            print("Please enter integer between 2 - 100")
            return getInput_i()
        return i
    except ValueError:
        print("Please enter only integer")
        return getInput_i()


def getInput_n():
    """This is a getInput_n function where to collect a targeted sum number"""

    try:
        n = int(input("What target sum do you expect ?: "))
        if n < 2 or n > 200:                                # control min and max sum from smallest and largest random
            print("Target sum should be between 2 - 200")
            return getInput_n()
        target = n
        return target
    except ValueError:
        print("Please enter integer")
        return getInput_n()


def randomNumber(i):
    """This is a randomNumber function where to generate a list of random number and rearrange in ascending"""

    import random
    randomNum = random.sample(range(1, 101), i)            # random number including 1 - 100
    sortedNum = sorted(randomNum)                          # rearrange number in the list
    print("The random number is: {}".format(sortedNum))
    return sortedNum


def GoldBachDeuce(sortedNum, target):
    """This is a GoldBachDeuce function where to determine if two of the numbers sum to n in O(n.log(n))
       The function is supposed to print out the first pair if found, otherwise return for regenerating random list
    """

    for num in sortedNum:                                  # iteration allows time complexity of O(n)
        start = 0                                          # binary search allows time complexity of O(log n)
        end = len(sortedNum) - 1                           # O(n) x O(log n) = n log n
        while start <= end:                                # start <+ end allowing sum of itself ex. 1+ 1 = 2
            mid = (start + end) // 2
            if num + sortedNum[mid] == target:
                print("Yes! Here is one pair found: {} + {} = {}".format(num, sortedNum[mid], target))
                return True
            elif target < sortedNum[mid]:
                end = mid - 1                              # move top marker down
            else:
                start = mid + 1                            # move bottom marker up
    print("No pair found in the current list, trying the next random number")
    return False                                           # return for regenerating new list until found a pair


if __name__ == "__main__":
    main()
