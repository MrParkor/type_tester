from phrases import *
from random import randint
import time
import datetime
import os


# Variables
now = datetime.datetime.now()
CurrentDateTime = now.strftime("%d/%m/%Y %H:%M:%S")

CurrentDirectory = os.getcwd()
CreateUserDir = os.path.join(CurrentDirectory, "Users")
UsersDirectory = f"{CurrentDirectory}/Users"
OSUserDirectory = os.path.join(UsersDirectory)

PhraseType = phrase[randint(0,len(phrase)-1)]
LetterPhraseSplitted = []
UserPhrase = []

# Functions
def PhraseSplit(SplittingPhrase, List):
    """
    The function `PhraseSplit` takes a phrase and splits it into individual letters, adding each letter
    to a list.
    
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
    :return: The function `TimerStart()` is returning the current time when it is called using
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
    The `Login` function prompts the user to enter a username, creates a directory based on the
    username, and handles login success or failure.
    """
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
    calls the respective functions based on the input.
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
    
    :param StartTime: The `StartTime` parameter represents the starting time of an event or process. It
    could be a specific point in time, such as the beginning of a task or an event
    :param EndTime: The `EndTime` parameter represents the time when a particular event or process ends
    :return: The function SetTime returns the difference between the EndTime and StartTime as an
    integer.
    """
    return int(EndTime - StartTime)


def main():
    MakeStartUserDir()
    LoginSignupChoise()

    print("Please enter this phrase as fast as you can:\n")
    PhraseSplit(PhraseType, LetterPhraseSplitted)
    print(PhraseType,"\n")

    StartTime = TimerStart()
    UserInput = input()
    EndTime = TimerEnd()
    print(f"Your Time was: {SetTime(StartTime, EndTime)} secs")

    PhraseSplit(UserInput, UserPhrase)




if __name__ == "__main__":
    main()