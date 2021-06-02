import csv
import sys
from collections import defaultdict
sys.path.append(r"")
from models.owner import Owner
from models.sitter import Sitter 
from models.stay import Stay 
from models.dog import Dog
from models.data_store import datastore

class DogController:

    def get_dog(self):
        return list(datastore.dogs.values())
    # not implemented











