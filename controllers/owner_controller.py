import csv
import sys
sys.path.append(r"")
from models.owner import Owner
from models.data_store import datastore

class OwnerController:
        
    def get_all_owners(self):
        return datastore.owners

    def get_owner(self, email: str):
        for owner in list(datastore.owners.values()):
            if owner.owner_email == email:
                return owner
        return None

owner_controller = OwnerController()



