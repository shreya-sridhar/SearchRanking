import unittest
import sys
sys.path.append(r"C:\Users\shrey\SearchRanking")
from models.stay import Stay
from models.sitter import Sitter
from models.dog import Dog
from models.owner import Owner
from controllers.sitter_controller import sitter_controller
from controllers.owner_controller import owner_controller
from controllers.stay_controller import stay_controller

class TestRatingsScore(unittest.TestCase):

    def testAllRatingsScores(self):
        self.stays_equals_zero()
        # self.stays_equals_ten()
        # self.stays_between_zero_and_ten()
        # self.stays_greater_than_ten()

    # when sitter has no stays
    def stays_equals_zero(self):
        sitter = sitter_controller.addSitter("Jim", "https://images.dog/dog1.jpg", 82345678, "zz35z.abc@gmail.com")[1]
        owner = owner_controller.GetOwner("user2555@verizon.net")
        stay1 = stay_controller.AddStay(6/5/2021, "hello there!", [], 6/2/2021, owner, sitter)[1]
        stay1_rated = stay_controller.AddRatingForStay(stay1, 5)
        sitter_controller.setSitter(sitter.sitter_email, 0, 0, 0, [stay1_rated])
        self.assertEqual(
            round(sitter_controller.ratings_score_calculator(sitter), 2), 5.0)

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


test_ratings_scores = TestRatingsScore()
test_ratings_scores.testAllRatingsScores()
