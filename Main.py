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

PhraseType = phrase[randint(0,len(phrase)-1)]
MainPhraseSplitted = []
UserPhraseSplitted = []

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
    Login_Signup = input("Do you want to log in (L) or sign up (S)?\n")

    if Login_Signup.lower() == "l":
        Login()
    elif Login_Signup.lower() == "s":
        SignUp()
    else:
        print(f"Something went wrong, try again")
        LoginSignupChoise()


def SetTime(StartTime, EndTime):
    int(EndTime - StartTime)


def AddTime(time, accuracy = 0):
    Directory = f"{os.getcwd()}/Users/{CurrentUser}"
    Place = os.path.join(Directory, f"{CurrentDate} {CurrentTime}.txt")
    with open(Place, "w") as File:
        File.write(f"Date: {CurrentDate}\n")
        File.write(f"Clock Time: {CurrentTime}\n")
        File.write(f"Your Time: {time} secs \n")
        File.write(f"Your accuracy: {accuracy}%\n")

def Checker(Phrase1, Phrase2):
    global CorrectCounter
    CorrectCounter = 0
    for index in range(len(Phrase1)):
        if Phrase1[index] == Phrase2[index]:
            CorrectCounter += 1


        
def Accuracy():
    if len(MainPhraseSplitted) >= len(UserPhraseSplitted):
        Checker(UserPhraseSplitted, MainPhraseSplitted)
    else:
        Checker(MainPhraseSplitted,UserPhraseSplitted)
    
    global AccuracyPercent
    if CorrectCounter != 0:
        AccuracyPercent = int(CorrectCounter/len(MainPhraseSplitted)*100)
    else:
        AccuracyPercent = 0

def Main():
    MakeStartUserDir()
    LoginSignupChoise()

    print("Please enter this phrase as fast as you can:\n")
    PhraseSplit(PhraseType, MainPhraseSplitted)
    print(PhraseType,"\n")

    StartTime = TimerStart()
    UserInput = input()
    EndTime = TimerEnd()
    Time = SetTime(StartTime, EndTime)

    PhraseSplit(UserInput, UserPhraseSplitted)
    Accuracy()

    AddTime(Time, AccuracyPercent)




if __name__ == "__main__":
    Main()