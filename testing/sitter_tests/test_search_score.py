import unittest
import sys
import random
sys.path.append(r"C:\Users\shrey\SearchRanking")
from testing.sitter_tests.test_ratings_score import test_ratings_scores
from testing.sitter_tests.test_profile_score import test_profile_scores
from models.stay import Stay
from models.sitter import Sitter
from models.dog import Dog
from models.owner import Owner
from controllers.sitter_controller import sitter_controller
from controllers.owner_controller import owner_controller
from controllers.stay_controller import stay_controller

class TestSearchScore(unittest.TestCase):

    def testAllSearchScores(self):
        self.stays_equals_zero()
        self.stays_equals_ten()
        self.stays_between_zero_and_ten()
        self.stays_greater_than_ten()

    # when sitter has no stays
    def stays_equals_zero(self):
        profile_score = test_profile_scores.mixed_letters_test()
        ratings_score = test_ratings_scores.stays_equals_zero()
        sitter = sitter_controller.GetSitter("jim.harrison@gmail.com")
        self.assertEqual(round(sitter_controller.search_score_calculator(sitter, profile_score, ratings_score), 2), 1.73)

    # # all distinct letters
    def stays_between_zero_and_ten(self):
        profile_score = test_profile_scores.mixed_letters_test()
        ratings_score = test_ratings_scores.stays_between_zero_and_ten()
        sitter = sitter_controller.GetSitter("jim.harrison@gmail.com")
        self.assertEqual(
            round(sitter_controller.search_score_calculator(sitter, profile_score, ratings_score), 2), 1.87)

    # # combination of cases1&2
    def stays_equals_ten(self):
        profile_score = test_profile_scores.mixed_letters_test()
        ratings_score = test_ratings_scores.stays_equals_ten()
        sitter = sitter_controller.GetSitter("jim.harrison@gmail.com")
        self.assertEqual(
            round(sitter_controller.search_score_calculator(sitter, profile_score, ratings_score), 2), 1.77)

    def stays_greater_than_ten(self):
        profile_score = test_profile_scores.mixed_letters_test()
        ratings_score = test_ratings_scores.stays_greater_than_ten()
        sitter = sitter_controller.GetSitter("jim.harrison@gmail.com")
        self.assertEqual(
            round(sitter_controller.search_score_calculator(sitter, profile_score, ratings_score), 2), 1.88)

test_Search_scores = TestSearchScore()
test_Search_scores.testAllSearchScores()




