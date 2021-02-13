import unittest

from UserIO import UserIO
from Bot import Bot
from GameEngine import GameEngine

class Test(unittest.TestCase):

    def test_validateInput(self):
        self.assertFalse(UserIO().validateInput("", 6)[0])
        self.assertFalse(UserIO().validateInput("abc", 6)[0])
        self.assertFalse(UserIO().validateInput("1 3 0 5", 6)[0])
        self.assertFalse(UserIO().validateInput("5 2 14", 6)[0])
        self.assertTrue(UserIO().validateInput("2 12 5 8", 12)[0])
        
    def test_botStupidity(self):
        self.assertEqual(Bot(0).pickDice([2, 3, 4, 5, 6]), [3])
        self.assertEqual(Bot(50).pickDice([1, 2, 3, 5, 6]), [1, 2, 3])
        self.assertEqual(Bot(100).pickDice([2, 3, 4, 5, 6]), [1, 2, 3, 4, 5])
        
    def test_botPick(self):
        self.assertEqual(Bot(0).pickDice([6]), [1])
        self.assertEqual(Bot(0).pickDice([1, 2, 3, 4]), [4])
        self.assertEqual(Bot(0).pickDice([4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4]), [1, 2, 3, 4, 5, 6, 7, 9, 10, 11])

    def test_scoreDice(self): #valid only with default ZERO_DICE value
        self.assertEqual(GameEngine().scoreDice([2, 4, 5]), 7)

if __name__ == '__main__':
    unittest.main()