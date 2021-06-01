'''
row i change and make cleaner w constants

'''
import copy
from typing import Dict
from collections import defaultdict
import csv
import sys
sys.path.append(r"C:\Users\shrey\SearchRanking")
from models.owner import Owner
from models.dog import Dog
from models.sitter import Sitter
from models.stay import Stay

# TODO : make this class a DataStore class in python  
class DataStore:

    __shared_instance = 'central_datastore'
  
    @staticmethod
    def getInstance():
        """Static Access Method"""
        if DataStore.__shared_instance == 'central_datastore':
            DataStore()
        return DataStore.__shared_instance
  
    def __init__(self, owners: Dict[str, 'Owner'] = {}, sitters: Dict[str, 'Sitter'] = {}, stays: Dict[str, Stay] = {}, dogs: Dict[str, Dog] = {}):
        self.owners = owners
        self.sitters = sitters
        self.stays = stays
        self.dogs = dogs
        """virtual private constructor"""
        if DataStore.__shared_instance != 'central_datastore':
            raise Exception ("This class is a DataStore class !")
        else:
            DataStore.__shared_instance = self

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
        sitter = self.sitters[email]
        sitter.profile_score = profile_score
        sitter.ratings_score = ratings_score
        sitter.search_score = search_score

    # TODO : make this private method
    def ReadCSV(self):
        # TODO : use relative Path
        with open(r'C:\Users\shrey\SearchRanking\db\reviews.csv', 'r') as read_obj:
            data = csv.reader(read_obj)
            header = next(data)
            # Check file as empty
            if header != None:
                # Iterate over each row after the header in the csv
                id = 0
                for row in data:
                    # TODO: move to a different function
                    # TODO: use validate methods 
                    owner = row[7]
                    owner_image = row[4]
                    owner_phone_number = row[11]
                    owner_email = row[12]
                    if owner_email not in self.owners:
                        # Owner does not already exist in database so add a new Owner
                        current_owner = Owner(
                            owner_phone_number, owner, owner_image, owner_phone_number, owner_email)
                    else:
                        current_owner = self.owners[owner_email]
                    sitter = row[6]
                    sitter_image = row[1]
                    sitter_phone_number = row[9]
                    sitter_email = row[10]
                    if sitter_email not in self.sitters:
                        # Sitter does not already exist in database so add a new Sitter
                        current_sitter = Sitter(
                            sitter_email, sitter, sitter_image, sitter_phone_number, sitter_email)
                    else:
                        current_sitter = self.sitters[sitter_email]
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
                    # TOdo : Add comment here and discuss alternatives 
                    id += 1
                    self.owners[owner_email] = current_owner
                    self.sitters[sitter_email] = current_sitter
                    # establishing relationship between stays, owners & sitters. A stay belongs to a single owner and sitter. A sitter can have many stays and an owner can have many stays
                    self.stays[stay_id].owner = self.owners[owner_email]
                    self.stays[stay_id].sitter = self.sitters[sitter_email]
                    self.owners[owner_email].stays = self.owners[owner_email].stays[:] + [self.stays[stay_id]]
                    self.sitters[sitter_email].stays = self.sitters[sitter_email].stays[:] + [self.stays[stay_id]]











