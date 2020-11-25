# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Write a function that takes a natural number as input and returns the number of digits the input has.

# Constraint: don't use any loops.

import re

def getDigits(number):
    SNumber = str(number)
    pattern = re.compile("^[1-9][0-9]*")
    if pattern.fullmatch(SNumber):
        return len(SNumber)
    else:
        return

print(getDigits(42))


