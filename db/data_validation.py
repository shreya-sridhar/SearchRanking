import sys
sys.path.append(r"")
import re
import phonenumbers
from models.constants import REGEX

class DataValidation:
    def validate_email(self,email:str):
        if(re.search(REGEX, email)):
            print("Valid Email")
            return True
        else:
            print("Invalid Email")
            return False

    def phone_number(self,num:int):
        my_number = phonenumbers.parse(str(num), "US")
        return phonenumbers.is_valid_number(my_number)

d = DataValidation()  



