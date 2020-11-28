import collections
import re
# pip install word2number
from num2words import num2words as n2w
from word2number import w2n

numberList = []


def removeLettersFromString(Sstring, Sletters):
    try:
        Sstring = str(Sstring)
        Sletters = str(Sletters)
    except:
        print("the input can not be casted to string")
    for char in Sletters:
        Sstring = Sstring.replace(char, '', 1)
    return Sstring


def stringContainsAllLetters(string, letters):
    counter = 0
    for letter in letters:
        if letter in string:
            counter += 1
            string = removeLettersFromString(string, letter)
        else:
            return False

    return True


def solveAnagramJenna(anagram):
    frequency = collections.Counter(anagram)
    solution = []
    for number, char in (
            (0, 'z'),
            (2, 'w'),
            (4, 'u'),
            (5, 'f'),
            (6, 'x'),
            (7, 's'),
            (8, 'g'),
            (9, 'i'),
            (1, 'o'),
            (3, 't')
    ):
        solution += [number] * frequency[char]
        frequency -= collections.Counter(n2w(number) * frequency[char])
    return sorted(solution)


# add constain if angram contains z,w,u,x,g remove (z)ero, t(w)o, fo(u)r, si(x), ei(g)ht because their appearence is
# unique
def solveAnagram(anagram):
    numberList = []

    if len(anagram) == 0:
        return numberList
    else:
        numbers = ["zero", "one", "two", "three", "four",
                   "five", "six", "seven", "eight", "nine"]
        for number in numbers:
            if stringContainsAllLetters(anagram, number):
                numberList.append(w2n.word_to_num(number))
                oldAnagram = anagram
                anagram = removeLettersFromString(anagram, number)
                result = solveAnagram(anagram)
                if result is not None:
                    for number in result:
                        numberList.append(number)
                    return numberList
                anagram = oldAnagram
                numberList.pop()

# anagram = "noethreesveen"
# anagram = "oentrheeisxevenseerthinenzero"
# anagram = "threesevenfoursixtwo"
# anagram = "fivezerotwo"

# print(solveAnagram("threesevenfoursixtwooneone"))
# print(solveAnagramJenna("fourthreeone"))
