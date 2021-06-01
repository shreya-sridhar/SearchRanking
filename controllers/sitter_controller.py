import csv
import sys
sys.path.append(r"C:\Users\shrey\SearchRanking")
from models.data_store import DataStore

class SitterController:

    def __init__(self):
        self.datastore = DataStore()
        self.datastore.ReadCSV()
   
    def getAllSitters(self):
        return list(self.datastore.GetAllSitters().values())

    def setSitter(self,sitter_email,profile_score,ratings_score,search_score):
        return self.datastore.SetSitter(sitter_email,profile_score,ratings_score,search_score)

    def AddSitting(self):
        # If no score compute the score,  save to db and  return to user
        # Not implemented 
        return
    
    def exportSitters(self):
        sitters = self.getAllSitters()
        # list of Sitter objects
        sitters.sort(key=lambda x: x.sitter)
        sitters.sort(key=lambda x: x.search_score, reverse=True)

        with open('data.csv', 'w',) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['email', 'name','profile_score','ratings_score','search_score'])
            for sitter in sitters:
                writer.writerow([sitter.sitter_email,sitter.sitter,sitter.profile_score,sitter.ratings_score,sitter.search_score])

    def overall_score_calculator(self):
        for sitter in self.getAllSitters():
            profile_score = self.profile_score_calculator(sitter)
            ratings_score = self.ratings_score_calculator(sitter)
            search_score = self.search_score_calculator(
                sitter, profile_score, ratings_score)
            self.setSitter(sitter.sitter_email,round(profile_score,2),round(ratings_score,2),round(search_score,2))
            self.exportSitters()

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
        stays = curr_sitter.stays
        total_ratings = 0
        count_ratings = 0
        for stay in stays:
            count_ratings += 1
            total_ratings += float(stay.rating)
        if total_ratings == 0 and count_ratings == 0:
            return 0
        return total_ratings/count_ratings

    def search_score_calculator(self, sitter, profile_score, ratings_score):
        # When a sitter has no stays, their Search Score is equal to the Profile Score. When a sitter has 10 or more
        # stays, their Search Score is equal to the Ratings Score. The idea is that as a sitter gets more reviews, we will weigh the
        # Ratings Score more heavily.
        stays = sitter.stays
        if len(stays) == 0:
            return profile_score
        if len(stays) >= 10:
            return ratings_score
        else:
            return len(stays)/10*ratings_score + (1-len(stays)/10)*profile_score

# s = SitterController()
# s.overall_score_calculator()


