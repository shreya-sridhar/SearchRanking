import csv
import sys
from collections import defaultdict
sys.path.append(r"C:\Users\shrey\SearchRanking")
from models.owner import Owner
from models.sitter import Sitter 
from models.stay import Stay 
from models.dog import Dog

class StayController:

    def __init__(self, owners=defaultdict(Owner), sitters=defaultdict(Sitter), stays=defaultdict(Stay), dogs = defaultdict(Dog)):
        self.owners = owners
        self.sitters = sitters
        self.stays = stays
        self.dogs = dogs

    def readCSV(self):
        with open(r'C:\Users\shrey\rover\static_data\reviews.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        id = 0
        for row in data:
            add_owner = False
            add_sitter = False
            owner = row[7]
            owner_image = row[4]
            owner_phone_number = row[11]
            owner_email = row[12]
            if owner_email not in self.owners:
                # Owner does not already exist in database so add a new Owner
                current_owner = Owner(
                    owner_phone_number, owner, owner_image, owner_phone_number, owner_email)
                add_owner = True
            sitter = row[6]
            sitter_image = row[1]
            sitter_phone_number = row[9]
            sitter_email = row[10]
            if sitter_email not in self.sitters:
                # Sitter does not already exist in database so add a new Sitter
                current_sitter = Sitter(
                    sitter_email, sitter, sitter_image, sitter_phone_number, sitter_email)
                add_sitter = True
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
            if add_owner:
                Stay.owner = current_owner
                current_owner.stays.append(current_stay)
                self.owners[owner_email] = current_owner
            if add_sitter:
                Stay.sitter = current_sitter
                current_sitter.stays.append(current_stay)
                self.sitters[sitter_email] = current_sitter
        return [self.owners, self.sitters, self.stays]





