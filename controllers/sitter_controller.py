import csv
import sys
sys.path.append(r"")
from models.sitter import Sitter
from models.data_store import datastore
from typing import List

class SitterController:

    def get_all_sitters(self) -> List['Sitter']:
        return list(datastore.sitters.values())

    def get_sitter(self, email: str) -> 'Sitter':
        for sitter in list(datastore.sitters.values()):
            if sitter.sitter_email == email:
                return sitter
        return None

    def set_sitter(self, sitter_email: str, profile_score: float = 0, ratings_score: float = 0, search_score: float =0,stays:List['Stay'] = []):
        for curr_sitter in list(datastore.sitters.values()):
            if curr_sitter.sitter_email == sitter_email:
                sitter = curr_sitter
        sitter.profile_score = profile_score
        sitter.ratings_score = ratings_score
        sitter.search_score = search_score
        sitter.stays = stays

    def add_sitter(self, sitter: str, sitter_image: str, sitter_phone_number: int, sitter_email: str) -> 'Sitter':
        if not self.get_sitter(sitter_email):
            count_sitters = len(datastore.sitters)
            sitter = Sitter(count_sitters, sitter, sitter_image,
                            sitter_phone_number, sitter_email)
            datastore.sitters[count_sitters] = sitter
        # sitter has to be initialized with sitter (name), image, phone and email
            return sitter
        return self.get_sitter(sitter_email)

    def overall_score_calculator(self):
        for sitter in self.get_all_sitters():
            profile_score = self.profile_score_calculator(sitter)
            ratings_score = self.ratings_score_calculator(sitter)
            search_score = self.search_score_calculator(sitter, profile_score, ratings_score)
            self.set_sitter(sitter.sitter_email, round(profile_score, 2), round(
                ratings_score, 2), round(search_score, 2))
            self._export_sitters_to_csv()

    def profile_score_calculator(self, curr_sitter: 'Sitter') -> float:
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

    def ratings_score_calculator(self, curr_sitter: 'Sitter') -> float:
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

    def search_score_calculator(self, sitter: 'Sitter', profile_score: float, ratings_score: float) -> float:
        stays = sitter.stays
        # When a sitter has no stays, their Search Score is equal to the Profile Score.
        if len(stays) == 0:
            return profile_score
        # When a sitter has 10 or more stays, their Search Score is equal to the Ratings Score.
        if len(stays) >= 10:
            return ratings_score
        # As a sitter gets more reviews, we will weigh the Ratings Score more heavily.
        else:
            return round((ratings_score * len(stays)/10) + (profile_score * (1-len(stays)/10)),2)

    '''private methods ''' 
    def _export_sitters_to_csv(self):
        headers = ['email', 'name', 'profile_score','ratings_score', 'search_score']
        sitters = self.get_all_sitters()
        # list of Sitter objects
        sitters.sort(key=lambda x: x.sitter)
        sitters.sort(key=lambda x: x.search_score, reverse=True)

        # Use custom user provided name
        with open('output.csv', 'w',) as csvfile:
            writer = csv.writer(csvfile)
            # todo ; Define output format in constant
            writer.writerow(headers)
            for sitter in sitters:
                writer.writerow([sitter.sitter_email, sitter.sitter,
                                sitter.profile_score, sitter.ratings_score, sitter.search_score])

sitter_controller = SitterController()
sitter_controller.overall_score_calculator()

