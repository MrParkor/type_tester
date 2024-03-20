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

class Parrent():
    def __init__(self):
        MakeStartUserDir()
        LoginSignupChoise()

        print("Please enter this phrase as fast as you can:\n")


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
    return int(EndTime - StartTime)


def WriteTime(time, accuracy, difficulty):
    Directory = f"{os.getcwd()}/Users/{CurrentUser}"
    Place = os.path.join(Directory, f"{CurrentDate} {CurrentTime}.txt")
    with open(Place, "w") as File:
        File.write(f"Date: {CurrentDate}\n")
        File.write(f"Clock Time: {CurrentTime}\n")
        File.write(f"Difficulty: {difficulty}\n")
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

def ChooseDifficulty():
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