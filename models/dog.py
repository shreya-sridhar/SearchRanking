class Dog:
    #  A dog belongs to an owner and can have many sitters through stays (join model) in a many-to-many relationship
    def __init__(self,name:str,owner:'Owner',stays:list('Stay')=[]):
        self.name = name 
        self.owner = owner
        self.stays = stays

