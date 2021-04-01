
def gradingLogic():
    """
    This function will ask user a series of questions. If answer is no, it will end.
    If all answers are yes, user can enter score as specified, then decide whether the submission is late or not.
    Program will return the total score including the late-submission penalty. Warning msg is displayed when detect
    invalid value.
    """

    question1 = input("Does a student submit a single uncompressed .py file? [yes/no] ")
    if question1.lower() not in ['yes']:  # using lower() to control capital letter from input
        print("Sorry, the grade is 0")
        return 0  # execution will end if user enter no or others
    question2 = input("Are both name and date included? [yes/no] ")
    if question2.lower() not in ['yes']:
        print("Sorry, the grade is 0")
        return 0
    question3 = input("Does a student provide the honor statement? [yes/no] ")
    if question3.lower() not in ['yes']:
        print("Sorry, the grade is 0")
        return 0
    question4 = input("Is the link to a 3-minute VDO presentation provided? [yes/no] ")
    if question4.lower() not in ['yes']:
        print("Sorry, the grade is 0")
        return 0

    # Using try and except blocks to handle error from inappropriate value as it is meant to enter only int
    try:
        criteria1 = int(input("Out of three points, how would you evaluate the correctness of the code? : "))
        criteria2 = int(input("Out of three points, how would you evaluate based on the elegance of the code? : "))
        criteria3 = int(input("Out of two points, how would you evaluate based on the code hygiene? : "))
        criteria4 = int(input("Out of two points, how would you evaluate based on the quality of the discussion in "
                              "the YouTube video? : "))

        lateSubmission = input("is the assignment late submitted ? [yes/no]  ")
        numberOfHour = 0
        if lateSubmission.lower() == "yes":
            numberOfHour = int(input("Number of hour for late submission : "))
        score = criteria1 + criteria2 + criteria3 + criteria4 - (numberOfHour * 0.01)
        print("The final grade is as below: ")
        return score

    # except block catches ValueError from try block
    # ValueError: raised when a function receives an inappropriate value
    except ValueError:
        print("\n")
        print("****  Your input is not valid, please restart and enter 'Integer' numbers  ****")


if __name__ == "__main__":
    # print(gradingLogic.__doc__)

    print("************************************************")
    print("Welcome to the grading logic program for DSC 430")
    print("************************************************")
    print(gradingLogic())
    print("End of evaluation, have a good day!")
