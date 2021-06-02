import unittest
import sys
import random
sys.path.append(r"")
from controllers.stay_controller import stay_controller
from controllers.owner_controller import owner_controller
from controllers.sitter_controller import sitter_controller
from models.owner import Owner
from models.dog import Dog
from models.sitter import Sitter
from models.stay import Stay

class TestRatingsScore(unittest.TestCase):

    # when sitter has no stays
    def test_stays_equals_zero(self):
        sitter = sitter_controller.add_sitter("Jim Harrison", "https://images.dog/dog1.jpg", 82345678, "jim.harrison@gmail.com")
        owner = owner_controller.get_owner("user2555@verizon.net")
        stays = []
        sitter_controller.set_sitter(sitter.sitter_email, 0, 0, 0, stays)
        self.assertEqual(round(sitter_controller.ratings_score_calculator(sitter), 2), 0)
        return sitter_controller.ratings_score_calculator(sitter)

    # sitter has greater than 0 and less than 10 stays
    def test_stays_between_zero_and_ten(self):
        sitter = sitter_controller.add_sitter(
            "Jim Harrison", "https://images.dog/dog1.jpg", 82345678, "jim.harrison@gmail.com")
        owner = owner_controller.get_owner("user2555@verizon.net")
        stays = []
        for i in range(5):
            stay = stay_controller.add_stay(
                6/5/2021+i, "hello there!", [], 6/2/2021+i, owner, sitter)
            stay_rated = stay_controller.add_rating_for_stay(stay, i % 5)
            stays.append(stay)
        sitter_controller.set_sitter(sitter.sitter_email, 0, 0, 0, stays)
        self.assertEqual(
            round(sitter_controller.ratings_score_calculator(sitter), 2), 2)
        return sitter_controller.ratings_score_calculator(sitter)

    # sitter has 10 stays
    def test_stays_equals_ten(self):
        sitter = sitter_controller.add_sitter(
            "Jim Harrison", "https://images.dog/dog1.jpg", 82345678, "jim.harrison@gmail.com")
        owner = owner_controller.get_owner("user2555@verizon.net")
        stays = []
        for i in range(9):
            stay = stay_controller.add_stay(
                6/5/2021+i, "hello there!", [], 6/2/2021+i, owner, sitter)
            stay_rated = stay_controller.add_rating_for_stay(stay, i % 5)
            stays.append(stay)
        sitter_controller.set_sitter(sitter.sitter_email, 0, 0, 0, stays)
        self.assertEqual(
            round(sitter_controller.ratings_score_calculator(sitter), 2), 1.78)
        return sitter_controller.ratings_score_calculator(sitter)

    # sitter has greater than 10 stays
    def test_stays_greater_than_ten(self):
        sitter = sitter_controller.add_sitter(
            "Jim Harrison", "https://images.dog/dog1.jpg", 82345678, "jim.harrison@gmail.com")
        owner = owner_controller.get_owner("user2555@verizon.net")
        stays = []
        for i in range(16):
            stay = stay_controller.add_stay(
                 6/5/2021+i, "hello there!", [], 6/2/2021+i, owner, sitter)
            stay_rated = stay_controller.add_rating_for_stay(stay, i % 5)
            stays.append(stay)
        sitter_controller.set_sitter(sitter.sitter_email, 0, 0, 0, stays)
        self.assertEqual(
            round(sitter_controller.ratings_score_calculator(sitter), 2), 1.88)
        return sitter_controller.ratings_score_calculator(sitter)

test_ratings_scores = TestRatingsScore()
# test_ratings_scores.testAllRatingsScores()
if __name__ == '__main__':
    unittest.main()




