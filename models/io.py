from collections import defaultdict
import csv
from owner import Owner
from sitter import Sitter
from stay import Stay

class ReadData:

    def __init__(self):
        owners = defaultdict(Owner)
        sitters = defaultdict(Sitter)
        stays = defaultdict(Stay)

    def readCSV(self):
        with open(r'C:\Users\shrey\rover\static_data\reviews.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        for row in data:
            id = 0
            owner = row[7]
            owner_image = row[4]
            owner_phone_number = row[11]
            owner_email = row[12]
            if owner_email not in self.owners:
                # Owner does not already exist in database so add a new Owner
                current_owner = Owner(owner_email,owner,owner_image,owner_phone_number,owner_email)
                self.owners[owner_email] = current_owner
            sitter = row[6]
            sitter_image = row[1]
            sitter_phone_number = row[9]
            sitter_email = row[10]
            if sitter_email not in self.sitters:
                 # Sitter does not already exist in database so add a new Sitter
                 current_sitter = Sitter(sitter_email,sitter,sitter_image,sitter_phone_number,sitter_email)
                 self.sitter[sitter_email] = current_sitter
            # Creating a new Stay 
            stay_id = id
            rating = row[0]
            start_date = row[8]
            end_date = row[2]
            text = row[3] 
            dogs = row[5]
            response_time_minutes = row[13]
            self.stays[stay_id] = Stay(stay_id,rating,end_date,text,dogs,start_date,reponse_time_minutes)
            id += 1
            # establishing relationship between stays, owners & sitters. A stay belongs to a single owner and sitter. A sitter can have many stays and an owner can have many stays

data = ReadData()
data.readCSV()


