import unittest
import sys
sys.path.append(r"C:\Users\shrey\SearchRanking")
from models.stay import Stay
from models.sitter import Sitter
from models.dog import Dog
from models.owner import Owner
from controllers.sitter_controller import sitter_controller

class TestProfileScore(unittest.TestCase):

    def testAllProfileScores(self):
        self.same_letters_test()
        self.distinct_letters_test()
        self.mixed_letters_test()
        self.zero_letters_test()
        self.special_chars_test()
        self.cased_letters_test()

    # when no distinct letters
    def same_letters_test(self):
        sitter = sitter_controller.addSitter("zzz", "https://images.dog/dog1.jpg", 12345678, "zzz.abc@gmail.com")[1]
        self.assertEqual(
            round(sitter_controller.profile_score_calculator(sitter), 2), 0.19)

    # # all distinct letters
    def distinct_letters_test(self):
        sitter = sitter_controller.addSitter(
            "riley jackson", "https://images.dog/dog2.jpg", 22345678, "riley.jackson@gmail.com")[1]
        self.assertEqual(
            round(sitter_controller.profile_score_calculator(sitter), 2), 2.31)

    # # combination of cases1&2
    def mixed_letters_test(self):
        sitter = sitter_controller.addSitter(
            "casey sanders", "https://images.dog/dog3.jpg", 32345678, "casey.sanders@gmail.com")[1]
        self.assertEqual(
            round(sitter_controller.profile_score_calculator(sitter), 2), 1.54)

    # # null name
    def zero_letters_test(self):
        sitter = sitter_controller.addSitter(
            "", "https://images.dog/dog4.jpg", 44345678, "xyzhge.abcdef@gmail.com")[1]
        self.assertEqual(
            round(sitter_controller.profile_score_calculator(sitter), 2), 0)

    # # name containing special characters like .
    def special_chars_test(self):
        sitter = sitter_controller.addSitter(
            "samuel p. jones", "https://images.dog/dog5.jpg", 52345678, "samuel.jones@gmail.com")[1]
        self.assertEqual(
            round(sitter_controller.profile_score_calculator(sitter), 2), 1.92)

    # # name in upper and lower cases
    def cased_letters_test(self):
        sitter = sitter_controller.addSitter(
            "Harry Potter", "https://images.dog/dog6.jpg", 62345678, "harry.potter@gmail.com")[1]
        self.assertEqual(
            round(sitter_controller.profile_score_calculator(sitter), 2), 1.54)

test_profile_scores = TestProfileScore()
test_profile_scores.testAllProfileScores()


