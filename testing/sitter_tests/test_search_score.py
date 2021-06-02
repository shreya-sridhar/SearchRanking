import unittest
import sys
import random
sys.path.append(r"C:\Users\shrey\SearchRanking")
from testing.sitter_tests.test_ratings_score import TestRatingsScore
from testing.sitter_tests.test_profile_score import TestProfileScore
from models.stay import Stay
from models.sitter import Sitter
from models.dog import Dog
from models.owner import Owner
from controllers.sitter_controller import sitter_controller
from controllers.owner_controller import owner_controller
from controllers.stay_controller import stay_controller

class TestSearchScore(unittest.TestCase):

    # when sitter has no stays
    def stays_equals_zero(self):
        profile_score = TestProfileScore.test_mixed_letters()
        ratings_score = TestRatingsScore.test_stays_equals_zero()
        sitter = sitter_controller.GetSitter("jim.harrison@gmail.com")
        self.assertEqual(round(sitter_controller.search_score_calculator(sitter, profile_score, ratings_score), 2), 1.73)

    # sitters has greater then 0 and less than 10 stays
    def stays_between_zero_and_ten(self):
        profile_score = TestProfileScore.test_mixed_letters()
        ratings_score = TestRatingsScore.test_stays_between_zero_and_ten()
        sitter = sitter_controller.GetSitter("jim.harrison@gmail.com")
        self.assertEqual(
            round(sitter_controller.search_score_calculator(sitter, profile_score, ratings_score), 2), 1.87)

    # sitter has 10 stays
    def stays_equals_ten(self):
        profile_score = TestProfileScore.test_mixed_letters()
        ratings_score = TestRatingsScore.test_stays_equals_ten()
        sitter = sitter_controller.GetSitter("jim.harrison@gmail.com")
        self.assertEqual(
            round(sitter_controller.search_score_calculator(sitter, profile_score, ratings_score), 2), 1.77)

    # sitter has more than 10 stays
    def stays_greater_than_ten(self):
        profile_score = TestProfileScore.test_mixed_letters()
        ratings_score = TestRatingsScore.test_stays_greater_than_ten()
        sitter = sitter_controller.GetSitter("jim.harrison@gmail.com")
        self.assertEqual(
            round(sitter_controller.search_score_calculator(sitter, profile_score, ratings_score), 2), 1.88)

test_Search_scores = TestSearchScore()
if __name__ == '__main__':
    unittest.main()









