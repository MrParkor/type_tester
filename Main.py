from phrases import *
from random import randint
import time
import datetime
import os

now = datetime.datetime.now()
CurrentDateTime = now.strftime("%d/%m/%Y %H:%M:%S")

CurrentDirectory = os.getcwd()
CreateUserDir = os.path.join(CurrentDirectory, "Users")
UsersDirectory = f"{CurrentDirectory}/Users"
OSUserDirectory = os.path.join(UsersDirectory)

PhraseType = phrase[randint(0,len(phrase)-1)]
LetterPhraseSplitted = []
UserPhrase = []
def PhraseSplit(SplittingPhrase, List):
    for Letter in SplittingPhrase:
        List.append(Letter)

def StartTime():
    time.time()

def EndTime():
    time.time()

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
        input("Test")
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


def main():
    LoginSignupChoise()
    print("Please enter this phrase as fast as you can:\n")
    PhraseSplit(PhraseType, LetterPhraseSplitted)
    time.sleep(3)
    print(PhraseType)
    StartTime()
    UserInput = input()
    EndTime()
    PhraseSplit(UserInput, UserPhrase)

if __name__ == "__main__":
    main()