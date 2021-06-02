class Owner:
    # An owner has many dogs. A owner has many sitters through stays (join model) in a many-to-many relationship

    def __init__(self, owner_id: int, owner: str, owner_image: str, owner_phone_number: int, owner_email: str, stays: list('Stay') = [], dogs: list('Dog') = []):
        self.owner_id = owner_id
        self.owner = owner
        self.owner_image = owner_image
        self.owner_phone_number = owner_phone_number
        self.owner_email = owner_email
        self.stays = stays
        # array of Stay objects
        self.dogs = dogs

        