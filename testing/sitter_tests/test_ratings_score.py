import unittest
import sys
import random
sys.path.append(r"C:\Users\shrey\SearchRanking")
from controllers.stay_controller import stay_controller
from controllers.owner_controller import owner_controller
from controllers.sitter_controller import sitter_controller
from models.owner import Owner
from models.dog import Dog
from models.sitter import Sitter
from models.stay import Stay

class TestRatingsScore(unittest.TestCase):

    def testAllRatingsScores(self):
        self.stays_equals_zero()
        self.stays_equals_ten()
        self.stays_between_zero_and_ten()
        self.stays_greater_than_ten()

    # when sitter has no stays
    def stays_equals_zero(self):
        sitter = sitter_controller.addSitter("Jim Harrison", "https://images.dog/dog1.jpg", 82345678, "jim.harrison@gmail.com")
        owner = owner_controller.GetOwner("user2555@verizon.net")
        self.assertEqual(round(sitter_controller.ratings_score_calculator(sitter), 2), 0)
        return sitter_controller.ratings_score_calculator(sitter)

    # # all distinct letters
    def stays_between_zero_and_ten(self):
        sitter = sitter_controller.addSitter(
            "Jim Harrison", "https://images.dog/dog1.jpg", 82345678, "jim.harrison@gmail.com")
        owner = owner_controller.GetOwner("user2555@verizon.net")
        stays = []
        for i in range(5):
            stay = stay_controller.AddStay(
                6/5/2021+i, "hello there!", [], 6/2/2021+i, owner, sitter)[1]
            stay_rated = stay_controller.AddRatingForStay(stay, i % 5)
            stays.append(stay)
        sitter_controller.setSitter(sitter.sitter_email, 0, 0, 0, stays)
        self.assertEqual(
            round(sitter_controller.ratings_score_calculator(sitter), 2), 2)
        return sitter_controller.ratings_score_calculator(sitter)

    # # combination of cases1&2
    def stays_equals_ten(self):
        sitter = sitter_controller.addSitter(
            "Jim Harrison", "https://images.dog/dog1.jpg", 82345678, "jim.harrison@gmail.com")
        owner = owner_controller.GetOwner("user2555@verizon.net")
        stays = []
        for i in range(9):
            stay = stay_controller.AddStay(
                6/5/2021+i, "hello there!", [], 6/2/2021+i, owner, sitter)[1]
            stay_rated = stay_controller.AddRatingForStay(stay, i % 5)
            stays.append(stay)
        sitter_controller.setSitter(sitter.sitter_email, 0, 0, 0, stays)
        self.assertEqual(
            round(sitter_controller.ratings_score_calculator(sitter), 2), 1.78)
        return sitter_controller.ratings_score_calculator(sitter)

    def stays_greater_than_ten(self):
        sitter = sitter_controller.addSitter(
            "Jim Harrison", "https://images.dog/dog1.jpg", 82345678, "jim.harrison@gmail.com")
        owner = owner_controller.GetOwner("user2555@verizon.net")
        stays = []
        for i in range(16):
            stay = stay_controller.AddStay(
                6/5/2021+i, "hello there!", [], 6/2/2021+i, owner, sitter)[1]
            stay_rated = stay_controller.AddRatingForStay(stay, i % 5)
            stays.append(stay)
        sitter_controller.setSitter(sitter.sitter_email, 0, 0, 0, stays)
        self.assertEqual(
            round(sitter_controller.ratings_score_calculator(sitter), 2), 1.88)
        return sitter_controller.ratings_score_calculator(sitter)

test_ratings_scores = TestRatingsScore()





