import csv
import sys
from collections import defaultdict
sys.path.append(r"C:\Users\shrey\SearchRanking")
from models.owner import Owner
from models.sitter import Sitter 
from models.stay import Stay 
from models.dog import Dog
from models.data_store import datastore

class StayController:

    def GetAllStays(self):
        return list(datastore.stays.values())

    def AddStay(self,end_date: 'datetime', text: str, dogs: list('Dog'), start_date:'datetime', owner: 'Owner' = None, sitter: 'Sitter' = None):
        # if not self.GetStay(end_date,text,dogs,start_date,owner,sitter):
            stay_count = len(datastore.stays)
            stay = Stay(stay_count, 0, end_date, text, dogs, start_date, 0, owner, sitter)
            datastore.stays[stay_count] = stay 
            return [True, stay]
        # return [False, None]

    def AddRatingForStay(self,stay:'Stay',rating:float):
        datastore.stays[stay.stay_id].rating = rating
        return datastore.stays[stay.stay_id]

stay_controller = StayController()








