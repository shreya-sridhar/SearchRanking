import copy
from typing import Dict
from collections import defaultdict
import csv
import sys
sys.path.append(r"C:\Users\shrey\SearchRanking")
from models.stay import Stay
from models.sitter import Sitter
from models.dog import Dog
from models.owner import Owner
from models.constants import *

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
            raise Exception("This class is a DataStore class !")
        else:
            DataStore.__shared_instance = self

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
                    
                    rating = row[RATING_INDEX]
                    sitter_image = row[SITTER_IMAGE_INDEX]
                    end_date = row[END_DATE_INDEX]
                    text = row[TEXT_INDEX]    
                    owner_image = row[OWNER_IMAGE_INDEX]
                    dogs = row[DOGS_INDEX]
                    sitter = row[SITTER_INDEX]
                    owner = row[OWNER_INDEX]
                    start_date = row[START_DATE_INDEX]
                    sitter_phone_number = row[SITTER_PHONE_NUMBER_INDEX]
                    sitter_email = row[SITTER_EMAIL_INDEX]
                    owner_phone_number = row[OWNER_PHONE_NUMBER_INDEX]
                    owner_email = row[OWNER_EMAIL_INDEX]
                    response_time_minutes = row[RESPONSE_TIME_MINUTES_INDEX]

                    if owner_email not in self.owners:
                        # Owner does not already exist in database so add a new Owner
                        current_owner = Owner(
                            id, owner, owner_image, owner_phone_number, owner_email)
                    else:
                        current_owner = self.GetOwner(owner_email)
                    
                    if sitter_email not in self.sitters:
                        # Sitter does not already exist in database so add a new Sitter
                        current_sitter = Sitter(
                            id, sitter, sitter_image, sitter_phone_number, sitter_email)
                    else:
                        current_sitter = self.GetSitter(sitter_email)
                   
                    # Creating a new Stay
                    current_stay = Stay(id, rating, end_date, text,
                                        dogs, start_date, response_time_minutes)
                    if current_owner.owner_id == id:
                        owner_id = id 
                        self.owners[owner_id] = current_owner
                    else:
                        owner_id = current_owner.owner_id 
                    if current_sitter.sitter_id == id:
                        sitter_id = id
                        self.sitters[sitter_id] = current_sitter
                    else:
                        sitter_id = current_sitter.sitter_id

                    # establishing relationship between stays, owners & sitters. A stay belongs to a single owner and sitter. A sitter can have many stays and an owner can have many stays
                    current_stay.owner = self.owners[owner_id]
                    current_stay.sitter = self.sitters[sitter_id]
                    self.stays[id] = current_stay
                    self.owners[owner_id].stays = self.owners[owner_id].stays[:] + [self.stays[id]]
                    self.sitters[sitter_id].stays = self.sitters[sitter_id].stays[:] + [self.stays[id]]
                    # TOdo : Add comment here and discuss alternatives
                    id += 1

datastore = DataStore()
datastore.ReadCSV()

