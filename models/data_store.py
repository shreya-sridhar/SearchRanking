import copy
from typing import Dict
from collections import defaultdict
import csv
import sys
sys.path.append(r"")
from models.stay import Stay
from models.sitter import Sitter
from models.dog import Dog
from models.owner import Owner
from models.constants import *

class DataStore:

    __shared_instance = 'central_datastore'

    @staticmethod
    def get_instance():
        # Static Access Method
        if DataStore.__shared_instance == 'central_datastore':
            DataStore()
        return DataStore.__shared_instance

    # Initializing Singleton Class
    def __init__(self, owners: Dict[str, 'Owner'] = {}, sitters: Dict[str, 'Sitter'] = {}, stays: Dict[str, Stay] = {}, dogs: Dict[str, Dog] = {}):
        self.owners = owners
        self.sitters = sitters
        self.stays = stays
        self.dogs = dogs
        # virtual private constructor
        if DataStore.__shared_instance != 'central_datastore':
            raise Exception("This class is a DataStore class !")
        else:
            DataStore.__shared_instance = self

    '''private methods'''
    def _find_or_create_owner(self,id:int,owner:str, owner_image:str, owner_phone_number: int, owner_email:str) -> int:
        # Checking if owner already exists in database
        owner_present = False 
        for iter_owner in list(self.owners.values()):
            if iter_owner.owner_email == owner_email:
                current_owner = iter_owner 
                owner_present = True
        # Owner does not already exist in database so add a new Owner
        if not owner_present:
            current_owner = Owner(id, owner, owner_image, owner_phone_number, owner_email)
        owner_id = current_owner.owner_id
        self.owners[owner_id] = current_owner
        return owner_id

    def _find_or_create_sitter(self,id:int,sitter:str, sitter_image:str, sitter_phone_number: int, sitter_email:str)-> int:
        # Checking if sitter already exists in database
        sitter_present = False 
        for iter_sitter in list(self.sitters.values()):
            if iter_sitter.sitter_email == sitter_email:
                current_sitter = iter_sitter 
                sitter_present = True
        # Sitter does not already exist in database so add a new Sitter
        if not sitter_present:
            current_sitter = Sitter(id, sitter, sitter_image, sitter_phone_number, sitter_email)
        sitter_id = current_sitter.sitter_id
        self.sitters[sitter_id] = current_sitter
        return sitter_id

    def _get_stay_data(self,row):
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
        return rating,sitter_image,end_date,text,owner_image,dogs, sitter, owner, start_date, sitter_phone_number, sitter_email, owner_phone_number, owner_email, response_time_minutes

    def _read_csv(self):
        with open(REVIEWS_PATH) as read_obj:
            data = csv.reader(read_obj)
            header = next(data)
            if header != None:
                id = 0
                for row in data:
                    
                    rating,sitter_image,end_date,text,owner_image,dogs, sitter, owner, start_date, sitter_phone_number, sitter_email, owner_phone_number, owner_email, response_time_minutes = self._get_stay_data(row)
                    
                    # Adding owner to db if not already present
                    owner_id = self._find_or_create_owner(id, owner, owner_image, owner_phone_number, owner_email)
                    sitter_id = self._find_or_create_sitter(id, sitter, sitter_image, sitter_phone_number, sitter_email)
                   
                    # Creating a new Stay
                    current_stay = Stay(id, rating, end_date, text,dogs, start_date, response_time_minutes)

                    # establishing relationship between stays, owners & sitters. A stay belongs to a single owner and sitter. A sitter can have many stays and an owner can have many stays
                    current_stay.owner = self.owners[owner_id]
                    current_stay.sitter = self.sitters[sitter_id]
                    self.stays[id] = current_stay
                    self.owners[owner_id].stays = self.owners[owner_id].stays[:] + [self.stays[id]]
                    self.sitters[sitter_id].stays = self.sitters[sitter_id].stays[:] + [self.stays[id]]
                    # TOdo : Add comment here and discuss alternatives
                    id += 1

datastore = DataStore()
datastore._read_csv()











