# Good morning! Here's your coding interview problem for today.

# This problem was asked by Slack.

# You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

# For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'. Note that there can be multiple instances of each integer.

# Given this string, return the original integers in sorted order. In the example above, this would be 357.

import re

def removeLettersFromString(Sstring,Sletters):
    for char in Sletters:
        Sstring = Sstring.replace(char,'',1)
    return Sstring

def anagrammToNumber(anagram):

    counter = 0
    realNumber = ""
    DOne = {
        "SNumber": "one",
        "INumber": 1,
        "ILen": 3
    }
    DTwo = {
        "SNumber": "two",
        "INumber": 2,
        "ILen": 3
    }
    DThree = {
        "SNumber": "three",
        "INumber": 3,
        "ILen": 5
    }
    DFour = {
        "SNumber": "four",
        "INumber": 4,
        "ILen": 4
    }
    Dfive = {
        "SNumber": "five",
        "INumber": 5,
        "ILen": 4
    }
    DSix = {
        "SNumber": "six",
        "INumber": 6,
        "ILen": 3
    }
    Dseven = {
        "SNumber": "seven",
        "INumber": 7,
        "ILen": 5
    }
    DEight = {
        "SNumber": "eight",
        "INumber": 8,
        "ILen": 5
    }
    DNine = {
        "SNumber": "nine",
        "INumber": 9,
        "ILen": 4
    }
    DZero = {
        "SNumber": "zero",
        "INumber": 0,
        "ILen": 4
    }

    numbers = [DOne, DTwo, DThree, DFour, Dfive,
               DSix, Dseven, DEight, DNine, DZero]

    for number in numbers:
        for char in number.get("SNumber"):
            if char in anagram:
                counter += 1

        if counter == number.get("ILen"):
            realNumber += str(number.get("INumber"))
            anagram = removeLettersFromString(anagram,number.get("SNumber"))
        counter = 0

    if len(anagram) == 0:
        return realNumber
    else:
        return

anagram = "niesevehrtfeev"
anagram = "eightninesveenwtonoefviehteerxisrouf"


print(anagrammToNumber(anagram))
