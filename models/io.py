import csv
from owner import * 
from sitter import * 
from stay.py import * 

class ReadData:
    
    def readCSV(self):
        with open('data/reviews.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        
        for row in data:
            
















