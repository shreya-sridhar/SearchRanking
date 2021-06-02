import csv
import sys
sys.path.append(r"C:\Users\shrey\SearchRanking")
from models.owner import Owner
from models.data_store import datastore

class OwnerController:
        
    def GetAllOwners(self):
        return datastore.owners

    def GetOwner(self, email: str):
        for owner in list(datastore.owners.values()):
            if owner.owner_email == email:
                return owner
        return None

owner_controller = OwnerController()



