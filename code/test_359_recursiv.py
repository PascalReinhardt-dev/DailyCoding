import unittest
import random
import Problem_359_recursiv
from num2words import num2words as n2w


class Test359_recursiv(unittest.TestCase):
    def test_removeLettersFromString(self):
        self.assertEqual(Problem_359_recursiv.removeLettersFromString("Test","es"), "Tt")
        self.assertEqual(Problem_359_recursiv.removeLettersFromString("","Test"),"")
        self.assertEqual(Problem_359_recursiv.removeLettersFromString("Test",""),"Test")
        self.assertEqual(Problem_359_recursiv.removeLettersFromString(2323,2323),"")
        self.assertEqual(Problem_359_recursiv.removeLettersFromString([4,23,4543,],"23"),"[4, , 4543]")

    def test_solveAnagram(self):

        for a in range(0,10**2):
            anagram = ''
            number = []
            for x in random.sample(range(0, 9), 3):
                anagram+=n2w(x)
                number.append(x)
            number = sorted(number)
            result = Problem_359_recursiv.solveAnagram(anagram)
            print(result)
            self.assertEqual(result,number)






if __name__ == '__main__':
    unittest.main()
