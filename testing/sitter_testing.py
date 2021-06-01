import unittest
import sys
sys.path.append(r"C:\Users\shrey\SearchRanking")
from models.stay import Stay
from models.sitter import Sitter
from models.dog import Dog
from models.owner import Owner
from controllers.sitter_controller import SitterController

class TestProfileScore(unittest.TestCase):

    def __init__(self):
        self.controllers = SitterController()

    def testAllProfileScores(self):
        self.same_letters_test()
        self.distinct_letters_test()
        self.mixed_letters_test()
        self.zero_letters_test()
        self.special_chars_test()
        self.cased_letters_test()

    # when no distinct letters
    def same_letters_test(self):
        sitter = Sitter(1, "Zzzz", "xyz.com", 1234567889,
                        "zzz.jackson@gmail.com", [], 0, 0, 0)
        self.assertEqual(self.controllers.profile_score_calculator(sitter), 0)
        return

    # # all distinct letters
    def distinct_letters_test(self):
        sitter = Sitter(1, "Riley Jackson", "xyz.com", 2234567889,
                        "riley.jackson@gmail.com", [], 0, 0, 0)
        self.assertEqual(self.controllers.profile_score_calculator(sitter), 0)
        return

    # # combination of cases1&2
    def mixed_letters_test(self):
        sitter = Sitter(2, "Casey Sanders", "xdfyz.com", 3234567889,
                        "casey.sanders@gmail.com", [], 0, 0, 0)
        self.assertEqual(self.controllers.profile_score_calculator(sitter), 0)
        return

    # # null name
    def zero_letters_test(self):
        sitter = Sitter(3, "", "xyfgz.com", 4234567889,
                        "harry.sanders@gmail.com", [], 0, 0, 0)
        self.assertEqual(self.controllers.profile_score_calculator(sitter), 0)
        return

    # # name containing special characters like .
    def special_chars_test(self):
        sitter = Sitter(4, "samuel p. jones", "xyfdfgz.com", 5234567889,
                        "samuel.jones@gmail.com", [], 0, 0, 0)
        self.assertEqual(self.controllers.profile_score_calculator(sitter), 0)
        return

    # # name in upper and lower cases
    def cased_letters_test(self):
        sitter = Sitter(5, "Harry Potter", "xyfdgz.com", 6234567889,
                        "harry.potter@gmail.com", [], 0, 0, 0)
        self.assertEqual(self.controllers.profile_score_calculator(sitter), 0)
        return
    



test_profile_scores = TestProfileScore()
test_profile_scores.testAllProfileScores()




