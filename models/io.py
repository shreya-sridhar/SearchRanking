from collections import defaultdict
import csv
from owner import Owner
from sitter import Sitter
from stay import Stay

class ReadData:

    def __init__(self):
        owners = defaultdict(Owner)
        sitters = {}
        stays = {}

    def readCSV(self):
        with open(r'C:\Users\shrey\rover\static_data\reviews.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        print(data)


data = ReadData()
data.readCSV()


