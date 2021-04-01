# Name: Natapong Sornprom
# Date: May 10, 2020
# Honour Statement: “I have not given or received any unauthorized assistance on this assignment”
# Link: https://youtu.be/EMljcPbgD00

from Assignment0501 import SixSidedDie as SixD
from Assignment0501 import TenSidedDie as TenD
from Assignment0501 import TwentySidedDie as TwentyD
from Assignment0501 import Cup

def main():
    """This is main function where gathers all major functions and allows user to restart the game again
       the starting balance is $100 and next round will allow the accumulated balance
    """

    balance = 100
    name = greetAndName()
    while True:
        startBalance(name, balance)
        enteringGame()
        goal = randomGoal()
        bet = amountBet()
        numSix, numTen, numTwenty = getInput()
        total = rollingDice(numSix, numTen, numTwenty)
        amount = calculateResult(goal, total, balance, bet)
        printResult(name, balance, amount)
        balance = amount
        if decision() != 1:
            break

def greetAndName():
    """This is greetingName function where to greet and get name input from user"""

    print("Welcome to Cup abd Dice Game!!!")
    name = input("Hello, What is your name? : ")
    return name


def startBalance(name, balance):
    """This is startBalance function where initiate the amount of money to play the game"""

    print("Hey, {}. Your balance for this round is ${}".format(name, balance))
    return balance


def enteringGame():
    """This is enteringGame function where """

    ask = input("Do you want to start the game now? [Y/N]: ")
    if ask.lower() == "y":
        print("Let's get started!")
    elif ask.lower() == "n":
        print("Ok!")
        return decision()
    else:
        print("Please enter 'Y' for yes and 'N' for no")
        return enteringGame()


def randomGoal():
    """This is a randomNumber function where to generate a goal from random number between -100"""

    import random
    goal = random.randint(1, 100)
    print("Your goal is: {}".format(goal))
    return goal


def amountBet():
    """This is amountBet function where to ask user for amount of money that they want to play
       the function will allow to bet only $100 at the maximum, though accumulated amount is over $100
    """

    try:
        bet = int(input("How much would you like to bet?: "))
        if bet > 100:
            print("You can bet only $100, enter amount again")
            return amountBet()
        elif bet < 0:
            print("You have to enter positive integer")
            return amountBet()
        return bet

    except ValueError:
        print("Please enter amount $1 - $100 ")
        return amountBet()


def getInput():
    """This is getInput function where ask user to input the amount of eac types of die"""

    try:
        numSix = int(input("How many six sided dices? : "))
        if numSix < 0:
            print("Please enter positive integer")
            return getInput()
        numTen = int(input("How many ten sided dices? : "))
        if numTen < 0:
            print("Please enter positive integer")
            return getInput()
        numTwenty = int(input("How many twenty sided dices? : "))
        if numTwenty < 0:
            print("Please enter positive integer")
            return getInput()
        return numSix, numTen, numTwenty

    except ValueError:
        print("Please enter only integer")
        return getInput()


def rollingDice(numSix, numTen, numTwenty):
    """This is rollingDice function where a cup filled with dices according to the user's input
       then display the result after rolling
    """

    cup = Cup(numSix, numTen, numTwenty)
    total = cup.roll()
    print("Cup({},{},{}) is rolling!!!".format(numSix, numTen, numTwenty))
    print("- - - - - - - - - - ")
    print("The sum is ", total)
    print("- - - - - - - - - - ")
    return total

def calculateResult(goal, total, balance, bet):
    """This is calculateResult function where the final amount is computed with various condition
       if they win the game, bet will be added to next round, but if lose, bet is subtracted
    """

    amount = balance
    if goal == total:
        amount += bet * 10
    elif (goal - total) in range(0, 4):
        amount += bet * 5
    elif (goal - total) in range(0, 11):
        amount += bet * 2
    else:
        amount -= bet
    return amount

def printResult(name, balance, amount):
    """This is printResult function where to print name and updated balance before the next round"""

    if balance < amount:
        print("Congratulations!!, {} your updated balance is {}".format(name, amount))
    elif balance > amount:
        print("That's unlucky, {}! your updated balance is {}".format(name, amount))
    elif balance == amount:
        print("Try again!!, {} your updated balance is {}".format(name, amount))

def decision():
    """This is a decision function where to ask user if they wish to continue or exit"""

    try:
        continueOrNot = int(input("Enter '1' to continue playing with current balance or '0' to exit: "))
        if continueOrNot == 1:
            print("*********************************************************")
            return 1
        elif continueOrNot == 0:
            print("You exited the game, Have a great day!")
            return 0
        elif continueOrNot not in [0, 1]:
            print("Your input is invalid")
            return decision()

    except ValueError:
        print("Your input is invalid")
        return decision()

if __name__ == "__main__":
    main()
