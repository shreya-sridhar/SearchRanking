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

    def __init__(self, owners=defaultdict(Owner), sitters=defaultdict(Sitter), stays=defaultdict(Stay), dogs = defaultdict(Dog)):
        self.owners = owners
        self.sitters = sitters
        self.stays = stays
        self.dogs = dogs

    def AddStay(self,end_date: 'datetime', text: str, dogs: list('Dog'), start_date:'datetime', owner: 'Owner' = None, sitter: 'Sitter' = None):
        stay_count = len(datastore.stays)
        curr_stay = Stay(stay_count,0,end_date,text,dogs,start_date,-1,owner,sitter)
        datastore.stays[stay_count] = curr_stay
        return [True,curr_stay]

    def AddRatingForStay(self,stay:'Stay',rating:float):
        datastore.stays[stay_id].rating = rating


















