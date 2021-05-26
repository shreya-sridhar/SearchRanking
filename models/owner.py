class Owner:
    def __init__(self,owner_id,owner,owner_image,owner_phone_number,owner_email,stays=[]):
        self.owner_id = owner_id
        # assuming owner_id is the owner phone number since it's unique
        self.owner = owner 
        self.owner_image = owner_image 
        self.owner_phone_number = owner_phone_number
        self.owner_email = owner_email 
        self.stays = stays
        # array of Stay objects



