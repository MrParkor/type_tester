
# Modules
from phrases import *
from random import randint
import time
import datetime
import os


# Variables
now = datetime.datetime.now()
CurrentDate = str(now.strftime("%d-%m-%Y"))
CurrentTime = str(now.strftime("%H.%M"))

CurrentDirectory = os.getcwd()
CreateUserDir = os.path.join(CurrentDirectory, "Users")
UsersDirectory = f"{CurrentDirectory}/Users"
OSUserDirectory = os.path.join(UsersDirectory)

TestPhraseType = TestPhrase[randint(0,len(TestPhrase)-1)]
MainPhraseSplitted = []
UserPhraseSplitted = []

# Classes

# The class `Parrent` initializes by creating a user directory and prompting the user to choose
# between logging in or signing up before displaying a message.
class Parrent():
    def __init__(self):
        MakeStartUserDir()
        LoginSignupChoise()

        print("Please enter this phrase as fast as you can:\n")


# The `Beginner` class in Python is designed to help beginners practice typing phrases and measure
# their accuracy and speed.
class Beginner(Parrent):
    def __init__(self):
        super().__init__()
        
        Phrase = BeginnerPhrase[randint(0,len(BeginnerPhrase)-1)]

        PhraseSplit(Phrase, MainPhraseSplitted)
        print(MainPhraseSplitted,"\n")

        StartTime = TimerStart()
        UserInput = input()
        EndTime = TimerEnd()
        Time = SetTime(StartTime, EndTime)

        Checker(UserPhraseSplitted, MainPhraseSplitted)

        PhraseSplit(UserInput, UserPhraseSplitted)
        Accuracy()

        WriteTime(Time, AccuracyPercent, __class__.__name__)
        print(Time)

# The `Intermidiate` class is designed to handle user input, check its accuracy against a main phrase,
# and record timing and accuracy metrics.
class Intermidiate(Parrent):
    def __init__(self):
        super().__init__()
        
        Phrase = IntiermidiatePhrase[randint(0,len(IntiermidiatePhrase)-1)]

        PhraseSplit(Phrase, MainPhraseSplitted)
        print(MainPhraseSplitted,"\n")

        StartTime = TimerStart()
        UserInput = input()
        EndTime = TimerEnd()
        Time = SetTime(StartTime, EndTime)

        Checker(UserPhraseSplitted, MainPhraseSplitted)

        PhraseSplit(UserInput, UserPhraseSplitted)
        Accuracy()

        WriteTime(Time, AccuracyPercent, __class__.__name__)
        print(Time)

# This Python class `Expert` initializes with a random phrase, prompts user input, calculates time
# taken, checks accuracy, and writes time and accuracy to a file.
class Expert(Parrent):
    def __init__(self):
        super().__init__()
        
        Phrase = ExpertPhrase[randint(0,len(ExpertPhrase)-1)]

        PhraseSplit(Phrase, MainPhraseSplitted)
        print(MainPhraseSplitted,"\n")

        StartTime = TimerStart()
        UserInput = input()
        EndTime = TimerEnd()
        Time = SetTime(StartTime, EndTime)

        Checker(UserPhraseSplitted, MainPhraseSplitted)

        PhraseSplit(UserInput, UserPhraseSplitted)
        Accuracy()

        WriteTime(Time, AccuracyPercent, __class__.__name__)
        print(Time)


def PhraseSplit(SplittingPhrase, List):
    """
    The function `PhraseSplit` takes a phrase and appends each letter to a given list.
    
    :param SplittingPhrase: The `SplittingPhrase` parameter is the phrase or string that you want to
    split into individual letters
    :param List: The `List` parameter in the `PhraseSplit` function is a list that will store the
    individual letters of the `SplittingPhrase` after splitting
    """
    for Letter in SplittingPhrase:
        List.append(Letter)

def TimerStart():
    """
    The function `TimerStart()` returns the current time when called.
    :return: The `TimerStart()` function is returning the current time when it is called using
    `time.time()`.
    """
    return time.time()

def TimerEnd():
    """
    The function `TimerEnd` returns the current time when called.
    :return: The function `TimerEnd()` is returning the current time when it is called using
    `time.time()`.
    """
    return time.time()

def MakeStartUserDir():
    """
    The function attempts to create a Users folder if it does not already exist.
    """
    try: # Make the Users Folder if it doesn't exist
        os.mkdir(CreateUserDir)
    except:
        pass

def SignUp():
    """
    The function `SignUp` prompts the user to enter a username, creates a directory with that username,
    and handles cases where the username already exists.
    """
    UserName = input("Please enter your Username: ")
    UserDir = os.path.join(OSUserDirectory, UserName)
    try:
        os.mkdir(UserDir)
    except:
        print("That User Already Exists try again \n")
        SignUp()

def Login():
    """
    The `Login` function prompts the user to enter a username, creates a directory for the user, and
    handles login success or failure.
    """
    global CurrentUser
    CurrentUser = input("Please enter the username: ")
    UserDir = os.path.join(OSUserDirectory, CurrentUser)
    try:
        os.mkdir(UserDir)
    except: # If successful login
        print("Success")
    else:
        print("User doesn't exist... Try again\n")
        os.rmdir(UserDir)
        Login()


def LoginSignupChoise():
    """
    The function `LoginSignupChoise` prompts the user to choose between logging in or signing up and
    then calls the respective functions based on the user's choice.
    """
    Login_Signup = input("Do you want to log in (L) or sign up (S)?\n")

    if Login_Signup.lower() == "l":
        Login()
    elif Login_Signup.lower() == "s":
        SignUp()
    else:
        print(f"Something went wrong, try again")
        LoginSignupChoise()


def SetTime(StartTime, EndTime):
    """
    The function SetTime calculates the difference in time between a start time and an end time.
    
    :param StartTime: The `StartTime` parameter represents the starting time, typically in a numerical
    format such as a timestamp or a numerical value representing a specific time
    :param EndTime: The `EndTime` parameter represents the time at which a particular event or process
    ends. It could be a specific point in time, such as the end of a task or the completion of an
    activity
    :return: The function `SetTime` returns the difference between `EndTime` and `StartTime` as an
    integer.
    """
    return int(EndTime - StartTime)


def WriteTime(time, accuracy, difficulty):
    """
    The function `WriteTime` writes time-related data to a text file in a specified directory.
    
    :param time: The `time` parameter in the `WriteTime` function represents the amount of time taken to
    complete a task or activity, typically measured in seconds
    :param accuracy: Accuracy refers to how close a measured value is to the true value. It is often
    expressed as a percentage and indicates the precision of the measurement. In the context of the
    `WriteTime` function you provided, accuracy would likely refer to the precision or correctness of
    the time measurement or task completion
    :param difficulty: The `WriteTime` function you provided seems to be writing some information to a
    text file. However, it seems like you haven't defined `CurrentUser`, `CurrentDate`, and
    `CurrentTime` in the function. You will need to pass these variables as arguments to the function or
    define them within
    """
    Directory = f"{os.getcwd()}/Users/{CurrentUser}"
    Place = os.path.join(Directory, f"{CurrentDate} {CurrentTime}.txt")
    with open(Place, "w") as File:
        File.write(f"Date: {CurrentDate}\n")
        File.write(f"Clock Time: {CurrentTime}\n")
        File.write(f"Difficulty: {difficulty}\n")
        File.write(f"Your Time: {time} secs \n")
        File.write(f"Your accuracy: {accuracy}%\n")

def Checker(Phrase1, Phrase2):
    """
    The function `Checker` compares two phrases character by character and counts the number of correct
    matches.
    
    :param Phrase1: The function `Checker` takes two input parameters `Phrase1` and `Phrase2`, which are
    strings that are being compared character by character. The function then counts the number of
    characters that match at the same position in both phrases and stores the count in the global
    variable `CorrectCounter`
    :param Phrase2: It looks like you have defined a function called `Checker` that takes two parameters
    `Phrase1` and `Phrase2`. The function compares the characters at each index of `Phrase1` and
    `Phrase2`, and increments a global variable `CorrectCounter` if the characters match
    """
    global CorrectCounter
    CorrectCounter = 0
    for index in range(len(Phrase1)):
        if Phrase1[index] == Phrase2[index]:
            CorrectCounter += 1


        
def Accuracy():
    """
    The `Accuracy` function calculates the accuracy percentage of a user's input compared to a main
    phrase by checking the correctness of each word.
    """
    if len(MainPhraseSplitted) >= len(UserPhraseSplitted):
        Checker(UserPhraseSplitted, MainPhraseSplitted)
    else:
        Checker(MainPhraseSplitted,UserPhraseSplitted)
    
    global AccuracyPercent
    if CorrectCounter != 0:
        AccuracyPercent = int(CorrectCounter/len(MainPhraseSplitted)*100)
    else:
        AccuracyPercent = 0

def ChooseDifficulty():
    """
    The function ChooseDifficulty allows the user to select a desired difficulty level (Beginner,
    Intermediate, Expert) for a game.
    """
    Difficulty = input("Please enter you disired difficulty:\nBeginner (B)\nIntermidiate (I)\nExpert (E)\n").lower()
    if Difficulty == "b":
        Beginner()
    elif Difficulty == "i":
        Intermidiate()
    elif Difficulty == "e":
        Expert()
    else:
        print("didn't understand: Please try again")
        ChooseDifficulty()

if __name__ == "__main__":
    ChooseDifficulty()
