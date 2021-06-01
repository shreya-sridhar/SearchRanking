from typing import Dict
from collections import defaultdict
import csv
import sys
sys.path.append(r"C:\Users\shrey\SearchRanking")
from models.stay import Stay
from models.sitter import Sitter
from models.dog import Dog
from models.owner import Owner

class DataStore:

    def __init__(self, owners: Dict[str, 'Owner']={}, sitters: Dict[str, 'Sitter']={}, stays: Dict[str, Stay]={}, dogs: Dict[str, Dog]={}):
        self.owners = owners
        self.sitters = sitters
        self.stays = stays
        self.dogs = dogs

    def GetAllOwners(self):
        return self.owners

    def GetAllSitters(self):
        return self.sitters

    def GetAllStays(self):
        return self.stays

    def GetOwner(self, email: str):
        for owner in self.owners:
            if owner.owner_email == email:
                return owner
        return None

    def GetSitter(self, email: str):
        if email in self.sitters:
            return self.sitters[email]
        return None

    def SetSitter(self, email: str, profile_score: float, ratings_score: float, search_score: float):
        for sitter in self.sitters:
            if sitter.sitter_email == email:
                sitter.profile_score = profile_score
                sitter.ratings_score = ratings_score
                sitters.search_score = search_score

    def ReadCSV(self):

        with open(r'C:\Users\shrey\SearchRanking\db\reviews.csv', 'r') as read_obj:
            data = csv.reader(read_obj)
            header = next(data)
            # Check file as empty
            if header != None:
                # Iterate over each row after the header in the csv
                id = 0
                for row in data:
                    # row variable is a list that represents a row in csv
                    # print(row)

        # with open(r'C:\Users\shrey\SearchRanking\db\reviews.csv', newline='') as f:
        #     reader = csv.reader(f)
        #     data = list(reader)
        # id = 0
        # for row in data:
                    owner = row[7]
                    owner_image = row[4]
                    owner_phone_number = row[11]
                    owner_email = row[12]
                    if owner_email not in self.owners:
                        # Owner does not already exist in database so add a new Owner
                        current_owner = Owner(
                            owner_phone_number, owner, owner_image, owner_phone_number, owner_email)
                        self.owners[owner_email] = current_owner
                    sitter = row[6]
                    sitter_image = row[1]
                    sitter_phone_number = row[9]
                    sitter_email = row[10]
                    if sitter_email not in self.sitters:
                        # Sitter does not already exist in database so add a new Sitter
                        current_sitter = Sitter(
                            sitter_email, sitter, sitter_image, sitter_phone_number, sitter_email)
                        self.sitters[sitter_email] = current_sitter
                    # Creating a new Stay
                    stay_id = id
                    rating = row[0]
                    start_date = row[8]
                    end_date = row[2]
                    text = row[3]
                    dogs = row[5]
                    response_time_minutes = row[13]
                    current_stay = Stay(stay_id, rating, end_date, text,
                                        dogs, start_date, response_time_minutes)
                    self.stays[stay_id] = current_stay
                    id += 1
                    # establishing relationship between stays, owners & sitters. A stay belongs to a single owner and sitter. A sitter can have many stays and an owner can have many stays
                    current_stay.owner = self.owners[owner_email]
                    current_stay.sitter = self.sitters[sitter_email]

# d = DataStore()
# d.ReadCSV()





