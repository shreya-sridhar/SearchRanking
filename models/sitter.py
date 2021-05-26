class Sitter:
    def __init__(self,sitter_id,sitter,sitter_image,sitter_phone_number,sitter_email,stays=[],profile_score=0,ratings_score=0,search_score = 0):
        self.sitter_id = sitter_id
        # assuming sitter_id is the sitter phone number since it's unique
        self.sitter = sitter 
        self.sitter_image = sitter_image
        self.sitter_phone_number = sitter_phone_number
        self.sitter_email = sitter_email 
        self.stays = stays
        # an array of Stay objects
        self.profile_score = profile_score
        self.ratings_score = ratings_score
        self.search_score = search_score



