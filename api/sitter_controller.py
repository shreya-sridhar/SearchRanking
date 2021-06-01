import csv
import sys
sys.path.append(r"C:\Users\shrey\SearchRanking")
from models.data_store import DataStore

class SitterController:

    def __init__(self):
        self.datastore = DataStore()
        self.datastore.ReadCSV()
    # def listAllSitters([ ]):
    #     # order it by score, email_id
    #     # dog ='Barbarian'
    #     # location =''
    #     #

    # def listAllSitters([ ]):

    # def GetSitter(string sitter_id):
    #     # Get

    # def AddSitting():
    #     # If no score Compute the score,  save to db and  return to user
    #     # Not implemented

    # def

    # Crud action
    # def update(sitter):

    # def delete():
    # unimplemented

    # Class Score Caluclator
    # Make this just a function
    def overall_score_calculator(self):
        for sitter in list(self.datastore.GetAllSitters().values()):
            profile_score = self.profile_score_calculator(sitter)
            ratings_score = self.ratings_score_calculator(sitter)
            search_score = self.search_score_calculator(
                sitter, profile_score, ratings_score)
            print(profile_score, ratings_score)

    def profile_score_calculator(self, curr_sitter):
        # calculates & updates sitter object with profile score
        sitter_name = curr_sitter.sitter
        distinct_chars = set()
        for letter in sitter_name:
            if letter.isalpha():
                distinct_chars.add(letter)
        # The Profile Score is 5 times the fraction of the English alphabet comprised by the
        # distinct letters in what we've recovered of the sitter's name.
        profile_score_val = 5/26*len(distinct_chars)
        # O(n) time, space complexity where n is len(sitter_name)
        return profile_score_val

    def ratings_score_calculator(self, curr_sitter):
        # calculates & updates sitter object with ratings score
        stays = list(self.datastore.GetAllStays().values())
        total_ratings = 0
        count_ratings = 0
        for stay in stays:
            # print(stay,"fow")
            if stay.sitter == curr_sitter:
                count_ratings += 1
                total_ratings += float(stay.rating)
        if total_ratings == 0 and count_ratings == 0:
            return 0
        return total_ratings/count_ratings

    def search_score_calculator(self, sitter, profile_score, ratings_score):
        # When a sitter has no stays, their Search Score is equal to the Profile Score. When a sitter has 10 or more
        # stays, their Search Score is equal to the Ratings Score. The idea is that as a sitter gets more reviews, we will weigh the
        # Ratings Score more heavily.

        return


s = SitterController()
s.overall_score_calculator()
