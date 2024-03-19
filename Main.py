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
    for Letter in SplittingPhrase:
        List.append(Letter)

def TimerStart():
    return time.time()

def TimerEnd():
    return time.time()

def MakeStartUserDir():
    try: # Make the Users Folder if it doesn't exist
        os.mkdir(CreateUserDir)
    except:
        pass

def SignUp():
    UserName = input("Please enter your Username: ")
    UserDir = os.path.join(OSUserDirectory, UserName)
    try:
        os.mkdir(UserDir)
    except:
        print("That User Already Exists try again \n")
        SignUp()

def Login():
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
    Login_Signup = input("Do you want to log in (L) or sign up (S)?\n")

    if Login_Signup.lower() == "l":
        Login()
    elif Login_Signup.lower() == "s":
        SignUp()
    else:
        print(f"Something went wrong, try again")
        LoginSignupChoise()


def SetTime(StartTime, EndTime):
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