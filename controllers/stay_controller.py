import csv
import sys
from collections import defaultdict
sys.path.append(r"")
from models.owner import Owner
from models.sitter import Sitter 
from models.stay import Stay 
from models.dog import Dog
from models.data_store import datastore

class StayController:

    def get_all_stays(self):
        return list(datastore.stays.values())

    def add_stay(self,end_date: 'datetime', text: str, dogs: list('Dog'), start_date:'datetime', owner: 'Owner' = None, sitter: 'Sitter' = None) -> 'Stay':
            stay_count = len(datastore.stays)
            stay = Stay(stay_count, 0, end_date, text, dogs, start_date, 0, owner, sitter)
            datastore.stays[stay_count] = stay 
            return stay

    def add_rating_for_stay(self,stay:'Stay',rating:float) -> 'Stay':
        datastore.stays[stay.stay_id].rating = rating
        return datastore.stays[stay.stay_id]

stay_controller = StayController()








