import re
from word2number import w2n

def removeLettersFromString(Sstring, Sletters):
    for char in Sletters:
        Sstring = Sstring.replace(char, '', 1)
    return Sstring


def solveAnagram(anagram):
    if len(anagram) == 0:
        return

    numbers = ["zero", "one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]
    for number in numbers:
        counter = 0
        for char in number:
            if char in anagram:
                counter += 1
            else:
                break
            if counter == len(number):
                print(w2n.word_to_num(number))
                solveAnagram(removeLettersFromString(
                    anagram, number))
                return


anagram = "noethreesveen"
anagram = "oentrheeisxevenseerthinenzero"
solveAnagram(anagram)
