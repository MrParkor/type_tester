from phrases import *
from random import randint
import time

PhraseType = phrase[randint(0,len(phrase)-1)]
LetterPhrase = []
LetterUser = []
def PhraseSplit(SplittingPhrase, List):
    for Letter in SplittingPhrase:
        List.append(Letter)

print(LetterPhrase)

def StartTime():
    time.time()

def EndTime():
    time.time()



def main():
    print("Please enter this phrase as fast as you can:\n")
    PhraseSplit(PhraseType, LetterPhrase)
    time.sleep(1)
    print(PhraseType)
    StartTime()
    UserInput = input()
    EndTime()
    PhraseSplit(UserInput, LetterUser)

