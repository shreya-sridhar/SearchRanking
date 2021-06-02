class Sitter:

    # A sitter can have many stays 

    def __init__(self, sitter_id: int, sitter: str, sitter_image: str, sitter_phone_number: int, sitter_email: str, stays: list('Stay') = [], profile_score: float = 0, ratings_score: float = 0, search_score: float = 0):
        self.sitter_id = sitter_id
        self.sitter = sitter
        self.sitter_image = sitter_image
        self.sitter_phone_number = sitter_phone_number
        self.sitter_email = sitter_email
        self.stays = stays
        # an array of Stay objects
        self.profile_score = profile_score
        self.ratings_score = ratings_score
        self.search_score = search_score
