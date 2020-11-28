# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

# For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.

import random


def solve(list):
    if(len(list) == 0):
        return

    calc = 0
    for number in list:
        calc += number
        if calc == 0:
            solve(list[list.index(number)+1:])
            return

    print(list[0])
    solve(list[1:])


list = [3, 4, -7, 5, -5523, -6, 6]
randomlist = random.sample(range(-30, 30), 20)
print(randomlist)
solve(randomlist)
