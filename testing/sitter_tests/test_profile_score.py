import unittest
import sys
sys.path.append(r"")
from models.stay import Stay
from models.sitter import Sitter
from models.dog import Dog
from models.owner import Owner
from controllers.sitter_controller import sitter_controller

class TestProfileScore(unittest.TestCase):

    # when no distinct letters
    def test_same_letters(self):
        sitter = sitter_controller.addSitter("zzz", "https://images.dog/dog1.jpg", 12345678, "zzz.abc@gmail.com")
        self.assertEqual(
            round(sitter_controller.profile_score_calculator(sitter), 2), 0.19)

    # all distinct letters
    def test_distinct_letters(self):
        sitter = sitter_controller.addSitter(
            "riley jackson", "https://images.dog/dog2.jpg", 22345678, "riley.jackson@gmail.com")
        self.assertEqual(
            round(sitter_controller.profile_score_calculator(sitter), 2), 2.31)

    # combination of cases1&2
    def test_mixed_letters(self):
        sitter = sitter_controller.addSitter(
            "Jim Harrison", "https://images.dog/dog3.jpg", 32345678, "jim.harrison@gmail.com")
        self.assertEqual(
            round(sitter_controller.profile_score_calculator(sitter), 2), 1.73)
        return sitter_controller.profile_score_calculator(sitter)

    # empty string name
    def test_zero_letters(self):
        sitter = sitter_controller.addSitter(
            "", "https://images.dog/dog4.jpg", 44345678, "xyzhge.abcdef@gmail.com")
        self.assertEqual(
            round(sitter_controller.profile_score_calculator(sitter), 2), 0)

    # name containing special characters like .
    def test_special_chars(self):
        sitter = sitter_controller.addSitter(
            "samuel p. jones", "https://images.dog/dog5.jpg", 52345678, "samuel.jones@gmail.com")
        self.assertEqual(
            round(sitter_controller.profile_score_calculator(sitter), 2), 1.92)

    # name in upper and lower cases
    def test_cased_letters(self):
        sitter = sitter_controller.addSitter(
            "Harry Potter", "https://images.dog/dog6.jpg", 62345678, "harry.potter@gmail.com")
        self.assertEqual(
            round(sitter_controller.profile_score_calculator(sitter), 2), 1.54)

# test_profile_scores = TestProfileScore()
if __name__ == '__main__':
    unittest.main()






