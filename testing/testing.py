import unittest 

class TestProfileScore(unittest.TestCase):
    # when no distinct letters 
    def self.same_letters_test(self):
        self.assertEqual(profile_score('j'),0)

    # all distinct letters
    def self.distinct_letters_test(self):
        self.assertEqual(profile_score('linda'),0)

    # combination of cases1&2 
    def self.mixed_letters_test(self):
        self.assertEqual(profile_score('casey sanders'),0)

    # null name 
    def self.same_letters(self):
        self.assertEqual(profile_score(''),0)

    # name containing special characters like .
    def self.same_letters(self):
        self.assertEqual(profile_score('samuel p. jones'),0)

    # name in upper and lower cases 
    def self.same_letters(self):
        self.assertEqual(profile_score('Harry Potter'),0)


class TestRatingsScore(unittest.TestCase):
    # when no stays
    
    # when large number of stays

    # when all stays have 0 ratings 


class TestSearchScore(unittest.TestCase):
    # no stays 

    # less than 10 stays

    # 10 or more stays






